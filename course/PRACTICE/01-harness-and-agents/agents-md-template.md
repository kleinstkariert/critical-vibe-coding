---
title: Template. AGENTS.md for student projects
date: 2026-11-18
tags:
  - course
  - howto
  - harness
status: current
canonical: true
---

# Template: `AGENTS.md` for your project

*reference implementation. Optional extension. Not required for assessment.* `AGENTS.md` is one way to state rules. It is not required. See [minimum path](../../PROJECT-WORK/01_minimum-path.md).

Copy this file to the **root of your project repo** as `AGENTS.md`.  
Hermes (and many coding agents) load it automatically. See [howto hermes efficient coding](howto-hermes-efficient-coding.md).

Course repo example: repository root `AGENTS.md`.

---

```markdown
# Project rules for agents

Read this file before editing.

Inspect the repository before creating a plan.

Create a plan with a maximum of five steps.

Change only files in the task scope.

Do not read secret files (`.env`, credentials, SSH keys).

Do not delete files without approval.

Run the project verification command after each meaningful change
(example: `scripts/verify` or your real test command).

Do not claim completion without command output.

Stop after three failed repair attempts.

Review the Git diff before completion.

## Stack (fill in)

- Language / framework:
- Format command:
- Test command:
- Build / export command:
- Folders agents may write:
- Folders that are human-only:

## Mode

Say which mode this task uses: **coding** | **production** | **hybrid**.

- coding: small slices, verify after each slice
- production: no drive-by refactors; human approval before push
- hybrid: keep research notes out of the code tree unless the task says otherwise

## Completion report

Task:
Changed files:
Checks:
- Format:
- Tests:
- Build:
- Git diff:
Remaining risks:
Human approval required:
```
