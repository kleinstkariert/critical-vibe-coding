"""Check Markdown links and Obsidian wikilinks in the course pack.

Exit 1 when a current student document has a broken link.
Archive, teacher, and research findings are printed and do not fail the run.
"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
SCAN = [ROOT / "course", ROOT / "research"]
WIKI = re.compile(r"\[\[([^\]|#]*)(#[^\]|]+)?(\|[^\]]+)?\]\]")
MD = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
FENCE = re.compile(r"^```", re.M)


def split_frontmatter(text):
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" not in line or line[:1] in " -":
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


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


def find_note(source, target):
    target = target.strip().replace("\\", "/")
    if not target:
        return source
    raw = unquote(target)
    if raw.endswith(".md"):
        candidates = [source.parent / raw]
    else:
        candidates = [source.parent / f"{raw}.md", source.parent / raw]
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    name = Path(raw).name
    if name.endswith(".md"):
        name = name[:-3]
    matches = []
    for base in SCAN:
        if not base.exists():
            continue
        matches.extend(base.rglob(f"{name}.md"))
    matches = [item.resolve() for item in matches if "UnlearGestaltung" not in item.parts]
    if len(matches) == 1:
        return matches[0]
    in_course = [item for item in matches if "course" in item.parts]
    if len(in_course) == 1:
        return in_course[0]
    return None


def check_file(path):
    text = path.read_text(encoding="utf-8")
    visible = outside_fences(text)
    visible = re.sub(r"`[^`\n]+`", "", visible)
    problems = []
    for match in WIKI.finditer(visible):
        target = match.group(1) or ""
        anchor = (match.group(2) or "").lstrip("#")
        dest = find_note(path, target)
        if dest is None:
            problems.append(f"wikilink not found: [[{match.group(0)[2:-2]}]]")
            continue
        if not anchor:
            problems.append(f"wikilink works in Obsidian only: [[{match.group(0)[2:-2]}]]")
            continue
        if slug(unquote(anchor)) not in headings(dest.read_text(encoding="utf-8")) and unquote(anchor) not in headings(dest.read_text(encoding="utf-8")):
            problems.append(f"wikilink heading not found: {anchor} in {dest.relative_to(ROOT).as_posix()}")
        else:
            problems.append(f"wikilink works in Obsidian only: [[{match.group(0)[2:-2]}]]")
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
        if not dest.is_file() and not dest.is_dir():
            problems.append(f"markdown link not found: {url}")
            continue
        if dest.is_dir():
            continue
        if anchor and slug(unquote(anchor)) not in headings(dest.read_text(encoding="utf-8")):
            problems.append(f"heading not found: #{anchor} in {dest.relative_to(ROOT).as_posix()}")
    return problems


def role(path, fields):
    rel = path.relative_to(ROOT).as_posix()
    if "archive-13-session-plan" in rel or fields.get("audience") == "archive":
        return "archive"
    if fields.get("audience") == "teacher" or rel.startswith("research/"):
        return "other"
    if fields.get("audience") == "student" and fields.get("status") == "current":
        return "current"
    if rel.startswith("course/"):
        return "current"
    return "other"


def main():
    current = []
    rest = []
    for base in SCAN:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if "scripts" in path.parts:
                continue
            fields = split_frontmatter(path.read_text(encoding="utf-8"))
            problems = check_file(path)
            if not problems:
                continue
            bucket = current if role(path, fields) == "current" else rest
            bucket.append((path.relative_to(ROOT).as_posix(), problems))
    print(f"current student files with link problems: {len(current)}")
    for name, problems in current:
        print(f"\n{name}")
        for problem in problems:
            print(f"  {problem}")
    print(f"\nother files still flagged: {len(rest)}")
    for name, problems in rest:
        print(f"\n{name}")
        for problem in problems:
            print(f"  {problem}")
    return 1 if current else 0


if __name__ == "__main__":
    sys.exit(main())
