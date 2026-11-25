---
title: How-to. Advanced Hermes config
date: 2026-11-25
tags:
  - course
  - howto
  - hermes
  - advanced
status: current
canonical: true
---

# How-to. Advanced Hermes config

*optional extension.* *not required for assessment.* Beginners: follow your OS install guide first. This page holds CLI install details, vault paths, skills, and the messaging gateway pointer.

Related: [providers and keys](howto-hermes-providers-and-keys.md) · [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md) · [efficient coding](howto-hermes-efficient-coding.md) · [Docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)

Official install matrix: https://hermes-agent.nousresearch.com/docs/getting-started/installation

## Read the installer before you run it

A pipe sends a downloaded script straight into a shell. Use the inspectable path (save the script, read it, then run it). The Hermes install page does not publish a checksum for `install.sh` or `install.ps1`. This course does not invent one.

While you check, look for `curl`, `irm`, and `git clone` lines. The host should be `hermes-agent.nousresearch.com`, `hermes-assets.nousresearch.com`, `github.com`, `api.github.com`, or `raw.githubusercontent.com/NousResearch/hermes-agent`. STOP if you see a different host. Official domains: https://hermes-agent.nousresearch.com/docs/getting-started/official-domains

## Windows CLI

Use this when Desktop (Store or `.appinstaller`) is not available. Windows 10 source-script support does not mean the MSIX package supports Windows 10. Details: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#windows-details).

1. Open a normal Windows Terminal. Do not start it as Administrator.
2. The host must be `hermes-agent.nousresearch.com`. STOP if it is not.

### Path A. Convenience

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

### Path B. Inspectable (prefer this)

```powershell
cd $HOME
curl.exe -fsSL https://hermes-agent.nousresearch.com/install.ps1 -o install.ps1
Select-String -Path .\install.ps1 -Pattern 'https?://[A-Za-z0-9.-]+' -AllMatches | ForEach-Object { $_.Matches.Value } | Sort-Object -Unique
```

Expected hosts on 25 Nov 2026: `https://api.github.com`, `https://github.com`, `https://hermes-assets.nousresearch.com`. STOP if you see any other host. Then:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -SkipComputerUse
```

Close the terminal, open it again, and type `hermes --help`.

What the Windows script changes (checked 20 Nov 2026): program files in `%LOCALAPPDATA%\hermes\hermes-agent\`, commands in `%LOCALAPPDATA%\hermes\bin\`, data in `%LOCALAPPDATA%\hermes\`, and that `bin` folder on your user `Path`.

Uninstall: `hermes uninstall --dry-run`, then `hermes uninstall`. Use `hermes uninstall --full` only when you also want the data folder deleted. A Store or MSIX app is removed in Settings, Apps, Installed apps. Docs: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native

## macOS and Linux CLI

Desktop on macOS is Apple Silicon only. Intel Macs and Linux use this CLI path. Linux beginner install already covers path B; this section is the shared detail.

### Path A. Convenience

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Do not type `sudo` before that line.

### Path B. Inspectable (prefer this)

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o install.sh
less install.sh
bash install.sh
```

Then: `source ~/.zshrc` (macOS zsh) or `source ~/.bashrc` (Linux bash). Type `hermes --help`.

What the script changes (checked 20 Nov 2026): program files in `~/.hermes/hermes-agent/`, command in `~/.local/bin/hermes`, data in `~/.hermes/`, and a PATH line in the shell profile. `.env` is set to owner-only access (mode 600).

Uninstall: `hermes uninstall --dry-run`, then `hermes uninstall`. Use `hermes uninstall --full` only when you also want `~/.hermes/` deleted. Docs: https://hermes-agent.nousresearch.com/docs/getting-started/updating

Optional: `hermes desktop` after CLI install when a Desktop build exists for your machine.

**WSL2:** use the Linux install script inside WSL. Keep vault and Hermes both inside WSL or both on Windows native, not half-and-half (*technical suggestion*).

**Docker (server):** https://hermes-agent.nousresearch.com/docs/user-guide/docker · class sandbox path: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)

## Point Hermes at a wiki folder

Do this after the smoke test works. Phone sync stays in [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md).

| Platform | Env file | Example |
|---|---|---|
| Windows | `%LOCALAPPDATA%\hermes\.env` | `WIKI_PATH=C:\path\to\MyVault\wiki` |
| macOS / Linux | `~/.hermes/.env` | `WIKI_PATH=/path/to/MyVault/wiki` |

```env
OBSIDIAN_VAULT_PATH=/absolute/path/to/MyVault/wiki
WIKI_PATH=/absolute/path/to/MyVault/wiki
```

- Use a real absolute path. File tools do not expand `$OBSIDIAN_VAULT_PATH` in path arguments.
- Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.
- A folder name is not a security boundary. Access table: [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).
- A full-vault path is convenience mode, not recommended for private material.
- Restart Hermes after you change `.env`.
- Optional skill: `hermes skills install official/research/llm-wiki`

## Skills (short)

```bash
hermes skills list
hermes skills browse
hermes skills install official/research/arxiv
```

In chat: `/skills`. Review third-party skills before install. Guide: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills · Coding harness: [howto hermes efficient coding](howto-hermes-efficient-coding.md)

## Messaging gateway (optional)

```bash
hermes gateway setup
```

Do not set up a gateway in class. Always set allowlists on a personal laptop. Rules: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#7-the-messaging-gateway). Docs: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/

## Common mistakes

1. Confusing Hermes Agent with Hermes 4 model weights.
2. Relative paths or `$OBSIDIAN_VAULT_PATH` inside tool calls.
3. Expecting Hermes on the phone. Notes sync via Obsidian; the agent stays on the computer.
4. Two writers on the same note (Obsidian and Hermes) without clear folders.
5. Pointing `WIKI_PATH` at a Joplin database: wrong store. See [knowledge store options](../02-knowledge-bases/knowledge-store-options.md).
6. macOS Desktop on Intel: unsupported; use the CLI above.
7. WSL and a Windows vault without one clear home for the files.

## Beginner entry

- [install windows](install-windows.md) · [install mac](install-mac.md) · [install linux](install-linux.md)
- [install why](install-why.md)
