---
title: Install guide. macOS
date: 2026-11-25
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
- Use your normal macOS login account. Hermes needs no root and no `sudo`.
- If macOS asks to let Hermes use Desktop, Documents, Downloads, Full Disk Access or Accessibility, click Don't Allow. The first test needs none of them (not verified).
- Do not point Hermes at a private vault. The class wiki folder comes in section 4.
- Safety rules and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). Why this order: [install why](install-why.md).

## 1. Install Hermes Desktop

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

### Apple Silicon

1. Open https://hermes-agent.nousresearch.com/desktop. The host must be `hermes-agent.nousresearch.com`. STOP if it is another host.
2. Download the macOS package. Open the DMG. Copy `Hermes.app` to Applications (or `~/Applications`).
3. Check the app before you open it. Open Terminal. Type `codesign --verify --deep --strict --verbose=2 /Applications/Hermes.app` and press Return. The output must end with `satisfies its Designated Requirement`. Then type `spctl --assess --type execute --verbose /Applications/Hermes.app` and press Return. It must say `accepted` and `source=Notarized Developer ID`. If you used `~/Applications`, change the path. Exact output on a Mac for this course: not verified. STOP if a check fails.
4. Open Hermes. If macOS blocks the app, STOP and run the two checks again. Click Open in Privacy and Security only after both checks pass.
5. Do not run Hermes as root.
6. On first start, choose Basic. "Choose provider later" is fine. You set the key in section 2.

### Intel Mac

There is no Desktop app for this Mac. Use the Terminal install in [advanced Hermes config](howto-hermes-advanced-config.md#macos-and-linux-cli). Then continue with section 2 using `hermes model` if Desktop is not open.

Hermes keeps its files in `~/.hermes/`.

## 2. Add an OpenRouter key

The class default is OpenRouter with a free model. No card is needed for model ids that end in `:free`. Create a key at https://openrouter.ai/settings/keys. Free models: 20 requests a minute and 50 a day. Your prompts may be logged. Use public text only. [Free models](https://openrouter.ai/collections/free-models)

1. In Hermes Desktop, open **Settings**, then **Providers**, then **OpenRouter**.
2. Add your API key. Paste the key. Do not type it in a shell command.
3. Set the main model to `nvidia/nemotron-3-ultra-550b-a55b:free` (class free OpenRouter NVIDIA route; checked 25 Nov 2026). Tell the teacher if your list shows a different free NVIDIA id.

Menu labels: **Settings → Providers → OpenRouter → add API key**. Exact wording on screen is not verified. Other providers, cards, and limits: [providers and keys](howto-hermes-providers-and-keys.md). Terminal or `.env` file: that page only.

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

1. Download Obsidian for macOS: https://obsidian.md/download
2. Open the DMG. Copy Obsidian to Applications. Create a new vault for class, for example `ClassVault`. Do not open your private vault.
3. Inside that vault, create a folder named `wiki` (or copy the starter tree from [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md)).
4. In Obsidian, open the vault root (`ClassVault`). You browse notes there. Hermes will only be pointed at `wiki/`.

### 4b. Point Hermes at `wiki/`

Hermes reads two paths from its env file. For class, set both to the **absolute** path of `wiki/` (not the whole vault, not `private/`).

1. Open Terminal.
2. Type `nano ~/.hermes/.env` and press Return.
3. Add these two lines. Replace the path with your real path. Do not add quote marks.

```env
OBSIDIAN_VAULT_PATH=/Users/you/ClassVault/wiki
WIKI_PATH=/Users/you/ClassVault/wiki
```

4. Press Control and O, then Return, then Control and X.

Official docs: set `WIKI_PATH` for the LLM Wiki skill. If you also use the Obsidian skill, set `OBSIDIAN_VAULT_PATH` to the same folder. Source: the LLM Wiki skill page above. More path rules: [advanced Hermes config](howto-hermes-advanced-config.md#point-hermes-at-a-wiki-folder).

### 4c. Install the LLM Wiki skill

1. In Terminal, type:

```bash
hermes skills install official/research/llm-wiki
```

2. Answer the prompts. Exact prompt wording on macOS is not verified.
3. Check it loaded. Type `hermes skills list` and press Return. The list must show the LLM Wiki skill (name on screen: not verified; look for `llm-wiki`).
4. Quit Hermes and open it again.

STOP if you pointed the paths at a private vault. Fix the paths before you chat about notes.

You are done for class when the skill is listed and Hermes restarts.

## Next steps (advanced)

One short line each. Do these at home, or when the teacher says so.

- Local models: [howto local models](../03-models-and-providers/howto-local-models.md)
- Phone sync for the class vault (homework): [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md)
- MCP examples (TouchDesigner): [howto example mcp servers](../06-mcp-and-tools/howto-example-mcp-servers.md)
- Docker sandbox: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)
- Efficient coding harness: [howto hermes efficient coding](howto-hermes-efficient-coding.md)
- CLI install, vault paths, skills, gateway; optional later file write test (not the vault): [advanced Hermes config](howto-hermes-advanced-config.md)
- Providers and keys (all rows, `.env`): [providers and keys](howto-hermes-providers-and-keys.md)
- Uninstall and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall)
- Why this order: [install why](install-why.md)
