# Knowledge store options

**Working title.** Other names that also fit: “Where notes live”, “Note tools for agent workflows”. This note compares three places to keep an agent-readable (and human-readable) knowledge base for Critical Vibe Coding / personal practice.

**Requirement (owner, 2026-10-15):** **Phone sync is mandatory.** A knowledge base that only lives on the laptop is not enough for today’s normal practice (read/capture on the phone, work on the PC).

**Course decision (updated):** For students → **Obsidian + personal cloud (e.g. Nextcloud)** so phone sync works **without** each person running a server. Joplin is not kept just for MCP. SilverBullet stays interesting for a personal open-source stack **if** you host a Server; it is **not** the class default because phone UI expects that Server.

| Stack piece | Open source? | Phone sync without own server? |
|-------------|--------------|--------------------------------|
| **Hermes Agent** | **Yes — MIT** | n/a (runs where files are) |
| **Obsidian** | Free; **closed source** | **Yes** — app + Nextcloud / Remotely Save (or paid Sync) |
| **SilverBullet Server** | **Yes — MIT** | Needs a **Server** up for PWA/phone |
| **SilverBullet Desktop** | Free personal/edu; Pro for work | Desktop only until Server sync |
| **Joplin** | **Yes — AGPL** | **Yes** native apps + Nextcloud — but SQLite, weak for Hermes folder wiki |

Detailed research: [[../research/obsidian-vs-joplin-hermes-llmwiki]] · [[../research/karpathy-llm-wiki-and-openclaw]] · MCP: [[what-is-mcp]] · How-tos: [[howto-obsidian-setup-and-sync]] · [[howto-silverbullet-setup-and-sync]]

---

## What we need from a “store”

For Hermes + a Karpathy-style (or hybrid) wiki:

1. Notes the **agent can edit** (ideally plain `.md` files in a folder).
2. Notes a **human can browse** on **PC and phone**.
3. **Phone sync** without expecting every student to run Docker/VPS (*requirement*).
4. Optional: **clip** websites into the store.

---

## Option A — Obsidian (chosen)

**What it is:** Closed-source app, free to use. A vault = a folder of markdown files (+ `.obsidian` settings).

### Pros
- Native fit for Hermes / Cursor / filesystem agents (no MCP required for the wiki).
- Matches Karpathy’s “Obsidian as IDE” pattern and Hermes’ bundled skills.
- Strong **Web Clipper** (Chrome, Firefox, Edge, **Safari / iPhone**).
- Huge community, plugins, graph view, wikilinks.
- Git-friendly folder; works next to code projects.

### Cons
- App itself is not open source.
- Official **Obsidian Sync** is paid; free phone sync needs setup (Nextcloud + plugin, etc.).
- Plugin ecosystem = extra trust surface.
- Windows + iCloud is a bad sync idea.

### How to set up (short)
1. Install Obsidian → create/open a vault folder.
2. Sync: see [[howto-obsidian-setup-and-sync]] (Nextcloud + Remotely Save recommended for Win + iPhone).
3. Optional: install Obsidian Web Clipper in the browser.
4. Point Hermes / the agent at the vault path (absolute path).
5. Optional LLM Wiki layout: `raw/`, `SCHEMA.md`, `index.md`, `log.md`, agent folders — see [[llm-wiki-standard-files]] · [[what-is-lint]] · [[references]].

---

## Option B — SilverBullet

**What it is:** Open-source (MIT) markdown space: files in a folder you control. Desktop app and/or self-hosted **server** + browser / PWA (including phone).

### Pros
- Plain `.md` folder → same agent story as Obsidian (filesystem tools).
- Open source; self-host one container; phone via browser/PWA without Obsidian Sync.
- Wikilinks, queries, optional git history; `sb` CLI for agents (experimental).
- Folders via `/` in page names (`Projects/Piece/Notes`).

### Cons
- Smaller ecosystem than Obsidian.
- Docs prefer a **flat** namespace + tags over deep folder trees.
- Clipper exists but is **community / thinner** than Obsidian’s (Chrome/Firefox; not Obsidian-level Safari tooling).
- Self-hosting or Desktop Pro features add ops overhead for beginners.

### How to set up (short)
1. **Desktop:** install SilverBullet Desktop → open a local folder as a space.  
   **Or Server:** run the container pointing at a data folder (see https://silverbullet.md/server).
2. Open in browser / install as PWA on the phone; sync Desktop ↔ Server if you use both.
3. Optional: install **SilverBullet Clipper** (Chrome/Firefox) → saves URL/selection to Inbox.
4. Point Hermes at the same space folder on disk (on the machine where the agent runs).
5. Organise lightly: `Inbox/`, `Journal/`, `Library/`, tags; avoid deep trees unless needed.

Docs: https://silverbullet.md/ · Folders: https://docs.silverbullet.md/Folder

---

## Option C — Joplin

**What it is:** Open-source (AGPL) notes app. Live store = **SQLite** (`database.sqlite`), not a vault of editable `.md` files. Sync to Nextcloud/WebDAV/Dropbox/… is first-party and free of a Joplin fee. Joplin Cloud is optional paid.

### Pros
- Free app; strong free sync (including **Nextcloud / WebDAV**).
- From 3.7: built-in **MCP server** (agent tools while the app/API is running).
- Good teaching example of “database + agent interface” — but we have other MCP exercises for that.

### Cons
- **Not** a plain folder wiki for Hermes file tools; sync folder must not be hand-edited.
- MCP needs the desktop app (or experimental CLI API server) running; localhost only by default.
- No bundled Hermes Joplin skill; wikilinks need a plugin.
- LLM Wiki pattern (agent patches markdown files) needs export/MCP workaround — awkward.

### How to set up (short) — reference only
1. Install Joplin desktop (+ mobile if needed).
2. Sync: Tools → Options → Synchronisation → Nextcloud/WebDAV (dedicated folder; do not also sync it with Nextcloud Desktop).
3. For agents: Joplin 3.7 → enable Web Clipper service → enable MCP tools as needed; configure the agent’s MCP client to Joplin’s local endpoint — **or** skip for this course’s wiki track.
4. Do not point Hermes’ file tools at `database.sqlite` or the sync directory as if it were an LLM Wiki.

---

## Side-by-side

| | Obsidian | SilverBullet | Joplin |
|---|---|---|---|
| Live data | Folder of `.md` | Folder of `.md` | SQLite |
| Hermes / LLM Wiki files | Natural | Natural | Indirect (MCP/export) |
| Open source app | No | Yes (MIT) | Yes (AGPL) |
| Free sync with Nextcloud | Via plugin / folder | Via own server / folder sync | Native |
| Browser clipper | Official, strong (incl. iOS Safari) | Community clipper | Built-in web clipper (different model) |
| Phone | App + sync setup or paid Sync | PWA / server | Native apps + sync |
| Course role | **Default** | Interesting alternative | Not required for wiki; MCP elsewhere |

---

## Recommendation for this course / personal Hermes setup

1. **Class default:** **Obsidian** + Nextcloud (or similar) so **phone sync works without a per-student server.** How-to: [[howto-obsidian-setup-and-sync]].
2. **Hermes** (MIT) on the PC vault folder for the LLM Wiki / hybrid pattern.
3. **SilverBullet:** optional personal experiment if *you* run a Server; **not** the student path while phone sync is required and ops must stay light. How-to: [[howto-silverbullet-setup-and-sync]].
4. **Do not** pick Joplin only to learn MCP.

Hybrid wiki reminder (personal media-art + engineering): agent maintains technical wiki pages; you keep artistic/project voice pages human-authored — see [[../research/karpathy-llm-wiki-and-openclaw]].
