---
title: AGENTS.md. Critical Vibe Coding course repo
date: 2026-11-18
---

# Project rules for agents

This repository is the **student course pack** for Critical Vibe Coding (Interface Cultures).

Read this file before editing.

## Scope

- Prefer edits under `course/` for student-facing materials.
- Do not rewrite the lecturer's authored overview prose in `course/PRACTICE/08-verification-and-provenance/local-llm-coding-with-hermes.md` unless the lecturer asks.
- Do not use em dashes. Prefer short sentences, commas, or colons.
- Aim for STE ~80% on new agent-written text.

## Before you edit

1. Inspect the repository and the relevant session or how-to note.
2. Create a short plan (maximum five steps).
3. Change only files in the task scope.

## Allowed / forbidden

- Do not read or commit secrets (`.env`, API keys, credentials).
- Do not delete files without approval.
- Do not invent calendar-time estimates.
- Keep Session 01 / Session 02 teaching slides sparse.

## Verification

After each meaningful change:

1. Confirm markdown links resolve to existing files when you add wiki links.
   Run `python course/scripts/check-course-links.py --strict`. It checks Markdown links, wikilinks, exact path case, and every `.md` path string in the speaker notes of the lecture decks (`.pptx` and `.odp`, read-only). Notes must name exact repo paths, such as `course/PRACTICE/02-knowledge-bases/what-is-lint.md`. Short forms and bare file names fail. Bare wikilinks never resolve into `research/externalReferences/UnlearGestaltungAI_Mainz`. Use `--decks-only` to run only the deck-note check. If you change the checker, run `python course/scripts/test_check_course_links.py`.
2. For code under `course/SESSIONS/lectures/**/`, do not run generators that rebuild decks unless asked.
   If a deck note names a wrong path, change only the note text inside the `.pptx` or `.odp` package (ZIP/XML level) and leave every other entry unchanged. `course/scripts/deck_note_paths.py` holds the shorthand-to-exact path map that `build_deck.py` and `patch_lecturer_edit.py` use. Write new note paths in full in the generators too.
   The course map is not a deck. Run `python course/scripts/generate-course-map.py --check` after you change a page title, status or location. It writes nothing. If it reports STALE, regenerate with `python course/scripts/generate-course-map.py --verified-on YYYY-MM-DD` and use today's date. An invalid date stops the script and leaves the map unchanged.
3. Report changed files and remaining risks.
4. Stop after three failed repair attempts on the same check.

## Course stack defaults

The technical object for students is a student-designed agentic production system. The required work is `course/PROJECT-WORK/01_minimum-path.md`: a personal manifesto, a knowledge store, an access boundary, a model endpoint, a tool set, a verification method, provenance, and a critical reflection. Input presentations are also required. No purchase is required. Alternatives are allowed.

The names below are one *reference implementation* for class demos. They are not the assessed architecture. Claude Code, Cursor, OpenCode, local scripts, and other agents are valid systems.

- Reference implementation for class demos: **Hermes Agent** (MIT). Cursor, Claude Code, and OpenCode are valid systems for repo work.
- Notes example: Obsidian vault + phone sync (see `course/PRACTICE/02-knowledge-bases/howto-obsidian-setup-and-sync.md`). A plain Markdown folder meets the knowledge store.
- Hermes beginner install: pick your OS guide under `course/PRACTICE/01-harness-and-agents/` (`install-windows.md`, `install-mac.md`, `install-linux.md`). Advanced: providers, config, local models, Docker, safe-install rules.
- Coding harness example: `course/PRACTICE/01-harness-and-agents/howto-hermes-efficient-coding.md`.
- Comparison: `course/PRACTICE/01-harness-and-agents/hermes-vs-coding-agents.md`.

## Modes (when coding on a student project)

State the mode in the first message:

| Mode | Use when | Rules |
|---|---|---|
| **coding** | New feature or experiment | Small slices, tests if present, repair limit 3 |
| **production** | Shared or shipping work | Stricter: no drive-by refactors, full verify, human approval before push |
| **hybrid** | Mixed research + code | Separate vault/wiki notes from code edits; do not mix private notes into the repo |

## Completion report

Task:  
Changed files:  
Checks (PASS/FAIL):  
Remaining risks:  
Human approval required:
