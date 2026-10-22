# How to: Obsidian setup and sync

Practical guide for Critical Vibe Coding on **Windows**, **macOS**, and **Linux**.

*requirement:* **Phone sync is mandatory** (work on computer, read/capture on phone). Course decision: **Obsidian** as the class note app — sync via personal cloud (e.g. Nextcloud) **without** each student running a server. Joplin is not kept only to practice MCP.

Related: [[knowledge-store-options]] · [[what-is-mcp]] · [[../research/obsidian-vs-joplin-hermes-llmwiki]] · [[howto-hermes-setup]]

## 1. Install and open a vault

### All platforms

1. Download Obsidian for your OS: https://obsidian.md/download  
   - **Windows:** installer / portable  
   - **macOS:** `.dmg` → Applications (Apple Silicon and Intel builds from Obsidian)  
   - **Linux:** AppImage, Snap, Flatpak, or distro package — pick one and stick to it  
2. Also install the **mobile** app (iOS / Android) if you use a phone.
3. Create a **vault** = a normal folder of files on disk.
4. Prefer one clear place the phone can sync to, e.g.:
   - Teacher (Windows): `C:\Users\sebas\Nextcloud\KnowledgeBaseObsidian`
   - macOS: `/Users/you/Nextcloud/KnowledgeBaseObsidian` or iCloud only if **Mac ↔ iPhone** (see §2)
   - Linux: `~/Nextcloud/KnowledgeBaseObsidian` (or Syncthing folder)
   - Students: vault inside Nextcloud, Dropbox, etc.
5. Notes are `.md` files. Agents (Hermes, Cursor, …) can read/write this folder with filesystem tools — Obsidian does not need to be open for that.

**Tip:** Keep a separate vault (or top-level folder) for an LLM Wiki so course/research agent edits do not mix with diary notes.

## 2. Sync options (overview)

| Method | Cost | Phone | Best for |
|--------|------|--------|----------|
| **Obsidian Sync** | Paid (official) | Excellent | Least hassle on any OS |
| **Personal cloud (Nextcloud / WebDAV)** via plugin | Free if you have the cloud | Works (plugin on mobile) | Win / Mac / Linux + phone + existing Nextcloud |
| **Nextcloud Desktop client** (folder sync) | Free if you have Nextcloud | Awkward on iPhone alone | Desktop ↔ desktop |
| **Syncthing** | Free | Android easier than iOS | Linux/Android peer-to-peer |
| **Git** | Free | Not native in Obsidian on iPhone | Desktop, history |
| **iCloud** | Free with Apple | Great **Mac ↔ iPhone** | Avoid as the bridge from **Windows** or **Linux** |

**Rule:** never sync the same vault with two methods at once (e.g. Nextcloud Desktop *and* Remotely Save *and* Obsidian Sync).

### Platform picks (*technical suggestion*)

| Your computer | Phone | Prefer |
|---|---|---|
| Windows | iPhone / Android | Remotely Save → Nextcloud WebDAV (below) |
| macOS | iPhone | Obsidian Sync, **or** iCloud vault folder, **or** Remotely Save → Nextcloud |
| macOS | Android | Remotely Save → Nextcloud (not iCloud) |
| Linux | Android | Syncthing **or** Remotely Save → Nextcloud |
| Linux | iPhone | Remotely Save → Nextcloud (Syncthing on iOS is weak) |

## 3. Recommended free path: personal cloud (Nextcloud) + Remotely Save

Fits: **Windows / macOS / Linux + phone**, university or personal Nextcloud.

### A. On Nextcloud (once)

1. In the Nextcloud web UI or Files app, create a dedicated folder, e.g. `Obsidian/MyVault` (or one folder per vault).
2. If 2FA is on, create an **app password** for sync (do not put your main password in plugins if you can avoid it).
3. Note your **WebDAV URL**. Typical form (check your server’s docs):
   - `https://YOUR-NEXTCLOUD/remote.php/dav/files/USERNAME/Obsidian/MyVault`
   - Or the parent folder if the plugin creates a subfolder named after the vault — Remotely Save often syncs into a `${vaultName}` subfolder; keep the **vault name identical** on every device.

### B. On the computer (Obsidian desktop — Win / Mac / Linux)

1. Create or open the vault as a **local folder** (can live outside Nextcloud Desktop sync to avoid double sync — see warning below).
2. Settings → Community plugins → Turn on community plugins → Browse → install **Remotely Save**.
3. Enable the plugin → open its settings → choose **WebDAV**.
4. Enter server URL, username, app password.
5. Run a first sync. Confirm files appear in Nextcloud.
6. Optional: schedule auto-sync; exclude or think carefully about `.obsidian` (settings/plugins). Many people sync `.obsidian` so plugins match; others keep settings per device to avoid plugin conflicts.

**Conflict mode (free):** Remotely Save’s free tier keeps the **newer** file when both sides changed. Do not edit the same note offline on phone and computer at once if you care about both versions.

### C. On the phone (iPhone / Android)

1. Install Obsidian from the App Store or Play Store.
2. Create or open a vault with the **same name** as on the computer (important for Remotely Save defaults).
3. Install and enable **Remotely Save** (community plugins work on mobile).
4. Enter the same WebDAV settings → sync.

### D. macOS + iPhone via iCloud (Apple-only shortcut)

*technical suggestion:* Put the vault folder in iCloud Drive and open it from Obsidian on Mac and iOS. Simple when **every** endpoint is Apple. Do **not** mix with Windows/Linux on the same vault. Obsidian documents iCloud edge cases — if you see duplicated folders, stop and switch to Remotely Save or Obsidian Sync.

### E. Nextcloud Desktop client instead of (or with?) the plugin

*technical suggestion:*

- **Either** put the vault inside a Nextcloud-synced folder and let the **desktop client** sync computer ↔ cloud (simple on desktop; on phone you still need Obsidian + usually a plugin).
- **Or** use **Remotely Save → WebDAV** on each Obsidian install and **do not** also sync that folder with Nextcloud Desktop (one writer to the sync target).

**Remotely Save on both ends → Nextcloud WebDAV** remains the clearer multi-OS student recipe.

## 4. Other free options (short)

### Syncthing
- Install Syncthing on the computer (common on **Linux**); on Android use a maintained client. iOS support is limited compared with Android.
- Exclude or carefully sync `.obsidian` (conflict files inside settings are a known pain).

### Git
- Desktop (all OS): vault as a git repo; commit/push (GitHub private repo, etc.).
- iPhone: not built into Obsidian — typically **Working Copy** then open that folder in Obsidian. Awkward as a class default.

### Obsidian Sync (paid)
- Settings → Sync → sign in. Easiest phone experience across OS. Student discount exists on Obsidian’s pricing page (check current %).

## 5. Checklist before an agent (Hermes / Cursor) uses the vault

- [ ] Vault path is a real folder of `.md` files on the machine where the agent runs
- [ ] Agent config points at that path with an **OS-correct absolute path** (see [[howto-hermes-setup]])
- [ ] Sync is settled so phone and computer do not fight (one sync method)
- [ ] LLM Wiki layout (if used): `raw/`, schema, `index.md`, agent-writable folders — see research notes
- [ ] Secrets (API keys) not stored in synced notes
- [ ] Linux: if using Flatpak Obsidian, confirm the agent sees the **same** folder path Flatpak can write (sandbox permissions)

## 6. Common mistakes

1. Two sync systems on one vault.
2. Editing the same note offline on two devices (free sync = keep newest → silent loss).
3. Expecting Git on iPhone to work like the desktop Git plugin.
4. Using iCloud as the bridge from **Windows** or **Linux** to iPhone.
5. Pointing the agent at a cloud-only / not-downloaded folder (OneDrive / iCloud “online only” files look missing).
6. Mixing path styles (`C:\...` vs `/mnt/c/...` in WSL) between Hermes and Obsidian.

## Sources

- Obsidian sync help: https://obsidian.md/help/sync-notes
- Obsidian Sync product: https://obsidian.md/sync
- Remotely Save: https://github.com/remotely-save/remotely-save · https://remotelysave.com/
- Nextcloud WebDAV: https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html
