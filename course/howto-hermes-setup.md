# How to: Hermes Agent setup

Practical guide for Critical Vibe Coding and personal use on **Windows**, **macOS**, and **Linux**. Hermes Agent is **MIT** open source (Nous Research). It is the **agent**, not the Hermes 4 chat models.

Related: [[howto-obsidian-setup-and-sync]] · [[knowledge-store-options]] · [[what-is-mcp]] · [[../research/karpathy-llm-wiki-and-openclaw]]

*requirement:* phone sync of the **notes** is via Obsidian + cloud (see Obsidian how-to). Hermes usually runs on the **computer** and edits the local vault folder. The phone does not need Hermes installed.

Official install matrix: https://hermes-agent.nousresearch.com/docs/getting-started/installation

---

## 1. What Hermes is (for this course)

| | |
|---|---|
| **Hermes Agent** | Tool-using agent: files, terminal, skills, optional MCP |
| **Hermes 4 models** | Separate chat/reasoning models — Portal docs say **not** ideal as the agent’s tool-calling model |
| **LLM Wiki skill** | Karpathy-style folder wiki (`WIKI_PATH`) |
| **Obsidian skill** | Same folder via `OBSIDIAN_VAULT_PATH` + file tools |

Docs: https://hermes-agent.nousresearch.com/docs/

---

## 2. Install by platform

### Windows

#### Option A — Desktop installer
Download Hermes Desktop from the Nous site and run the installer (CLI + desktop). Opens with Windows App Installer (`.appinstaller` / MSIX).

#### Option B — CLI only (PowerShell)

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

*verified fact (Hermes install docs, 2026-10-18):* Desktop package is **Apple Silicon only**. Intel Macs are not a supported Desktop platform — use the CLI script or another machine.

#### Option A — Desktop (Apple Silicon)
1. Download the macOS package from the Hermes site.
2. Open the DMG → copy `Hermes.app` to Applications.
3. First launch may need System Settings → Privacy & Security approval if Gatekeeper blocks an unidentified developer build (follow on-screen / Nous notes).

#### Option B — CLI (Apple Silicon or when Desktop is unavailable)

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

CLI is the primary path (Desktop may be available via source/`hermes desktop` depending on release — prefer the documented script first).

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
source ~/.bashrc   # or ~/.zshrc
hermes --help
```

**Prerequisites (*verified fact* from install docs):** Git, curl, tar, SHA-256 utilities. Source installs use a managed Python via PM. On minimal Debian/Ubuntu/RHEL images, `libatomic` may be required for managed Node (`libatomic1` on apt).

**Docker** (server / headless): see Hermes docs for the image and mounted data dir (`/opt/data/` pattern). Useful if the agent should live on a VPS with a synced vault.

Default data home: `~/.hermes/`  
Nix/NixOS: best-effort flake path in docs — not the class default.

**WSL2:** use the Linux/macOS install script inside WSL; point vault paths at a Windows folder only if you understand the mount path (`/mnt/c/...`) and sync/locking costs — *technical suggestion:* keep vault + Hermes both inside WSL **or** both on Windows native, not half-and-half.

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

You need **some** API / Portal access — Hermes itself is free/MIT; model usage is separate.

---

## 4. Point Hermes at your Obsidian vault

Teacher vault on Windows (*verified fact* for this workspace):

`C:\Users\sebas\Nextcloud\KnowledgeBaseObsidian`

| Platform | Env file | Example absolute paths |
|---|---|---|
| Windows | `%LOCALAPPDATA%\hermes\.env` | `OBSIDIAN_VAULT_PATH=C:\Users\sebas\Nextcloud\KnowledgeBaseObsidian` |
| macOS / Linux | `~/.hermes/.env` | `OBSIDIAN_VAULT_PATH=/Users/you/Nextcloud/KnowledgeBaseObsidian` or `/home/you/Nextcloud/...` |

```env
# Absolute paths — no $variables inside paths Hermes file tools will use
OBSIDIAN_VAULT_PATH=/absolute/path/to/your/vault
WIKI_PATH=/absolute/path/to/your/vault
```

**Important:**

- Use a **real absolute path**. File tools do not expand `$OBSIDIAN_VAULT_PATH` in path arguments.
- For a dedicated LLM Wiki inside the vault later, set both paths to e.g. `.../KnowledgeBaseObsidian/wiki` (create that folder first). Hybrid pattern: agent owns `wiki/`, you own artistic project notes elsewhere.
- Restart Hermes after changing `.env`.

Obsidian skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian  
LLM Wiki skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki

---

## 5. First run

```bash
hermes
```

Or Desktop if installed:

```bash
hermes desktop
```

Try: ask it to list notes in the vault, or to create a test page under a folder you agree is agent-writable (e.g. `wiki/`).

**Keep Obsidian open** on the side if you want to watch files appear (Karpathy: “Obsidian is the IDE; the LLM is the programmer”).

---

## 6. LLM Wiki layout (when you turn it on)

```text
wiki/   (or whole vault if WIKI_PATH = vault)
  SCHEMA.md   (or AGENTS.md / CLAUDE.md — co-evolve with the agent)
  index.md
  log.md
  raw/          # immutable sources
  entities/
  concepts/
  comparisons/
  queries/
```

Session habit: read schema + index + recent log before ingest/query/lint.

Course notes: [[llm-wiki-standard-files]] · [[what-is-lint]] · [[references]]  
Skill docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki  
Karpathy gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f  
Optional Obsidian plugin: https://community.obsidian.md/plugins/karpathywiki

---

## 7. Optional: MCP (incl. CAD / 3D)

Hermes can attach MCP servers (stdio / HTTP). Use this for tools that are **not** a folder of files — including **Blender / Fusion / FreeCAD / Meshy** in session 5.

Course notes: [[what-is-mcp]] · [[what-is-harness]] · [[sessions/05-mcp-and-tools]]  
Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp

---

## 8. Checklist

- [ ] `hermes` works in a **new** terminal after install
- [ ] Model / Portal configured (`hermes setup --portal` or `hermes model`)
- [ ] `.env` has absolute `OBSIDIAN_VAULT_PATH` and `WIKI_PATH` for **this** OS
- [ ] Vault folder exists and syncs to the phone via Obsidian (not via Hermes)
- [ ] Clear rule: which folders Hermes may write vs human-only
- [ ] Secrets (API keys) in Hermes config / env — **not** in synced notes
- [ ] macOS: Apple Silicon if using Desktop; Intel → CLI only

---

## 9. Common mistakes

1. Confusing Hermes **Agent** with Hermes **4** model weights.
2. Relative paths or `$OBSIDIAN_VAULT_PATH` inside tool calls.
3. Expecting Hermes on the **phone** — notes sync via Obsidian; agent stays on the computer (unless you deliberately run Hermes on a VPS with a synced/mounted vault).
4. Two writers fighting: edit the same note in Obsidian while Hermes patches it (use clear folders).
5. Pointing `WIKI_PATH` at Joplin’s SQLite / sync DB — wrong store; see [[knowledge-store-options]].
6. macOS Desktop on Intel — unsupported; use the curl installer instead.
7. WSL + Windows vault without a clear single home for the files.

---

## Sources

- Docs home: https://hermes-agent.nousresearch.com/docs/
- Installation: https://hermes-agent.nousresearch.com/docs/getting-started/installation
- Windows native: https://hermes-agent.nousresearch.com/docs/user-guide/windows-native
- Obsidian skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian
- LLM Wiki skill: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki
- GitHub: https://github.com/NousResearch/hermes-agent
