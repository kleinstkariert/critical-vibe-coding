# How to: SilverBullet setup and sync

Practical guide for **personal** SilverBullet / Hermes experiments on **Windows**, **macOS**, and **Linux**. Companion to [[howto-obsidian-setup-and-sync]] and [[knowledge-store-options]].

*requirement for the course:* **phone sync.** SilverBullet’s smooth phone path needs a **Server that stays up** — too heavy to require of every student. **Class default remains Obsidian + Nextcloud.** Use this how-to if *you* self-host; do not set it as the student baseline.

**Licensing (*verified fact*, 2026-10-15):**

| Piece | License / cost |
|-------|----------------|
| **SilverBullet Server** + `sb` CLI | **MIT** open source — free to run on your own hardware |
| **SilverBullet Desktop** | Free for **personal and education**; **Pro** ($50/user/year) required for **work** use; Pro also adds Meta Space / edge channel |

So: “open source” is accurate for the **server and the format (plain `.md` folder)**. Desktop is a native client with a personal/edu free tier, not the same as “the whole product is AGPL/MIT with no commercial tier.”

Related: [[../research/obsidian-vs-joplin-hermes-llmwiki]] · Hermes is also MIT — see below in [[knowledge-store-options]].

---

## 1. What you get

- A **space** = a normal folder of markdown (and attachments) on disk.
- Folders via `/` in page names (`Projects/Piece/Notes` → folders on disk).
- Hermes / Cursor can treat that folder like an Obsidian vault (filesystem tools).
- Phone: browser or **PWA** against a Server; Desktop can sync to that Server.

---

## 2. Two install paths (pick one starting point)

### Path A — Desktop only (fastest local edit)

1. Download Desktop for your OS: https://silverbullet.md/desktop/download  
   - **Windows:** 64-bit installer (if SmartScreen blocks: *More info* → *Run anyway* — documented on the download page)  
   - **macOS:** Desktop build from the same page (Apple Silicon / Intel as offered upstream)  
   - **Linux:** Desktop build if listed; otherwise prefer Path B (Server) or open the space folder with any markdown editor + Hermes
2. Open or create a **folder** as a space, e.g.:
   - Windows: `C:\Users\you\Nextcloud\...\silverbullet-space`
   - macOS / Linux: `~/Nextcloud/silverbullet-space` or `~/silverbullet-space`
3. You now have plain `.md` files. Point Hermes at that **absolute** folder path ([[howto-hermes-setup]]).

**Sync later:** connect this space to a Server (section 4) when you want the phone.

### Path B — Server (self-host) — best for computer + phone

Needs Docker (or the server binary). Natural on **Linux** (home NAS, VPS, Raspberry Pi) and fine on Mac/Windows with Docker Desktop. Phone reaches it via LAN, Tailscale/VPN, or hosted URL.

**Docker Compose** (recommended by upstream — same on Linux / Mac / Win + Docker):

```yaml
services:
  silverbullet:
    image: ghcr.io/silverbulletmd/silverbullet:latest
    restart: unless-stopped
    environment:
      # Single-space auth example — change these!
      SB_USER: "sebastian:CHANGE_ME"
    volumes:
      - ./data:/data
    ports:
      - "3000:3000"
```

```bash
docker compose up -d
```

Then open `http://localhost:3000` (or your host) and finish setup.

**Plain Docker:**

```bash
mkdir -p data
docker run -d --restart unless-stopped \
  --name silverbullet \
  -p 3000:3000 \
  -e SB_USER=sebastian:CHANGE_ME \
  -v ./data:/data \
  ghcr.io/silverbulletmd/silverbullet:latest
```

Docs: https://silverbullet.md/Install/Docker · https://silverbullet.md/server

**Linux without Docker:** use the upstream server binary / install docs if you prefer systemd over containers — still put auth in front of any non-localhost bind.

**Auth notes (*verified fact*):**

- Default modern installs use **multi-space accounts** (Dashboard).
- Classic **single-space**: `SB_USER=username:password`.
- With **no** credentials, a reachable server is open to anyone who can hit the URL — do not expose that to the public internet.
- Desktop Sync docs: do **not** put the server only behind a generic auth proxy yet (not supported the same way); use SilverBullet’s own auth.

---

## 3. Phone access

1. Run a Server you can reach (LAN URL, Tailscale, or hosted SB).
2. On the iPhone: Safari → open `https://your-server/` → log in.
3. Optional: *Add to Home Screen* → **PWA** (works offline; syncs when back online). Feature list: https://silverbullet.md/features · PWA: https://silverbullet.md/PWA
4. Or use Desktop on PC **and** browser/PWA on phone, with Desktop Sync to the same Server (section 4).

---

## 4. Sync options

| Method | What it does | Notes |
|--------|----------------|-------|
| **Desktop ↔ SilverBullet Server** | Official two-way sync | Space settings (gear) → Sync → Server URL + user/password or token. Docs: https://docs.silverbullet.md/Desktop%20Sync |
| **Hosted SilverBullet** | Someone else runs Server | Same sync idea; paid hosting possible |
| **Any file sync on the folder** | Nextcloud Desktop, Syncthing, Git, … | Space = plain files — works, but **don’t** combine with Desktop↔Server sync on the same files (two writers) |
| **Git** | Version history / backup | Officially encouraged; Desktop can open a repo folder as a space |

### Personal cloud (Nextcloud) — how it fits

SilverBullet does **not** need Remotely Save the way Obsidian does for phone.

*technical suggestion (Win / Mac / Linux + phone + Nextcloud):*

1. **Preferred open-source stack:** run **SilverBullet Server** (Docker on a machine you control — Linux NAS/VPS is ideal — or Docker Desktop on Mac/Win). Use Desktop on the computer synced to that Server; phone via browser/PWA. Nextcloud can still **back up** the `./data` folder — backup, not a second live editor sync.
2. **Without a Server:** put the space folder in Nextcloud and sync computer ↔ cloud with the Nextcloud client; phone access to raw files is then via Nextcloud Files / another editor — **not** as smooth as SB’s own PWA. For a real SilverBullet UI on the phone, you want a Server.
3. Never: Nextcloud Desktop live-sync **and** Desktop↔Server sync on the same folder at once.

---

## 5. Browser clipping / bookmarks

| Tool | Role |
|------|------|
| **SilverBullet Clipper** | Community extension (Chrome/Opera + Firefox): URL or selection → markdown in **Inbox**. Store: Chrome Web Store / Firefox Add-ons. |
| **Obsidian-level clipper** | Not matched yet (highlights, templates, Safari/iOS official clipper are Obsidian’s strength). |
| **Forks** | Community ports of Obsidian Web Clipper toward SilverBullet exist; treat as experimental. |

Simple bookmarking: yes. Heavy research clipping on iPhone Safari: Obsidian still ahead.

---

## 6. Folders and layout for Hermes

- Create hierarchy with `/` in names: `wiki/entities/Tool Name`, `raw/Article Title`.
- Upstream prefers a mostly **flat** space + tags; use folders for clear groups (`Inbox/`, `Journal/`, `Library/`, `wiki/`, `raw/`).
- Same hybrid idea as with Obsidian: agent-writable wiki folders vs human artistic project pages.

Point Hermes at the **absolute path** of the space folder on the machine where the agent runs (local Desktop space, or the Server’s `/data` volume if the agent runs on that host).

---

## 7. Checklist before Hermes uses the space

- [ ] Space is a real folder of `.md` files on the agent’s machine (or mounted there)
- [ ] Absolute path configured for the agent
- [ ] Only **one** live sync method for that folder
- [ ] Server has auth if reachable beyond localhost
- [ ] Clipper (optional) aimed at Inbox / `raw/`
- [ ] Personal vs work: Desktop free tier is OK for personal/edu; university **work** use may need Desktop Pro — check https://docs.silverbullet.md/Licensing

---

## 8. Common mistakes

1. Exposing Server with no `SB_USER` / accounts on the public internet.
2. Double-sync (Nextcloud Desktop + Desktop↔Server on the same files).
3. Expecting Obsidian-grade Safari clipper on day one.
4. Deep folder trees when tags would do (SB culture is flatter).
5. Agent on laptop while files only exist on a remote Server volume you never mount — sync or run the agent where the files are.

---

## Sources

- Homepage / open source: https://silverbullet.md/
- Desktop download & pricing: https://silverbullet.md/desktop/download · https://silverbullet.md/desktop
- Licensing: https://docs.silverbullet.md/Licensing
- Docker install: https://silverbullet.md/Install/Docker
- Server: https://silverbullet.md/server
- Desktop Sync: https://docs.silverbullet.md/Desktop%20Sync
- Authentication: https://docs.silverbullet.md/Authentication
- Folders: https://docs.silverbullet.md/Folder
- Best practices: https://docs.silverbullet.md/Guide/Best%20Practices
