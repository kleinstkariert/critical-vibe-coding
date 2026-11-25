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
- Do not point Hermes at Program Files, Documents, Desktop, or a private vault. The class folder is `%USERPROFILE%\workspaces\llm-wiki\vault` (section 4).
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

## 2. Add a free model path

Hermes setup can offer a free start with the `nous/welcome` model (no account, no API key, once per OS user, when you answer setup in a terminal; not in a container, CI, or scripted run; shown only when available). Source: Hermes Quickstart, checked 25 Nov 2026: https://hermes-agent.nousresearch.com/docs/getting-started/quickstart. Use that for the first chat if it appears.

**Optional and visible (best privacy):** run a model on your machine. In Hermes Desktop open **Settings → Providers → Local Models**, install the runtime, download a model that fits, then click **Use**. Full steps: [howto local models](../03-models-and-providers/howto-local-models.md). Do this after the smoke test if class time is short. Local models stay optional for assessment.

**Class cloud path:** OpenRouter free models (ids that end in `:free`). No card is needed. Create a key at https://openrouter.ai/settings/keys. Free models: 20 requests a minute and 50 a day. Use public text only. Compare ethics, quota, and Hermes fit: [free cloud models for class](../03-models-and-providers/free-cloud-models-for-class.md). Live list: [OpenRouter free models](https://openrouter.ai/collections/free-models).

1. In Hermes Desktop, open **Settings**, then **Providers**, then **OpenRouter**.
2. Add your API key. Paste the key. Do not type it in a shell command.
3. In your OpenRouter account privacy settings, turn off free-model training if you can (exact label: not verified). That skips hosts OpenRouter marks as may-train.
4. Set the main model. Prefer one of these (*technical suggestion*, checked 25 Nov 2026):
   - `google/gemma-4-26b-a4b-it:free` (open weights; better privacy tags than NVIDIA free on OpenRouter's table; Hermes fitness not verified)
   - or `openrouter/free` (router picks a free model)
   - still listed: `nvidia/nemotron-3-ultra-550b-a55b:free` (strong for agents, but the free quota **burns fast** with tool loops; OpenRouter marks NVIDIA as may train). Demoted as the class default. Prefer Gemma, `openrouter/free`, or a local model when you can.

Menu labels: **Settings → Providers → OpenRouter → add API key**. Exact wording on screen is not verified. Other providers, cards, and limits: [providers and keys](howto-hermes-providers-and-keys.md). Terminal or `.env` file: that page only (advanced).

Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets).

## 3. First chat and smoke test

This test checks that your free model answers in chat. Do not point Hermes at your vault.

1. Set the main model to the id you chose in section 2 (Gemma free, `openrouter/free`, Nemotron free, `nous/welcome`, or a local model).
2. Open a new chat in Hermes Desktop (preferred). Terminal chat is advanced.
3. Send this short prompt: Reply with one short sentence that says you work.
4. Expect a short reply. Then continue with section 4.

STOP if Hermes names your vault or starts reading folders you did not ask for. Tell the teacher.

## 4. Connect Obsidian, Hermes, and LLM Wiki

Obsidian is the note app. It opens a **vault** (a folder of Markdown files). Hermes is the agent. The **LLM Wiki** skill tells Hermes how to build and keep a wiki in that folder. Official skill docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-llm-wiki

Class default folder (user profile only, not Program Files):

`%USERPROFILE%\workspaces\llm-wiki\vault`

Example: `C:\Users\<username>\workspaces\llm-wiki\vault`

Why this path: it is your user space. Hermes can write files there without administrator rights. That keeps the rest of Windows safer. Do not use a private vault. Phone sync is homework: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md).

### 4a. Create the vault and open it in Obsidian

1. Download Obsidian for Windows: https://obsidian.md/download
2. Install it.
3. Create the folders. Open a normal Windows Terminal (not Administrator). Type this block and press Enter:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\workspaces\llm-wiki\vault" | Out-Null
Write-Output "$env:USERPROFILE\workspaces\llm-wiki\vault"
```

4. In Obsidian, choose **Open folder as vault** (exact label: not verified). Select that `vault` folder.
5. Optional: copy the starter tree into this vault from [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).

### 4b. Point Hermes at the same folder

Desktop Settings for vault path fields: not verified. Use the `.env` steps below (advanced when Desktop has no path fields).

Official docs: set `WIKI_PATH` for the LLM Wiki skill. If you also use the Obsidian skill, set `OBSIDIAN_VAULT_PATH` to the **same** folder. Both must be absolute paths.

1. In the same normal terminal, type `notepad "$env:LOCALAPPDATA\hermes\.env"` and press Enter. If Notepad asks to create the file, click Yes.
2. Add these two lines. Replace `<username>` with your Windows user name. Do not add quote marks.

```env
OBSIDIAN_VAULT_PATH=C:\Users\<username>\workspaces\llm-wiki\vault
WIKI_PATH=C:\Users\<username>\workspaces\llm-wiki\vault
```

3. Click File, then Save. Do not use Save As.
4. A path with spaces is not verified. If your user name has spaces, tell the teacher.

More path rules: [advanced Hermes config](howto-hermes-advanced-config.md#point-hermes-at-a-wiki-folder).

### 4c. Install the LLM Wiki skill

Prefer Hermes Desktop if it shows Skills under Settings (path and labels: not verified). If Desktop has no Skills install UI, use the terminal commands below (advanced).

1. In the same normal terminal, type:

```powershell
hermes skills install official/research/llm-wiki
```

2. Answer the prompts. Exact prompt wording on Windows is not verified.
3. Check it loaded. Type `hermes skills list` and press Enter. The list must show the LLM Wiki skill (name on screen: not verified; look for `llm-wiki`).
4. Quit Hermes Desktop and open it again.

STOP if the paths point at Program Files, Documents, Desktop, or a private vault. Fix the paths before you chat about notes.

You are done for class when the skill is listed and Hermes restarts.

## Next steps (advanced)

After Hermes works, feed Hermes short files from the agent pack instead of the long human guides.

- Free cloud models (ethics and quota): [free cloud models for class](../03-models-and-providers/free-cloud-models-for-class.md)
- Local models (Hermes Desktop Local Models first): [howto local models](../03-models-and-providers/howto-local-models.md)
- Agent pack (short files for Hermes; feed one at a time): [agent-install/](agent-install/README.md)

One short line each. Do these at home, or when the teacher says so.

- Phone sync for the class vault (homework): [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md)
- MCP examples (vvvv): [howto example mcp servers](../06-mcp-and-tools/howto-example-mcp-servers.md)
- Docker sandbox: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)
- Efficient coding harness: [howto hermes efficient coding](howto-hermes-efficient-coding.md)
- CLI install, vault paths, skills, gateway; optional later file write test (not the vault): [advanced Hermes config](howto-hermes-advanced-config.md)
- Providers and keys (all rows, `.env`): [providers and keys](howto-hermes-providers-and-keys.md)
- Uninstall and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall)
- Why this order: [install why](install-why.md)
