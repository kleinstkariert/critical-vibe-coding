---
title: Install guide. Linux
date: 2026-11-20
tags:
  - course
  - howto
  - install
  - linux
status: current
canonical: true
---

# Install guide. Linux

Follow this file from top to bottom. Do not open the Windows or macOS guides.

## Before you start

- Use your normal user. Hermes needs no root. Do not put `sudo` in front of a Hermes command or its installer. Do not run `curl ... | sudo bash`. Linux has no UAC, so the Windows rules do not apply here.
- The installer can ask for your password once. It runs `sudo -v` only when Node.js needs the `libatomic` package (Debian and Ubuntu: `libatomic1`) and your terminal can answer a prompt. If no prompt shows and Node.js fails, the installer prints the exact command to give to an administrator. Source: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Do not start the gateway at boot in class. That needs `sudo`. A user in the `docker` group has root-level privileges: https://docs.docker.com/engine/install/linux-postinstall/
- No release offers a Linux Desktop package yet (Hermes platform support page, checked 25 Nov 2026). You use the terminal installer in section 1.
- Work only in the test folder `hermes-smoke-test` (section 4). Do not use your vault.
- Safety rules and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). Why this order: [install why](install-why.md).

## 1. Install Hermes Desktop

You install Hermes on your own laptop.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

1. Open https://hermes-agent.nousresearch.com/desktop in your browser.
2. Read the address bar. The host must be `hermes-agent.nousresearch.com`.
3. Stop if the host is any other name.
4. Hermes lists the command-line script as the Linux install. No release offers a Linux Desktop package yet (Hermes platform support page, checked 25 Nov 2026). If the page shows a Linux file anyway, do not open it. Ask the teacher.
5. Use a terminal for the command-line installer below.

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
- `~/.hermes/.env` is set to owner-only access (mode 600)
- One `sudo -v` prompt, only if Node.js needs `libatomic` (see Account and privileges)

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

Edge cases, including WSL and Docker, stay in [howto hermes setup](howto-hermes-setup.md) §2. Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `~/.hermes/`.

## 2. Load one local model (optional)

Do this after the first test in section 4 works, or at home. A local model runs on this computer. It needs no key and no card, and nothing leaves your computer. Small models are weaker at agent work than cloud models. Why, and more models: [model types and local model tiers](../03-models-and-providers/model-types-and-local-model-tiers.md).

VRAM is the memory on the graphics card. Pick a row at or below your VRAM. Sizes are from the model pages (checked 25 Nov 2026). This course did not run these models with Hermes (not verified).

| VRAM | Model | Download | Get |
|---|---|---|---|
| 8 GB | Qwen3.5 4B | 3.3 GB | [Ollama](https://ollama.com/library/qwen3.5:4b) · [LM Studio](https://lmstudio.ai/models/qwen3.5) |
| 8 GB | Granite 4.1 3B | 2.1 GB | [Ollama](https://ollama.com/library/granite4.1:3b) · [LM Studio](https://lmstudio.ai/models/granite-4.1) |
| 12 GB | Gemma 4 12B | 8.0 GB | [Ollama](https://ollama.com/library/gemma4:12b) · [LM Studio](https://lmstudio.ai/models/gemma-4) |
| 12 GB | Qwen3.5 9B | 6.6 GB | [Ollama](https://ollama.com/library/qwen3.5:9b) · [LM Studio](https://lmstudio.ai/models/qwen3.5) |
| 16 GB | Gemma 4 12B, 8-bit | 13 GB | [Ollama](https://ollama.com/library/gemma4:12b-it-q8_0) |
| 16 GB | MiMo V2.6 9B | 6.6 to 8.7 GB | [Ollama](https://ollama.com/library/mimo-v2.6:9b) · [Hugging Face](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B) |
| 16 GB | Gemma 4 26B A4B (tight, may use system RAM) | 16 to 19 GB | [Ollama](https://ollama.com/library/gemma4:26b) · [LM Studio](https://lmstudio.ai/models/gemma-4) |
| 24 GB | Qwen3.8 27B | 16.5 GB | [Hermes catalog](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json) · [Ollama](https://ollama.com/library/qwen3.8:27b) · [LM Studio](https://lmstudio.ai/models/qwen3.8) |
| 24 GB | Gemma 4 31B | 19 to 20 GB | [Ollama](https://ollama.com/library/gemma4:31b) · [LM Studio](https://lmstudio.ai/models/gemma-4) |

1. Hermes Desktop, if it is open: click Settings, then Providers, then Local Models, then Install runtime. Terminal only: type `hermes model`, choose Local models, and follow the prompt that installs the runtime.
2. Read the fit label on a model row. Click Download only when the label says the model fits. Then click Use. The Hermes catalog lists only Qwen3.8 27B (24 GB row). For the other rows, use the Find more models box, LM Studio, or Ollama: [install why](install-why.md#local-runtime-steps).
3. Hermes needs a context of at least 64,000 tokens. If the label says the model uses system RAM or is too big, or the model prints raw tool text, stop and go to section 3.

Linux note from the Hermes docs: NVIDIA CUDA needs a CUDA 13 driver for the managed runtime. If the runtime refuses the GPU, stop. Do not install a random driver. Hermes local model docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

## 3. Connect a model provider and key

Hermes needs one model. Choose one row. The class default is OpenRouter with a free model and no card: [howto hermes setup](howto-hermes-setup.md) §3.

| Provider | Get a key | Card needed | Key name in the env file | Notes |
|---|---|---|---|---|
| OpenRouter, free route | [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys) | No, for models whose id ends in `:free` | `OPENROUTER_API_KEY` | Free models: 20 requests a minute and 50 a day. After you buy US $10 of credit, 1,000 a day. Your prompts may be logged. [Free models](https://openrouter.ai/collections/free-models) |
| OpenAI API | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | Yes. Prepaid credit | `OPENAI_API_KEY` | ChatGPT Plus has no API credit. [Billing help](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) |
| Anthropic (Claude API) | [platform.claude.com/settings/keys](https://platform.claude.com/settings/keys) | Yes. Prepaid credit. A key without credit fails | `ANTHROPIC_API_KEY` | Hermes cannot log in with a Claude Pro plan. Use a key. [Billing help](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage) |
| Google Gemini | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | No, for the free tier | `GOOGLE_API_KEY` (or `GEMINI_API_KEY`) | Google can use free-tier prompts to improve its products. Hermes docs: a free key can run out after a few agent turns. [Billing](https://aistudio.google.com/docs/billing) |
| Nous Portal | [portal.nousresearch.com](https://portal.nousresearch.com) | Subscription. Card: not verified | None. Log in with `hermes model` | One login for many models. Price: not verified |
| Local, with Ollama or LM Studio | [ollama.com/download](https://ollama.com/download) or [lmstudio.ai/download](https://lmstudio.ai/download) | No | None | Section 2 |

Key pages ask you to sign in. The links load (checked 25 Nov 2026). The page labels can change (not verified). Hermes supports more providers: [Hermes providers](https://hermes-agent.nousresearch.com/docs/integrations/providers).

Enter the key in one of these ways. Never type a key in a shell command.

1. In Hermes Desktop, if it is open: open Settings, then Providers, then the API keys part. Choose the provider and paste the key. The exact menu labels can differ (not verified).
2. Or type `hermes model` and paste the key at its prompt.
3. Or open the env file in a text editor. Type `nano ~/.hermes/.env` and press Return. Add one line with the key name from the table, for example `OPENROUTER_API_KEY=your-key`. Press Control and O, then Return, then Control and X.
4. Choose a small model that says it supports tools. Tell the teacher the name you chose.
5. Set a spend limit if the provider has one. Revoke the key after the class. A free cloud model can log your prompts: use public text only.

Hermes stores the key in `~/.hermes/.env`. Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets). The first test is in section 4.

## 4. Install Obsidian and the LLM wiki

1. Download Obsidian for Linux: https://obsidian.md/download
2. Install one package type and keep it. Create a vault. A vault is the folder of notes Obsidian opens.
3. Set up phone sync. Follow [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md). Do not copy that page into this one.
4. Copy the starter tree and the `SCHEMA.md` stub from [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).
5. In `~/.hermes/.env`, set both paths to the `wiki` folder inside that vault. Use the full Linux path.

```env
OBSIDIAN_VAULT_PATH=/home/you/Nextcloud/MyVault/wiki
WIKI_PATH=/home/you/Nextcloud/MyVault/wiki
```

Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.

The first folders for Hermes are `wiki/`, the `hermes-smoke-test` folder in the steps below, and project folders you name in the request.

A folder name is not a security boundary. The access table is in [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).

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

Path rules and the skill links: [howto hermes setup](howto-hermes-setup.md) §4.

Store choices, if you do not want Obsidian: [knowledge store options](../02-knowledge-bases/knowledge-store-options.md).

## 5. Rules and the first SCHEMA.md

The stub you copied is the first `SCHEMA.md`. Do not paste the long security notes into it.

Read these, in this order, and keep them as links:

1. Course rules: [AGENTS.md](../../../AGENTS.md)
2. A project copy for later: [agents md template](agents-md-template.md)
3. Do not run as root. Do not expose the gateway. Keys stay in the Hermes env file: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets)
4. Command approvals: see section 6 and [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#6-approvals). Hermes does not ask before it writes a file.
5. Secrets stay out of the vault: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §12
6. Stop after three failed repair attempts: [howto hermes efficient coding](howto-hermes-efficient-coding.md)

## 6. Personal laptop

Security on a personal laptop matters. The agent can read your files and run commands.

The rules for all systems are on one page: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). The novice baseline, in short:

1. Start with a disposable folder, such as `hermes-smoke-test`. Ask for reading first.
2. Use `manual` approvals: type `hermes config set approvals.mode manual`. The default is `smart`. Never set `off`.
3. Hermes writes files without asking. Before a write task, make a Git commit or copy the folder. After the task, look at what changed.
4. Point `WIKI_PATH` at `wiki/` only. This is a habit, not a lock. Do not point this work at a private vault.
5. Keep keys in the Hermes env file only.

Docker is an advanced safety module, not the baseline: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md).

Work and personal machine notes from Hermes: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine

Mounts, secrets, and the rule list: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §§9 to 14.

Stop here. There is no Linux MCP example in this guide. An MCP is a connector that lets Hermes talk to another program. External software and MCP servers are examples only. What an MCP is, and the permissions rule: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).
