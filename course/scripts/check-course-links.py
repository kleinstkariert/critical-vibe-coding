"""Check Markdown links and Obsidian wikilinks in the course pack.

Exit 1 when any scanned file has a broken link.
Path case must match exactly, because GitHub and Linux are case-sensitive.
A wikilink without an anchor is counted as a notice (it works in Obsidian only).
Use --strict to resolve wikilinks by path only, not by file name.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
SCAN = [ROOT / "course", ROOT / "research", ROOT / "archive", ROOT / "documentation"]
EXTRA_FILES = [ROOT / "README.md", ROOT / "AGENTS.md"]
WIKI = re.compile(r"\[\[([^\]|#]*)(#[^\]|]+)?(\|[^\]]+)?\]\]")
MD = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"^```", re.M)


def slug(text):
    text = text.strip().lower()
    text = text.replace("'", "")
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


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


def exact_exists(path):
    """True when every path part matches the case on disk."""
    try:
        path = Path(path)
        rel = path.resolve().relative_to(ROOT)
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
    matches = [item for item in matches if "UnlearGestaltung" not in item.parts]
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
            dest = (path.parent / path_part).resolve()
        if not (is_file_exact(dest) or is_dir_exact(dest)):
            broken.append(f"markdown link not found (case must match): {url}")
            continue
        if dest.is_dir():
            continue
        if anchor and slug(unquote(anchor)) not in headings(dest.read_text(encoding="utf-8")):
            broken.append(f"heading not found: #{anchor} in {dest.relative_to(ROOT).as_posix()}")
    return broken, notices


def main():
    strict = "--strict" in sys.argv
    problems_by_file = []
    notices = 0
    files = 0
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
    failed = bool(problems_by_file)
    print("RESULT: " + ("FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
