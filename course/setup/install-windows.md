---
title: Install guide. Windows
date: 2026-11-20
tags:
  - course
  - howto
  - session-02
  - windows
---

# Install guide. Windows

Follow this file from top to bottom. Do not open the Linux or macOS guides.

External software and MCP servers in this file are examples. You can replace them with tools you prefer. Why: [[install-why]].

An MCP is a connector that lets Hermes talk to another program. The Windows example is vvvv. vvvv is a live visual programming environment.

## 1. Install Hermes Desktop

You install Hermes on your own laptop. Sebastian is in the room. Ask him when a button name does not match this page.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

1. Open https://hermes-agent.nousresearch.com/desktop
2. Download the Windows package, or use the Microsoft Store link on that page.
3. Open the `.appinstaller` or MSIX file with Windows App Installer.
4. Open Hermes from the Start menu.
5. Do not run Hermes as Administrator.

More Windows notes, including the command-line installer: [[howto-hermes-setup]] §2. Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `%LOCALAPPDATA%\hermes\`.

## 2. Load one local model

A local model runs on this computer. It does not need an API key.

The room demo GPU is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. VRAM is the memory on the graphics card. Your laptop may differ. Use the model below, then read the fit label on the machine in front of you.

1. In Hermes Desktop, open Settings, then Providers, then Local Models.
2. Click Install runtime. Wait until the runtime finishes.
3. Download **Qwen3.8 27B**.
4. Read the fit label.
5. Click Use when the label says the model fits, or that it uses system RAM.
6. Stop when the label says the model is too big. Use the API model in the next section.

Why this model fits a 16 GB card: [[install-why]].

Free cloud models already listed for this course: [[../lectures/01-welcome-landscape-deep-dives/default-setup]] §4 and [[howto-hermes-setup]] §3. Do not copy that list. Do not send private notes through a free cloud model until you have read §4.

Local model docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

## 3. Connect an OpenAI API key

ChatGPT Plus does not include OpenAI API credits.

You create an OpenAI API key. You do not reuse the ChatGPT password as a key.

1. Open https://platform.openai.com/api-keys and create a key.
2. Open API billing from https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform and add a payment method.
3. Set a low spend limit before the first class run.
4. In a terminal, run `hermes model`.
5. Choose the OpenAI API provider.
6. Paste the key when Hermes asks. Hermes stores it in `%LOCALAPPDATA%\hermes\.env`.
7. Choose the model `gpt-5.4-mini`.

`gpt-5.4-mini` is the class pick. Hermes lists it under the OpenAI API provider. On the OpenAI price page, checked 20 Nov 2026, this mini model is US $0.75 per million input tokens and US $4.50 per million output tokens. Price page: https://developers.openai.com/api/docs/pricing

Plus fact: https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus

Hermes can also log in with a ChatGPT subscription for Codex models (`hermes model`, then ChatGPT or Codex Subscription). That login is not an API key. The Hermes docs do not yet say which Plus limits it uses. In class, create the API key. Provider page: https://hermes-agent.nousresearch.com/docs/integrations/providers

Do not put the key in the vault, in chat, or in Git.

## 4. Install Obsidian and the LLM wiki

1. Download Obsidian for Windows: https://obsidian.md/download
2. Install it and create a vault. A vault is the folder of notes Obsidian opens.
3. Set up phone sync. Follow [[howto-obsidian-setup-and-sync]]. Do not copy that page into this one.
4. Copy the starter tree and the `SCHEMA.md` stub from [[starter-knowledge-base]].
5. In `%LOCALAPPDATA%\hermes\.env`, set both paths to that vault folder. Use the full Windows path.

```env
OBSIDIAN_VAULT_PATH=C:\Users\you\Nextcloud\MyVault
WIKI_PATH=C:\Users\you\Nextcloud\MyVault
```

6. Quit Hermes Desktop and open it again.
7. Ask Hermes to create `wiki/hello.md` with one sentence.
8. In Obsidian, confirm that file. If Hermes writes somewhere else, stop and tell Sebastian.

Path rules and the skill links: [[howto-hermes-setup]] §4.

Store choices, if you do not want Obsidian: [[knowledge-store-options]].

## 5. Rules and the first SCHEMA.md

The stub you copied is the first `SCHEMA.md`. Do not paste the long security notes into it.

Read these, in this order, and keep them as links:

1. Course rules: [AGENTS.md](../../AGENTS.md)
2. A project copy for later: [[agents-md-template]]
3. Do not run as root. Do not expose the gateway. Keys stay in the Hermes env file: [[howto-hermes-setup]] §5d
4. Approvals stay on: [[howto-hermes-docker-sandbox]] §4
5. Secrets stay out of the vault: [[Local LLM Coding with Hermes]] §12
6. Stop after three failed repair attempts: [[howto-hermes-efficient-coding]]

## 6. Personal laptop

Security on a personal laptop matters. The agent can read your files and run commands.

Use the current course guidance. Do not write a second security essay.

- The default local command backend has no isolation. Sandbox path: [[howto-hermes-docker-sandbox]]. Mount rules: [[Local LLM Coding with Hermes]] §§9 to 10.
- Do not run as root. Do not expose the gateway. [[howto-hermes-setup]] §5d · [[Local LLM Coding with Hermes]] §14.
- Keep approvals on. Review the Git diff before you accept edits. [[howto-hermes-docker-sandbox]] §4.
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

The README also says skills work with compatible coding agents, not only Claude. If `npx skills` does not list Hermes, use the manual copy. Ask Sebastian before you install a skill you have not opened.

### vvvv MCP

The server is https://github.com/digitalwannabe/vvvv-mcp

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
5. If the snippet names Hermes, paste it. If it does not, tell Sebastian. Do not invent a second config.
6. Hermes MCP shape, when you must add a server by hand: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

Skip the in-editor chat extension in class. The README marks `VL.MCP.HDE` as an experimental preview. Live tools need that extension. Offline search and patch tools do not.

Student use of vvvv-mcp is non-commercial under its license. Read https://github.com/digitalwannabe/vvvv-mcp/blob/main/LICENSE.md before any paid client work.
