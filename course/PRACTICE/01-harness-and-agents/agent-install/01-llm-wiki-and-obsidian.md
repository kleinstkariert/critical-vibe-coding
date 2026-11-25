---
title: Agent. LLM Wiki and Obsidian
date: 2026-11-25
status: current
canonical: true
---

# Agent. LLM Wiki and Obsidian

Do not use Program Files or a private vault.

## Paths (class default)

| OS | Vault folder |
|---|---|
| Windows | `%USERPROFILE%\workspaces\llm-wiki\vault` → `C:\Users\<username>\workspaces\llm-wiki\vault` |
| macOS | `~/workspaces/llm-wiki/vault` → `/Users/<username>/workspaces/llm-wiki/vault` |
| Linux | `~/workspaces/llm-wiki/vault` → `/home/<username>/workspaces/llm-wiki/vault` |

Why: user space. No admin or root for agent writes.

## Create folder

Windows (normal PowerShell, not Administrator):

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\workspaces\llm-wiki\vault" | Out-Null
```

macOS / Linux:

```bash
mkdir -p "$HOME/workspaces/llm-wiki/vault"
```

## Obsidian

1. Install Obsidian: https://obsidian.md/download
2. Open folder as vault (label not verified): select the `vault` folder above.
3. Optional tree: [starter knowledge base](../../02-knowledge-bases/starter-knowledge-base.md)

## Hermes env (same path for both keys)

Official: `WIKI_PATH` for LLM Wiki. Set `OBSIDIAN_VAULT_PATH` to the **same** folder if Obsidian skill is used. Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-llm-wiki

| OS | Env file |
|---|---|
| Windows | `%LOCALAPPDATA%\hermes\.env` |
| macOS / Linux | `~/.hermes/.env` |

```env
OBSIDIAN_VAULT_PATH=<absolute-path-to-vault>
WIKI_PATH=<absolute-path-to-vault>
```

- Absolute path only. No `$VAR` inside path args.
- Save. Restart Hermes.

## Skill install

```bash
hermes skills install official/research/llm-wiki
hermes skills list
```

Check: list shows `llm-wiki` (display name not verified).

## STOP

- STOP if path is Program Files, Documents, Desktop, or a private vault.
- STOP if Hermes names a private vault.
