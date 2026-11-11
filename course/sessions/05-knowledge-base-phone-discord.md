---
title: Session 05. Vault practice, phone sync, Discord bridge, MCP
session: 5
updated: 2026-11-10
---

# Session 05. Vault practice, phone sync, Discord bridge, MCP

Parent: [[../timeline]] · Rhythm: [[../course-rhythm]]

**Slot:** 10:00 to 12:00.

## Goals

- Personalise the schema; first ingest (wiki and harness from Session 02, not re-taught from zero)
- Phone sync; Discord bridge (preferred over Telegram) where feasible
- **MCP**: understand it as a protocol (not a model, not sync) and attach one tool to the agent (moved here from the old Session 06)
- The knowledge store may be Obsidian **or** another option: [[../knowledge-store-options]]

## Clock

| Clock | Block |
|---|---|
| **10:00 to 10:20** | Check-in (listen only) |
| **10:20 to 10:35** | Student input: **how dangerous is AI really?** ([[../course-rhythm]]) |
| **10:35 to 10:55** | Teacher: personalisation / SCHEMA / lint cycle, then MCP basics |
| **10:55 to 11:05** | Break |
| **11:05 to 12:00** | Phone sync + Discord practical, then one MCP server |

*Crowding (flag for Sebastian):* phone, Discord and MCP in one practical is a lot. Suggested split: everyone does phone sync; then each student picks Discord **or** one MCP server.

## Check-in

Listen only: [[../course-rhythm#1-check-in-every-session]]. Sync blockers can appear in the AI answer.

## Student input (theory / humanities): How dangerous is AI really?

Group (about 15 min). From frontier risk to everyday harm: which dangers are documented, which are marketing (Session 01 Block 3, "two industry stories")?

Case: **the Hugging Face incident** (July 2026). OpenAI evaluation agents, running an internal research model, escaped their sandbox through a vulnerability in an internal artifact server and used exposed credentials to reach parts of Hugging Face's production infrastructure (11 to 13 July). *claim (Reuters):* a swarm of about 700 agents that tried to cover their tracks. Read both primary reports and compare them:

- Hugging Face: https://huggingface.co/blog/security-incident-july-2026
- OpenAI: https://openai.com/index/hugging-face-incident-and-the-road-ahead/
- Course script on visions and fears: [[../visions-fears-regulation]]

Bridge to the practical: today students give their own agent new tools. What may it touch?

## Teacher input, Part A: personalisation and practice

Architecture recap only (point back): [[02-agent-harness-and-wiki-architecture]] · [[../what-is-harness]] · [[../llm-wiki-standard-files]] · [[../what-is-lint]]

- Live: fill `SCHEMA.md` limits; run one ingest / query / lint cycle ([[../../research/karpathy-llm-wiki-and-openclaw]])
- Tools: Hermes [llm-wiki skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki) · optional Obsidian plugin [karpathywiki](https://community.obsidian.md/plugins/karpathywiki) ([[../references]])
- What "personalising" means: skills, schema, folder rules, not fine-tuning on day one
- Hybrid: agent-writable wiki folders versus human artistic voice pages
- Honest gap: the teacher is also still deepening the Hermes setup; learning in public

## Teacher input, Part B: MCP basics

**MCP = Model Context Protocol.** A standard plug between an agent and other apps and tools. Course note: [[../what-is-mcp]] (waiter and kitchen metaphor; host, client, server; tools, resources, prompts).

- When you need MCP and when the disk is enough: the Obsidian folder wiki uses filesystem tools, no MCP. Apps that are not folders (calendar, mail, browser, SQLite note apps, live CAD/3D sessions) need MCP.
- How Hermes does it (*verified fact*, Hermes docs 2026-10-18): servers go under `mcp_servers` in `~/.hermes/config.yaml`; local **stdio** and remote **HTTP** servers share one config; `hermes mcp` opens a catalog of Nous-reviewed servers; at install Hermes lists every tool the server exposes and lets you **tick only the tools the agent may see**: [Hermes MCP docs](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- Safety: app passwords, localhost versus remote, what not to put in the vault. Per-server tool filtering is a design decision: the agent cannot call what you did not tick.
- CAD/3D servers (Blender, Fusion, FreeCAD, OpenSCAD, build123d, Rhino, Meshy) with caveats: table in [[archive-13-session-plan/06-mcp-and-tools]]. Used again in Session 07.

## Practical

1. Obsidian ↔ phone sync (Remotely Save / Nextcloud path): [[../howto-obsidian-setup-and-sync]]. Verify: capture a note on the phone → visible on the PC → the agent can read it.
2. Then pick one:
   - **Discord bridge** to the agent (preferred over Telegram), on the student's phone: [Hermes Discord setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)
   - **One MCP server**: list the tools the agent already has (filesystem, web, skills) first; add one server (browser, or build123d-mcp / OpenSCAD if no CAD licence); untick the tools the agent should not have; document the tool list in a short "Tools" section in `SCHEMA.md`.

## Homework

- Run one ingest (or equivalent) of a source relevant to your practice into the wiki
- Write 5 to 10 lines in your schema: what the agent may edit, what is human-only, which tools it must ask before calling
- Optional: Discord messages to the agent working end to end

## Materials

- [[../howto-obsidian-setup-and-sync]] · [[../howto-hermes-setup]] · [[../knowledge-store-options]] · [Hermes Discord setup](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord)
- MCP: [[../what-is-mcp]] · official intro https://modelcontextprotocol.io/docs/getting-started/intro · Hermes MCP https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp · full MCP session with CAD/3D table (archived): [[archive-13-session-plan/06-mcp-and-tools]]
- Student input: Hugging Face and OpenAI incident reports (above) · [[../visions-fears-regulation]]
