---
title: Install guide. Windows
date: 2026-11-25
tags:
  - course
  - howto
  - install
  - windows
status: current
canonical: true
---

# Install guide. Windows

Follow this file from top to bottom. Do not open the Linux or macOS guides.

## Before you start

- Windows 11, version 22H2 or later. Press the Windows key and R together, type `winver`, and press Enter.
- Use a normal terminal. Do not choose "Run as administrator". An account in the Administrators group is fine with UAC on. Hermes needs no administrator rights.
- Work only in the test folder `hermes-smoke-test` (section 3). Do not use Documents, the Desktop, or your vault.
- About 5 GB of free disk space (not verified).
- Safety rules, UAC facts, checks and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#windows-details). Why this order: [install why](install-why.md).

## 1. Install Hermes Desktop

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

1. Open https://hermes-agent.nousresearch.com/desktop. The host in the address bar must be `hermes-agent.nousresearch.com`. STOP if it is another host.
2. Click the Microsoft Store button. If the Store is blocked on your laptop, click the main download button. It gives you an `.appinstaller` file. The exact label of that button is not verified.
3. Do not click "Download .exe instead". That file builds Hermes from source. It takes much longer.
4. For the `.appinstaller` file, open it with Windows App Installer. The publisher must be Nous Research. STOP if it is another name. If App Installer says sideloading is blocked, STOP and use the Store button. Do not change a policy.
5. STOP if a UAC prompt appears during the install. Click No. No official page says Hermes Desktop needs one.
6. Open Hermes from the Start menu, as a normal user.
7. On first start, Hermes asks you to choose a layout and a provider. Choose Basic. "Choose provider later" is fine. You set the key in section 2.

Hermes keeps its files in `%LOCALAPPDATA%\hermes\`. For the Store package this is not verified on a real machine. Older Windows, or no Store: [advanced Hermes config](howto-hermes-advanced-config.md#windows-cli).

## 2. Add an OpenRouter key

The class default is OpenRouter with a free model. No card is needed for model ids that end in `:free`. Create a key at https://openrouter.ai/settings/keys. Free models: 20 requests a minute and 50 a day. Your prompts may be logged. Use public text only. [Free models](https://openrouter.ai/collections/free-models)

1. In Hermes Desktop, open **Settings**, then **Providers**, then **OpenRouter**.
2. Add your API key. Paste the key. Do not type it in a shell command.
3. Choose a small free model that says it supports tools. A class example is `nvidia/nemotron-3-ultra-550b-a55b:free` (not verified on every build). Tell the teacher the name you chose.

Menu labels: **Settings → Providers → OpenRouter → add API key**. Exact wording on screen is not verified. Other providers, cards, and limits: [providers and keys](howto-hermes-providers-and-keys.md). Terminal or `.env` file: that page only.

Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets).

## 3. First chat and smoke test

This test checks the model and one file read. It does not use your notes.

1. Click the Start button, type `Windows Terminal`, and press Enter. If it is not in the list, type `PowerShell` and press Enter. Do not start it as Administrator.
2. Type this block and press Enter:

```powershell
New-Item -ItemType Directory -Force "$HOME\hermes-smoke-test" | Out-Null
Set-Content -Path "$HOME\hermes-smoke-test\note.txt" -Value "The smoke test file says hello."
Write-Output "$HOME\hermes-smoke-test\note.txt"
```

3. Select the path that the last line prints and copy it.
4. In Hermes, open a new chat. Paste this request. Put your copied path in place of PATH: Read only this file: PATH. Reply with the one sentence in that file. Do not open any other folder.
5. The reply must be: The smoke test file says hello. If Hermes names your vault or another folder, STOP and tell the teacher.

If you prefer File Explorer: click the address bar, type `%USERPROFILE%`, press Enter, then create the folder `hermes-smoke-test` and the file `note.txt` there. Windows may hide file extensions, so check that the name is not `note.txt.txt`.

You are done for class when the reply is correct.

## Next steps (advanced)

One short line each. Do these at home, or when the teacher says so.

- Local models: [howto local models](../03-models-and-providers/howto-local-models.md)
- Obsidian and phone sync: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md)
- MCP examples (vvvv): [howto example mcp servers](../06-mcp-and-tools/howto-example-mcp-servers.md)
- Docker sandbox: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)
- Efficient coding harness: [howto hermes efficient coding](howto-hermes-efficient-coding.md)
- CLI install, vault paths, skills, gateway: [advanced Hermes config](howto-hermes-advanced-config.md)
- Providers and keys (all rows, `.env`): [providers and keys](howto-hermes-providers-and-keys.md)
- Uninstall and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall)
- Why this order: [install why](install-why.md)
