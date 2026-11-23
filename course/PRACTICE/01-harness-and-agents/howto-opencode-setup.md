---
title: How-to. OpenCode setup
date: 2026-11-18
tags:
  - course
  - howto
  - opencode
  - coding-agent
audience: student
status: current
canonical: true
---

# How-to. Set up OpenCode

*optional extension.* OpenCode is a valid system. It is *not required for assessment*. See [minimum path](../../PROJECT-WORK/minimum-path.md).

OpenCode is an **open-source coding agent** (MIT) by Anomaly. It is built for work inside a code repository: edits, diffs, commands, and review.

This is **not** Hermes. Hermes is a multipurpose agent harness. OpenCode is a coding-first loop. Pair them: [howto hermes opencode pairing](howto-hermes-opencode-pairing.md).

Source types: [references](../../REFERENCES/bibliography.md#source-types). A label names the source kind. It is not independent verification. Labels: *technical suggestion*. Check current docs when versions change.

Official site: https://opencode.ai  
Docs: https://opencode.ai/docs/  
GitHub: https://github.com/anomalyco/opencode

---

## 1. What OpenCode is

| | |
|---|---|
| **Product** | Open-source AI coding agent (terminal, desktop, web) |
| **Job** | Deep work in a repo: implement, refactor, review |
| **Models** | Many providers, including local. Configure with `/connect` |
| **Licence** | MIT (*institutional summary* from project docs) |

Built-in agents (switch in the UI):

- **build**: full access for development work (default)
- **plan**: read-only analysis; asks before bash

Docs: https://opencode.ai/docs/ · https://opencode.ai/terminal

---

## 2. Install (current paths)

Prefer the official install page for your OS: https://opencode.ai/docs/

### CLI (common)

```bash
# curl installer (macOS / Linux; check docs for your OS)
curl -fsSL https://opencode.ai/v2/install | bash
```

```bash
# npm (also used on Windows when package managers are limited)
npm install -g @opencode/cli
```

```bash
# Homebrew (macOS / Linux)
brew install anomalyco/tap/opencode-v2
```

Standalone binaries and Desktop downloads: https://opencode.ai/docs/ and https://opencode.ai/download

*institutional summary (OpenCode docs):* Windows package managers are not supported the same way; use the npm path or a standalone Windows binary from the docs.

After install, open a **new** terminal and check:

```bash
opencode --version
```

---

## 3. First run

1. Go to a git project folder.
2. Start OpenCode:

```bash
opencode
```

Or point at another folder:

```bash
opencode ~/code/my-project
```

3. Connect a model provider in the TUI:

```text
/connect
```

4. Try a small read-only ask first (use **plan** if you want fewer write risks).
5. For one-shot scripts:

```bash
opencode run "Explain this repository"
```

Optional Desktop app: download from the OpenCode site. Same agent family as the CLI.

---

## 4. How Hermes talks to OpenCode

Hermes can **hand coding work** to OpenCode through an official optional skill.

Install the skill in Hermes:

```bash
hermes skills install official/autonomous-ai-agents/opencode
```

Skill docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-opencode

Then Hermes can:

- run bounded jobs with `opencode run "…"`
- start longer OpenCode sessions and watch progress
- report file changes and next steps back to you

You still need OpenCode installed and authenticated on that machine.

Hermes compare page also notes OpenCode Zen / OpenCode Go as model providers in some setups. That is separate from the coding CLI skill. Prefer the skill for **repo coding handoff**.

Practical pairing: [howto hermes opencode pairing](howto-hermes-opencode-pairing.md)

---

## 5. Course checklist

- [ ] `opencode --version` works
- [ ] Provider connected (`/connect` or env keys)
- [ ] You can open a project and get a reply
- [ ] Optional: Hermes OpenCode skill installed
- [ ] Keys stay out of the Obsidian vault

---

## Sources

- https://opencode.ai/docs/
- https://opencode.ai/terminal
- https://github.com/anomalyco/opencode
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-opencode
- https://hermes-agent.nousresearch.com/compare
