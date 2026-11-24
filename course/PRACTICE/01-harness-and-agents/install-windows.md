---
title: Install guide. Windows
date: 2026-11-20
tags:
  - course
  - howto
  - install
  - windows
audience: student
status: current
canonical: true
---

# Install guide. Windows

Follow this file from top to bottom. Do not open the Linux or macOS guides.

External software and MCP servers in this file are examples. You can replace them with tools you prefer. Why: [install why](install-why.md).

An MCP is a connector that lets Hermes talk to another program. The Windows example is vvvv. vvvv is a live visual programming environment.

Read the permissions and capability rule before section 7: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

## 1. Install Hermes Desktop

You install Hermes on your own laptop.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

1. Open https://hermes-agent.nousresearch.com/desktop
2. Download the Windows package, or use the Microsoft Store link on that page.
3. Open the `.appinstaller` or MSIX file with Windows App Installer.
4. Open Hermes from the Start menu.
5. Do not run Hermes as Administrator.

More Windows notes, including the command-line installer: [howto hermes setup](howto-hermes-setup.md) §2. Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `%LOCALAPPDATA%\hermes\`.

## 2. Load one local model

A local model runs on this computer. It does not need an API key.

VRAM is the memory on the graphics card. The room demo card is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. That card does not prove that a 27B model fits in 16 GB. 27B means 27 billion parameters. Your computer may have a different card.

Use these sizes for the first local experiment:

- 8 to 16 GB of VRAM: a 7B to 8B model
- A 24 GB card: a 14B to 20B model
- **Qwen3.8 27B** is an advanced model. It is not the first download.

System memory is the normal RAM in the computer. Offload means Hermes puts part of the model in that RAM. The model can run. It can also be slow.

A long context is a long chat plus the files the agent sends. A long context can make a model unusable even when the weights fit.

The Hermes catalog checked on 20 Nov 2026 has no 7B to 8B model. This course does not invent a catalog id. Open the Local Models list and read the names there. Catalog file: https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json

Tool calling means the model asks Hermes to run a tool.

1. In Hermes Desktop, open Settings.
2. Open Providers.
3. Open Local Models.
4. Click Install runtime.
5. Wait until the runtime finishes.
6. Read each row name.
7. If a row says 7B or 8B, read its text.
8. Download that row when the text says agent or tool calling.
9. Read the fit label before you click Use.
10. Click Use when the label says the model fits.
11. If the label says the model uses system RAM, stop. Use the API model in the next section.
12. If the label says the model is too big, stop. Use the API model in the next section.
13. If no 7B or 8B row is in the list, skip the local download. Use the API model in the next section.

Advanced model: **Qwen3.8 27B**, catalog id `qwen3.8-27b`. The catalog text calls it the best all-round agent model.

1. Read [install why](install-why.md) before you download this model.
2. Read the fit label on the Qwen3.8 27B row.
3. Download it only when the label says the model fits, or when the label says it uses system RAM and you accept the slowdown.
4. Click Use only after that read.
5. Stop when the label says the model is too big.

Size bands and file sizes: [install why](install-why.md). Research note: [local gpu hardware for llms](../../../research/software&DataManagement/local-gpu-hardware-for-llms.md).

Free cloud models already listed for this course: [default setup](default-setup.md) §4 and [howto hermes setup](howto-hermes-setup.md) §3. Do not copy that list. Do not send private notes through a free cloud model until you have read §4.

Local model docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

## 3. Connect an OpenAI API key

ChatGPT Plus does not include OpenAI API credits.

You create an OpenAI API key. You do not reuse the ChatGPT password as a key.

1. Open https://platform.openai.com/api-keys and create a key.
2. Open API billing from https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform and add a payment method.
3. Set a low spend limit before the first run.
4. In a terminal, run `hermes model`.
5. Choose the OpenAI API provider.
6. Paste the key when Hermes asks. Hermes stores it in `%LOCALAPPDATA%\hermes\.env`.
7. Choose the model `gpt-5.4-mini`.

`gpt-5.4-mini` is the suggested model. Hermes lists it under the OpenAI API provider. On the OpenAI price page, checked 20 Nov 2026, this mini model is US $0.75 per million input tokens and US $4.50 per million output tokens. Price page: https://developers.openai.com/api/docs/pricing

Plus fact: https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus

Hermes can also log in with a ChatGPT subscription for Codex models (`hermes model`, then ChatGPT or Codex Subscription). That login is not an API key. The Hermes docs do not yet say which Plus limits it uses. Create the API key. Provider page: https://hermes-agent.nousresearch.com/docs/integrations/providers

Do not put the key in the vault, in chat, or in Git.

## 4. Install Obsidian and the LLM wiki

1. Download Obsidian for Windows: https://obsidian.md/download
2. Install it and create a vault. A vault is the folder of notes Obsidian opens.
3. Set up phone sync. Follow [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md). Do not copy that page into this one.
4. Copy the starter tree and the `SCHEMA.md` stub from [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).
5. In `%LOCALAPPDATA%\hermes\.env`, set both paths to the `wiki` folder inside that vault. Use the full Windows path.

```env
OBSIDIAN_VAULT_PATH=C:\Users\you\Nextcloud\MyVault\wiki
WIKI_PATH=C:\Users\you\Nextcloud\MyVault\wiki
```

Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.

The first folders for Hermes are `wiki/`, the `hermes-smoke-test` folder in the steps below, and project folders you name in the request.

A folder name is not a security boundary. The access table is in [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).

A full-vault path is convenience mode, not recommended for private material.

6. Quit Hermes Desktop and open it again.
7. Open File Explorer. Click the folder icon on the taskbar.
8. In the left sidebar, click your user folder.
9. Right-click an empty area.
10. Click New, then Folder.
11. Type `hermes-smoke-test` and press Enter.
12. Double-click `hermes-smoke-test`.
13. Right-click an empty area.
14. Click New, then Text Document.
15. Type `note.txt` and press Enter. If the name already ends in `.txt`, type `note` only.
16. Double-click `note.txt`.
17. Type this sentence: The smoke test file says hello.
18. Click File, then Save.
19. Close Notepad.
20. Click the address bar in File Explorer. Copy the folder path.
21. In Hermes, paste this request. Put your copied path in place of PATH: Read only this file: PATH\note.txt. Reply with the one sentence in that file. Do not open any other folder.
22. Send the request.
23. The reply must be: The smoke test file says hello. If Hermes names your vault or another folder, stop.

Path rules and the skill links: [howto hermes setup](howto-hermes-setup.md) §4.

Store choices, if you do not want Obsidian: [knowledge store options](../02-knowledge-bases/knowledge-store-options.md).

## 5. Rules and the first SCHEMA.md

The stub you copied is the first `SCHEMA.md`. Do not paste the long security notes into it.

Read these, in this order, and keep them as links:

1. Course rules: [AGENTS.md](../../../AGENTS.md)
2. A project copy for later: [agents md template](agents-md-template.md)
3. Do not run as root. Do not expose the gateway. Keys stay in the Hermes env file: [howto hermes setup](howto-hermes-setup.md) §5d
4. Approvals stay on. The novice baseline is in section 6.
5. Secrets stay out of the vault: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §12
6. Stop after three failed repair attempts: [howto hermes efficient coding](howto-hermes-efficient-coding.md)

## 6. Personal laptop

Security on a personal laptop matters. The agent can read your files and run commands.

Use the current course guidance. Do not write a second security essay.

The novice baseline:

1. Read the files first. Do not ask Hermes to edit them yet.
2. Use a disposable project folder, such as `hermes-smoke-test`.
3. Keep manual approvals on. Review the diff before you accept an edit.
4. Give Hermes one narrow folder to write in. The default folder is `wiki/`.
5. Make a Git commit, or copy the folder, before you accept edits.
6. Do not point this work at a private vault.

Docker is an advanced safety module. Use it as a demonstration or in a separate workshop: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md).

Docker adds filesystem sharing, path translation, ownership, network, performance, GPU access, images, and Windows/macOS virtualisation, so it is not the two-hour baseline.

- Do not run as root. Do not expose the gateway. [howto hermes setup](howto-hermes-setup.md) §5d · [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §14.
- Work and personal machine notes from Hermes: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine

## 7. Example: vvvv skills and vvvv MCP

Do this only after sections 1 to 6 work. You can skip it, or swap in another program.

### vvvv

1. If you want the live editor, install current vvvv gamma from https://vvvv.org
2. You can install the MCP below without vvvv. The vvvv MCP README says: "Works **without a vvvv installation** for all knowledge, search, read, and generate tools." Source: https://github.com/digitalwannabe/vvvv-mcp#readme

### vvvv skills

Skills are instruction files the agent loads for one kind of work. The vvvv skills repo is https://github.com/tebjan/vvvv-skills

The README's recommended install is:

```bash
npx skills add tebjan/vvvv-skills
```

That command needs Node.js: https://nodejs.org

The README's manual Windows copy targets Claude Code, not Hermes. Quote from the README (https://github.com/tebjan/vvvv-skills#manual-installation):

```powershell
git clone https://github.com/tebjan/vvvv-skills %TEMP%\vvvv-skills
xcopy /E /I %TEMP%\vvvv-skills\skills\* %USERPROFILE%\.claude\skills\
```

For Hermes, clone with the same first command. Copy each skill folder into `%LOCALAPPDATA%\hermes\skills\`. The README rule still applies: each `SKILL.md` is one folder down, not deeper.

The README also says skills work with compatible coding agents, not only Claude. If `npx skills` does not list Hermes, use the manual copy.

### vvvv MCP

The server is https://github.com/digitalwannabe/vvvv-mcp

Before these install steps, read [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

The README install, quoted from https://github.com/digitalwannabe/vvvv-mcp#install-end-users :

> Requires [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later.

```powershell
dotnet tool install -g vvvv-mcp
vvvv-mcp --setup
```

1. Install the .NET 8 SDK from the link in that quote.
2. Open a new PowerShell window.
3. Run the two commands above.
4. `--setup` writes client config, or prints a snippet when it cannot detect the client. The README says it "prints the config snippet for anything it can't auto-detect."
5. If the snippet names Hermes, paste it. If it does not, do not invent a second config.
6. Hermes MCP shape, when you must add a server by hand: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

Skip the in-editor chat extension. The README marks `VL.MCP.HDE` as an experimental preview. Live tools need that extension. Offline search and patch tools do not.

Student use of vvvv-mcp is non-commercial under its license. Read https://github.com/digitalwannabe/vvvv-mcp/blob/main/LICENSE.md before any paid client work.
