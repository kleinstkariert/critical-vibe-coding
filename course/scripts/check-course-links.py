"""Check Markdown links, Obsidian wikilinks and deck-note paths in the course pack.

Exit 1 when any scanned file has a broken link or a deck note names a missing path.
Path case must match exactly, because GitHub and Linux are case-sensitive.
A wikilink without an anchor is counted as a notice (it works in Obsidian only).
Use --strict to resolve wikilinks by path only, not by file name.

Deck notes: the checker also opens the lecture decks (.pptx notes slides and .odp
content.xml) read-only. Every string that ends in .md must be an exact repo path,
for example course/THEORY/04-bias-flattening/flattening-and-the-norm.md.
A bare file name or a short course/<name>.md form fails.
    --no-decks     skip the deck-note check
    --decks-only   run only the deck-note check

Bare wikilinks never resolve into the external reference trees listed in
EXTERNAL_TREES. Use the full path for those notes.
"""

import os
import posixpath
import re
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
SCAN = [ROOT / "course", ROOT / "research", ROOT / "archive", ROOT / "documentation"]
EXTRA_FILES = [ROOT / "README.md", ROOT / "AGENTS.md"]
EXTERNAL_TREES = {"UnlearGestaltungAI_Mainz"}
DECK_ROOT = Path("course") / "SESSIONS" / "lectures"
DECK_NOTE_IGNORE = set()
WIKI = re.compile(r"\[\[([^\]|#]*)(#[^\]|]+)?(\|[^\]]+)?\]\]")
MD = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"^```", re.M)
MD_PATH = re.compile(r"(?<![\w./&:*~$%@\\-])[\w./&@-]*[\w&@-]\.md(?![\w/-]|\.\w)")

A_NS = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
P_NS = "{http://schemas.openxmlformats.org/presentationml/2006/main}"
R_NS = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
REL_NS = "{http://schemas.openxmlformats.org/package/2006/relationships}"
ODF_TEXT = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"
ODF_DRAW = "{urn:oasis:names:tc:opendocument:xmlns:drawing:1.0}"
ODF_PRES = "{urn:oasis:names:tc:opendocument:xmlns:presentation:1.0}"


def slug(text):
    text = text.strip().lower()
    text = text.replace("'", "")
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s", "-", text)
    return text


def headings(text):
    found = []
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            found.append(slug(match.group(1)))
    return found


def outside_fences(text):
    parts = FENCE.split(text)
    kept = []
    for index, part in enumerate(parts):
        if index % 2 == 0:
            kept.append(part)
        else:
            kept.append("")
    return "".join(kept)


def normalize(path):
    """Make a path absolute and drop . and .. parts. Unlike resolve(), this keeps the written case."""
    return Path(os.path.normpath(os.path.abspath(path)))


def exact_exists(path):
    """True when every path part matches the case on disk."""
    try:
        path = Path(path)
        rel = normalize(path).relative_to(ROOT)
    except (ValueError, OSError):
        return path.exists()
    current = ROOT
    for part in rel.parts:
        try:
            names = {entry.name for entry in current.iterdir()}
        except OSError:
            return False
        if part not in names:
            return False
        current = current / part
    return True


def is_file_exact(path):
    return Path(path).is_file() and exact_exists(path)


def is_dir_exact(path):
    return Path(path).is_dir() and exact_exists(path)


def all_notes():
    notes = []
    for base in SCAN:
        if base.exists():
            notes.extend(base.rglob("*.md"))
    notes.extend(item for item in EXTRA_FILES if item.exists())
    return notes


def find_note(source, target, strict=False):
    """Return (path or None, how). how is 'path', 'root', 'name' or ''."""
    target = target.strip().replace("\\", "/")
    if not target:
        return source, "path"
    raw = unquote(target)
    if raw.endswith(".md"):
        candidates = [(source.parent / raw, "path"), (ROOT / raw, "root")]
    else:
        candidates = [
            (source.parent / f"{raw}.md", "path"),
            (source.parent / raw, "path"),
            (ROOT / f"{raw}.md", "root"),
        ]
    for candidate, how in candidates:
        if is_file_exact(candidate):
            return candidate.resolve(), how
    if strict and "/" in raw:
        return None, ""
    name = Path(raw).name
    if name.endswith(".md"):
        name = name[:-3]
    matches = [item.resolve() for item in all_notes() if item.name == f"{name}.md"]
    matches = [item for item in matches if not EXTERNAL_TREES.intersection(item.parts)]
    if len(matches) == 1:
        return matches[0], "name"
    in_course = [item for item in matches if "course" in item.parts]
    if len(in_course) == 1:
        return in_course[0], "name"
    return None, ""


def check_file(path, strict=False):
    """Return (broken, notices) as lists of strings."""
    text = path.read_text(encoding="utf-8")
    visible = outside_fences(text)
    visible = re.sub(r"`[^`\n]+`", "", visible)
    broken = []
    notices = []
    for match in WIKI.finditer(visible):
        target = (match.group(1) or "").rstrip("\\")
        anchor = (match.group(2) or "").lstrip("#")
        dest, how = find_note(path, target, strict)
        label = match.group(0)[2:-2]
        if dest is None:
            broken.append(f"wikilink not found: [[{label}]]")
            continue
        if strict and how == "name" and "/" in target:
            broken.append(f"wikilink path is wrong, found by name only: [[{label}]]")
            continue
        if anchor:
            body = dest.read_text(encoding="utf-8")
            if slug(unquote(anchor)) not in headings(body) and unquote(anchor) not in headings(body):
                broken.append(f"wikilink heading not found: {anchor} in {dest.relative_to(ROOT).as_posix()}")
                continue
        notices.append(f"wikilink works in Obsidian only: [[{label}]]")
    for match in MD.finditer(visible):
        url = match.group(1).strip()
        if url.startswith(("http://", "https://", "mailto:")):
            continue
        path_part, _, anchor = url.partition("#")
        path_part = unquote(path_part)
        if not path_part:
            dest = path
        else:
            dest = normalize(path.parent / path_part)
        if not (is_file_exact(dest) or is_dir_exact(dest)):
            broken.append(f"markdown link not found (case must match): {url}")
            continue
        if dest.is_dir():
            continue
        if anchor and slug(unquote(anchor)) not in headings(dest.read_text(encoding="utf-8")):
            broken.append(f"heading not found: #{anchor} in {dest.relative_to(ROOT).as_posix()}")
    return broken, notices


def deck_files():
    base = ROOT / DECK_ROOT
    if not base.exists():
        return []
    decks = []
    for pattern in ("*.pptx", "*.odp"):
        for item in base.rglob(pattern):
            if "archive" in item.parts or item.stem.endswith("_Old"):
                continue
            decks.append(item)
    return sorted(decks)


def odf_text(element):
    out = [element.text or ""]
    for child in element:
        if child.tag in (ODF_TEXT + "s", ODF_TEXT + "tab", ODF_TEXT + "line-break"):
            out.append(" ")
        else:
            out.append(odf_text(child))
        out.append(child.tail or "")
    return "".join(out)


def pptx_slide_numbers(archive):
    """Map notes slide entry name to its slide number, or None when unknown."""
    try:
        presentation = ET.fromstring(archive.read("ppt/presentation.xml"))
        rels = ET.fromstring(archive.read("ppt/_rels/presentation.xml.rels"))
    except (KeyError, ET.ParseError):
        return {}
    targets = {rel.get("Id"): rel.get("Target") for rel in rels.iter(REL_NS + "Relationship")}
    order = {}
    for index, slide in enumerate(presentation.iter(P_NS + "sldId"), 1):
        target = targets.get(slide.get(R_NS + "id"))
        if target:
            order[posixpath.normpath(posixpath.join("ppt", target))] = index
    numbers = {}
    for name in archive.namelist():
        match = re.fullmatch(r"ppt/notesSlides/(notesSlide\d+\.xml)", name)
        if not match:
            continue
        rels_name = f"ppt/notesSlides/_rels/{match.group(1)}.rels"
        try:
            note_rels = ET.fromstring(archive.read(rels_name))
        except (KeyError, ET.ParseError):
            continue
        for rel in note_rels.iter(REL_NS + "Relationship"):
            if rel.get("Type", "").endswith("/slide"):
                target = posixpath.normpath(posixpath.join("ppt/notesSlides", rel.get("Target")))
                numbers[name] = order.get(target)
    return numbers


def deck_note_paragraphs(deck):
    """Yield (location, paragraph text) for every speaker-note paragraph in a deck."""
    with zipfile.ZipFile(deck) as archive:
        if deck.suffix == ".pptx":
            numbers = pptx_slide_numbers(archive)
            for name in sorted(archive.namelist()):
                if not re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name):
                    continue
                root = ET.fromstring(archive.read(name))
                number = numbers.get(name)
                where = f"slide {number}" if number else name
                for paragraph in root.iter(A_NS + "p"):
                    parts = []
                    for element in paragraph.iter():
                        if element.tag == A_NS + "t":
                            parts.append(element.text or "")
                        elif element.tag == A_NS + "br":
                            parts.append(" ")
                    yield where, "".join(parts)
        else:
            root = ET.fromstring(archive.read("content.xml"))
            for number, page in enumerate(root.iter(ODF_DRAW + "page"), 1):
                for notes in page.iter(ODF_PRES + "notes"):
                    for paragraph in notes.iter(ODF_TEXT + "p"):
                        yield f"page {number}", odf_text(paragraph)


def note_path_strings(text):
    """Return the .md path strings that one note paragraph contains."""
    found = []
    for match in MD_PATH.finditer(text):
        token = match.group(0)
        if token.startswith("./"):
            token = token[2:]
        found.append(token)
    return found


def check_deck_note_path(token, names):
    """Return None when token is an exact repo path, else the reason as text."""
    if token in DECK_NOTE_IGNORE:
        return None
    clean = posixpath.normpath(token)
    if clean.startswith("..") or clean.startswith("/"):
        return "not a repo-relative path"
    target = ROOT / clean
    if is_file_exact(target):
        return None
    reason = "case differs from the file on disk" if target.is_file() else "no such file"
    same_name = names.get(posixpath.basename(clean).lower(), [])
    if same_name:
        reason += "; same name exists at: " + ", ".join(same_name)
    return reason


def check_decks():
    """Return (problems, decks, strings). problems is a list of (deck, location, text)."""
    names = {}
    for note in all_notes():
        rel = note.relative_to(ROOT).as_posix()
        names.setdefault(note.name.lower(), []).append(rel)
    problems = []
    decks = deck_files()
    strings = 0
    for deck in decks:
        label = deck.relative_to(ROOT).as_posix()
        for where, text in deck_note_paragraphs(deck):
            for token in note_path_strings(text):
                strings += 1
                reason = check_deck_note_path(token, names)
                if reason:
                    problems.append((label, where, f"{token}: {reason}"))
    return problems, len(decks), strings


def main():
    strict = "--strict" in sys.argv
    decks_only = "--decks-only" in sys.argv
    with_decks = "--no-decks" not in sys.argv
    problems_by_file = []
    notices = 0
    files = 0
    if not decks_only:
        for path in sorted(set(all_notes())):
            if "scripts" in path.parts:
                continue
            files += 1
            broken, note = check_file(path, strict)
            notices += len(note)
            if broken:
                problems_by_file.append((path.relative_to(ROOT).as_posix(), broken))
        print(f"files scanned: {files}")
        print(f"files with broken links: {len(problems_by_file)} ({sum(len(p) for _, p in problems_by_file)} links)")
        for name, problems in problems_by_file:
            print(f"\n{name}")
            for problem in problems:
                print(f"  {problem}")
        print(f"\nnotices (wikilinks that work in Obsidian only): {notices}")
    deck_problems = []
    if with_decks or decks_only:
        deck_problems, deck_count, strings = check_decks()
        print(f"\ndeck notes: {deck_count} decks, {strings} .md path strings, {len(deck_problems)} bad")
        for deck, where, text in deck_problems:
            print(f"  {deck} ({where}): {text}")
    failed = bool(problems_by_file) or bool(deck_problems)
    print("RESULT: " + ("FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
