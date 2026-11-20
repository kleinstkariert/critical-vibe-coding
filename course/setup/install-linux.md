---
title: Install guide. Linux
date: 2026-11-20
tags:
  - course
  - howto
  - install
  - linux
---

# Install guide. Linux

Follow this file from top to bottom. Do not open the Windows or macOS guides.

This guide has no MCP example. An MCP is a connector that lets Hermes talk to another program. External software and MCP servers are examples only. You can add a program you prefer later. What an MCP is: [[../concepts/what-is-mcp]]. Why this order: [[install-why]].

Read the permissions and capability rule before you add a server: [[../concepts/what-is-mcp#Permissions and capability boundary]].

## 1. Install Hermes Desktop

You install Hermes on your own laptop.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

1. Open https://hermes-agent.nousresearch.com/desktop in your browser.
2. Read the address bar. The host must be `hermes-agent.nousresearch.com`.
3. Stop if the host is any other name.
4. If that page offers a Linux download, save the file and open it. That file is a download you open.
5. If the page has no Linux app, use a terminal for the command-line installer below.

A terminal is a window where you type commands.

1. Press the Super key. Super is the key with the logo.
2. Type `Terminal`.
3. Press Enter.
4. On Ubuntu, you can also press Ctrl+Alt+T.

Check the download address before you type a command.

1. The host in the commands below must be `hermes-agent.nousresearch.com`.
2. The address must start with `https://`.
3. Stop if the host is different.

The Hermes install page does not publish a checksum for `install.sh`. A checksum is a short fingerprint of a file. This course does not invent one. Page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Use path B. Path A is the short path. It runs the script before you can read it.

### Path A. Convenience

1. Click the terminal window.
2. Type `cd` and press Enter. You are in your home folder.
3. Type the next line and press Enter. The script runs as soon as it downloads.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

4. Do not type `sudo` before that line.

### Path B. Inspectable

1. Click the terminal window.
2. Type `cd` and press Enter.
3. Type the next line and press Enter. This saves `install.sh` in your home folder. It does not run it.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o install.sh
```

4. Type `less install.sh` and press Enter. The script text fills the window.
5. Press the space bar to move down.
6. Press `q` to close the viewer.
7. While you read, look for `curl` and `git clone` lines.
8. Those hosts should be `hermes-agent.nousresearch.com`, `hermes-assets.nousresearch.com`, or `github.com`.
9. Stop if you see a different host.
10. Type the next line and press Enter. Do not type `sudo` before it.

```bash
bash install.sh
```

What the script changes, from the Hermes install layout and from `install.sh`, checked 20 Nov 2026:

- Program files: `~/.hermes/hermes-agent/`
- Command: `~/.local/bin/hermes`
- Your Hermes data: `~/.hermes/`
- Install log: `~/.hermes/logs/install.log`
- A PATH line in `~/.bashrc` and `~/.profile` when your shell is bash

1. Type `source ~/.bashrc` and press Enter.
2. Type `hermes --help` and press Enter.
3. If the shell says the command is missing, close the terminal and open a new one.
4. Type `hermes --help` again.
5. If no window opened, type `hermes desktop` and press Enter.
6. Do not run Hermes as root.

Uninstall, from https://hermes-agent.nousresearch.com/docs/getting-started/updating :

1. Open a terminal.
2. Type `hermes uninstall --dry-run` and press Enter. This lists files. It does not delete them.
3. Type `hermes uninstall` and press Enter to remove the program and keep your data.
4. Type `hermes uninstall --full` only when you also want `~/.hermes/` deleted.

Edge cases, including WSL and Docker, stay in [[howto-hermes-setup]] §2. Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `~/.hermes/`.

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

Use one path. Use Path A when Hermes Desktop is open. Use Path B when you have only a terminal.

### Path A. Hermes Desktop

1. Click Settings.
2. Open Providers.
3. Open Local Models.
4. Click Install runtime.
5. Wait until the runtime finishes.

### Path B. Terminal

1. Open a terminal the way section 1 says.
2. Type `hermes model` and press Enter.
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

Linux note from those docs: NVIDIA CUDA needs a CUDA 13 driver for the managed runtime. If the runtime refuses the GPU, stop. Do not install a random driver.

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

1. Download Obsidian for Linux: https://obsidian.md/download
2. Install one package type and keep it. Create a vault. A vault is the folder of notes Obsidian opens.
3. Set up phone sync. Follow [[howto-obsidian-setup-and-sync]]. Do not copy that page into this one.
4. Copy the starter tree and the `SCHEMA.md` stub from [[starter-knowledge-base]].
5. In `~/.hermes/.env`, set both paths to the `wiki` folder inside that vault. Use the full Linux path.

```env
OBSIDIAN_VAULT_PATH=/home/you/Nextcloud/MyVault/wiki
WIKI_PATH=/home/you/Nextcloud/MyVault/wiki
```

Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.

The first folders for Hermes are `wiki/`, the `hermes-smoke-test` folder in the steps below, and project folders you name in the request.

A folder name is not a security boundary. The access table is in [[starter-knowledge-base]].

A full-vault path is convenience mode, not recommended for private material.

6. Quit Hermes and open it again.
7. Open a terminal the way section 1 says.
8. Type `mkdir "$HOME/hermes-smoke-test"` and press Enter.
9. Type `printf '%s\n' 'The smoke test file says hello.' > "$HOME/hermes-smoke-test/note.txt"` and press Enter.
10. Type `xdg-open "$HOME/hermes-smoke-test"` and press Enter. The file manager opens the folder.
11. Type `echo "$HOME/hermes-smoke-test/note.txt"` and press Enter. Copy that path.
12. In Hermes, paste this request. Put your copied path in place of PATH: Read only this file: PATH. Reply with the one sentence in that file. Do not open any other folder.
13. Send the request.
14. The reply must be: The smoke test file says hello. If Hermes names your vault or another folder, stop.

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

Stop here. There is no Linux MCP example in this guide.
