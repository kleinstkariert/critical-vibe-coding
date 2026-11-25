---
title: How-to. Pair Hermes and OpenCode
date: 2026-11-18
tags:
  - course
  - howto
  - hermes
  - opencode
  - pairing
status: current
canonical: true
---

# How-to. Pair Hermes and OpenCode

*reference implementation. Advanced path. Not required for assessment.* Pairing is one option. OpenCode alone is a valid system. See [minimum path](../../PROJECT-WORK/01_minimum-path.md).

Use **Hermes** as the always-on assistant. Use **OpenCode** when a repository needs a strong coding loop.

Setup notes: [Windows](install-windows.md) · [macOS](install-mac.md) · [Linux](install-linux.md) · [howto opencode setup](howto-opencode-setup.md)  
Concept: [hermes vs coding agents](hermes-vs-coding-agents.md)

Source types: [references](../../REFERENCES/bibliography.md#source-types). A label names the source kind. It is not independent verification. Labels: *technical suggestion*.

---

## Split of work

| Job | Prefer |
|---|---|
| Chat, notes, vault, messaging, MCP tools | **Hermes** |
| 24/7 assist on your machine | **Hermes** |
| Deep edit / refactor / review in a large repo | **OpenCode** (or another coding agent) |
| Short shell or file task | Either; keep Hermes for small work |

Hermes is multipurpose. OpenCode is coding-first. Do not force one tool to do the other job.

---

## Recommended pattern

1. Plan and gather context in **Hermes** (vault, tickets, design notes).
2. Hand the coding task to **OpenCode** in the repo folder.
3. Let OpenCode edit, run, and report diffs.
4. Bring results back to Hermes for notes, wiki pages, or student handoff.

### From Hermes with the OpenCode skill

```bash
hermes skills install official/autonomous-ai-agents/opencode
```

Then ask Hermes to run a bounded coding job. Hermes can call `opencode run "…"`, watch longer sessions, and summarise changes.

*technical suggestion:* keep the first handoff small (one file or one failing test). Grow the task after you trust the loop.

### Side by side (no skill)

1. Keep Hermes open for research and messaging.
2. Open a terminal in the repo and run `opencode`.
3. Paste goals from Hermes into OpenCode.
4. Paste OpenCode summaries back into Hermes or the vault.

---

## What not to do

- Do not put API keys in the Obsidian vault.
- Do not run two agents that write the same files at the same time.
- Do not use OpenCode as your only note system. Keep notes in the vault.
- Do not expect Hermes alone to match a coding-agent IDE loop on a large repo.

---

## Quick check

- [ ] Hermes works for daily assist and MCP
- [ ] OpenCode opens the target repo
- [ ] One clear owner per file change
- [ ] Results land in git + vault notes

---

## Sources

- [howto opencode setup](howto-opencode-setup.md)
- [Windows](install-windows.md) · [macOS](install-mac.md) · [Linux](install-linux.md)
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-opencode
- https://opencode.ai/docs/
