---
title: Install guide. macOS
date: 2026-11-20
tags:
  - course
  - howto
  - install
  - macos
status: current
canonical: true
---

# Install guide. macOS

Follow this file from top to bottom. Do not open the Windows or Linux guides.

## Before you start

- Hermes Desktop needs an Apple Silicon Mac. An Intel Mac uses the Terminal route in section 1. The macOS version that Hermes needs: not verified.
- Use your normal macOS login account. Hermes needs no root and no `sudo`. macOS has no UAC, so the Windows rules do not apply here.
- A password prompt is expected only in two cases. One: you copy `Hermes.app` to Applications. You can use `~/Applications` instead. Two: an Intel Mac runs `brew install git` or `xcode-select --install`. Read the prompt first. Whether Apple's installer asks for a password: not verified.
- If macOS asks to let Hermes use Desktop, Documents, Downloads, Full Disk Access or Accessibility, click Don't Allow. The first test needs none of them (not verified).
- Work only in the test folder `hermes-smoke-test` (section 4). Do not use your vault.
- Safety rules and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). Why this order: [install why](install-why.md).

## 1. Install Hermes Desktop

You install Hermes on your own laptop.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program. The Apple Silicon limit is recorded in [howto hermes setup](howto-hermes-setup.md) §2.

### Apple Silicon

1. Open https://hermes-agent.nousresearch.com/desktop and download the macOS package.
2. Open the DMG. Copy `Hermes.app` to Applications.
3. Check the app before you open it. Open Terminal. Type `codesign --verify --deep --strict --verbose=2 /Applications/Hermes.app` and press Return. The output must end with `satisfies its Designated Requirement`. Then type `spctl --assess --type execute --verbose /Applications/Hermes.app` and press Return. It must say `accepted` and `source=Notarized Developer ID`. If you used `~/Applications`, change the path. Hermes build notes say the macOS release is Developer ID signed and notarized. The exact output on a Mac was not seen for this course (not verified). Stop if a check fails. Sources: https://github.com/NousResearch/hermes-agent/blob/main/apps/desktop/BUILDING.md and the `codesign` and `spctl` manual pages.
4. Open Hermes. If macOS blocks the app, stop and run the two checks again. Click Open in Privacy and Security only after both checks pass.
5. Do not run Hermes as root.
6. To remove the Desktop app, quit Hermes and move `Hermes.app` to the Trash. Your data stays in `~/.hermes/`. All rules: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall).

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
- `~/.hermes/.env` is set to owner-only access (mode 600)
- If Git is missing: Homebrew installs Git, or Apple's Command Line Tools installer opens

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

## 2. Load one local model (optional)

Do this after the first test in section 4 works, or at home. A local model runs on your Mac. It needs no key and no card, and nothing leaves your Mac. Small models are weaker at agent work than cloud models. Why, and more models: [model types and local model tiers](../03-models-and-providers/model-types-and-local-model-tiers.md).

A Mac uses unified memory, shared by the processor and the graphics. macOS and your other apps use part of it. Read the table with your unified memory in place of VRAM, and pick one row lower (*technical suggestion*, not verified). Sizes are from the model pages (checked 25 Nov 2026). This course did not run these models with Hermes (not verified).

| Memory tier | Model | Download | Get |
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

1. Apple Silicon: open Hermes Desktop, then Settings, then Providers, then Local Models. Click Install runtime. Intel Mac: open Terminal, type `hermes model`, choose Local models, and follow the prompt that installs the runtime.
2. Read the fit label on a model row. Click Download only when the label says the model fits. Then click Use. The Hermes catalog lists only Qwen3.8 27B (24 GB row). For the other rows, use the Find more models box, LM Studio, or Ollama: [install why](install-why.md#local-runtime-steps).
3. Hermes needs a context of at least 64,000 tokens. If the label says the model uses system RAM or is too big, or the model prints raw tool text, stop and go to section 3.

Hermes local model docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

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

1. Apple Silicon: in Hermes Desktop, open Settings, then Providers, then the API keys part. Choose the provider and paste the key. The exact menu labels can differ (not verified).
2. Or type `hermes model` and paste the key at its prompt.
3. Or open the env file in a text editor. Type `nano ~/.hermes/.env` and press Return. Add one line with the key name from the table, for example `OPENROUTER_API_KEY=your-key`. Press Control and O, then Return, then Control and X.
4. Choose a small model that says it supports tools. Tell the teacher the name you chose.
5. Set a spend limit if the provider has one. Revoke the key after the class. A free cloud model can log your prompts: use public text only.

Hermes stores the key in `~/.hermes/.env`. Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets). The first test is in section 4.

## 4. Install Obsidian and the LLM wiki

1. Download Obsidian for macOS: https://obsidian.md/download
2. Open the DMG and copy Obsidian to Applications. Create a vault. A vault is the folder of notes Obsidian opens.
3. Set up phone sync. Follow [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md). Do not copy that page into this one.
4. Copy the starter tree and the `SCHEMA.md` stub from [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).
5. In `~/.hermes/.env`, set both paths to the `wiki` folder inside that vault. Use the full macOS path.

```env
OBSIDIAN_VAULT_PATH=/Users/you/Nextcloud/MyVault/wiki
WIKI_PATH=/Users/you/Nextcloud/MyVault/wiki
```

Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.

The first folders for Hermes are `wiki/`, the `hermes-smoke-test` folder in the steps below, and project folders you name in the request.

A folder name is not a security boundary. The access table is in [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).

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

## 7. Example: TouchDesigner MCP

Do this only after sections 1 to 6 work. You can skip it, or swap in another program. External software and MCP servers in this file are examples. Why: [install why](install-why.md).

An MCP is a connector that lets Hermes talk to another program. The macOS example is TouchDesigner, and only because the official project below is real and current. Read the permissions and capability rule first: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

The example is real. TDMCP is the official TouchDesigner MCP from Derivative. It is in public beta. Checked 20 Nov 2026.

- Repo: https://github.com/TouchDesigner/TDMCP
- Docs: https://docs.derivative.ca/MCP
- Releases: https://github.com/TouchDesigner/TDMCP/releases
- TouchDesigner download: https://derivative.ca/download

The README says the component needs **TouchDesigner 2025.33230 or newer**. Earlier builds will not open it. Quote and version notes: https://github.com/TouchDesigner/TDMCP#start-here

Hermes is not in the README's Install For list. The README says TDMCP "works with any client that speaks streamable-HTTP MCP." The steps below use that HTTP endpoint with Hermes. The endpoint URL is from the README. The YAML shape is from the Hermes MCP page: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

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
