# Obsidian vs Joplin for Hermes and an LLM Wiki

Research date: 2026-10-15. Claims are labeled *requirement*, *verified fact*, *technical suggestion*, or *anecdote*. Prices and product behavior are taken from pages fetched on this date. A claim that could not be checked is marked unverified, with what was checked.

## Question

*requirement*: Students in the Interface Cultures seminar Critical Vibe Coding need a free tool with which they can practice setting up an agent-readable information structure. The note store under consideration is either Obsidian or Joplin, used with a Hermes agent in an LLM Wiki approach. Joplin stays in the comparison because that free-tool requirement is why it is on the table.

The owner’s working table, treated here as a hypothesis:

| Capability | Obsidian + Hermes | Joplin + Hermes |
|---|---|---|
| Data engine | Native plain-text .md files | Internal SQLite database |
| Hermes integration | Native filesystem tools (instantaneous) | Requires an MCP server or file exporter |
| Cloud sync cost | Paid (Obsidian Sync) or tricky third-party workarounds | Free and native (Dropbox, OneDrive, WebDAV) |

This note records where those rows match current docs, where they do not, and what a student exercise would actually have to set up. It does not select a tool.

## What Hermes refers to

*verified fact*: The capability table matches **Hermes Agent**, the MIT-licensed agent from Nous Research (`NousResearch/hermes-agent`, copyright 2025, homepage `https://hermes-agent.nousresearch.com`). It ships filesystem tools (`read_file`, `write_file`, `patch`, `search_files`) and a bundled Obsidian skill that tells the agent to use those tools on a vault path. It also ships a bundled `llm-wiki` skill, related to the Obsidian skill, that maintains a directory of markdown files and says that directory can be opened as an Obsidian vault.

*verified fact*: A second Nous product is in circulation under the same name: the **Hermes model family**. The Hermes 4 technical report (Nous Research, PDF dated in the August 2025 path) describes hybrid-reasoning chat models. The Hugging Face card for `NousResearch/Hermes-4-405B` compares Hermes 4 with Hermes 3. The Hermes Agent Nous Portal docs list `Hermes-4-70B` and `Hermes-4-405B` and state that these models are not recommended inside Hermes Agent, because they are tuned for chat and reasoning rather than the agent’s tool-calling loop. The Portal text says to use them for research workflows or from other tooling, and to pick a frontier agentic model for agent work.

*verified fact*: Searches of the Hermes Agent docs and GitHub tree, and of 2025–2026 writeups, found Obsidian and LLM Wiki material aimed at Hermes Agent. They did not find a bundled Joplin skill or a published Hermes Agent + Joplin pairing. Third-party writeups that do pair Hermes Agent with Obsidian include the agent’s own skill docs, a Dexio guide that restates those docs, and a WikiHub tutorial that describes Hermes Agent maintaining an Obsidian-compatible LLM Wiki. `hermes-agent.ai` restates the filesystem Obsidian setup; the Nous docs host above is the primary source used here.

*technical suggestion*: In this seminar the table’s “Hermes” is the agent, not the Hermes 4 weights. Using a Hermes 4 checkpoint as the agent’s model would be a separate, and officially discouraged, choice.

## What LLM Wiki refers to

*verified fact*: Andrej Karpathy published the pattern as a GitHub gist, `llm-wiki.md`, dated 4 April 2026 (`https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`). He describes it as an idea file to paste to an agent (he names Codex, Claude Code, OpenCode / Pi, and “etc.”), not as a product. The core contrast with RAG is that the model incrementally maintains a persistent wiki of markdown files instead of re-deriving an answer from raw chunks on every query.

The gist defines three layers:

1. **Raw sources** — immutable documents the model reads and does not modify.
2. **The wiki** — “a directory of LLM-generated markdown files” that the model owns: summaries, entity pages, concept pages, comparisons.
3. **The schema** — a configuration document (his examples are `CLAUDE.md` or `AGENTS.md`) that states structure, conventions, and the ingest / query / lint workflows.

Two navigation files sit beside those layers: `index.md` (a catalog the model reads before answering) and `log.md` (an append-only action log). He writes that at moderate scale, on the order of 100 sources and hundreds of pages, the index can replace an embedding index. He also writes: “In practice, I have the LLM agent open on one side and Obsidian open on the other. … Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.” Graph view, Dataview, and the Obsidian Web Clipper are listed as optional. He says the wiki “is just a git repo of markdown files.”

*verified fact*: Hermes Agent’s bundled `llm-wiki` skill (docs page version 2.1.0) says it is based on that pattern. Its default path is `WIKI_PATH`, or `~/wiki` if unset. The layout it specifies is a directory: `SCHEMA.md`, `index.md`, `log.md`, `raw/` (immutable), and agent-owned folders `entities/`, `concepts/`, `comparisons/`, `queries/`. Each session is instructed to read the schema, the index, and the last 20–30 log lines before ingest, query, or lint. Operations are file-tool calls (`read_file`, `search_files`) plus small Python for lint. The skill states: “The wiki is just a directory of markdown files — open it in Obsidian, VS Code, or any editor. No database, no special tooling required.” If the Obsidian skill is used as well, `OBSIDIAN_VAULT_PATH` is set to the same directory.

*verified fact*: The pattern, in both the gist and the Hermes skill, depends on the agent being able to open, search, create, and patch files in a folder. Wikilinks (`[[page]]`), YAML frontmatter, and a filesystem index are part of the schema the Hermes skill writes. A database that stores note bodies in a column can hold the same sentences, but it is not the artifact those two documents tell the agent to maintain. An export folder can become that artifact after a conversion step. A live SQLite file is not that artifact.

*technical suggestion*: “Agent-readable information structure,” for this pattern, means a folder the agent can list and edit, plus a schema file the agent reads before it writes. Notebooks, tags, and a running API are a different structure. They can still be practiced. They are not what the Karpathy gist or the Hermes `llm-wiki` skill describe.

## Capability check

### Data engine

**Owner row:** Obsidian = native plain-text `.md` files. Joplin = internal SQLite database.

*verified fact*: Obsidian’s help page “Sync your notes across devices” says the data “is simply stored as files in a folder called a vault.” “How Obsidian stores data” says a vault is a folder on the local file system, that Obsidian creates an `.obsidian` configuration folder in the vault root (hotkeys, themes, community plugins), and that notes remain files that can be moved with ordinary file tools, Git included. The same page says IndexedDB is a local database used for the state of Obsidian Sync connections and for the metadata cache after the app closes. The excerpt fetched for this note breaks off at “If Apple's”; the rest of that warning was not captured. Note bodies are files. The app also keeps a hidden config folder and a cache database.

*verified fact*: Joplin’s user-profile spec says the desktop, mobile, and CLI apps share a profile. Default locations are `~/.config/joplin-desktop` (Linux, macOS) and `%UserProfile%\.config\joplin-desktop` (Windows). `database.sqlite` is “the central SQLite database file where all notes, notebooks, tags, and metadata are stored.” Attachments live as hash-named files in `resources/`. The database schema describes the note `body` as “The note body, in Markdown. May also contain HTML.” A later migration adds `markup_language` with the comment `1: Markdown, 2: HTML`. “Markdown” here is the text stored in a column, not a `.md` file per note.

*verified fact*: Joplin’s FAQ, “Is it possible to use real file and folder names in the sync target?”, says the sync format is open and “does not mean the sync files are meant to be user-editable,” and: “Joplin sync directory is basically just a database.” The official external-editor FAQ documents a “Text editor command” that opens a note in an editor such as VS Code or Notepad and waits for it to close. That is an app-mediated edit. It is not a vault of durable note files.

*anecdote*: On the Joplin forum thread “Where are my notes' .md files?” a reply states: “The database contains all your notes. The MD files are used only for synchronisation purposes. … you're not supposed to edit them outside of Joplin.” Another reply on “Editing Joplin .md files directly does not update app contents” says not to edit the sync target, and that the external-editor button is the supported route because Joplin exports a file and watches it. Those are forum replies, not the profile spec.

*verified fact*: Joplin’s import/export help says a JEX file is a lossless export (notes plus metadata such as geolocation, timestamps, and tags can be re-imported). A “raw” export is the same data as a directory of one file per item. Plain Markdown files and directories can be imported. The CLI `export` formats documented in the terminal readme include `jex`, `raw`, `md`, and `md_frontmatter`. Joplin 3.7’s release note adds import of an Obsidian vault on desktop and CLI.

*anecdote*: A Joplin forum post, “Export Summary: what each option does” (thread 48564), describes MD export as recreating notebook folders and note titles while dropping object metadata, and RAW export as id-named files whose hierarchy is in properties. That is a community write-up of the official formats, not the manual itself.

**Table check:** The storage row matches the docs for the live note store. Two qualifications belong next to it. Obsidian’s notes are plain files, and the vault also contains `.obsidian` plus an IndexedDB cache. Joplin’s note text is Markdown (or HTML) inside SQLite; Markdown files appear as export, as an external-editor handoff, or as the non-editable sync directory. Pointing a filesystem agent at `database.sqlite` or at the sync folder does not give it the LLM Wiki layout.

### Agent integration

**Owner row:** Obsidian + Hermes = native filesystem tools, “instantaneous.” Joplin + Hermes = an MCP server or a file exporter.

*verified fact*: The bundled Obsidian skill (docs version 1.0.0, platforms linux, macos, windows) says to resolve `OBSIDIAN_VAULT_PATH` from `${HERMES_HOME:-~/.hermes}/.env`, or else use `~/Documents/Obsidian Vault`, and then call file tools with a concrete absolute path. It says file tools do not expand `$OBSIDIAN_VAULT_PATH`. A secondary integration page on the same docs host says that when the file tools run on the same machine as the vault, Obsidian does not need to be running, and that a laptop vault is not visible to a VPS, Docker container, or other remote runtime unless that runtime has its own mounted or synced copy. A May 2026 pull request in `NousResearch/hermes-agent` (#19332) changed the skill text from shell commands toward those file tools. The word “instantaneous” does not appear in the skill.

*verified fact*: The `llm-wiki` skill tells a headless machine to install `obsidian-headless` and log into an Obsidian account “with Sync subscription,” then run `ob sync --continuous`. It says changes then “appear within seconds.” Obsidian’s own help page “Obsidian Headless” (open beta, Node.js 22+, package `obsidian-headless`) describes that CLI as a headless client for Obsidian Sync and Publish, and lists “give agentic tools access to a vault without access to your full computer” as a reason to use it. That path is paid Sync plus a beta CLI. It is not the local file-tool path.

*verified fact*: Hermes Agent has a built-in MCP client (stdio and HTTP) that registers remote tools next to `read_file` and `terminal`. No Joplin entry showed up in the Hermes Agent skill or integration pages checked for this note.

*verified fact*: Joplin 3.7 adds a built-in MCP server. Laurent Cozic’s forum post “What's new in Joplin 3.7” (31 August 2026) says external tools can read and write notes through it. The `dev` branch file `readme/apps/ai_mcp.md` says the server is off by default, runs on the Web Clipper port (normally 41184), listens only on `127.0.0.1`, and requires the Web Clipper service to be started. Each tool (search, read, create, update, trash, tags, notebooks) is individually off until enabled. Joplin does not ask for confirmation on writes. The desktop app has to be running. The changelog entry “New: Add MCP server” is in the 3.7.3 pre-release (published 2026-06-23). Forum replies say the 3.7 desktop line became a full release in the first week of September 2026 (one reply on 6 September 2026: “It's released for Desktop now”). GitHub releases showed `v3.7.21` on 2026-09-25. A later tag was not checked past the releases page snippet retrieved on 2026-10-15.

*verified fact*: The older Joplin Data API remains documented: REST on the clipper port, token from the Web Clipper screen, JSON in and out, note body as Markdown or HTML. Third-party MCP servers wrap that API. `alondmnt/joplin-mcp` (MIT, created 2025-07-06) is one of them; its changelog records releases through v0.9.0 on 2026-06-10. A registry page claimed a later commit on 2026-09-12; that commit was not re-checked on GitHub. The Joplin forum also has, in 2025–2026, posts for other servers (read-only and read-write variants, a script-execution server posted by a user as `belsar-ai`, and a standalone server that talks to a Joplin sync server rather than a local app). Upstream’s own MCP server is the one maintained in the Joplin repo. The others are community projects with uneven update dates.

*verified fact*: The Joplin CLI can `export` and `import` and can run `joplin sync` from cron. An export is a snapshot. The Hermes `llm-wiki` skill does not document a Joplin export loop.

**Table check:** “Native filesystem tools” matches Hermes Agent’s Obsidian skill for a vault on the same machine. “Instantaneous” is not a documented property. Local reads and writes are ordinary file-tool calls after a path is resolved; a remote Hermes process does not see the vault until something mounts or syncs it; the skill’s “within seconds” sentence is about paid Obsidian Sync, and it was not measured here.

“Requires an MCP server or file exporter” is still the right shape, with a 2026 change of who provides the MCP server. Joplin’s live notes are not files the Hermes file tools can edit in place. As of Joplin 3.7 the MCP server can be Joplin itself, on localhost, with the desktop app open. A third-party MCP server, the Data API, or a Markdown/JEX export remain the other documented routes. Hermes can attach an HTTP MCP server in general. An end-to-end Hermes Agent session against Joplin’s `/mcp?token=` URL was not found in the sources checked and was not run for this note. That pairing is unverified.

*technical suggestion* (pros / cons, not a choice):

- Obsidian path: one folder, the agent’s existing file tools, no note app required while the agent writes. The cons are path setup (`OBSIDIAN_VAULT_PATH` must be a real absolute path), no access from a remote agent until the folder is mounted or synced, and a paid Sync subscription if the link between machines is Obsidian Headless.
- Joplin path: the app already speaks MCP, so a student can practice an agent boundary without adopting Obsidian’s file layout. The cons are a running desktop app, a token, tools that default to off, no bundled Hermes skill, and a schema (`SCHEMA.md`, `index.md`, wikilinks on disk) that the Joplin MCP does not implement by itself.

### Wikilinks and the schema

*verified fact*: Joplin’s Markdown help documents internal links as `[label](:/noteId)`, created with “Copy Markdown link,” not as `[[wikilinks]]`. A community plugin, `joplin.plugin.alondmnt.wikilinks` version 0.4.1 (plugin page last updated 2026-02-25, minimum Joplin 3.5), adds `[[wikilinks]]` in the editor and preview. The feature request thread was still open as a request in March 2025; the plugin author replied on that thread in February 2026.

*verified fact*: Obsidian’s linking model, including `[[wikilinks]]` and graph view, is what both Karpathy’s gist and the Hermes skill assume. The Hermes skill also names the Dataview community plugin as optional.

*technical suggestion*: A Joplin exercise can store a schema as a note and ask an agent to keep related notes consistent through MCP. Rendering `[[wikilinks]]` and a graph still depends on Obsidian, or on that third-party Joplin plugin. Those are different exercises.

## Sync and cost

### The applications

*verified fact*: Obsidian’s license overview says the app is free for personal, commercial, nonprofit, educational, and government use. The pricing page says “Free without limits” and “No sign-up required.” A commercial license is optional ($50 USD per user per year on the pricing page) and the help page says applying it does not add features. The terms grant a limited license to install and run the software; the company retains the software rights. The app is free to use and closed-source.

*verified fact*: Joplin’s December 2022 license note says the desktop, mobile, CLI, and web clipper apps are AGPL-3.0 and remain free to use. No Joplin account is required for a local profile. Joplin Cloud and Joplin Server Business are separate paid products.

*verified fact*: Hermes Agent is MIT-licensed software. The model it calls is not included. Portal docs list many hosted models and say Hermes 4 weights are a poor fit for the tool loop. What a student would pay for an API key, a Portal subscription, or a local model was not priced in this pass. That cost is unverified.

### Obsidian sync

*verified fact*: On 2026-10-15 the English pricing page lists Sync at **$4 USD per user per month, billed annually**, with end-to-end encryption, version history, shared vaults, and priority support. Students, faculty, and nonprofit employees are offered a **40% discount** on Sync and Publish. Refunds for Sync and Publish are full within 7 days. The English Sync product page lists **Sync Standard** as 1 vault, 1 GB, 5 MB maximum file size, and 1 month of version history, and it still has a **Sync Plus** section. The Japanese Sync page lists Standard at $4 USD and Plus at $8 USD. A 20 March 2024 blog post states Standard at $4 per month billed annually or $5 billed monthly, and Plus at $8 per month billed annually, with Plus at 10 vaults, 200 MB files, 10 GB (expandable to 100 GB for $16 per month billed annually), and 12 months of history. The help page “Plans and storage limits” still describes those Standard and Plus limits (Plus storage “10 GB to 100 GB”). The English pricing card fetched on this date shows the $4 annual figure and does not repeat the Plus dollar amount. The $8 Plus figure is taken from the Japanese product page and the 2024 post, not from a fresh English price table.

*verified fact*: Obsidian’s help page “Sync your notes across devices” documents methods the community uses, besides first-party Sync:

- **iCloud**, recommended for macOS and iOS, with the vault inside `iCloud Drive/Obsidian/`. iCloud Drive on Windows “may lead to file duplication or corruption.” Files should stay downloaded (“Keep Downloaded” / avoid Optimize Mac Storage).
- **OneDrive**, for Windows and macOS, with limited Android behavior and no official iOS support. The vault must be “Always keep on this device.” Files On-Demand is called out as a way for Obsidian to treat offloaded files as missing.
- **Google Drive**, for Windows, macOS, and Android, “not officially supported,” and not officially supported on iOS.
- **Syncthing**, for Windows, macOS, and Linux. The official Android Syncthing app is described as unmaintained, with Syncthing-Fork as the community continuation. The page says to exclude `.obsidian` if each device should keep its own settings, and that sync works best when one device stays on.
- **Git**, for Windows, macOS, and Linux, manual push and pull. **Working Copy** on iOS is described as a community Git client; some of its features need a paid in-app purchase.

The same page says Dropbox, Google Drive, OneDrive, and Syncthing are not officially supported on iOS. It says not to sync one vault through two services at once. The Sync setup page names iCloud, OneDrive, Dropbox, “or other syncing folder” as something to move out of before turning on Obsidian Sync. Dropbox is therefore an acknowledged file-sync case, and it is not in the main recommended list on the sync-notes page. Nextcloud and WebDAV are not named on that official sync-notes page.

*verified fact*: Community plugins exist that sync a vault to Nextcloud (`nextcloud-sync`, `nextsync` in the community plugin directory). They are not Obsidian Sync. The Nextcloud user manual’s recommended computer sync is the Nextcloud desktop client, which can keep a local folder. Because an Obsidian vault is a folder, that client can sync the folder. That arrangement was not tested here.

*anecdote*: Obsidian Forum thread “How do you sync your vaults?” includes a report of Syncthing conflict files inside `.obsidian`, named like `workspace.sync-conflict-20210811-000000-0AAAA0A`. A 2021 staff reply on “Help! disappearing files…” says using two sync providers on the same files can cause race conditions, corruption, or duplication. A 27 November 2025 feature request reports that Sync Standard’s 5 MB file cap skipped part of a community plugin (`main.js` “just north of 6mb”) and left a broken plugin install while `data.json` still synced.

**Table check:** “Paid (Obsidian Sync)” matches the first-party service. “Tricky third-party workarounds” is stronger than the current help page, which documents iCloud, OneDrive, Google Drive, Syncthing, and Git as normal methods and then lists the failure modes (offloaded files, mixed sync services, iOS gaps, manual Git, `.obsidian` conflicts). They are free of an Obsidian fee when the storage account is free. They are not feature-equivalent to Obsidian Sync, and several are officially unsupported on a phone. Nextcloud is possible because the vault is a folder, or through community plugins. It is not a built-in Obsidian sync target.

### Joplin sync

*verified fact*: Joplin’s synchronisation help says targets are **Joplin Cloud, Nextcloud, S3, WebDAV, Dropbox, OneDrive, or the local filesystem**, with no hard dependency on one vendor. Background sync runs while the desktop app is running; the CLI can `joplin sync` from cron. The Nextcloud instructions say to create a dedicated `Joplin` directory, paste the full WebDAV URL ending in that directory, and then disable the Nextcloud desktop client’s sync for that directory so only Joplin writes it. The FAQ says a WebDAV URL change onto an empty folder makes Joplin treat the notes as deleted locally. Nextcloud 2FA needs an app password. Known non-working WebDAV hosts listed in the FAQ include Jianguoyun and pCloud. Mobile “does not have a background sync”: sync stops when the app is closed, backgrounded, or the screen sleeps.

*verified fact*: Joplin Cloud is optional and paid. The plans page (fetched 2026-10-15) shows a Basic block at **2.99€ / month** and **2.40€ / month (28.69€ / year)** next to **10 MB** per note or attachment and **2 GB** storage. The comparison table lists Pro at 200 MB and 30 GB, Pro 100 GB at 100 GB, and Teams at 50 GB. The Pro monthly euro amount did not come through cleanly in the page text retrieved here. That number is unverified. Education discount: 50% for students and teachers, requested from a university or school email, valid for one year and renewable. The vendor states that Joplin Cloud data is in France and that the service is carbon neutral via a partnership with carbone.eco. Those two sentences are vendor statements; they were not independently checked.

*verified fact*: Dropbox, OneDrive, WebDAV, Nextcloud, filesystem, and S3 sync do not require a Joplin Cloud subscription. Whether the storage account itself is free depends on that provider. A Joplin sync directory on Nextcloud is Joplin’s sync database, not a folder of notes an agent should edit. The FAQ forbids treating it as user-editable files.

**Table check:** “Free and native” matches Dropbox, OneDrive, and WebDAV as first-party Joplin targets, and it should also name Nextcloud, S3, and the local filesystem. “Free” means Joplin does not charge for those drivers. Joplin Cloud is a paid native target sitting beside them. The files those drivers store are the wrong surface for an LLM Wiki agent.

### Nextcloud, because this workspace already uses it

*requirement*: The owner already uses Nextcloud. That is relevant to sync choice. It does not decide the note app.

*technical suggestion*:

- Joplin has a documented Nextcloud/WebDAV target. A student with an account can sync without Joplin Cloud. The agent still cannot treat the Nextcloud Joplin folder as the wiki. The agent path remains MCP or an export. Setup costs that are easy to miss: a dedicated folder, an app password if 2FA is on, and the Nextcloud desktop client must not also sync that folder. An empty new URL can delete the local notes.
- Obsidian has no equivalent official target. A vault folder inside a Nextcloud-synced directory is ordinary file sync, with the same class of conflicts the Obsidian help already describes for other file sync (two writers, offloaded files, `.obsidian`). Community WebDAV plugins are a second route and are third-party code. Neither was tested against this owner’s Nextcloud.

## User experiences

Official docs and forum reports are separated. Quotes are short and from the pages fetched. They are single reports, not rates.

### Agent or LLM use

*verified fact (official)*: Hermes Agent’s Obsidian and `llm-wiki` skills are the maintained implementation of “agent edits markdown, human reads it in Obsidian.” Joplin’s 3.7 MCP document is the maintained implementation of “agent calls tools, Joplin answers from the database,” with an explicit warning that the connected model may send note text to that model’s own provider, independent of Joplin’s chat settings.

*anecdote*: The Joplin thread “AI agents and Joplin” (opened around the `alondmnt/joplin-mcp` release) describes search, tagging, and note creation through MCP, including a small local model. A later post contrasts typed MCP tools with a script-execution server that smaller models handled poorly. “100% standalone Joplin MCP server” describes a homelab setup where the local built-in MCP is the fit when the Joplin app stays running, and a server-side MCP is the fit when clients only sync to a central Joplin server. A 6 September 2026 reply on the 3.7 announcement reports AI provider errors (`empty response`, `AI provider returned 400`) during chat setup. That report is about Joplin’s own chat provider, not about the MCP toggle.

No Hermes-specific Joplin field report was found in the searches above.

### Sync reliability

*verified fact (official)*: Obsidian Sync’s troubleshooting page says conflict copies are separate files, that some conflicts (daily notes, Templater) can drop a local version, and that plugin and settings changes often need a restart, including a force-quit on mobile. Joplin’s 3.7 note says bulk deletes on Joplin Server and Joplin Cloud are faster and that typing during an incoming update is less likely to be overwritten. Joplin’s FAQ still says mobile sync does not run in the background.

*anecdote*: See the Syncthing `.obsidian` conflict filenames, the two-provider warning, and the 5 MB plugin-file report in the sync section. A Joplin forum thread “Never-ending sync” (March 2025, Dropbox, Joplin 3.2.13) includes the log line `SQLITE_CORRUPT: database disk image is malformed` and a reply to make a new profile and sync again, using a JEX export for notes that existed only locally.

### SQLite lock and corruption

*verified fact (official)*: Joplin’s architecture spec says every client uses a local SQLite database. The profile spec includes a `lock` file so only one instance uses the profile.

*anecdote*: GitHub issue 11686 (unexpected shutdown, maintainer reply 2025-01-20): “That cannot be recovered from, so you'll need to recover from backup.” GitHub issue 2129 (2019) has the same class of `SQLITE_CORRUPT` report and a maintainer comment that corruption can come from causes outside the app, such as a failing disk, and that the remedy is a backup. GitHub issue 10802 (2024, `SQLITE_BUSY: database is locked`) was closed after the reporter wrote that turning some plugins off made the lock stop. These are incident reports. They do not establish how often the database fails.

Obsidian’s note store is not SQLite. Its IndexedDB cache is a separate local database; this pass did not collect corruption reports for it.

### Markdown round-trip

*verified fact (official)*: Joplin documents lossless JEX/raw and also Markdown import and export. Obsidian’s note files are the Markdown. Renaming a note inside Obsidian updates links; a file renamed only on disk is a different situation the help page’s link rules are about, and that case was not re-tested here.

*anecdote*: The export-summary forum post treats Markdown export as lossy for metadata (timestamps, ids, tags) and JEX/raw as the backup form. The “Where are my notes” thread treats sync-folder Markdown as unsafe to edit. Both match the official split between an editable store and an export, in user language.

### Plugins and mobile

*anecdote / official mix*: Obsidian help says community plugin settings generally need an app restart after sync, and the November 2025 forum report above is about a plugin binary larger than the Standard file cap. Joplin’s 3.7 note says startup no longer processes every plugin file, which is an official performance change, not a fragility finding. The `SQLITE_BUSY` plugin report is one incident.

*verified fact (official)*: On iOS, Obsidian’s supported sync methods on the help page are Obsidian Sync and iCloud, with the vault in a specific iCloud folder. The configuration-folder help says there is no built-in way to see `.obsidian` on iOS or iPadOS. Joplin’s mobile FAQ says sync stops when the app is not in the foreground. Joplin iOS notes are not included in an iOS backup to a Mac, according to that FAQ.

## Teaching fit

*requirement*: The exercise is to practice an agent-readable information structure with a free tool. Both apps can be installed without paying. The structure the Hermes `llm-wiki` skill already knows is a folder. Joplin remains available for students who should practice a database plus an explicit agent interface.

What a student has to set up:

| Step | Obsidian | Joplin |
|---|---|---|
| Install cost of the note app | Free, no account (*verified fact*) | Free, no account for local use (*verified fact*) |
| Account | None until Sync or Publish (*verified fact*) | None until Joplin Cloud (*verified fact*) |
| Where the notes are | A vault folder of `.md` files, plus `.obsidian` (*verified fact*) | `database.sqlite` plus `resources/` (*verified fact*) |
| What Hermes Agent can see with its built-in skills | The folder, after `OBSIDIAN_VAULT_PATH` / `WIKI_PATH` (*verified fact*) | Nothing from the bundled skills. Unverified until an MCP server or an export is added |
| Extra process that must stay running | Not the Obsidian app, if the agent is local (*verified fact*). A remote agent needs a mount or a sync client | The Joplin desktop app, Web Clipper, and MCP toggle, for the built-in server (*verified fact*) |
| Sync a student can use without paying Obsidian or Joplin | iCloud, OneDrive, Google Drive, Syncthing, Git, or a Nextcloud folder, with the documented constraints (*verified fact* plus *technical suggestion* for Nextcloud) | Dropbox, OneDrive, WebDAV, Nextcloud, S3, or filesystem (*verified fact*). The synced tree is not the wiki |
| Phone | Officially Sync or iCloud (*verified fact*) | First-party apps; sync only while the app is open (*verified fact*) |

*technical suggestion* (pros / cons):

- **Obsidian exercise.** Pros: it is the layout Karpathy wrote down and the layout Hermes already loads; the agent and the human can look at the same files; leaving the app leaves the Markdown behind; Git is a documented sync and history method. Cons: the application is closed-source; graph view and wikilink resolution are features of that app; community plugins are a separate trust and sync surface; a remote or phone copy needs a sync method that is either paid or constrained; Nextcloud is do-it-yourself.
- **Joplin exercise.** Pros: the app is AGPL; Nextcloud/WebDAV sync is a documented target for people who already have Nextcloud; the 3.7 MCP server is a concrete “agent may read and write” switch with per-tool permissions and a localhost-only default; students meet a real boundary between a database and an agent. Cons: the Hermes wiki skill does not speak that boundary; wikilinks are a plugin; an export is a copy, and Markdown export drops metadata that JEX keeps; the sync folder must not be used as the wiki; the desktop app has to be running for the built-in MCP; mobile sync pauses in the background.

*verified fact* (local vs remote, from the products themselves): Both apps keep the working copy on the device. Obsidian’s pricing FAQ says the company cannot read Obsidian Sync data because it is AES-256 end-to-end encrypted. Joplin can sync to a server the student or the university runs (Nextcloud, WebDAV, S3, filesystem, or Joplin Server) or to Joplin Cloud, whose operator says the data sits in France. Hermes Agent’s own docs describe running the agent on a VPS or a container. In that setup the note files are readable only if they are on that machine. A local agent reading a local vault does not require that hop. Joplin’s MCP server refuses non-localhost connections, so a remote Hermes process cannot attach to it without a tunnel the Joplin doc does not provide.

*verified fact* (vendor ecology claim, not checked further): Joplin Cloud’s plans page says the hosted service is carbon neutral and cites a reforestation partnership. No equivalent carbon claim was fetched for Obsidian Sync. Nothing here converts those facts into a footprint comparison.

## Open points

- Unverified: a measured latency for Hermes file tools. “Instantaneous” was not in the skill docs. “Within seconds” is the skill’s description of continuous Obsidian Sync, not a test.
- Unverified: Hermes Agent actually completing a tool call against Joplin’s built-in MCP. The two HTTP endpoints are documented separately. No pairing write-up was found.
- Unverified: Joplin Cloud Pro’s euro price on 2026-10-15. Limits were visible (30 GB, 200 MB). The monthly price was not.
- Unverified: whether the English Obsidian pricing page still sells Plus at $8. The Japanese Sync page and the March 2024 blog say $8. The English card fetched here advertises $4 billed annually.
- Unverified: the remainder of Obsidian’s IndexedDB / Apple warning. The fetch stopped mid-sentence.
- Unverified: current maintenance of every third-party Joplin MCP repository beyond `alondmnt/joplin-mcp`’s changelog through June 2026 and the forum posts that still link them.
- Unverified: behavior of this owner’s Nextcloud with either an Obsidian vault folder or a Joplin WebDAV target. The docs describe the mechanisms. They were not run here.
- Unverified: Hermes Agent version number in the wild. A third-party guide mentioned v0.42.5. That was not checked against the repository.

## Sources

### Hermes Agent and Hermes models

- Hermes Agent documentation, Nous Research. https://hermes-agent.nousresearch.com/docs/
- Obsidian skill, Hermes Agent. https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian
- `skills/note-taking/obsidian/SKILL.md`, `NousResearch/hermes-agent`. https://github.com/NousResearch/hermes-agent/blob/main/skills/note-taking/obsidian/SKILL.md
- LLM Wiki skill, Hermes Agent. https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki
- `skills/research/llm-wiki/SKILL.md`, `NousResearch/hermes-agent`. https://github.com/NousResearch/hermes-agent/blob/HEAD/skills/research/llm-wiki/SKILL.md
- MCP feature, Hermes Agent. https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- MCP config reference, Hermes Agent. https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
- Nous Portal, Hermes Agent (Hermes 4 not recommended for the agent loop). https://hermes-agent.nousresearch.com/docs/integrations/nous-portal
- LICENSE, `NousResearch/hermes-agent` (MIT, 2025). https://github.com/NousResearch/hermes-agent/blob/main/LICENSE
- Pull request 19332, Obsidian skill file tools, merged May 2026. https://github.com/NousResearch/hermes-agent/pull/19332
- Hermes 4 technical report, Nous Research. https://nousresearch.com/wp-content/uploads/2025/08/Hermes_4_Technical_Report.pdf
- `NousResearch/Hermes-4-405B`, Hugging Face. https://huggingface.co/NousResearch/Hermes-4-405B

### LLM Wiki

- Andrej Karpathy, `llm-wiki.md` gist, 4 April 2026. https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

### Obsidian

- Pricing. https://obsidian.md/pricing
- License overview. https://obsidian.md/license
- Terms of service. https://obsidian.md/terms
- “Obsidian is now free for work.” https://obsidian.md/blog/free-for-work/
- Commercial license help. https://obsidian.md/help/teams/license
- Obsidian Sync product page. https://obsidian.md/sync
- Japanese Sync page (Standard $4, Plus $8). https://obsidian.md/ja/sync
- “Obsidian Sync now starts at $4 per month,” 20 March 2024. https://obsidian.md/blog/standard-plan/
- Plans and storage limits. https://obsidian.md/help/sync/plans
- Sync FAQ. https://obsidian.md/help/sync/faq
- Sync your notes across devices. https://obsidian.md/help/sync-notes
- How Obsidian stores data. https://obsidian.md/help/data-storage
- Configuration folder. https://obsidian.md/help/configuration-folder
- Set up Obsidian Sync. https://obsidian.md/help/sync/setup
- Troubleshoot Obsidian Sync. https://obsidian.md/help/sync/troubleshoot
- Obsidian Headless. https://obsidian.md/help/headless
- `obsidianmd/obsidian-headless`. https://github.com/obsidianmd/obsidian-headless/
- “How do you sync your vaults?”, Obsidian Forum. https://forum.obsidian.md/t/how-do-you-sync-your-vaults/21332
- “Help! disappearing files and multiplying folders after using sync!”, Obsidian Forum. https://forum.obsidian.md/t/help-disappearing-files-and-multiplying-folders-after-using-sync/16529
- Plugin file size and Sync, Obsidian Forum, 27 November 2025. https://forum.obsidian.md/t/ability-to-repair-community-plugin-installations-when-sync-fails-to-copy-some-portion-due-to-file-size-limits/108441
- Nextcloud Sync community plugin. https://community.obsidian.md/plugins/nextcloud-sync
- NextSync community plugin. https://community.obsidian.md/plugins/nextsync

### Joplin

- Synchronisation. https://joplinapp.org/help/apps/sync/
- Nextcloud synchronisation, repository readme. https://github.com/laurent22/joplin/blob/dev/readme/apps/sync/nextcloud.md
- WebDAV synchronisation. https://github.com/laurent22/joplin/blob/dev/readme/apps/sync/webdav.md
- FAQ, including the sync-directory paragraph and the external editor. https://github.com/laurent22/joplin/blob/dev/readme/faq.md
- User profile spec (`database.sqlite`). https://github.com/laurent22/joplin/blob/dev/readme/dev/spec/user_profile.md
- Architecture (local SQLite; Joplin Server components). https://github.com/laurent22/joplin/blob/dev/readme/dev/spec/architecture.md
- Import and export. https://joplinapp.org/help/apps/import_export
- Terminal application (CLI export formats). https://github.com/laurent22/joplin/blob/dev/readme/apps/terminal.md
- Data API. https://joplinapp.org/help/api/references/rest_api
- MCP server, `readme/apps/ai_mcp.md` on `dev`. https://github.com/laurent22/joplin/blob/dev/readme/apps/ai_mcp.md
- “What's new in Joplin 3.7,” Joplin Forum, 31 August 2026. https://discourse.joplinapp.org/t/whats-new-in-joplin-3-7/50794
- Desktop changelog (`v3.7.21`, 2026-09-25; MCP added in the 3.7 line). https://github.com/laurent22/joplin/blob/dev/readme/about/changelog/desktop.md
- Release `v3.7.3` (pre-release, 2026-06-23, “Add MCP server”). https://github.com/laurent22/joplin/releases/tag/v3.7.3
- Joplin Cloud plans. https://joplinapp.org/plans/
- AGPL switch, 21 December 2022. https://github.com/laurent22/joplin/blob/dev/readme/news/20221221-agpl.md
- Markdown, links to other notes. https://raw.githubusercontent.com/laurent22/joplin/master/readme/markdown.md
- Wikilinks plugin. https://joplinapp.org/plugins/plugin/joplin.plugin.alondmnt.wikilinks/
- “Add wikilink internal link support,” Joplin Forum. https://discourse.joplinapp.org/t/add-wikilink-internal-link-support/44560
- `alondmnt/joplin-mcp`. https://github.com/alondmnt/joplin-mcp/
- Changelog, `alondmnt/joplin-mcp` (through v0.9.0, 2026-06-10). https://github.com/alondmnt/joplin-mcp/blob/main/CHANGELOG.md
- “AI agents and Joplin,” Joplin Forum. https://discourse.joplinapp.org/t/ai-agents-and-joplin/46168
- “Joplin MCP server is released!,” Joplin Forum. https://discourse.joplinapp.org/t/joplin-mcp-server-is-released-use-notes-in-ai-tools/44726
- “100% standalone Joplin MCP server,” Joplin Forum. https://discourse.joplinapp.org/t/100-standalone-joplin-mcp-server/50217
- “Joplin-mcp: Smarter & Faster,” Joplin Forum, 18 February 2026. https://discourse.joplinapp.org/t/joplin-mcp-smarter-faster/48685
- “Where are my notes' .md files?,” Joplin Forum. https://discourse.joplinapp.org/t/where-are-my-notes-md-files/33435
- “Editing Joplin .md files directly does not update app contents,” Joplin Forum. https://discourse.joplinapp.org/t/editing-joplin-md-files-directly-does-not-update-app-contents/19638
- “Export Summary: what each option does,” Joplin Forum. https://discourse.joplinapp.org/t/export-summary-what-each-option-does/48564
- “Never-ending sync,” Joplin Forum, March 2025. https://discourse.joplinapp.org/t/never-ending-sync/44431
- `SQLITE_CORRUPT` after unexpected shutdown, `laurent22/joplin` issue 11686. https://github.com/laurent22/joplin/issues/11686
- `SQLITE_BUSY: database is locked`, issue 10802. https://github.com/laurent22/joplin/issues/10802
- Database corruption report, issue 2129 (2019). https://github.com/laurent22/joplin/issues/2129

### Nextcloud

- Accessing Nextcloud files using WebDAV, Nextcloud user manual. https://docs.nextcloud.com/server/latest/user_manual/eu/files/access_webdav.html
