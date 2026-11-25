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

- Windows 11, version 22H2 or later, for Hermes Desktop. Press the Windows key and R together, type `winver`, and press Enter to see your version.
- About 5 GB of free disk space for Hermes (not verified). A local model needs 20 GB or more.
- A web connection. A local model download is large. Do it at home.
- You do not need administrator rights. Do not run Hermes as Administrator.
- Section 3, path B needs a payment card. Path A does not.
- Section 7 only: Git for Windows (https://git-scm.com/downloads/win), Node.js 22.20 or later, and a .NET SDK. Section 7 gives the details.
- Optional: update your graphics driver before you use a local model. The minimum driver version on Windows is not verified.

External software and MCP servers in this file are examples. You can replace them with tools you prefer. Why: [install why](install-why.md).

An MCP is a connector that lets Hermes talk to another program. The Windows example is vvvv. vvvv is a live visual programming environment.

Read the permissions and capability rule before section 7: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

## 1. Install Hermes Desktop

You install Hermes on your own laptop.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

Check your Windows version first. Press the Windows key and R together, type `winver`, and press Enter. You need Windows 11, version 22H2 or later. If you have an older version, do not use this package. Work with a neighbour, or use the command-line route in [howto hermes setup](howto-hermes-setup.md) §2, Option B.

1. Open https://hermes-agent.nousresearch.com/desktop
2. Click the Microsoft Store button. If the Store is blocked on your laptop, click the main download button. It gives you an `.appinstaller` file. The exact label of that button is not verified.
3. Do not click "Download .exe instead". That file builds Hermes from source. It takes much longer.
4. If you downloaded the `.appinstaller` file, open it with Windows App Installer.
5. Open Hermes from the Start menu.
6. Do not run Hermes as Administrator.
7. On first start, Hermes asks you to choose a layout and a provider. Choose Basic. "Choose provider later" is fine. You set the model in section 3.

More Windows notes, including the command-line installer: [howto hermes setup](howto-hermes-setup.md) §2. Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `%LOCALAPPDATA%\hermes\`. For the Store package this is not verified on a real machine. After you save a key in section 3, check that `%LOCALAPPDATA%\hermes\.env` exists.

## 2. Load one local model

A local model runs on this computer. It does not need an API key.

In class, skip this section unless you have a 24 GB card. The Hermes list has no 7B to 8B model. The 27B model is about 18.5 GB to download. Do this section at home on a good connection. In class, go to section 3.

VRAM is the memory on the graphics card. The room demo card is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. That card does not prove that a 27B model fits in 16 GB. 27B means 27 billion parameters. Your computer may have a different card.

Use these sizes for the first local experiment:

- 8 to 16 GB of VRAM: a 7B to 8B model
- A 24 GB card: a 14B to 20B model
- **Qwen3.8 27B** is an advanced model. It is not the first download.

System memory is the normal RAM in the computer. Offload means Hermes puts part of the model in that RAM. The model can run. It can also be slow.

A long context is a long chat plus the files the agent sends. A long context can make a model unusable even when the weights fit.

The Hermes catalog checked on 25 Nov 2026 has no 7B to 8B model. This course does not invent a catalog id. Open the Local Models list and read the names there. Catalog file: https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json

Tool calling means the model asks Hermes to run a tool.

1. In Hermes Desktop, open Settings.
2. Open Providers.
3. Open Local Models.
4. Click Install runtime.
5. Wait until the runtime finishes.
6. Read each row name.
7. If a row says 7B or 8B, read its text.
8. Download that row when the text says agent or tool calling.
9. Read the fit label before you click Use.
10. Click Use when the label says the model fits.
11. If the label says the model uses system RAM, stop. Use the API model in the next section.
12. If the label says the model is too big, stop. Use the API model in the next section.
13. If no 7B or 8B row is in the list, skip the local download. Use the API model in the next section.

The same page has a Find more models box. It searches Hugging Face and shows a fit check for each file. Hermes does not test those models. We did not try this box in class (not verified for this course).

If a download is not done after 5 minutes, stop and go to section 3. On the first reply, a local model can stay silent for minutes. Hermes sends a large fixed prompt each time. This is expected.

Advanced model: **Qwen3.8 27B**, catalog id `qwen3.8-27b`. The catalog text calls it the best all-round agent model. The model file is about 16.5 GB. With the image file and the draft file, the download is about 18.5 GB.

1. Read [install why](install-why.md) before you download this model.
2. Read the fit label on the Qwen3.8 27B row.
3. Download it only when the label says the model fits, or when the label says it uses system RAM and you accept the slowdown.
4. Click Use only after that read.
5. Stop when the label says the model is too big.

Size bands and file sizes: [install why](install-why.md). Research note: [local gpu hardware for llms](../../../research/software&DataManagement/local-gpu-hardware-for-llms.md).

Free cloud models already listed for this course: [default setup](default-setup.md) §4 and [howto hermes setup](howto-hermes-setup.md) §3. Do not copy that list. Do not send private notes through a free cloud model until you have read §4. Section 3, path A, uses that free route.

Local model docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

## 3. Connect a model

A local model can be too big or too slow. Connect a cloud model instead. Choose one path.

Path A, no card: a free model through OpenRouter. Follow [howto hermes setup](howto-hermes-setup.md) §3, "Free-to-use endpoint used in class". Your prompts may be logged. Use this path only with the smoke test file and public text.

Path B, API key: OpenAI. You need a payment card. The steps are below.

### Path B. OpenAI API key

ChatGPT Plus does not include OpenAI API credits.

You create an OpenAI API key. You do not reuse the ChatGPT password as a key.

1. Open https://platform.openai.com/api-keys and create a key.
2. Add a payment method. Billing help: https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform
3. Add a small prepaid amount. Do not turn on automatic recharge.
4. In Hermes Desktop, open Settings, then Providers. Open the API keys part. Choose OpenAI API. Paste the key. The exact menu labels can differ (not verified). Command-line alternative: type `hermes model` in a terminal.
5. Choose a small model from the list. We suggest `gpt-6.1-terra`. The cheapest choice is `gpt-6-luna`.
6. Hermes stores the key in `%LOCALAPPDATA%\hermes\.env`.

OpenAI models page, checked 25 Nov 2026: `gpt-6.1-terra` costs US $1 per million input tokens and US $5 per million output tokens. `gpt-6-luna` costs US $0.10 and US $0.50. Page: https://developers.openai.com/api/docs/models

It is not verified that the Hermes list shows these names. If your list does not show them, choose the smallest model that says it supports tools. Tell the teacher the name you chose.

Plus fact: https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus

Hermes can also log in with a ChatGPT subscription for Codex models (`hermes model`, then ChatGPT or Codex Subscription). That login is not an API key. The Hermes docs do not yet say which Plus limits it uses. Create the API key. Provider page: https://hermes-agent.nousresearch.com/docs/integrations/providers

Do not put the key in the vault, in chat, or in Git.

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
3. Do not run as root. Do not expose the gateway. Keys stay in the Hermes env file: [howto hermes setup](howto-hermes-setup.md) §5d
4. Command approvals: see section 6. Hermes does not ask before it writes a file.
5. Secrets stay out of the vault: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §12
6. Stop after three failed repair attempts: [howto hermes efficient coding](howto-hermes-efficient-coding.md)

## 6. Personal laptop

Security on a personal laptop matters. The agent can read your files and run commands.

Use the current course guidance. Do not write a second security essay.

The novice baseline:

1. Start with a disposable folder, such as `hermes-smoke-test`. Ask for reading first.
2. Hermes asks for approval only before dangerous shell commands. The default mode is `smart`. In `smart`, a helper model approves low-risk commands for you. To be asked every time, type `hermes config set approvals.mode manual`. Never set it to `off`.
3. Hermes writes files without asking. Before you give it a write task, make a copy of the folder or a Git commit. A Git commit is a saved snapshot of a folder. After the task, look at what changed.
4. Point `WIKI_PATH` at `wiki/` only. This is a habit. It does not stop Hermes from reading other folders. Do not point this work at a private vault.
5. Keep keys in the Hermes env file only.

Docker is an advanced safety module. Use it as a demonstration or in a separate workshop: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md).

Docker adds filesystem sharing, path translation, ownership, network, performance, GPU access, images, and Windows/macOS virtualisation, so it is not the two-hour baseline.

- Do not run as root. Do not expose the gateway. [howto hermes setup](howto-hermes-setup.md) §5d · [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §14.
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

Before these install steps, read [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

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
