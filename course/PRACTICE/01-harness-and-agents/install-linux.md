---
title: Install guide. Linux
date: 2026-11-25
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

- Use your normal user. Hermes needs no root. Do not put `sudo` in front of a Hermes command or its installer. Do not run `curl ... | sudo bash`.
- The installer can ask for your password once when Node.js needs `libatomic` (Debian and Ubuntu: `libatomic1`). Source: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Do not start the gateway at boot in class. That needs `sudo`.
- No release offers a Linux Desktop package yet (Hermes platform support page, checked 25 Nov 2026). You use the terminal installer in section 1. If a Desktop window opens later, use it for the key step.
- Do not point Hermes at a private vault. The class wiki folder comes in section 4.
- Safety rules and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). Why this order: [install why](install-why.md).

## 1. Install Hermes (terminal)

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program. On Linux you install through the terminal.

1. Open a terminal (Super key, type `Terminal`, press Enter; on Ubuntu you can press Ctrl+Alt+T).
2. The host in the commands below must be `hermes-agent.nousresearch.com`. The address must start with `https://`. STOP if the host is different.
3. Use path B. Path A runs the script before you can read it. The Hermes install page does not publish a checksum for `install.sh`. This course does not invent one.

### Path A. Convenience

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Do not type `sudo` before that line.

### Path B. Inspectable (use this)

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o install.sh
```

1. Type `less install.sh` and press Enter. Press the space bar to move down. Press `q` to close.
2. While you read, look for `curl` and `git clone` lines. Those hosts should be `hermes-agent.nousresearch.com`, `hermes-assets.nousresearch.com`, or `github.com`. STOP if you see a different host.
3. Type `bash install.sh` and press Enter. Do not type `sudo` before it.
4. Type `source ~/.bashrc` and press Enter. Then type `hermes --help` and press Enter.
5. If the shell says the command is missing, close the terminal and open a new one. Type `hermes --help` again.
6. If no window opened, type `hermes desktop` and press Enter. Do not run Hermes as root.

Hermes keeps its files in `~/.hermes/`. Uninstall, WSL, and Docker notes: [advanced Hermes config](howto-hermes-advanced-config.md#macos-and-linux-cli).

## 2. Add an OpenRouter key

The class default is OpenRouter with a free model. No card is needed for model ids that end in `:free`. Create a key at https://openrouter.ai/settings/keys. Free models: 20 requests a minute and 50 a day. Your prompts may be logged. Use public text only. [Free models](https://openrouter.ai/collections/free-models)

If a Desktop window is open:

1. Open **Settings**, then **Providers**, then **OpenRouter**.
2. Add your API key. Paste the key. Do not type it in a shell command.
3. Set the main model to `nvidia/nemotron-3-ultra-550b-a55b:free` (class free OpenRouter NVIDIA route; checked 25 Nov 2026). Tell the teacher if your list shows a different free NVIDIA id.

Menu labels: **Settings → Providers → OpenRouter → add API key**. Exact wording on screen is not verified. If Desktop is not available, use [providers and keys](howto-hermes-providers-and-keys.md) (`hermes model` or the `.env` file). Other providers and cards: that page.

Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets).

## 3. First chat and smoke test

This test checks that the free OpenRouter model answers in chat. Do not point Hermes at your vault.

1. Set the main model to `nvidia/nemotron-3-ultra-550b-a55b:free` (or the free OpenRouter NVIDIA model you chose in section 2).
2. Open a new chat in Hermes.
3. Send this short prompt: Reply with one short sentence that says you work.
4. Expect a short reply. Then continue with section 4.

STOP if Hermes names your vault or starts reading folders you did not ask for. Tell the teacher.

## 4. Connect Obsidian, Hermes, and LLM Wiki

Obsidian is the note app. It opens a **vault** (a folder of Markdown files). Hermes is the agent. The **LLM Wiki** skill tells Hermes how to build and keep a wiki in one folder. Official skill docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-llm-wiki

Use a **class vault**, not your private vault. Phone sync is homework: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md).

### 4a. Obsidian and the wiki folder

1. Download Obsidian for Linux: https://obsidian.md/download
2. Install one package type and keep it. Create a new vault for class, for example `ClassVault`. Do not open your private vault.
3. Inside that vault, create a folder named `wiki` (or copy the starter tree from [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md)).
4. In Obsidian, open the vault root (`ClassVault`). You browse notes there. Hermes will only be pointed at `wiki/`.

### 4b. Point Hermes at `wiki/`

Hermes reads two paths from its env file. For class, set both to the **absolute** path of `wiki/` (not the whole vault, not `private/`).

1. Open a terminal.
2. Type `nano ~/.hermes/.env` and press Enter.
3. Add these two lines. Replace the path with your real path. Do not add quote marks.

```env
OBSIDIAN_VAULT_PATH=/home/you/ClassVault/wiki
WIKI_PATH=/home/you/ClassVault/wiki
```

4. Press Control and O, then Enter, then Control and X.

Official docs: set `WIKI_PATH` for the LLM Wiki skill. If you also use the Obsidian skill, set `OBSIDIAN_VAULT_PATH` to the same folder. Source: the LLM Wiki skill page above. More path rules: [advanced Hermes config](howto-hermes-advanced-config.md#point-hermes-at-a-wiki-folder).

### 4c. Install the LLM Wiki skill

1. In the terminal, type:

```bash
hermes skills install official/research/llm-wiki
```

2. Answer the prompts. Exact prompt wording on Linux is not verified.
3. Check it loaded. Type `hermes skills list` and press Enter. The list must show the LLM Wiki skill (name on screen: not verified; look for `llm-wiki`).
4. Quit Hermes and open it again (or type `hermes desktop` if you use a Desktop window).

STOP if you pointed the paths at a private vault. Fix the paths before you chat about notes.

You are done for class when the skill is listed and Hermes restarts.

## Next steps (advanced)

One short line each. Do these at home, or when the teacher says so.

- Local models: [howto local models](../03-models-and-providers/howto-local-models.md)
- Phone sync for the class vault (homework): [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md)
- MCP examples: [howto example mcp servers](../06-mcp-and-tools/howto-example-mcp-servers.md)
- Docker sandbox: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)
- Efficient coding harness: [howto hermes efficient coding](howto-hermes-efficient-coding.md)
- CLI details, vault paths, skills, gateway; optional later file write test (not the vault): [advanced Hermes config](howto-hermes-advanced-config.md)
- Providers and keys (all rows, `.env`): [providers and keys](howto-hermes-providers-and-keys.md)
- Uninstall and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall)
- Why this order: [install why](install-why.md)
