---
title: How-to. OpenCode setup
date: 2026-11-18
tags:
  - course
  - howto
  - opencode
  - coding-agent
audience: student
status: current
canonical: true
---

# How-to. Set up OpenCode

*optional extension.* OpenCode is a valid system. It is *not required for assessment*. See [minimum path](../../PROJECT-WORK/minimum-path.md).

OpenCode is an **open-source coding agent** (MIT) by Anomaly. It is built for work inside a code repository: edits, diffs, commands, and review.

This is **not** Hermes. Hermes is a multipurpose agent harness. OpenCode is a coding-first loop. Pair them: [howto hermes opencode pairing](howto-hermes-opencode-pairing.md).

Source types: [references](../../REFERENCES/bibliography.md#source-types). A label names the source kind. It is not independent verification. Labels: *technical suggestion*. Check current docs when versions change.

Official site: https://opencode.ai  
Docs: https://opencode.ai/docs/  
GitHub: https://github.com/anomalyco/opencode

---

## 1. What OpenCode is

| | |
|---|---|
| **Product** | Open-source AI coding agent (terminal, desktop, web) |
| **Job** | Deep work in a repo: implement, refactor, review |
| **Models** | Many providers, including local. Configure with `/connect` |
| **Licence** | MIT (*institutional summary* from project docs) |

Built-in agents (switch in the UI):

- **build**: full access for development work (default)
- **plan**: read-only analysis; asks before bash

Docs: https://opencode.ai/docs/ · https://opencode.ai/terminal

---

## 2. Install (current paths)

Prefer a download you can open: https://opencode.ai/download  
Docs: https://opencode.ai/docs/

The curl line below is a pipe. A pipe runs the script before you can read it. Use path B.

The script at `https://opencode.ai/v2/install` does not publish a checksum of itself. This course does not invent one.

Release archives do have a checksum file. Release v2.3.2 includes a file named `SHA256SUMS`. The project says this starts at v2.2.0. That file checks an archive. It does not check the install script. Page: https://github.com/anomalyco/opencode/releases/tag/v2.3.2

1. Open https://github.com/anomalyco/opencode/releases in your browser.
2. Read the address bar. The host must be `github.com`.
3. Open the newest release whose tag starts with `v2`.
4. Save `SHA256SUMS` and one archive into your Downloads folder.
5. Open a terminal the way the next section says.
6. On Linux or macOS, type `cd ~/Downloads` and press Enter.
7. On Windows, type `cd $HOME\Downloads` and press Enter.
8. On Linux, type `sha256sum -c SHA256SUMS` and press Enter.
9. On macOS, type `shasum -a 256 -c SHA256SUMS` and press Return.
10. A line that ends in `OK` matches. Stop if your file line says `FAILED`.
11. On Windows, type `notepad SHA256SUMS` and press Enter.
12. Find the line for your archive.
13. Type `Get-FileHash .\` then the archive file name, then ` -Algorithm SHA256`, and press Enter.
14. The hash in Notepad and the hash in the terminal must be the same text. Stop if they differ.

### Open a terminal

Windows:

1. Click Start.
2. Type `Windows Terminal`.
3. Press Enter.

Linux:

1. Press the Super key.
2. Type `Terminal`.
3. Press Enter.

macOS:

1. Press Command and the space bar together.
2. Type `Terminal`.
3. Press Return.

### Path A. Convenience (macOS or Linux)

1. The host in the next command must be `opencode.ai`.
2. The address must start with `https://`.
3. Stop if the host is different.
4. Click the terminal window.
5. Type `cd` and press Enter.
6. Type the next line and press Enter. The script runs as soon as it downloads.

```bash
curl -fsSL https://opencode.ai/v2/install | bash
```

### Path B. Inspectable (macOS or Linux)

1. The host in the next command must be `opencode.ai`.
2. The address must start with `https://`.
3. Stop if the host is different.
4. Click the terminal window.
5. Type `cd` and press Enter.
6. Type the next line and press Enter. This saves the script as `install`. It does not run it.

```bash
curl -fsSL https://opencode.ai/v2/install -o install
```

7. Type `less install` and press Enter.
8. Press the space bar to move down.
9. Press `q` to close the viewer.
10. While you read, look for `curl` lines.
11. Those hosts should be `opencode.ai` or `registry.npmjs.org`.
12. Stop if you see a different host.
13. Type `bash install` and press Enter.

What this script changes, from the script at that URL, checked 20 Nov 2026:

- It creates `~/.opencode/bin`.
- It puts the `opencode` program in that folder.
- It can add a PATH line to one shell startup file, often `~/.zshrc` or `~/.bashrc`.
- The script option `--no-modify-path` skips that startup-file edit. To use it, type `bash install --no-modify-path` instead of `bash install`.

1. Close the terminal and open a new one.
2. Type `opencode --version` and press Enter.

Uninstall, from the command source checked 20 Nov 2026: https://github.com/anomalyco/opencode/blob/a5fc5fd93dcdab58c19e1d1cc5c12cc2d5ad7207/packages/cli/src/commands/handlers/uninstall.ts

1. Open a terminal.
2. Type `opencode uninstall --dry-run` and press Enter. This lists files. It does not delete them.
3. Type `opencode uninstall` and press Enter.
4. This command removes the cache.
5. It also removes a PATH line that mentions `.opencode/bin`.
6. It does not delete config, sessions, or credentials.
7. For a curl install, the command then prints an `rm` line for the program file.
8. Read that path.
9. Type the line only when the path is inside `~/.opencode/bin`.

### Other install paths

```bash
# npm (also used on Windows when package managers are limited)
npm install -g @opencode/cli
```

```bash
# Homebrew (macOS / Linux)
brew install anomalyco/tap/opencode-v2
```

Standalone binaries and Desktop downloads: https://opencode.ai/docs/ and https://opencode.ai/download

*institutional summary (OpenCode docs):* Windows package managers are not supported the same way; use the npm path or a standalone Windows binary from the docs.

The npm command is not a pipe. It still runs a package install script. Read the package page before you type it: https://www.npmjs.com/package/@opencode/cli

---

## 3. First run

1. Go to a git project folder.
2. Start OpenCode:

```bash
opencode
```

Or point at another folder:

```bash
opencode ~/code/my-project
```

3. Connect a model provider in the TUI:

```text
/connect
```

4. Try a small read-only ask first (use **plan** if you want fewer write risks).
5. For one-shot scripts:

```bash
opencode run "Explain this repository"
```

Optional Desktop app: download from the OpenCode site. Same agent family as the CLI.

---

## 4. How Hermes talks to OpenCode

Hermes can **hand coding work** to OpenCode through an official optional skill.

Install the skill in Hermes:

```bash
hermes skills install official/autonomous-ai-agents/opencode
```

Skill docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-opencode

Then Hermes can:

- run bounded jobs with `opencode run "…"`
- start longer OpenCode sessions and watch progress
- report file changes and next steps back to you

You still need OpenCode installed and authenticated on that machine.

Hermes compare page also notes OpenCode Zen / OpenCode Go as model providers in some setups. That is separate from the coding CLI skill. Prefer the skill for **repo coding handoff**.

Practical pairing: [howto hermes opencode pairing](howto-hermes-opencode-pairing.md)

---

## 5. Course checklist

- [ ] `opencode --version` works
- [ ] Provider connected (`/connect` or env keys)
- [ ] You can open a project and get a reply
- [ ] Optional: Hermes OpenCode skill installed
- [ ] Keys stay out of the Obsidian vault

---

## Sources

- https://opencode.ai/docs/
- https://opencode.ai/terminal
- https://github.com/anomalyco/opencode
- https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/autonomous-ai-agents/autonomous-ai-agents-opencode
- https://hermes-agent.nousresearch.com/compare
