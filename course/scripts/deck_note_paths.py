"""Exact repo paths in lecture deck speaker notes.

One place for three users:
- check-course-links.py finds the .md path strings in deck notes (MD_PATH, note_path_strings).
- build_deck.py and patch_lecturer_edit.py map old shorthand to exact paths before
  they write notes (fix_note_paths, normalize_presentation_notes).
- test_check_course_links.py tests all of it.

NOTE_PATH_FIXES holds the shorthand that hand-edited decks used. A note that still
carries one of these strings is rewritten to the exact current path.
"""

import re

MD_PATH = re.compile(r"(?<![\w./&:*~$%@\\-])[\w./&@-]*[\w&@-]\.md(?![\w/-]|\.\w)")

NOTE_PATH_FIXES = {
    "course/course-outline.md": "course/SESSIONS/overview/course-outline.md",
    "course/course-rhythm.md": "course/SESSIONS/overview/course-rhythm.md",
    "course/what-is-harness.md": "course/PRACTICE/01-harness-and-agents/what-is-harness.md",
    "course/what-is-lint.md": "course/PRACTICE/02-knowledge-bases/what-is-lint.md",
    "course/what-is-mcp.md": "course/PRACTICE/06-mcp-and-tools/what-is-mcp.md",
    "course/visions-fears-regulation.md": "course/THEORY/06-danger-and-risk/visions-fears-regulation.md",
    "course/eu-ai-act-and-datenschutz.md": "course/THEORY/05-privacy-regulation/eu-ai-act-and-datenschutz.md",
    "course/howto-hermes-setup.md": "course/PRACTICE/01-harness-and-agents/howto-hermes-setup.md",
    "course/howto-obsidian-setup-and-sync.md": "course/PRACTICE/02-knowledge-bases/howto-obsidian-setup-and-sync.md",
    "course/knowledge-store-options.md": "course/PRACTICE/02-knowledge-bases/knowledge-store-options.md",
    "course/llm-wiki-standard-files.md": "course/PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md",
    "default-setup.md": "course/PRACTICE/01-harness-and-agents/default-setup.md",
    "ecology.md": "course/THEORY/03-ecology-infrastructure/ecology.md",
    "flattening-and-the-norm.md": "course/THEORY/04-bias-flattening/flattening-and-the-norm.md",
    "course/student-share-structure.md": "course/templates/group-input-presentation.md",
    "prompting-and-model-choice.md": "course/PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md",
}


def note_path_strings(text):
    """Return the .md path strings that one note paragraph contains."""
    found = []
    for match in MD_PATH.finditer(text):
        token = match.group(0)
        if token.startswith("./"):
            token = token[2:]
        found.append(token)
    return found


def fix_note_paths(text):
    """Replace known shorthand paths with exact repo paths. Other text stays as it is."""
    return MD_PATH.sub(lambda match: NOTE_PATH_FIXES.get(match.group(0), match.group(0)), text)


def normalize_presentation_notes(presentation):
    """Apply fix_note_paths to every speaker note of a python-pptx presentation.

    Formatting of the first run in a changed paragraph is kept. Returns the number of
    changed paragraphs.
    """
    changed = 0
    for slide in presentation.slides:
        if not slide.has_notes_slide:
            continue
        for paragraph in slide.notes_slide.notes_text_frame.paragraphs:
            runs = list(paragraph.runs)
            old = "".join(run.text for run in runs)
            new = fix_note_paths(old)
            if runs and new != old:
                runs[0].text = new
                for run in runs[1:]:
                    run.text = ""
                changed += 1
    return changed
