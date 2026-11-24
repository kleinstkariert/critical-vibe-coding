---
status: current
canonical: true
---

# How to: Hermes Agent setup

*reference implementation. Optional extension. Not required for assessment.* This page is the worked Hermes install. It is not the assessed system. See [minimum path](../../PROJECT-WORK/01_minimum-path.md). Other tools are compared in the [tool comparison](../../../research/software&DataManagement/vibe-coding-tools-and-agent-environments.md).

Practical guide for Critical Vibe Coding and personal use on **Windows**, **macOS**, and **Linux**. Hermes Agent is **MIT** open source (Nous Research). It is the **agent**, not the Hermes 4 chat models.

Related: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md) · [knowledge store options](../02-knowledge-bases/knowledge-store-options.md) · [what is mcp](../06-mcp-and-tools/what-is-mcp.md) · [howto hermes efficient coding](howto-hermes-efficient-coding.md) · [agents md template](agents-md-template.md) · [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) · [karpathy llm wiki and openclaw](../../../research/software&DataManagement/karpathy-llm-wiki-and-openclaw.md)

*requirement:* phone sync of the **notes** is via Obsidian + cloud (see Obsidian how-to). Hermes usually runs on the **computer** and edits the local vault folder. The phone does not need Hermes installed.

Official install matrix: https://hermes-agent.nousresearch.com/docs/getting-started/installation  
Hermes Desktop product page: https://hermes-agent.nousresearch.com/desktop  
Desktop docs: https://hermes-agent.nousresearch.com/docs/user-guide/desktop

---

## 1. What Hermes is (for this course)

| | |
|---|---|
| **Hermes Agent** | Tool-using agent: files, terminal, skills, optional MCP |
| **Hermes Desktop** | Native GUI for the **same** agent (sessions, skills, memory, tools). Closer to Cursor / Claude Cowork as an app surface than the terminal alone |
| **Hermes 4 models** | Separate chat/reasoning models. Portal docs say they are **not** ideal as the agent’s tool-calling model |
| **LLM Wiki skill** | Karpathy-style folder wiki (`WIKI_PATH`) |
| **Obsidian skill** | Same folder via `OBSIDIAN_VAULT_PATH` + file tools |

Docs: https://hermes-agent.nousresearch.com/docs/

Architecture / security overview (course): [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md)

---

## 2. Install by platform

*technical suggestion for class:* install **Hermes Desktop** when your OS supports it. You get a GUI agent workspace (chat, skills, tools) without living only in the terminal. CLI still works and shares the same config.

The Desktop package is a file you open. It is not a script piped into a shell. Prefer it when the download page offers it.

## Read the installer before you run it

A pipe sends a downloaded script straight into a shell. The shell runs it before you can read it.

Each command-line install below has two paths.

- Path A is the convenience path. The pipe stays there.
- Path B saves the script, shows it, then runs it.

Use path B.

The Hermes install page does not publish a checksum for `install.sh` or `install.ps1`. A checksum is a short fingerprint of a file. This course does not invent one. Page: https://hermes-agent.nousresearch.com/docs/getting-started/installation

The script does check the uv tool it downloads. That check does not prove that `install.sh` or `install.ps1` is the file from the official page. Read the saved file.

While you read, look for `curl`, `irm`, and `git clone` lines. The host should be `hermes-agent.nousresearch.com`, `hermes-assets.nousresearch.com`, or `github.com`. Stop if you see a different host.

### Windows

#### Option A. Hermes Desktop (recommended UI)

1. Open https://hermes-agent.nousresearch.com/desktop and download the Windows package, **or** install from the Microsoft Store listing linked there.
2. Open the `.appinstaller` / MSIX with **Windows App Installer** (signed bundle). MSIX Desktop needs a recent Windows 11 build for the Store/MSIX path; source CLI still supports Windows 10.
3. First launch uses the same Hermes home as the CLI: `%LOCALAPPDATA%\hermes\`.
4. Optional: if you already installed CLI only, run `hermes desktop` to build/launch the desktop shell against your existing config.

#### Option B. CLI only (PowerShell)

1. Click the Start button.
2. Type `Windows Terminal`.
3. Press Enter.
4. If Windows Terminal is not in the list, type `PowerShell` and press Enter.
5. You type at the blinking cursor. Do not start the window as Administrator.

The host must be `hermes-agent.nousresearch.com`. Stop if it is not.

##### Path A. Convenience

1. Click the terminal window.
2. Type the next line and press Enter. The script runs as soon as it downloads.

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

`irm` downloads the text. `iex` runs that text. You do not see the script first.

##### Path B. Inspectable

1. Click the terminal window.
2. Type `cd $HOME` and press Enter.
3. Type the next line and press Enter. This saves `install.ps1` in your home folder. It does not run it.

```powershell
curl.exe -fsSL https://hermes-agent.nousresearch.com/install.ps1 -o install.ps1
```

4. Type `notepad install.ps1` and press Enter. Notepad opens the script.
5. Read the script. Close Notepad.
6. Type the next line and press Enter.

```powershell
powershell -NoProfile -File .\install.ps1
```

What the Windows script changes, from the Hermes install layout and from `install.ps1`, checked 20 Nov 2026:

- Program files: `%LOCALAPPDATA%\hermes\hermes-agent\`
- Commands: `%LOCALAPPDATA%\hermes\bin\`
- Your Hermes data: `%LOCALAPPDATA%\hermes\`
- It adds that `bin` folder to your user `Path`

1. Close the terminal.
2. Open Windows Terminal again.
3. Type `hermes --help` and press Enter.

Uninstall, from https://hermes-agent.nousresearch.com/docs/user-guide/windows-native :

1. Open Windows Terminal.
2. Type `hermes uninstall --dry-run` and press Enter. This lists files. It does not delete them.
3. Type `hermes uninstall` and press Enter to remove the program and keep your data.
4. Type `hermes uninstall --full` only when you also want the data folder deleted.
5. A Store or MSIX app is removed in Settings, Apps, Installed apps. The script uninstaller does not remove that package.

Windows native notes: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native  
Default data home: `%LOCALAPPDATA%\hermes\`

---

### macOS

*institutional summary (Hermes install docs, 2026-10-18):* Desktop package is **Apple Silicon only**. Intel Macs are not a supported Desktop platform: use the CLI script or another machine.

#### Option A. Hermes Desktop (Apple Silicon, recommended UI)
1. Download the macOS package from https://hermes-agent.nousresearch.com/desktop
2. Open the DMG → copy `Hermes.app` to Applications.
3. First launch may need System Settings → Privacy & Security approval if Gatekeeper blocks an unidentified developer build (follow on-screen / Nous notes).
4. Same agent core as CLI: config, keys, sessions, skills.

#### Option B. CLI (Apple Silicon or when Desktop is unavailable)

1. Press Command and the space bar together.
2. Type `Terminal`.
3. Press Return.

##### Path A. Convenience

1. Click the Terminal window.
2. Type `cd` and press Return.
3. Type the next line and press Return. Do not type `sudo` before it.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

##### Path B. Inspectable

1. Click the Terminal window.
2. Type `cd` and press Return.
3. Type the next line and press Return.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o install.sh
```

4. Type `less install.sh` and press Return.
5. Press the space bar to move down. Press `q` to close the viewer.
6. Type the next line and press Return. Do not type `sudo` before it.

```bash
bash install.sh
```

What the script changes, checked 20 Nov 2026:

- Program files: `~/.hermes/hermes-agent/`
- Command: `~/.local/bin/hermes`
- Your Hermes data: `~/.hermes/`
- A PATH line in `~/.zshrc` and `~/.zprofile` when your shell is zsh

1. Type `source ~/.zshrc` and press Return. On bash, type `source ~/.bashrc` instead.
2. Type `hermes --help` and press Return.
3. If the command is missing, quit Terminal, open it again, and type `hermes --help`.

Uninstall: type `hermes uninstall --dry-run`, then `hermes uninstall`. Use `hermes uninstall --full` only when you also want `~/.hermes/` deleted. Docs: https://hermes-agent.nousresearch.com/docs/getting-started/updating

Default data home: `~/.hermes/`  
CLI launcher typically: `~/.local/bin/hermes` (that directory must be on your `PATH`).

Optional after CLI install:

```bash
hermes desktop
```

---

### Linux

CLI is the primary path (Desktop may be available via source/`hermes desktop` depending on release: prefer the documented script first).

1. Press the Super key.
2. Type `Terminal`.
3. Press Enter.

##### Path A. Convenience

1. Click the terminal window.
2. Type `cd` and press Enter.
3. Type the next line and press Enter. Do not type `sudo` before it.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

##### Path B. Inspectable

1. Click the terminal window.
2. Type `cd` and press Enter.
3. Type the next line and press Enter.

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh -o install.sh
```

4. Type `less install.sh` and press Enter.
5. Press the space bar to move down. Press `q` to close the viewer.
6. Type the next line and press Enter. Do not type `sudo` before it.

```bash
bash install.sh
```

What the script changes, checked 20 Nov 2026:

- Program files: `~/.hermes/hermes-agent/`
- Command: `~/.local/bin/hermes`
- Your Hermes data: `~/.hermes/`
- A PATH line in `~/.bashrc` and `~/.profile` when your shell is bash

1. Type `source ~/.bashrc` and press Enter. On zsh, type `source ~/.zshrc` instead.
2. Type `hermes --help` and press Enter.

Uninstall: type `hermes uninstall --dry-run`, then `hermes uninstall`. Use `hermes uninstall --full` only when you also want `~/.hermes/` deleted. Docs: https://hermes-agent.nousresearch.com/docs/getting-started/updating

**Prerequisites (*institutional summary* from install docs):** Git, curl, tar, SHA-256 utilities. Source installs use a managed Python via PM. On minimal Debian/Ubuntu/RHEL images, `libatomic` may be required for managed Node (`libatomic1` on apt).

**Docker** (server / headless): see Hermes docs for the image and mounted data dir (`/opt/data/` pattern). Useful if the agent should live on a VPS with a synced vault. Official page: https://hermes-agent.nousresearch.com/docs/user-guide/docker · Terminal sandbox click-path: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)

Default data home: `~/.hermes/`  
Nix/NixOS: best-effort flake path in docs: not the class default.

**WSL2:** use the Linux/macOS install script inside WSL; point vault paths at a Windows folder only if you understand the mount path (`/mnt/c/...`) and sync/locking costs. *technical suggestion:* keep vault + Hermes both inside WSL **or** both on Windows native, not half-and-half.

---

## 3. Model / API setup (all platforms)

Fastest path from the docs:

```bash
hermes setup --portal
```

(Windows PowerShell: same command once `hermes` is on PATH.)

One OAuth flow for a model + Tool Gateway (web search, etc.) via Nous Portal.

Or configure another provider:

```bash
hermes model
```

You need **some** API / Portal access. Hermes itself is free/MIT; model usage is separate.

### Free-to-use endpoint used in class (Session 02)

*technical suggestion* (page consulted 10 Nov 2026): **NVIDIA Nemotron 3 Ultra** through OpenRouter. The materials are openly distributed under OpenMDW-1.1. This route is a free-to-use hosted endpoint: $0 per token, tool calling, up to 1 million tokens of context.

1. Create a free account and API key at https://openrouter.ai
2. Add the key to the Hermes env file (`~/.hermes/.env`, on Windows `%LOCALAPPDATA%\hermes\.env`):

   ```env
   OPENROUTER_API_KEY=your-key
   ```

3. Run `hermes model`, choose OpenRouter, then the model `nvidia/nemotron-3-ultra-550b-a55b:free`.

Limits and privacy: 20 requests per minute and 50 per day on a free account. Prompts may be logged. The model is too large for most student machines. Keep private notes away from it until you have checked the data policy. The route is a hosted cloud service: [default setup](default-setup.md) §4. Fallback: the free plan of Nous Portal (`hermes setup --portal`). Hermes guide: https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free

---

## 4. Point Hermes at your Obsidian vault

| Platform | Env file | Example absolute paths |
|---|---|---|
| Windows | `%LOCALAPPDATA%\hermes\.env` | `WIKI_PATH=C:\path\to\MyVault\wiki` |
| macOS / Linux | `~/.hermes/.env` | `WIKI_PATH=/path/to/MyVault/wiki` or `/path/to/MyVault/wiki` |

```env
# Absolute paths. Do not put $variables inside paths Hermes file tools will use.
OBSIDIAN_VAULT_PATH=/absolute/path/to/MyVault/wiki
WIKI_PATH=/absolute/path/to/MyVault/wiki
```

**Important:**

- Use a **real absolute path**. File tools do not expand `$OBSIDIAN_VAULT_PATH` in path arguments.
- Hybrid pattern: the agent owns `wiki/`. You own your artistic project notes elsewhere.
- Obsidian still opens the whole vault. These two Hermes paths point at `wiki/`.
- The first folders for Hermes are `wiki/`, a disposable folder such as `hermes-smoke-test`, and project folders you name in the request.
- A folder name is not a security boundary. The access table is in [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).
- A full-vault path is convenience mode, not recommended for private material.
- Restart Hermes (or Desktop) after changing `.env`.

### Vault path vs AgentShare (two layers)

| Layer | What students do in class | Safer hardening later |
|---|---|---|
| **Hermes `.env` paths** | Point `OBSIDIAN_VAULT_PATH` and `WIKI_PATH` at `MyVault/wiki` | A full-vault path is convenience mode, not recommended for private material |
| **Docker / sandbox mounts** | Optional. Overview [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) recommends mounting only an `AgentShare/` tree into containers | Never mount `Private/`, finance, health, or credential folders into a coding container |

The smoke test uses a new folder named `hermes-smoke-test` in your home folder. It does not use the vault. The vault path in `.env` is for later note work. Container `AgentShare` rules are **extra** isolation for untrusted or Docker runs. They do not replace Obsidian sync. Phone sync: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md).

Obsidian skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian  
LLM Wiki skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki

---

## 5. First run (CLI or Desktop)

**Desktop (GUI closer to Cursor / Cowork):** open Hermes Desktop from the Start menu / Applications, or:

```bash
hermes desktop
```

**CLI:**

```bash
hermes
```

The first request uses one synthetic file. Make that file before you ask Hermes anything.

Windows:

1. Open File Explorer from the taskbar.
2. Open your user folder.
3. Create a folder named `hermes-smoke-test` and open it.
4. Create `note.txt` in that folder.
5. Type this sentence in the file: The smoke test file says hello.
6. Save the file.
7. Copy the folder path from the address bar.

Linux:

1. Open a terminal.
2. Type `mkdir "$HOME/hermes-smoke-test"` and press Enter.
3. Type `printf '%s\n' 'The smoke test file says hello.' > "$HOME/hermes-smoke-test/note.txt"` and press Enter.
4. Type `xdg-open "$HOME/hermes-smoke-test"` and press Enter.
5. Type `echo "$HOME/hermes-smoke-test/note.txt"` and press Enter. Copy that path.

macOS:

1. Open Finder.
2. Click Go, then Home.
3. Create a folder named `hermes-smoke-test` and open it.
4. Open TextEdit. Click Format, then Make Plain Text.
5. Type this sentence: The smoke test file says hello.
6. Save the file as `note.txt` inside `hermes-smoke-test`.
7. Open Terminal. Type `echo "$HOME/hermes-smoke-test/note.txt"` and press Return. Copy that path.

Then paste this request in Hermes. Put your copied path in place of PATH:

Read only this file: PATH. Reply with the one sentence in that file. Do not open any other folder.

The reply must be: The smoke test file says hello. If Hermes names your vault or another folder, stop.

**Keep Obsidian open** on the side if you want to watch files appear (Karpathy: “Obsidian is the IDE; the LLM is the programmer”).

---

## 5b. Skills (short)

Skills are on-demand instruction packages (`SKILL.md`).

```bash
hermes skills list
hermes skills browse
hermes skills install official/research/arxiv   # example
```

In chat: `/skills`. Review third-party skills before install.  
Guide: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills  
Coding harness + skill links: [howto hermes efficient coding](howto-hermes-efficient-coding.md) · template: [agents md template](agents-md-template.md)

---

## 5c. Messaging gateway (optional, Session 05+)

```bash
hermes gateway setup
```

Supported in Hermes docs include Telegram, Discord, Matrix, Signal (`signal-cli`), and others.  
Always set allowlists / pairing on a personal laptop.  
Index: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/  
Signal: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/signal

---

## 5d. Security (minimum)

- Do not run as root. Do not expose the gateway publicly.
- Keys only in Hermes `.env`, never in synced vault notes.
- Novice baseline: read the files first, use a disposable project, keep manual approvals on, give Hermes one narrow write folder, keep a Git or filesystem snapshot, and do not use a private vault.
- Docker is an advanced safety module. Use it as a demonstration or in a separate workshop: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md). Docker adds filesystem sharing, path translation, ownership, network, performance, GPU access, images, and Windows/macOS virtualisation, so it is not the two-hour baseline.
- Concepts and mounts: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §§8 to 9
- Approvals + Git diff review. See overview security rules and https://hermes-agent.nousresearch.com/docs/user-guide/security  
- Work / personal laptop guide: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine  
- Academic chat portals are usually **not** an agent API: [academic ai austria](../03-models-and-providers/academic-ai-austria.md)

---

## 6. LLM Wiki layout (when you turn it on)

```text
wiki/
  SCHEMA.md   (or AGENTS.md / CLAUDE.md; co-evolve with the agent)
  index.md
  log.md
  raw/          # immutable sources
  entities/
  concepts/
  comparisons/
  queries/
```

The default `WIKI_PATH` is `MyVault/wiki`. A full-vault path is convenience mode, not recommended for private material.

Session habit: read schema + index + recent log before ingest/query/lint.

Course notes: [llm wiki standard files](../02-knowledge-bases/llm-wiki-standard-files.md) · [what is lint](../02-knowledge-bases/what-is-lint.md) · [references](../../REFERENCES/bibliography.md)  
Skill docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki  
Karpathy gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
Optional Obsidian plugin: https://community.obsidian.md/plugins/karpathywiki

---

## 7. Optional: MCP (incl. CAD / 3D)

Hermes can attach MCP servers (stdio / HTTP). Use this for tools that are **not** a folder of files, including **Blender / Fusion / FreeCAD / Meshy** (Sessions 05 and 07).

Read the permissions and capability rule before you attach a server: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

Course notes: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary) · [what is harness](what-is-harness.md) · [05 knowledge base phone discord](../../SESSIONS/05-knowledge-base-phone-discord.md) · CAD/3D table: [06 mcp and tools](../06-mcp-and-tools/what-is-mcp.md#cad-and-3d-servers-table-from-retired-session-06)  
Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

---

## 8. Checklist

- [ ] Hermes Desktop **or** `hermes` CLI works after install (new terminal if CLI)
- [ ] Model / Portal configured (`hermes setup --portal` or `hermes model` or the free-to-use OpenRouter endpoint)
- [ ] `.env` has absolute `OBSIDIAN_VAULT_PATH` and `WIKI_PATH` for **this** OS
- [ ] Vault folder exists and syncs to the phone via Obsidian (not via Hermes)
- [ ] Clear rule: which folders Hermes may write vs human-only (`SCHEMA.md` / `AGENTS.md`)
- [ ] Secrets (API keys) in Hermes config / env, **not** in synced notes
- [ ] macOS: Apple Silicon if using Desktop; Intel → CLI only
- [ ] Optional: skills browsed; messaging gateway only with allowlists

---

## 9. Common mistakes

1. Confusing Hermes **Agent** with Hermes **4** model weights.
2. Relative paths or `$OBSIDIAN_VAULT_PATH` inside tool calls.
3. Expecting Hermes on the **phone**. Notes sync via Obsidian; agent stays on the computer (unless you deliberately run Hermes on a VPS with a synced/mounted vault).
4. Two writers fighting: edit the same note in Obsidian while Hermes patches it (use clear folders).
5. Pointing `WIKI_PATH` at Joplin’s SQLite / sync DB: wrong store; see [knowledge store options](../02-knowledge-bases/knowledge-store-options.md).
6. macOS Desktop on Intel: unsupported; use the curl installer instead.
7. WSL + Windows vault without a clear single home for the files.

---

## Sources

- Docs home: https://hermes-agent.nousresearch.com/docs/
- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Hermes Desktop: https://hermes-agent.nousresearch.com/desktop · https://hermes-agent.nousresearch.com/docs/user-guide/desktop
- Windows native: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- Security: https://hermes-agent.nousresearch.com/docs/user-guide/security
- Messaging: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/
- Obsidian skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian
- LLM Wiki skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki
- GitHub: https://github.com/NousResearch/hermes-agent
