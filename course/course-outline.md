---
title: Critical Vibe Coding — course outline
date: 2026-10-18
tags:
  - course
  - outline
---

# Critical Vibe Coding — course outline

Interface Cultures · short public / syllabus sheet. Full session notes: [[timeline]]. Labels: *requirement* | *todo*.

*Inspired in form by* [HKUST AMCC6500 — Critical AI and Artistic Creation](https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf) *(Giannoutakis)* — weekly topic + one-line cover, not a copy of their themes.

---

## Course description

Hands-on seminar: students build and run a personal LLM-agent setup while unpacking the political and economic forces that make these tools feel inevitable. Prompting is the entry into creative coding, node/GUI tools, text frameworks, and **3D/CAD** applications — each needing different translation and debugging habits.

“Vibe coding” is not taught as a frictionless shortcut. The course asks when AI helps, when it wastes time, which models and infrastructures fit a task, and how authorship, labour, platform dependency, and ecology shift when an **agent** sits between you and the stack. The agent itself is treated as interface material for media-art practice, not only as a means to an output.

Each class is **10:00–12:00** (120 min, short break). Opens with a **listen-only check-in**. From session 2, one student **pair** (~15 min) brings a **humanities** question; teacher leads **technical practice** after. Full rhythm + clocks: [[course-rhythm]]. Midpoint and final: **working personal setup** + critical reflection.

*requirement (brief):* visual/node environments, GUI tools, text coding, and 3D/CAD; criteria for useful vs unnecessary AI; proprietary cloud vs local/open infra; shared space for hopes, fears, and authorship questions.

---

## Learning outcomes

Students will be able to:

1. Run a personal agent (default: Hermes + Obsidian / LLM Wiki) with a clear knowledge store and at least one external tool path (MCP or equivalent).
2. Choose and justify models, tools, and infrastructures for a given creative task — including when **not** to use AI.
3. Translate prompts across stacks (code, node, CAD/3D) and document where the agent helps vs fails.
4. Articulate authorship, labour, platform, and ecological questions in relation to their own practice.
5. Present the **setup** (architecture + one artistic/research use) as the main deliverable, not a polished exhibition by default.

---

## Planned assessment (*todo* — weights TBD)

| Assessment | What | % (*todo*) |
|---|---|---|
| Midpoint demo + proposal | Live agent setup + short written proposal (how the setup enters a project) | TBD |
| Final presentation | Architecture walkthrough + one artistic/research use + short critical reflection | TBD |
| Student input / rotating demos | Short tool or theme presentations | TBD |
| Seminar participation | Check-ins, studio critique, peer feedback | TBD |

---

## Weekly schedule (session map)

| Week | Topic | What this session covers |
|---|---|---|
| 1 | Welcome + landscape | Outdoor/check-in; drivers/visions/fears/regulation; bubble seed; setup proposal. [[sessions/01-welcome-and-landscape]] · [[visions-fears-regulation]] · [[lectures/01-welcome-landscape-lecture]] |
| 2 | Harness + wiki architecture | **Agent = Model + Harness**, then LLM Wiki / Obsidian. [[sessions/02-agent-harness-and-wiki-architecture]] · [[what-is-harness]] |
| 3 | Models, prompting, install | Landscape; chat vs reasoning; prompting; **cloud** Hermes install; academic AI honesty. [[sessions/03-models-prompting-install]] · [[prompting-and-model-choice]] · [[academic-ai-austria]] |
| 4 | Local hardware + open LLMs | Ready-made (Apple/Spark), DIY GPU / multi-GPU split, open models vs RAM. [[sessions/04-local-hardware-and-open-llms]] · [[howto-local-llm-hardware]] · [[../research/local-gpu-hardware-for-llms]] |
| 5 | Wiki practice + phone + Discord | Personalise agent; phone sync; Discord bridge. [[sessions/05-knowledge-base-phone-discord]] |
| 6 | MCP and tools (incl. 3D/CAD) | One interface to many systems; **agent ↔ CAD / 3D**. [[sessions/06-mcp-and-tools]] |
| 7 | Agent as interface | Setup/skills/tools as artistic material. [[sessions/07-agent-as-interface]] |
| 8 | Agents across creative stacks | Code, node, GUI, **3D/CAD**, fab. [[sessions/08-agents-across-creative-stacks]] |
| 9 | Midpoint | Working setup demo + project proposal. [[sessions/09-midpoint-demo-and-proposal]] |
| 10 | Authorship, labour, platforms | Ghost work, style/IP, platform dependency; EU/AT pointer. [[sessions/10-authorship-labour-platforms]] · [[eu-ai-act-and-datenschutz]] |
| 11 | Ecology, when not | Data-centre siting/energy; refuse AI; data location (*how* to build local → session 04). [[sessions/11-local-ecology-when-not]] · [[../research/data-centers-energy-ecology-economy]] |
| 12 | Studio + peer critique | Build/break/document + critique setup+project. [[sessions/12-studio-and-peer-critique]] |
| 13 | Final presentations | Architecture + use + reflection. [[sessions/13-final-presentations]] |

Rhythm / crowding / 10 student pairs: [[course-rhythm]]. Keep 1–4 (socio → harness → install → local) and midpoint (9) fixed.

---

## Software and platforms (default stack)

| Role | Default | Notes |
|---|---|---|
| Agent | [Hermes Agent](https://hermes-agent.nousresearch.com/docs/) (MIT) | Not the Hermes 4 chat models |
| Notes / wiki | [Obsidian](https://obsidian.md/) + LLM Wiki habit | Phone sync via personal cloud (e.g. Nextcloud) |
| Harness concept | Agent = Model + Harness | [[what-is-harness]] · session 2 |
| Protocol for apps | [MCP](https://modelcontextprotocol.io/) | Calendar, browser, **CAD/3D**, etc. |
| Optional | Discord bridge; Nextcloud Context Agent (one MCP) | Not required student infra |

Install guides (Windows / macOS / Linux): [[howto-hermes-setup]] · [[howto-obsidian-setup-and-sync]] · optional [[howto-silverbullet-setup-and-sync]]

Creative AI tool survey (extra): [[ai-tools-creative-processes]]

Local hardware (session 04): [[../research/local-gpu-hardware-for-llms]] · [[howto-local-llm-hardware]]

Class rhythm: [[course-rhythm]]

Student materials pack (do not share full vault): [[student-share-structure]]

---

## Core readings (short)

Full list: [[references]]. Critical sessions lean on free-to-read pieces listed there and in sessions 8–9.

| Theme | Starter |
|---|---|
| LLM Wiki method | [Karpathy, `llm-wiki.md` gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) |
| Political economy / bubble | Course research note [[../research/ai-bubble-productivity-datacenter]]; Tooze / BIS as cited there |
| Authorship & labour | Session 9 table · jobs evidence [[../research/ai-jobs-rising-tide-productivity]] |
| Ecology / data centres / when not | Session 11 + [[../research/data-centers-energy-ecology-economy]]; IEA; Be Smart overview video |
| Local hardware / open weights | Session 04 + [[../research/local-gpu-hardware-for-llms]] · [[howto-local-llm-hardware]] |

Peer-course patterns (not required texts): HKUST AMCC6500; Birkbeck Critical and Creative AI; HM Munich *Our Br00d* — see [[timeline#peer-courses-web-research-2026-10-18]].

---

## Still open (*todo*)

- Exact calendar, room, ECTS, grading weights
- Model cost guidance for students
- Whether a shared class wiki sits beside personal vaults
