---
title: Agent. AGENTS.md and safety
date: 2026-11-25
status: current
canonical: true
---

# Agent. AGENTS.md and safety

Human detail: [safe install rules](../../05-security-and-privacy/howto-hermes-safe-install-rules.md) · template: [agents-md-template.md](../agents-md-template.md)

## AGENTS.md

1. Copy [agents-md-template.md](../agents-md-template.md) to project root as `AGENTS.md`.
2. Hermes loads (first match): `.hermes.md` → `AGENTS.override.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules`. Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files
3. Fill stack, write folders, human-only folders, verify command.
4. State mode: `coding` | `production` | `hybrid`.
5. Check: ask Hermes which project rules it sees.

## Safety (imperative)

- Work only in the class vault: `%USERPROFILE%\workspaces\llm-wiki\vault` or `~/workspaces/llm-wiki/vault`.
- Do not read `.env`, credentials, SSH keys, or private vaults.
- Do not write secrets into the vault or into chat.
- Do not run Hermes as Administrator or as root.
- Do not expose the messaging gateway in class.
- Approvals: `hermes config set approvals.mode manual`. Never set `off`. Default is `smart`.
- File writes have no approval prompt. Snapshot or Git commit before write tasks. Check the diff after.
- Stop after three failed repair attempts.
- Prefer read-only first. Name folders in the request.

## STOP

- STOP if asked to touch Program Files or a private vault.
- STOP if asked to paste an API key into a shell command.
- STOP if a UAC / sudo prompt appears for Hermes itself.