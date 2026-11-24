---
title: How-to. Hermes for efficient coding
date: 2026-11-18
tags:
  - course
  - howto
  - hermes
  - harness
  - coding
status: current
canonical: true
---

# How-to. Set up Hermes for efficient coding

*reference implementation. Advanced path. Not required for assessment.* This page is one Hermes coding example. See [minimum path](../../PROJECT-WORK/01_minimum-path.md).

Complement to [howto hermes setup](howto-hermes-setup.md). That guide installs Hermes. This guide sets a **coding harness**: project rules, verification, skills, and repair limits.

Source types: [references](../../REFERENCES/bibliography.md#source-types). A label names the source kind. It is not independent verification. Labels: *technical suggestion*. Writing style target: STE ~80%.

Related: [02 agent harness and wiki architecture](../../SESSIONS/02-agent-harness-and-wiki-architecture.md) · [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) · [howto local llm hardware](../04-local-and-cloud/howto-local-llm-hardware.md) · [agents md template](agents-md-template.md) · course root `AGENTS.md`

---

## 0. Goal

You want the agent to:

1. Inspect the repo before it edits.
2. Change a small scope.
3. Run project checks after each meaningful change.
4. Repair a limited number of times.
5. Show command output before it claims success.
6. Stop for human review of the Git diff.

This matches harness practice (rules + mechanical checks), not "better prompting alone".

### Harness loop (short)

```text
task → plan → one edit → verify → repair (≤3) → Git diff → human approve
```

If verify fails three times, stop and report. Do not keep guessing.

### Modes (state one at the start of a task)

| Mode | When | Extra rules |
|---|---|---|
| **coding** | Features, experiments, class exercises | Small slices; run verify after each slice |
| **production** | Shared repos, demos, anything you ship | No drive-by refactors; full verify; human approval before push |
| **hybrid** | Research notes + code in one session | Keep vault/wiki notes out of the code tree unless the task says to commit them |

Put the mode line in `AGENTS.md` or in the first chat message. Template: [agents md template](agents-md-template.md).

---

## 1. Install Hermes first

Follow [howto hermes setup](howto-hermes-setup.md) until `hermes` runs and a model answers.

Minimum for coding agents (*technical suggestion*):

- A model with **tool calling**
- Context window **≥ 64 000** tokens (Hermes agent work)
- Keys only in `%LOCALAPPDATA%\hermes\.env` (Windows) or `~/.hermes/.env`

---

## 2. Project context file (`AGENTS.md`)

*institutional summary:* Hermes loads project context files. Priority (first match wins among project types): `.hermes.md` → `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`. Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files

Create `AGENTS.md` at the repo root:

```markdown
# Project rules for agents

Read this file before editing.

Inspect the repository before creating a plan.

Create a plan with a maximum of five steps.

Change only files in the task scope.

Do not read secret files (`.env`, credentials, SSH keys).

Do not delete files without approval.

Run the project verification command after each meaningful change.

Do not claim completion without command output.

Stop after three failed repair attempts.

Review the Git diff before completion.
```

Add stack facts the agent must not invent (test command, formatter, build command).

---

## 3. Verification entry point

Create one command the agent always runs. Example name: `scripts/verify` (or `scripts/verify.ps1` on Windows).

The script should call **this** project's tools:

1. Format check
2. Static / type check (if you have one)
3. Tests
4. Build or export (if relevant)
5. Print PASS or FAIL per step

Do not invent a universal language stack. Wire what the repo already uses.

Evidence rule for the agent:

```text
You have three repair attempts.
Run the failed check after each repair.
Stop after the third failed attempt.
Report the remaining problem with command output.
```

Research support (*claim* from training literature, not a Hermes product feature): agents improve when they use execution feedback and when verification can tell a good patch from a bad one. See Mohsin et al., *Teaching Agents to Code Reliably*, arXiv:2610.03984.

---

## 4. Skills to install (optional, useful)

Skills are on-demand packages. Guide: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills

### Bundled / hub (Hermes)

```bash
hermes skills list
hermes skills browse
# examples (names change; search first):
hermes skills install official/research/arxiv
```

Useful coding-related patterns once installed or available:

| Skill / plugin | Why |
|---|---|
| Planning / `/plan`-style skills | Force a short plan before edits |
| GitHub PR workflow skills | Branch, commit, PR with checks |
| Project-local skills under `~/.hermes/skills/coding/` | Your verify + repair loop |

Creating skills: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills

### Community coding workflows (review before trust)

*technical suggestion:* marketplace plugin with planning / dual-model / subagent patterns:

```bash
hermes plugins install singhguri/hades-coding-workflows --enable
```

Marketplace page: https://hermes-agent.nousresearch.com/marketplace/hades-coding-workflows

Skills inside (namespaced), including:

- `dual-model-harness`
- `subagent-driven-development`
- `writing-plans`

**Security:** review every third-party skill and plugin. Prefer Skills Guard / hub trust levels. Do not install scripts you did not read.

### Harness pattern library (cross-tool)

Practical field guide (Claude-oriented plugin, but the **rules and hooks** transfer):

- https://github.com/q-qp-p/jrenaldi79-harness-engineering
- Teacher vault clipping: the jrenaldi79 harness engineering README.

Core idea: mechanical enforcement (hooks, linters, tests) beats long prose instructions alone (Karpathy: agents often ignore written rules).

---

## 5. Execution backend for coding

| Backend | When |
|---|---|
| `local` | Trusted personal project only (no isolation) |
| `docker` | Default *technical suggestion* for untrusted or third-party code |
| `ssh` / cloud sandbox | Stronger separation from your laptop |

Secure laptop guide: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine  
Security overview: https://hermes-agent.nousresearch.com/docs/user-guide/security

Laptop checklist:

1. Approvals: prefer `manual` on a machine with employer or personal secrets
2. `HERMES_WRITE_SAFE_ROOT` for the project (+ Hermes home if needed)
3. Do not mount the full Obsidian vault into a coding container
4. Messaging gateway: allowlists / pairing only

---

## 6. Suggested coding skill layout (local)

Mirror the course overview structure if you build your own:

```text
~/.hermes/skills/
├── coding/
│   ├── verified-coding/SKILL.md
│   ├── repository-inspection/SKILL.md
│   ├── test-and-repair/SKILL.md
│   └── git-diff-review/SKILL.md
└── security/
    └── sandboxed-coding/SKILL.md
```

Each `SKILL.md` needs: purpose, inputs, allowed files/commands, checks, forbidden actions, repair limit, approval points, output format.

---

## 7. Session recipe (efficient loop)

1. Open the project directory as the Hermes working directory.
2. Confirm `AGENTS.md` loaded (ask Hermes what project rules it sees).
3. Load a coding skill if you use one (`/skills` or `skill_view(...)`).
4. State acceptance conditions in the first message.
5. Approve the short plan.
6. Let it edit one slice → run `scripts/verify` → repair ≤3 times.
7. You read the diff. You decide merge.

Optional: enable checkpoints (`hermes chat --checkpoints` or config) so `/rollback` can undo file damage.

---

## 8. What “efficient” means here

Efficiency is not “faster tokens”.

For this course it means:

- Fewer wasted retries (clear acceptance + repair limit)
- Checks that can **fail** a wrong patch (differential / project tests)
- Skills that load only when needed (progressive disclosure)
- Structure on disk (`AGENTS.md`, wiki, verify script) that survives the chat scrollback

Session 02 places the same bet: **wiki + schema + tools** before model shopping.

---

## 9. Checklist

- [ ] Hermes install done ([howto hermes setup](howto-hermes-setup.md)), Desktop or CLI
- [ ] Model has tool calling + large enough context
- [ ] `AGENTS.md` (or `.hermes.md`) at repo root ([agents md template](agents-md-template.md))
- [ ] One verify command the agent must run
- [ ] Repair limit stated (default: 3)
- [ ] Mode stated: coding / production / hybrid
- [ ] Secrets out of the vault
- [ ] Backend chosen for this machine (`local` vs Docker)
- [ ] Third-party skills reviewed
- [ ] You reviewed the Git diff before accepting work

## 10. Measurement checklist (did the harness help?)

Use this after a coding session (*technical suggestion*):

| Check | Pass if |
|---|---|
| Plan first | Agent produced a ≤5-step plan before edits |
| Scope | Diff touches only agreed paths |
| Verify | Project checks ran after meaningful edits |
| Evidence | Completion claim includes command output |
| Repair limit | Stopped by attempt 3 on the same failure |
| Human gate | You read the Git diff before merge/push |
| Secrets | No keys landed in notes or commits |
| Mode | coding / production / hybrid was explicit |

If most rows fail, fix `AGENTS.md` and `scripts/verify` before you chase a bigger model.

---

## Sources

| What | Link |
|---|---|
| Hermes install (course) | [howto hermes setup](howto-hermes-setup.md) |
| Hermes docs | https://hermes-agent.nousresearch.com/docs/ |
| Context files | https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files |
| Skills guide | https://hermes-agent.nousresearch.com/docs/guides/work-with-skills |
| Creating skills | https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills |
| Security | https://hermes-agent.nousresearch.com/docs/user-guide/security |
| Secure on a work/personal machine | https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine |
| Local models | https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Hades coding workflows plugin | https://hermes-agent.nousresearch.com/marketplace/hades-coding-workflows |
| Harness engineering README | https://github.com/q-qp-p/jrenaldi79-harness-engineering |
| Mohsin et al. 2026 (arXiv) | https://arxiv.org/pdf/2610.03984 |
| LangChain: Anatomy of an agent harness | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness |
| Karpathy LLM Wiki gist | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Course overview (vault) | `Local LLM Coding with Hermes.md` |
