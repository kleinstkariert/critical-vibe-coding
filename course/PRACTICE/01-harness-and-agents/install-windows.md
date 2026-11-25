---
title: Install guide. Windows
date: 2026-11-25
tags:
  - course
  - howto
  - install
  - windows
status: current
canonical: true
---

# Install guide. Windows

Follow this file from top to bottom. Do not open the Linux or macOS guides.

## Before you start

- Windows 11, version 22H2 or later. Press the Windows key and R together, type `winver`, and press Enter to see your version.
- Use a normal terminal. Do not choose "Run as administrator". An account in the Administrators group is fine with UAC on. Hermes needs no administrator rights.
- Work only in the test folder `hermes-smoke-test` (section 3b). Do not use Documents, the Desktop, or your vault.
- About 5 GB of free disk space (not verified). A local model (section 2) is optional. Download it at home.
- Section 7 only: Git for Windows, Node.js 22.20 or later, and a .NET SDK. Those installers can ask for UAC.
- Safety rules, UAC facts, checks and rollback: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#windows-details). Why this order: [install why](install-why.md).

## 1. Install Hermes Desktop

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

1. Open https://hermes-agent.nousresearch.com/desktop. The host in the address bar must be `hermes-agent.nousresearch.com`. STOP if it is another host.
2. Click the Microsoft Store button. If the Store is blocked on your laptop, click the main download button. It gives you an `.appinstaller` file. The exact label of that button is not verified.
3. Do not click "Download .exe instead". That file builds Hermes from source. It takes much longer.
4. For the `.appinstaller` file, open it with Windows App Installer. The publisher must be Nous Research. STOP if it is another name. If App Installer says sideloading is blocked, STOP and use the Store button. Do not change a policy.
5. STOP if a UAC prompt appears during the install. Click No. No official page says Hermes Desktop needs one.
6. Open Hermes from the Start menu, as a normal user.
7. On first start, Hermes asks you to choose a layout and a provider. Choose Basic. "Choose provider later" is fine. You set the model in section 3.

Hermes keeps its files in `%LOCALAPPDATA%\hermes\`. For the Store package this is not verified on a real machine. Windows checks (token, signature, uninstall): [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#windows-details). Older Windows, or no Store: the command-line route in [howto hermes setup](howto-hermes-setup.md) §2, Option B.

## 2. Load one local model (optional)

Do this after the first test in section 3b works, or at home. A local model runs on your computer. It needs no key and no card, and nothing leaves your computer. Small models are weaker at agent work than cloud models. Why, and more models: [model types and local model tiers](../03-models-and-providers/model-types-and-local-model-tiers.md).

VRAM is the memory on the graphics card. Find yours in Task Manager: Performance tab, then your GPU, then "Dedicated GPU memory". Pick a row at or below your VRAM. Sizes are from the model pages (checked 25 Nov 2026). This course did not run these models with Hermes (not verified).

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

1. Hermes Desktop: open Settings, then Providers, then Local Models. Click Install runtime. Wait until it finishes.
2. Read the fit label on a model row. Click Download only when the label says the model fits. Then click Use. The Hermes catalog lists only Qwen3.8 27B (24 GB row). For the other rows, use the Find more models box, LM Studio, or Ollama: [install why](install-why.md#local-runtime-steps).
3. Hermes needs a context of at least 64,000 tokens. If a download is not done after 5 minutes, or the model prints raw tool text such as `{"name": ...}`, stop and go to section 3.

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

1. In Hermes Desktop, open Settings, then Providers, then the API keys part. Choose the provider and paste the key. The exact menu labels can differ (not verified).
2. Or type `hermes model` in a normal terminal and paste the key at its prompt.
3. Or open the env file in a text editor: type `notepad "$env:LOCALAPPDATA\hermes\.env"` and press Enter. Add one line with the key name from the table, for example `OPENROUTER_API_KEY=your-key`. Click File, then Save. Do not use Save As.
4. Choose a small model that says it supports tools. Tell the teacher the name you chose.
5. Set a spend limit if the provider has one. Revoke the key after the class. A free cloud model can log your prompts: use public text only.

Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets).

## 3b. First test: one small file

This test checks the model and one file read. It does not use your notes. The test file is public text. It is safe on any model.

1. Click the Start button, type `Windows Terminal`, and press Enter. If it is not in the list, type `PowerShell` and press Enter. Do not start it as Administrator.
2. Type this block and press Enter:

```powershell
New-Item -ItemType Directory -Force "$HOME\hermes-smoke-test" | Out-Null
Set-Content -Path "$HOME\hermes-smoke-test\note.txt" -Value "The smoke test file says hello."
Write-Output "$HOME\hermes-smoke-test\note.txt"
```

3. Select the path that the last line prints and copy it. If your user name has spaces or letters like ä, ö, ü, keep the path as it is.
4. In Hermes, paste this request. Put your copied path in place of PATH: Read only this file: PATH. Reply with the one sentence in that file. Do not open any other folder.
5. The reply must be: The smoke test file says hello. If Hermes names your vault or another folder, stop and tell the teacher.

If you prefer File Explorer: click the address bar, type `%USERPROFILE%`, press Enter, then create the folder `hermes-smoke-test` and the file `note.txt` there. Windows may hide file extensions, so check that the name is not `note.txt.txt`.

If time runs out, stop here. Finish sections 4 to 7 at home.

## 4. Install Obsidian and the LLM wiki

1. Download Obsidian for Windows: https://obsidian.md/download
2. Install it and create a vault. A vault is the folder of notes Obsidian opens. Use a plain folder such as `C:\Users\you\MyVault`. Do not use an online-only cloud folder. Online-only files look empty to Hermes.
3. Skip phone sync today. Do it at home later: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md). Do not copy that page into this one.
4. Copy the starter tree and the `SCHEMA.md` stub from [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).
5. Open the Hermes env file. In Windows Terminal, type `notepad "$env:LOCALAPPDATA\hermes\.env"` and press Enter. If Notepad asks to create the file, click Yes. Add the two lines below. Use your own path. Do not add quote marks. A path with spaces is not verified. If your path has spaces, tell the teacher. Click File, then Save. Do not use Save As.

```env
OBSIDIAN_VAULT_PATH=C:\Users\you\MyVault\wiki
WIKI_PATH=C:\Users\you\MyVault\wiki
```

Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.

The first folders for Hermes are `wiki/`, the `hermes-smoke-test` folder from section 3b, and project folders you name in the request.

A folder name is not a security boundary. The access table is in [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).

A full-vault path is convenience mode, not recommended for private material.

6. Install the LLM Wiki skill. It is an optional skill, not a bundled one. Type `hermes skills install official/research/llm-wiki` and press Enter. Answer the prompts. The prompt wording on Windows is not verified.
7. Quit Hermes Desktop and open it again.

Path rules and the skill links: [howto hermes setup](howto-hermes-setup.md) §4.

Store choices, if you do not want Obsidian: [knowledge store options](../02-knowledge-bases/knowledge-store-options.md).

## 5. Rules and the first SCHEMA.md

The stub you copied is the first `SCHEMA.md`. Do not paste the long security notes into it.

Read these, in this order, and keep them as links:

1. Course rules: [AGENTS.md](../../../AGENTS.md)
2. A project copy for later: [agents md template](agents-md-template.md)
3. Do not run Hermes as Administrator. Do not expose the gateway. Keys stay in the Hermes env file: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets)
4. Command approvals: see section 6 and [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#6-approvals). Hermes does not ask before it writes a file.
5. Secrets stay out of the vault: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §12
6. Stop after three failed repair attempts: [howto hermes efficient coding](howto-hermes-efficient-coding.md)

## 6. Personal laptop

The agent can read your files and run commands. The rules for all systems are on one page: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). In short:

1. Start with the disposable folder `hermes-smoke-test`. Ask for reading first.
2. Use `manual` approvals: type `hermes config set approvals.mode manual`. The default is `smart`. Never set `off`.
3. Hermes writes files without asking. Before a write task, make a Git commit or copy the folder. After the task, look at what changed.
4. Point `WIKI_PATH` at `wiki/` only. This is a habit, not a lock. Do not point this work at a private vault.
5. Keep keys in the Hermes env file only. Do not set up the messaging gateway in class.

Docker is advanced, not the baseline: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md). Mounts, secrets, and the rule list: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §§9 to 14. Rollback and uninstall: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall).

## 7. Example: vvvv skills and vvvv MCP

Do this only after sections 1 to 6 work. You can skip it, or swap in another program. External software and MCP servers in this file are examples. Why: [install why](install-why.md).

An MCP is a connector that lets Hermes talk to another program. The Windows example is vvvv, a live visual programming environment. Read the permissions and capability rule first: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

Elevate only for a named step. Only these installers may ask for UAC: the .NET SDK (system-wide, needs administrator rights) and Git for Windows. Node.js: not verified. Read the UAC window. It must show a verified publisher. Click Yes for that one installer, then close it and go back to your normal terminal. Details: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#windows-details).

### vvvv

1. If you want the live editor, install current vvvv gamma from https://vvvv.org
2. You can install the MCP below without vvvv. The vvvv MCP README says: "Works **without a vvvv installation** for all knowledge, search, read, and generate tools." Source: https://github.com/digitalwannabe/vvvv-mcp#readme

### vvvv skills

Skills are instruction files the agent loads for one kind of work. The vvvv skills repo is https://github.com/tebjan/vvvv-skills

The README's recommended install is:

```bash
npx skills add tebjan/vvvv-skills
```

That command needs Node.js 22.20 or later: https://nodejs.org (the `npx skills` README states this version). It also needs Git for Windows for the manual copy below.

The README's manual Windows copy targets Claude Code, not Hermes. Its lines are `cmd` syntax (`%TEMP%`, `xcopy`). They do not work in PowerShell. Source: https://github.com/tebjan/vvvv-skills#manual-installation

The skills tool has an agent name for Hermes. On Windows it may write to `%USERPROFILE%\.hermes\skills`, not to `%LOCALAPPDATA%\hermes\skills`. This is not verified. Use the manual copy for Hermes. Type these lines in Windows Terminal:

```powershell
git clone https://github.com/tebjan/vvvv-skills "$env:TEMP\vvvv-skills"
New-Item -ItemType Directory -Force "$env:LOCALAPPDATA\hermes\skills" | Out-Null
Copy-Item "$env:TEMP\vvvv-skills\skills\*" "$env:LOCALAPPDATA\hermes\skills\" -Recurse
```

Each `SKILL.md` must be one folder down, for example `...\hermes\skills\vvvv-shaders\SKILL.md`. Then type `hermes skills list` and check that the vvvv skills appear.

Do not run the Python patch editor that the `vvvv-fileformat` skill includes. It is not part of this class.

### vvvv MCP

The server is https://github.com/digitalwannabe/vvvv-mcp

The README install, quoted from https://github.com/digitalwannabe/vvvv-mcp#install-end-users :

> Requires [.NET 8 SDK](https://dotnet.microsoft.com/download/dotnet/8.0) or later.

```powershell
dotnet tool install -g vvvv-mcp
vvvv-mcp --setup
```

1. Install the .NET 10 SDK from https://dotnet.microsoft.com/download. The README asks for the .NET 8 SDK or later. .NET 8 left support on 10 Nov 2026. The tool package targets `net8.0`. It is not verified that the tool runs with only .NET 10. If Hermes later reports that .NET 8 is missing, also install the .NET 8 runtime, for class use only.
2. Open a new PowerShell window.
3. Run the first command only: `dotnet tool install -g vvvv-mcp`.
4. Do not run `vvvv-mcp --setup`. The README says it detects Claude Desktop, VS Code, Cursor and Kilo, and writes their config files. Hermes is not on that list. It would change the settings of other programs.
5. Add the server to Hermes by hand. In Windows Terminal, type `notepad "$env:LOCALAPPDATA\hermes\config.yaml"` and press Enter. Add this block. Hermes MCP shape: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

```yaml
mcp_servers:
  vvvv:
    command: "vvvv-mcp"
    tools:
      include: [search_nodes, get_node_details, list_categories, list_packages, list_knowledge, read_knowledge, search_knowledge, read_patch, explain_patch]
```

   This allows read and search tools only. It leaves out every tool that writes a patch. Two points are not verified: that `command: "vvvv-mcp"` without arguments starts the server, and that these tool names match the current version (they come from the README).
6. Quit Hermes and open it again. Write the tool list in your capability inventory: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

Skip the in-editor chat extension. The README marks `VL.MCP.HDE` as an experimental preview. Live tools need that extension. Offline search and patch tools do not.

Student use of vvvv-mcp is non-commercial under its license. Read https://github.com/digitalwannabe/vvvv-mcp/blob/main/LICENSE.md before any paid client work. vvvv itself counts academic research as commercial use. Teaching and learning are free. Source: https://vvvv.org

To undo this section, see step 7 of [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall).
