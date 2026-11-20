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

One reference GPU for the model below is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. VRAM is the memory on the graphics card. Your computer may differ. Use the model below, then read the fit label.

1. In Hermes Desktop, open Settings, then Providers, then Local Models.
2. Click Install runtime. Wait until the runtime finishes.
3. Download **Qwen3.8 27B**.
4. Read the fit label.
5. Click Use when the label says the model fits, or that it uses system RAM.
6. Stop when the label says the model is too big. Use the API model in the next section.
7. If you have no Desktop window, run `hermes model` and choose Local models. The same catalog is there.

Why this model fits a 16 GB card: [[install-why]].

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
5. In `~/.hermes/.env`, set both paths to that vault folder. Use the full Linux path.

```env
OBSIDIAN_VAULT_PATH=/home/you/Nextcloud/MyVault
WIKI_PATH=/home/you/Nextcloud/MyVault
```

6. Quit Hermes and open it again.
7. Ask Hermes to create `wiki/hello.md` with one sentence.
8. In Obsidian, confirm that file. If Hermes writes somewhere else, stop.

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

Stop here. There is no Linux MCP example in this guide.
