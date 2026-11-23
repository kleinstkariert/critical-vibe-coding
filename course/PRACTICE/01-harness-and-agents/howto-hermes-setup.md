---
audience: student
status: current
canonical: true
---

# How to: Hermes Agent setup

*reference implementation. Optional extension. Not required for assessment.* This page is the worked Hermes install. It is not the assessed system. See [minimum path](../../PROJECT-WORK/minimum-path.md).

Practical guide for Critical Vibe Coding and personal use on **Windows**, **macOS**, and **Linux**. Hermes Agent is **MIT** open source (Nous Research). It is the **agent**, not the Hermes 4 chat models.

Related: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md) · [knowledge store options](../02-knowledge-bases/knowledge-store-options.md) · [what is mcp](../06-mcp-and-tools/what-is-mcp.md) · [howto hermes efficient coding](howto-hermes-efficient-coding.md) · [agents md template](agents-md-template.md) · [Local LLM Coding with Hermes](../08-verification-and-provenance/Local%20LLM%20Coding%20with%20Hermes.md) · [karpathy llm wiki and openclaw](../../../research/karpathy-llm-wiki-and-openclaw.md)

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

Architecture / security overview (course): [Local LLM Coding with Hermes](../08-verification-and-provenance/Local%20LLM%20Coding%20with%20Hermes.md)

---

## 2. Install by platform

*technical suggestion for class:* install **Hermes Desktop** when your OS supports it. You get a GUI agent workspace (chat, skills, tools) without living only in the terminal. CLI still works and shares the same config.

### Windows

#### Option A. Hermes Desktop (recommended UI)

1. Open https://hermes-agent.nousresearch.com/desktop and download the Windows package, **or** install from the Microsoft Store listing linked there.
2. Open the `.appinstaller` / MSIX with **Windows App Installer** (signed bundle). MSIX Desktop needs a recent Windows 11 build for the Store/MSIX path; source CLI still supports Windows 10.
3. First launch uses the same Hermes home as the CLI: `%LOCALAPPDATA%\hermes\`.
4. Optional: if you already installed CLI only, run `hermes desktop` to build/launch the desktop shell against your existing config.

#### Option B. CLI only (PowerShell)

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

Then **open a new terminal** (PATH updates to `%LOCALAPPDATA%\hermes\bin`).

```powershell
hermes --help
```

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

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Reload the shell, then check:

```bash
source ~/.zshrc   # or ~/.bashrc
hermes --help
```

Default data home: `~/.hermes/`  
CLI launcher typically: `~/.local/bin/hermes` (ensure that directory is on your `PATH`).

Optional after CLI install:

```bash
hermes desktop
```

---

### Linux

CLI is the primary path (Desktop may be available via source/`hermes desktop` depending on release: prefer the documented script first).

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc   # or ~/.zshrc
hermes --help
```

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
| Windows | `%LOCALAPPDATA%\hermes\.env` | `OBSIDIAN_VAULT_PATH=C:\path\to\your\notes` |
| macOS / Linux | `~/.hermes/.env` | `OBSIDIAN_VAULT_PATH=/path/to/your/notes` |

```env
# Absolute paths. Do not put $variables inside paths Hermes file tools will use.
OBSIDIAN_VAULT_PATH=/absolute/path/to/your/vault
WIKI_PATH=/absolute/path/to/your/vault
```

**Important:**

- Use a **real absolute path**. File tools do not expand `$OBSIDIAN_VAULT_PATH` in path arguments.
- For a dedicated LLM Wiki inside the vault later, set both paths to for example `wiki/` inside your own notes folder (create that folder first). Hybrid pattern: agent owns `wiki/`, you own artistic project notes elsewhere.
- Restart Hermes (or Desktop) after changing `.env`.

### Vault path vs AgentShare (two layers)

| Layer | What students do in class | Safer hardening later |
|---|---|---|
| **Hermes `.env` paths** | Point `OBSIDIAN_VAULT_PATH` / `WIKI_PATH` at the vault (or `wiki/`) so Hermes can edit notes | Narrow to an agent-writable subfolder when you are ready |
| **Docker / sandbox mounts** | Optional. Overview [Local LLM Coding with Hermes](../08-verification-and-provenance/Local%20LLM%20Coding%20with%20Hermes.md) recommends mounting only an `AgentShare/` tree into containers | Never mount `Private/`, finance, health, or credential folders into a coding container |

Class smoke test uses the vault path in `.env`. Container `AgentShare` rules are **extra** isolation for untrusted or Docker runs. They do not replace Obsidian sync. Phone sync: [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md).

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

Try: ask it to list notes in the vault, or to create a test page under a folder you agree is agent-writable (e.g. `wiki/`).

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
- Prefer Docker / sandbox for untrusted code. Local backend = **no** isolation.
- Turn on the Docker terminal backend: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md) · https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Concepts and mounts: [Local LLM Coding with Hermes](../08-verification-and-provenance/Local%20LLM%20Coding%20with%20Hermes.md) §§8 to 9
- Approvals + Git diff review. See overview security rules and https://hermes-agent.nousresearch.com/docs/user-guide/security  
- Work / personal laptop guide: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine  
- Academic chat portals are usually **not** an agent API: [academic ai austria](../03-models-and-providers/academic-ai-austria.md)

---

## 6. LLM Wiki layout (when you turn it on)

```text
wiki/   (or whole vault if WIKI_PATH = vault)
  SCHEMA.md   (or AGENTS.md / CLAUDE.md; co-evolve with the agent)
  index.md
  log.md
  raw/          # immutable sources
  entities/
  concepts/
  comparisons/
  queries/
```

Session habit: read schema + index + recent log before ingest/query/lint.

Course notes: [llm wiki standard files](../02-knowledge-bases/llm-wiki-standard-files.md) · [what is lint](../02-knowledge-bases/what-is-lint.md) · [references](../../syllabus/references.md)  
Skill docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki  
Karpathy gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
Optional Obsidian plugin: https://community.obsidian.md/plugins/karpathywiki

---

## 7. Optional: MCP (incl. CAD / 3D)

Hermes can attach MCP servers (stdio / HTTP). Use this for tools that are **not** a folder of files, including **Blender / Fusion / FreeCAD / Meshy** (Sessions 05 and 07).

Course notes: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary) · [what is harness](what-is-harness.md) · [05 knowledge base phone discord](../../SESSIONS/05-knowledge-base-phone-discord.md) · CAD/3D table: [06 mcp and tools](../../SESSIONS/archive-13-session-plan/06-mcp-and-tools.md)  
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
