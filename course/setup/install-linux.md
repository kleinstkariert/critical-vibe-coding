---
title: Install guide. Linux
date: 2026-11-20
tags:
  - course
  - howto
  - session-02
  - linux
---

# Install guide. Linux

Follow this file from top to bottom. Do not open the Windows or macOS guides.

This guide has no MCP example. An MCP is a connector that lets Hermes talk to another program. External software and MCP servers are examples only. You can add a program you prefer later. What an MCP is: [[../concepts/what-is-mcp]]. Why the class install looks like this: [[install-why]].

## 1. Install Hermes Desktop

You install Hermes on your own laptop. Sebastian is in the room. Ask him when a button name does not match this page.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

1. Open https://hermes-agent.nousresearch.com/desktop
2. If that page offers a Linux download, install it. Then open the app.
3. If it does not, install the command-line agent. Do not run the command as root.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc
hermes --help
```

4. If the script succeeds and no window opened, run `hermes desktop`.
5. Do not run Hermes as root.

Edge cases, including WSL and Docker, stay in [[howto-hermes-setup]] §2. Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `~/.hermes/`.

## 2. Load one local model

A local model runs on this computer. It does not need an API key.

The room demo GPU is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. VRAM is the memory on the graphics card. Your laptop may differ. Use the model below, then read the fit label on the machine in front of you.

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

Linux note from those docs: NVIDIA CUDA needs a CUDA 13 driver for the managed runtime. If the runtime refuses the GPU, tell Sebastian. Do not install a random driver in class.

## 3. Connect an OpenAI API key

ChatGPT Plus does not include OpenAI API credits.

You create an OpenAI API key. You do not reuse the ChatGPT password as a key.

1. Open https://platform.openai.com/api-keys and create a key.
2. Open API billing from https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform and add a payment method.
3. Set a low spend limit before the first class run.
4. Run `hermes model`.
5. Choose the OpenAI API provider.
6. Paste the key when Hermes asks. Hermes stores it in `~/.hermes/.env`.
7. Choose the model `gpt-5.4-mini`.

`gpt-5.4-mini` is the class pick. Hermes lists it under the OpenAI API provider. On the OpenAI price page, checked 20 Nov 2026, this mini model is US $0.75 per million input tokens and US $4.50 per million output tokens. Price page: https://developers.openai.com/api/docs/pricing

Plus fact: https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus

Hermes can also log in with a ChatGPT subscription for Codex models (`hermes model`, then ChatGPT or Codex Subscription). That login is not an API key. The Hermes docs do not yet say which Plus limits it uses. In class, create the API key. Provider page: https://hermes-agent.nousresearch.com/docs/integrations/providers

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

Stop here. There is no Linux MCP example in this class guide.
