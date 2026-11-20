---
title: Starter knowledge base
date: 2026-11-20
tags:
  - course
  - howto
  - llm-wiki
---

# Starter knowledge base

Copy this tree into your vault. It is a starter. It does not replace [[llm-wiki-standard-files]] or [[knowledge-store-options]].

## First suggestion

Start from the Wanderloots LLM Wiki examples. Callum (Wanderloots) shows three layers in public: raw sources, wiki pages, and a schema that is the contract with the agent. The tree below is a copy of that split. It is not a copy of his private vault.

- How to build it: https://www.youtube.com/watch?v=QbjAQFJJyt0
- Channel already cited in this repo: https://www.youtube.com/@Wanderloots/videos ([[Local LLM Coding with Hermes]] §15)

The same three jobs are the Karpathy pattern. Primary source, already in this repo: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f · [[../syllabus/references]]

[[llm-wiki-standard-files]] is the Hermes file list for those jobs. This page nests the wiki pages under `wiki/`, which matches the Wanderloots split between raw and wiki. Use one layout. Do not mix both trees in one folder.

Where notes may live, and why phone sync is required: [[knowledge-store-options]].

## Copy this tree

```text
MyVault/
  SCHEMA.md
  index.md
  log.md
  raw/
    articles/
    papers/
    transcripts/
    assets/
  wiki/
    entities/
    concepts/
    comparisons/
    queries/
  private/
    journal/
    health/
    finance/
```

Create the folders before you point Hermes at the vault. Empty folders are fine. Put one line in `index.md`: "Map of this vault." Put one line in `log.md`: "Log starts here."

## Who may read what

Folder names are not a lock. The course states that in [[Local LLM Coding with Hermes]] §10. This table is the rule you also write into `SCHEMA.md`.

| Path | Agent | You |
|---|---|---|
| `raw/` | May read. Must not edit. | You add sources. |
| `wiki/` | May read and write. | You review the diff. |
| `SCHEMA.md` | May read. Must ask before an edit. | You own the rules. |
| `index.md`, `log.md` | May update when it changes the wiki. | You can correct them. |
| `private/` | Must not read. Must not write. | Journal, health, and finance stay here. |
| Keys, passwords, `.env` | Must not read. | Do not put them in the vault, including `private/`. |

Point `WIKI_PATH` at `MyVault/wiki`. The path steps are in [[howto-hermes-setup]] §4. A full-vault path is convenience mode, not recommended for private material.

## SCHEMA.md stub

Copy this into `MyVault/SCHEMA.md`. Then stop. The longer rules stay in the links.

```markdown
# Schema

Domain: my course notes and project facts.

The agent may read and write: wiki/
The agent may read, and must not edit: raw/
The agent must not read: private/

Do not read secret files (.env, keys, passwords).
Do not put secrets in this vault.
Do not delete files without approval.
Do not run as root.
Do not expose the gateway.
Stop after three failed repair attempts.
Ask before a command that deletes, sends, or installs.

Access table: see the course starter page that this file was copied from.
```

Links for those lines, without pasting them again:

- [AGENTS.md](../../AGENTS.md) · [[agents-md-template]]
- [[howto-hermes-setup]] §5d
- [[howto-hermes-docker-sandbox]]
- [[Local LLM Coding with Hermes]] §§9 to 14
- [[howto-hermes-efficient-coding]]
