---
title: Install guide. macOS
date: 2026-11-20
tags:
  - course
  - howto
  - install
  - macos
---

# Install guide. macOS

Follow this file from top to bottom. Do not open the Windows or Linux guides.

External software and MCP servers in this file are examples. You can replace them with tools you prefer. Why: [[install-why]].

An MCP is a connector that lets Hermes talk to another program. The macOS example is TouchDesigner, and only because the official project below is real and current. If you do not use TouchDesigner, skip section 7.

Read the permissions and capability rule before section 7: [[../concepts/what-is-mcp#Permissions and capability boundary]].

## 1. Install Hermes Desktop

You install Hermes on your own laptop.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

Hermes Desktop is Apple Silicon only. An Intel Mac uses the command-line install below. That limit is recorded in [[howto-hermes-setup]] §2.

### Apple Silicon

1. Open https://hermes-agent.nousresearch.com/desktop and download the macOS package.
2. Open the DMG. Copy `Hermes.app` to Applications.
3. Open Hermes. If macOS blocks the app, use the on-screen Privacy and Security prompt.
4. Do not run Hermes as root.

### Intel Mac

There is no Desktop app for this Mac. Use Terminal.

1. Press Command and the space bar together.
2. Type `Terminal`.
3. Press Return.
4. A window opens. You type at the blinking cursor.

You can also open Finder, click Go, click Utilities, and double-click Terminal.

Check the address before you download.

1. The host in the commands below must be `hermes-agent.nousresearch.com`.
2. The address must start with `https://`.
3. Stop if the host is different.

The Hermes install page does not publish a checksum for `install.sh`. A checksum is a short fingerprint of a file. This course does not invent one. Page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Use path B. Path A is the short path. It runs the script before you can read it.

#### Path A. Convenience

1. Click the Terminal window.
2. Type `cd` and press Return.
3. Type the next line and press Return. Do not type `sudo` before it.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

#### Path B. Inspectable

1. Click the Terminal window.
2. Type `cd` and press Return.
3. Type the next line and press Return. This saves `install.sh` in your home folder. It does not run it.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o install.sh
```

4. Type `less install.sh` and press Return.
5. Press the space bar to move down.
6. Press `q` to close the viewer.
7. While you read, look for `curl` and `git clone` lines.
8. Those hosts should be `hermes-agent.nousresearch.com`, `hermes-assets.nousresearch.com`, or `github.com`.
9. Stop if you see a different host.
10. Type the next line and press Return. Do not type `sudo` before it.

```bash
bash install.sh
```

What the script changes, from the Hermes install layout and from `install.sh`, checked 20 Nov 2026:

- Program files: `~/.hermes/hermes-agent/`
- Command: `~/.local/bin/hermes`
- Your Hermes data: `~/.hermes/`
- Install log: `~/.hermes/logs/install.log`
- A PATH line in `~/.zshrc` and `~/.zprofile` when your shell is zsh

1. Type `source ~/.zshrc` and press Return.
2. Type `hermes --help` and press Return.
3. If the shell says the command is missing, quit Terminal and open it again.
4. Type `hermes --help` again.
5. Use `hermes` in Terminal for the steps below.

Uninstall, from https://hermes-agent.nousresearch.com/docs/getting-started/updating :

1. Open Terminal.
2. Type `hermes uninstall --dry-run` and press Return. This lists files. It does not delete them.
3. Type `hermes uninstall` and press Return to remove the program and keep your data.
4. Type `hermes uninstall --full` only when you also want `~/.hermes/` deleted.

Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `~/.hermes/`.

## 2. Load one local model

A local model runs on this computer. It does not need an API key.

VRAM is the memory on the graphics card. The room demo card is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. That card does not prove that a 27B model fits in 16 GB. 27B means 27 billion parameters. Your Mac may have a different amount of memory.

A Mac uses unified memory. Unified memory is RAM shared by the processor and the graphics. Read the fit label. The same model can be too big on a Mac.

Use these sizes for the first local experiment:

- 8 to 16 GB of memory for the model: a 7B to 8B model
- A 24 GB class machine: a 14B to 20B model
- **Qwen3.8 27B** is an advanced model. It is not the first download.

System memory is the normal RAM in the computer. Offload means Hermes puts part of the model in that RAM. The model can run. It can also be slow.

A long context is a long chat plus the files the agent sends. A long context can make a model unusable even when the weights fit.

The Hermes catalog checked on 20 Nov 2026 has no 7B to 8B model. This course does not invent a catalog id. Open the Local Models list and read the names there. Catalog file: https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json

Tool calling means the model asks Hermes to run a tool.

Use one path. Use Apple Silicon when your Mac has the Desktop app. Use Intel when section 1 said there is no Desktop app.

### Apple Silicon

1. Open Hermes Desktop.
2. Open Settings.
3. Open Providers.
4. Open Local Models.
5. Click Install runtime.
6. Wait until the runtime finishes.

### Intel Mac

1. Open Terminal the way section 1 says.
2. Type `hermes model` and press Return.
3. Choose Local models.
4. Follow the prompt that installs the runtime.
5. Wait until the runtime finishes.

### Choose the row

1. Read each row name.
2. If a row says 7B or 8B, read its text.
3. Download that row when the text says agent or tool calling.
4. Read the fit label before you click Use.
5. Click Use when the label says the model fits.
6. If the label says the model uses system RAM, stop. Use the API model in the next section.
7. If the label says the model is too big, stop. Use the API model in the next section.
8. If no 7B or 8B row is in the list, skip the local download. Use the API model in the next section.

Advanced model: **Qwen3.8 27B**, catalog id `qwen3.8-27b`. The catalog text calls it the best all-round agent model.

1. Read [[install-why]] before you download this model.
2. Read the fit label on the Qwen3.8 27B row.
3. Download it only when the label says the model fits, or when the label says it uses system RAM and you accept the slowdown.
4. Click Use only after that read.
5. Stop when the label says the model is too big.

Size bands and file sizes: [[install-why]]. Research note: [[../../research/local-gpu-hardware-for-llms]].

Free cloud models already listed for this course: [[../lectures/01-welcome-landscape-deep-dives/default-setup]] §4 and [[howto-hermes-setup]] §3. Do not copy that list. Do not send private notes through a free cloud model until you have read §4.

Local model docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

## 3. Connect an OpenAI API key

ChatGPT Plus does not include OpenAI API credits.

You create an OpenAI API key. You do not reuse the ChatGPT password as a key.

1. Open https://platform.openai.com/api-keys and create a key.
2. Open API billing from https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform and add a payment method.
3. Set a low spend limit before the first run.
4. Run `hermes model`.
5. Choose the OpenAI API provider.
6. Paste the key when Hermes asks. Hermes stores it in `~/.hermes/.env`.
7. Choose the model `gpt-5.4-mini`.

`gpt-5.4-mini` is the suggested model. Hermes lists it under the OpenAI API provider. On the OpenAI price page, checked 20 Nov 2026, this mini model is US $0.75 per million input tokens and US $4.50 per million output tokens. Price page: https://developers.openai.com/api/docs/pricing

Plus fact: https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus

Hermes can also log in with a ChatGPT subscription for Codex models (`hermes model`, then ChatGPT or Codex Subscription). That login is not an API key. The Hermes docs do not yet say which Plus limits it uses. Create the API key. Provider page: https://hermes-agent.nousresearch.com/docs/integrations/providers

Do not put the key in the vault, in chat, or in Git.

## 4. Install Obsidian and the LLM wiki

1. Download Obsidian for macOS: https://obsidian.md/download
2. Open the DMG and copy Obsidian to Applications. Create a vault. A vault is the folder of notes Obsidian opens.
3. Set up phone sync. Follow [[howto-obsidian-setup-and-sync]]. Do not copy that page into this one.
4. Copy the starter tree and the `SCHEMA.md` stub from [[starter-knowledge-base]].
5. In `~/.hermes/.env`, set both paths to the `wiki` folder inside that vault. Use the full macOS path.

```env
OBSIDIAN_VAULT_PATH=/Users/you/Nextcloud/MyVault/wiki
WIKI_PATH=/Users/you/Nextcloud/MyVault/wiki
```

Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.

The first folders for Hermes are `wiki/`, the `hermes-smoke-test` folder in the steps below, and project folders you name in the request.

A folder name is not a security boundary. The access table is in [[starter-knowledge-base]].

A full-vault path is convenience mode, not recommended for private material.

6. Quit Hermes and open it again.
7. Open Finder.
8. Click Go in the menu bar.
9. Click Home.
10. Click File, then New Folder.
11. Type `hermes-smoke-test` and press Return.
12. Double-click `hermes-smoke-test`.
13. Open TextEdit. It is in Applications.
14. Click Format, then Make Plain Text.
15. Type this sentence: The smoke test file says hello.
16. Click File, then Save.
17. Save the file as `note.txt` inside `hermes-smoke-test`.
18. If TextEdit asks about the `.txt` ending, click Use .txt.
19. Open Terminal the way section 1 says.
20. Type `echo "$HOME/hermes-smoke-test/note.txt"` and press Return. Copy that path.
21. In Hermes, paste this request. Put your copied path in place of PATH: Read only this file: PATH. Reply with the one sentence in that file. Do not open any other folder.
22. Send the request.
23. The reply must be: The smoke test file says hello. If Hermes names your vault or another folder, stop.

Path rules and the skill links: [[howto-hermes-setup]] §4.

Store choices, if you do not want Obsidian: [[knowledge-store-options]].

## 5. Rules and the first SCHEMA.md

The stub you copied is the first `SCHEMA.md`. Do not paste the long security notes into it.

Read these, in this order, and keep them as links:

1. Course rules: [AGENTS.md](../../AGENTS.md)
2. A project copy for later: [[agents-md-template]]
3. Do not run as root. Do not expose the gateway. Keys stay in the Hermes env file: [[howto-hermes-setup]] §5d
4. Approvals stay on. The novice baseline is in section 6.
5. Secrets stay out of the vault: [[Local LLM Coding with Hermes]] §12
6. Stop after three failed repair attempts: [[howto-hermes-efficient-coding]]

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

Docker is an advanced safety module. Use it as a demonstration or in a separate workshop: [[howto-hermes-docker-sandbox]].

Docker adds filesystem sharing, path translation, ownership, network, performance, GPU access, images, and Windows/macOS virtualisation, so it is not the two-hour baseline.

- Do not run as root. Do not expose the gateway. [[howto-hermes-setup]] §5d · [[Local LLM Coding with Hermes]] §14.
- Work and personal machine notes from Hermes: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine

## 7. Example: TouchDesigner MCP

Do this only after sections 1 to 6 work. You can skip it, or swap in another program.

The example is real. TDMCP is the official TouchDesigner MCP from Derivative. It is in public beta. Checked 20 Nov 2026.

- Repo: https://github.com/TouchDesigner/TDMCP
- Docs: https://docs.derivative.ca/MCP
- Releases: https://github.com/TouchDesigner/TDMCP/releases
- TouchDesigner download: https://derivative.ca/download

The README says the component needs **TouchDesigner 2025.33230 or newer**. Earlier builds will not open it. Quote and version notes: https://github.com/TouchDesigner/TDMCP#start-here

Hermes is not in the README's Install For list. The README says TDMCP "works with any client that speaks streamable-HTTP MCP." The steps below use that HTTP endpoint with Hermes. The endpoint URL is from the README. The YAML shape is from the Hermes MCP page: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

Before these install steps, read [[../concepts/what-is-mcp#Permissions and capability boundary]].

1. Install TouchDesigner 2025.33230 or newer.
2. Download `TDMCP.tox` from the releases page. Drag it into the root of your project.
3. On the component's MCP page, turn **Active** on.
4. Open the README section linked above. If the localhost URL is not `http://127.0.0.1:13316/mcp`, use the URL from that README. The port here was checked on 20 Nov 2026.
5. Add this block to `~/.hermes/config.yaml`, then restart Hermes:

```yaml
mcp_servers:
  touchdesigner:
    url: "http://127.0.0.1:13316/mcp"
```

6. Ask Hermes what TouchDesigner project it can see.
7. TouchDesigner shows a consent panel. The README says nothing gets control until you allow it there. Click allow only if the panel names your Hermes app.
8. Leave the server on localhost. The README refuses other machines by default. Do not open it to the network.

**Install Skills** on the component is written for the clients in the Install For list. Hermes is not in that list. If the pulse does not place skills in `~/.hermes/skills/`, skip skills. Do not copy the files into a guessed folder.

The server can run Python inside TouchDesigner. Treat that like a shell on your Mac. Security notes from the project: https://github.com/TouchDesigner/TDMCP/blob/main/docs/security.md
