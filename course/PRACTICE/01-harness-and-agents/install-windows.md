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
- About 5 GB of free disk space for Hermes (not verified). A local model is optional. Its file is 3 to 20 GB, by model (section 2).
- A web connection. A local model download is large. Do it at home.
- You do not need administrator rights. Do not run Hermes as Administrator. If your account belongs to the Administrators group, read "Use an administrator account safely" before section 1.
- Section 3, path B needs a payment card. Path A does not.
- Section 7 only: Git for Windows (https://git-scm.com/downloads/win), Node.js 22.20 or later, and a .NET SDK. Section 7 gives the details.
- Optional: update your graphics driver before you use a local model. The minimum driver version on Windows is not verified.

External software and MCP servers in this file are examples. You can replace them with tools you prefer. Why: [install why](install-why.md).

An MCP is a connector that lets Hermes talk to another program. The Windows example is vvvv. vvvv is a live visual programming environment.

Read the permissions and capability rule before section 7: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

## Use an administrator account safely

Many people use an account that belongs to the Administrators group. That is fine for this guide. A separate standard account is not required. Hermes does not need administrator rights.

The rules that all systems share are on one page: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). This section keeps the Windows facts and the Windows checks.

An administrator account has two tokens when User Account Control (UAC) is on. A token is the list of rights that a program gets. Windows starts Explorer and your normal terminal with the filtered token. That token works like a standard user. Windows uses the full token only when you approve a UAC prompt. Source: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/user-account-control/how-it-works (checked 25 Nov 2026).

Know these limits:

- Microsoft calls a standard account the more secure way to run Windows. An administrator account in Admin Approval Mode is a supported second choice. For work with real data, a standard daily account is the better habit.
- UAC is not a security boundary. Microsoft says so: https://learn.microsoft.com/en-us/archive/blogs/e7/update-on-uac
- Hermes runs as your Windows user, with or without a UAC prompt. A normal terminal can still read and change your own files. Hermes approvals are a guardrail for honest mistakes. They are not a sandbox. Source: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine
- Some Windows 11 computers use "Administrator protection". It is off by default. Microsoft says that a security baseline can turn it on. With it, an elevated program runs as a hidden second account with its own profile. Anything you install in an elevated window may land in that other profile. This is one more reason to install without elevation. Source: https://learn.microsoft.com/en-us/windows/security/application-security/application-control/administrator-protection/ (whether it is on for the test computer: not verified).

What each install method does, checked 25 Nov 2026:

| | Hermes Desktop (MSIX, `.appinstaller`) | Hermes Desktop (Microsoft Store) | Command-line script `install.ps1` |
|---|---|---|---|
| Scope | Per user (Microsoft: MSIX installs per user) | Per user, Store-owned | Per user |
| Needs elevation | No (not verified on a real machine) | No (not verified on a real machine) | No. Hermes docs say "No admin rights required". The script has no administrator check or UAC call |
| Program files | Inside the package. Windows keeps package files under `C:\Program Files\WindowsApps` and locks them | The same | `%LOCALAPPDATA%\hermes\hermes-agent\` |
| Your data | `%LOCALAPPDATA%\hermes\` (Hermes docs; not verified for the Store package) | The same | `%LOCALAPPDATA%\hermes\` |
| Signature | Signed bundle. Publisher in the build files: `CN=Nous Research Inc.` | Store signs it. Publisher name: not verified | None on the script. It checks the SHA-256 hash of the uv and Git files that it downloads. Hermes publishes no checksum for `install.ps1` (not found) |
| Hosts | Hermes download page | Microsoft Store | `github.com`, `api.github.com`, `hermes-assets.nousresearch.com` (script text). Later steps may use more hosts (not verified) |
| Update | The Update control in Hermes, through Windows App Installer | Microsoft Store | `hermes update` |
| Remove | Windows Settings, Apps, Installed apps | The same | `hermes uninstall` |
| Changes to PATH | Execution aliases (`hermes`, `hermes-agent`, `hermes-acp`) | The same | Your user `Path` only |

Sources: https://hermes-agent.nousresearch.com/docs/getting-started/installation, https://hermes-agent.nousresearch.com/docs/user-guide/windows-native, https://hermes-agent.nousresearch.com/docs/getting-started/updating, the Hermes desktop build notes (`apps/desktop/BUILDING.md` in the Hermes repository), and Microsoft: https://learn.microsoft.com/en-us/windows/msix/desktop/desktop-to-uwp-behind-the-scenes

### Test-run checklist

Do these in order. A line that starts with STOP means: stop, do not continue, and tell the teacher.

1. Keep UAC on. Search the Start menu for "Change User Account Control settings". Leave the slider at its default. Do not choose "Never notify". With that setting Windows still gives you a split token but approves every elevation for you (Microsoft Win32 UAC page).
2. Open a normal Windows Terminal, as in section 3b. Do not choose "Run as administrator". Check it. Type `whoami /groups | Select-String "Mandatory Label"` and press Enter. The line must say `Medium Mandatory Level`. STOP if it says `High Mandatory Level`. Close the window and open a normal one.
3. Install Hermes Desktop from the official page (section 1). Check the host name in the address bar: `hermes-agent.nousresearch.com`. STOP if it is another host.
4. Read the Windows App Installer window before you click Install. It shows the app name and the publisher. The publisher must be Nous Research. How the window shows the publisher: not verified. STOP if the publisher is another name, or if the file is not signed.
5. After the install, type this in the normal terminal and press Enter: `Get-AppxPackage *hermes* | Format-List Name, Publisher, SignatureKind, InstallLocation`. For the `.appinstaller` package, expect a Publisher that contains `CN=Nous Research Inc.`. The value of `SignatureKind` is not verified. Write down what you see.
6. STOP if any UAC prompt appears while you install or start Hermes Desktop. No official page says Hermes Desktop needs one. Click No.
7. Elevate only for a named step. In this guide, only section 7 may ask for UAC:
   - The .NET SDK installer. Microsoft says the native installer installs system-wide and needs administrator rights.
   - The Git for Windows installer. For an administrator account it asks for UAC and installs to `C:\Program Files\Git` (Git for Windows installer script). Hermes does not need it. You need it only for the `git clone` step in section 7.
   - Node.js: not verified.
   Read the UAC window. It must show a verified publisher. Click Yes for that one installer. Then close the installer. Go back to your normal terminal. Do not keep an elevated window open.
8. Do not paste a secret in a terminal. Enter keys in the Hermes Settings window or in the `.env` file (section 4, step 5). PowerShell saves typed commands in a history file, and its filter can miss a key. For this window, you can type `Set-PSReadLineOption -HistorySaveStyle SaveNothing`. What to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets).
9. Use manual approvals before the first task. Type `hermes config set approvals.mode manual`. Then type `hermes config get approvals.mode`. The answer must be `manual`. Hermes still does not ask before it writes a file. Details: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#6-approvals).
10. Use the test folder only: `hermes-smoke-test` from section 3b. Not Documents, the Desktop, a cloud-sync folder, or your private vault. Details: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#4-the-test-folder).
11. Do not run `hermes gateway install` or set up messaging today. On Windows it registers a Scheduled Task and asks for UAC once. Details: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#7-the-messaging-gateway).
12. Do not update during the class. An update changes the package while you work.

### Rollback and uninstall

1. Quit Hermes.
2. Desktop package: open Windows Settings, then Apps, then Installed apps. Find Hermes and choose Uninstall. This removes the app. It does not remove your data.
3. Script install: type `hermes uninstall --dry-run` and read the list. Then type `hermes uninstall`.
4. Do not use `--full` unless you want to delete your config, keys, chats and skills. Make a backup first. All rules: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#9-rollback-and-uninstall).
5. Delete the `hermes-smoke-test` folder yourself. Revoke the API key at the provider.
6. If you did section 7, type `dotnet tool uninstall -g vvvv-mcp` (not verified). Remove the vvvv MCP block from `config.yaml`.
7. If you installed .NET or Git, remove them in Windows Settings, Apps, Installed apps. The UAC prompt may appear again.

Not verified, on a real Windows 11 Enterprise 25H2 machine: all of the items marked above, the label of every window, and whether company policy blocks sideloaded packages. Windows 11 has sideloading on by default (Microsoft Learn). If App Installer says it is blocked, STOP and use the Microsoft Store button. Do not change a policy to make it work.

## 1. Install Hermes Desktop

You install Hermes on your own laptop.

Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

Check your Windows version first. Press the Windows key and R together, type `winver`, and press Enter. You need Windows 11, version 22H2 or later. If you have an older version, do not use this package. Work with a neighbour, or use the command-line route in [howto hermes setup](howto-hermes-setup.md) §2, Option B.

1. Open https://hermes-agent.nousresearch.com/desktop
2. Click the Microsoft Store button. If the Store is blocked on your laptop, click the main download button. It gives you an `.appinstaller` file. The exact label of that button is not verified.
3. Do not click "Download .exe instead". That file builds Hermes from source. It takes much longer.
4. If you downloaded the `.appinstaller` file, open it with Windows App Installer.
5. Open Hermes from the Start menu.
6. Do not run Hermes as Administrator. Start it from the Start menu, as a normal user.
7. On first start, Hermes asks you to choose a layout and a provider. Choose Basic. "Choose provider later" is fine. You set the model in section 3.

More Windows notes, including the command-line installer: [howto hermes setup](howto-hermes-setup.md) §2. Install page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

Hermes keeps its files in `%LOCALAPPDATA%\hermes\`. For the Store package this is not verified on a real machine. After you save a key in section 3, check that `%LOCALAPPDATA%\hermes\.env` exists.

## 2. Load one local model (optional)

A local model runs on this computer. It does not need an API key. Nothing leaves your computer.

This section is optional. The default for class is section 3, path A (a free OpenRouter model, no card). Do section 3 and the first test (section 3b) first. Come back here when the first test works, or at home on a good connection. A model file is 3 to 20 GB.

Small local models are weaker at agent tasks than cloud models. They make more mistakes with tool calls. They lose the thread of a long task sooner. They are often slower. Example from the Gemma 4 model card (vendor numbers, checked 25 Nov 2026): on the Tau2 tool-use test, the 31B model scores 76.9% and the E4B model scores 42.2%. Use a small model to learn how the parts fit. Do not expect it to match a cloud model.

VRAM is the memory on the graphics card. The Windows test machine for this guide has an NVIDIA GeForce RTX 5080 with 16 GB of VRAM (Windows 11 Enterprise 25H2). Your computer may have a different card. Find your VRAM in Task Manager: open the Performance tab, then click your GPU, and read "Dedicated GPU memory".

Pick a row for your VRAM. Sizes are download sizes from the model pages, checked 25 Nov 2026. All models in the table are marked "tools" on the Ollama or LM Studio pages. This course did not run any of them with Hermes on 25 Nov 2026 (not verified).

| VRAM | Example models (4-bit unless noted) | Download | Tool calls | Trade-offs |
|---|---|---|---|---|
| 8 GB | Qwen3.5 4B; Gemma 4 E4B | 3.3 GB; 6.6 GB | Yes; yes | Fast and small. Gemma 4 E4B is tight at 64K context. Weakest at multi-step work |
| 12 GB | Gemma 4 12B; Qwen3.5 9B | 8.0 GB; 6.6 GB | Yes; yes | Good first choice. Less room for a long chat |
| 16 GB | Gemma 4 12B or Qwen3.5 9B (8-bit); Gemma 4 26B A4B | 13 GB or 10 GB; 15.6 GB | Yes; yes | 8-bit is a little more exact. The 26B model may spill into system RAM and slow down |
| 24 GB | Qwen3.8 27B (Hermes catalog); Gemma 4 31B | 16.5 GB (18.5 GB with image and draft files); 19 to 20 GB | Yes; yes | Best quality here. Big download. The Hermes Ollama guide names only Gemma 4 31B as reliable for tools |

"Reasoning" models think before they answer. Gemma 4, Qwen3.5, and Qwen3.8 are marked as reasoning models. They use more tokens and take longer for each reply. Granite 4.1 (3B, 8B) has tool calls but no reasoning mark. Details, sources, and more models: [install why](install-why.md).

Context is the chat plus the files the agent sends. Hermes needs at least 64,000 tokens of context for tool work. Hermes sets this for you only for models it loads itself. Ollama starts with 4,096 tokens when the card has less than 24 GB of VRAM, so you must raise it. A larger context also needs more VRAM. The sources do not give that size (not verified). Check the fit before you download or load.

System memory is the normal RAM in the computer. Offload means part of the model sits in that RAM. The model can run. It can also be slow.

Tool calling means the model asks Hermes to run a tool.

Choose one route.

Route 1, the Hermes catalog. The catalog has no small model. It lists Qwen3.8 27B first. It fits the 24 GB row. On 16 GB, the fit label can say the model uses system RAM. Hermes docs say 16 GB or more runs the 27B to 35B models at high quality. This course did not check that on the 5080 (not verified).

1. In Hermes Desktop, open Settings.
2. Open Providers.
3. Open Local Models.
4. Click Install runtime. Wait until it finishes.
5. Read the fit label on the Qwen3.8 27B row.
6. Click Download only when the label says the model fits, or when it says "uses system RAM" and you accept the slowdown.
7. Read the label again. Click Use.
8. If the label says the model is too big, stop. Use route 2 or section 3.

Route 2, Find more models. The same page has a Find more models box. It searches Hugging Face and shows a fit check for each file. Search for a name from the table, for example `gemma-4-12b` or `qwen3.5-9b`. Pick a 4-bit file (`Q4_K_M` or similar) that the fit check marks green. Hermes picks the context window from the model file. Hermes did not test these models. This course did not try the box (not verified).

Route 3, LM Studio. Hermes lists LM Studio as a model provider. LM Studio shows a size estimate before it loads a model. This exact order was not run on Windows for this course (not verified).

1. Install LM Studio from https://lmstudio.ai/download.
2. In LM Studio, search for a model from the table and download it. Example model id: `google/gemma-4-12b`.
3. Open Windows Terminal. Check the fit: `lms load google/gemma-4-12b --context-length 64000 --estimate-only`
4. If the estimate is more than your VRAM, choose a smaller model.
5. Load the model: `lms load google/gemma-4-12b --context-length 64000`
6. Start the server: `lms server start`
7. In Windows Terminal, type `hermes model`. Choose LM Studio. Press Enter to use `http://localhost:1234/v1`. Pick the model.

Ollama works too. Hermes needs a 64,000 token context there. Set it before you start the server. In PowerShell, type `$env:OLLAMA_CONTEXT_LENGTH = 64000` and then `ollama serve`. If the Ollama app already runs in the tray, quit it first, or the setting may not apply (not verified). Then type `ollama ps` and read the CONTEXT column. In `hermes model`, choose Custom endpoint and use `http://localhost:11434/v1`. The Ollama installer step on Windows is not described here (not verified).

If a download is not done after 5 minutes, stop and go to section 3. On the first reply, a local model can stay silent for minutes. Hermes sends a large fixed prompt each time. This is expected.

If the model prints raw tool text such as `{"name": ...}` instead of running the tool, the server is not set up for tool calls. Hermes docs say this is usually the server, not the model. Use section 3 for class.

Facts, sources, and the Qwen3.8 27B file sizes: [install why](install-why.md). Research note: [local gpu hardware for llms](../../../research/software&DataManagement/local-gpu-hardware-for-llms.md).

Free cloud models already listed for this course: [default setup](default-setup.md) §4 and [howto hermes setup](howto-hermes-setup.md) §3. Do not copy that list. Do not send private notes through a free cloud model until you have read §4. Section 3, path A, uses that free route.

Hermes local model docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

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
3. Do not run Hermes as Administrator. Do not expose the gateway. Keys stay in the Hermes env file: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets)
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
