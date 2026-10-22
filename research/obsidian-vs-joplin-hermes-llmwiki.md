# Obsidian vs Joplin for Hermes / LLM Wiki

Research: 2026-10-15 (cut short). Full detail lived here earlier; decisions moved to [[../course/knowledge-store-options]].

**Hermes** = Nous **Hermes Agent** (MIT, filesystem tools + Obsidian / `llm-wiki` skills) — not Hermes 4 chat models. **LLM Wiki** = Karpathy’s folder of markdown the agent maintains (`raw/` + wiki pages + schema); needs files on disk, not a DB.

| | Obsidian | Joplin |
|---|---|---|
| Store | Vault = `.md` folder (+ `.obsidian`) | Live store = **SQLite**; sync folder not for hand-edit |
| Hermes | File tools on vault path | MCP (3.7, app/API running) or export — no bundled skill |
| Sync | Sync paid; free via Nextcloud plugin / Syncthing / Git (more setup) | Free Nextcloud/WebDAV/Dropbox/…; that tree ≠ LLM Wiki |

***requirement:* phone sync.** Class path: **Obsidian + Nextcloud** (no per-student server). SilverBullet needs a Server for phone UI → not the class default. Not Joplin for folder wiki / MCP-only. See [[../course/knowledge-store-options]], [[../course/howto-obsidian-setup-and-sync]].
