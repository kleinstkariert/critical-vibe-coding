---
title: AGENTS.md. Critical Vibe Coding course repo
date: 2026-11-18
---

# Project rules for agents

This repository is the **student course pack** for Critical Vibe Coding (Interface Cultures).

Read this file before editing.

## Scope

- Prefer edits under `course/` for student-facing materials.
- Do not rewrite Sebastian’s authored overview prose in `course/setup/Local LLM Coding with Hermes.md` unless he asks.
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
2. For code under `course/lectures/**/`, do not run generators that rebuild decks unless asked.
3. Report changed files and remaining risks.
4. Stop after three failed repair attempts on the same check.

## Course stack defaults

- Default agent runtime for students: **Hermes Agent** (MIT), with optional Cursor / Claude Code for deep repo coding.
- Notes: Obsidian vault + phone sync (see `course/setup/howto-obsidian-setup-and-sync.md`).
- Install: `course/setup/howto-hermes-setup.md`.
- Coding harness: `course/setup/howto-hermes-efficient-coding.md`.
- Comparison: `course/concepts/hermes-vs-coding-agents.md`.

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
