---
title: Critical Vibe Coding. Course outline
date: 2026-10-18
updated: 2026-11-10
tags:
  - course
  - outline
---

# Critical Vibe Coding: course outline

Interface Cultures · short public / syllabus sheet. Full session notes: [[timeline]]. Labels: *requirement* | *todo*.

*Inspired in form by* [HKUST AMCC6500, Critical AI and Artistic Creation](https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf) *(Giannoutakis)*: weekly topic + one-line cover, not a copy of their themes.

---

## Course description

Hands-on seminar: students build and run a personal LLM-agent setup while unpacking the political and economic forces that make these tools feel inevitable. Prompting is the entry into creative coding, node/GUI tools, text frameworks and **3D/CAD** applications, each needing different translation and debugging habits.

"Vibe coding" is not taught as a frictionless shortcut. The course asks when AI helps, when it wastes time, which models and infrastructures fit a task, and how authorship, labour, platform dependency and ecology shift when an **agent** sits between you and the stack. The agent itself is treated as interface material for media-art practice, not only as a means to an output.

**Eight sessions**, each **10:00 to 12:00** (120 min, short break). Each opens with a **listen-only check-in**. In Sessions 02, 03, 05, 06 and 07 a student group (about 15 min) brings a **humanities** question; the teacher leads **technical practice** after. Full rhythm + clocks: [[course-rhythm]]. Midpoint (Session 04) and final (Session 08): **working personal setup** + critical reflection.

*requirement (brief):* visual/node environments, GUI tools, text coding and 3D/CAD; criteria for useful versus unnecessary AI; proprietary cloud versus local/open infra; shared space for hopes, fears and authorship questions.

---

## Learning outcomes

Students will be able to:

1. Run a personal agent (default: Hermes + Obsidian / LLM Wiki) with a clear knowledge store and at least one external tool path (MCP or equivalent).
2. Choose and justify models, tools and infrastructures for a given creative task, including when **not** to use AI.
3. Translate prompts across stacks (code, node, CAD/3D) and document where the agent helps and where it fails.
4. Articulate authorship, labour, platform and ecological questions in relation to their own practice.
5. Present the **setup** (architecture + one artistic/research use) as the main deliverable, not a polished exhibition by default.

---

## Planned assessment (*todo*: weights TBD)

| Assessment | What | % (*todo*) |
|---|---|---|
| Midpoint (Session 04) | Project presentation + semester plan + setup as it stands | TBD |
| Final presentation (Session 08) | Architecture walkthrough + one artistic/research use + short critical reflection | TBD |
| Student input | One group input (Sessions 02, 03, 05, 06 or 07) | TBD |
| Seminar participation | Check-ins, studio critique, peer feedback | TBD |

---

## Weekly schedule (session map)

| Week | Topic | Student input | What this session covers |
|---|---|---|---|
| 1 | Welcome + landscape | (groups choose topics) | Outdoor check-in; LLMs and agents; drivers, visions, fears, regulation; economy and the bubble; ecology; labour; media-art workflows; default setup. [[sessions/01-welcome-and-landscape]] · [[lectures/01-welcome-landscape-lecture]] |
| 2 | Harness, wiki architecture, model landscape, **install Hermes** | Flattening | **Agent = Model + Harness**, LLM Wiki / Obsidian structure, what students can use; Hermes install with a free open model. [[sessions/02-agent-harness-and-wiki-architecture]] · [[what-is-harness]] |
| 3 | Hardware, open models, prompting | Closed versus open weights as power | Ready-made (Apple/Spark), DIY GPU / multi-GPU split, open models versus RAM; prompting; chat versus reasoning. [[sessions/03-hardware-open-models-prompting]] · [[howto-local-llm-hardware]] · [[prompting-and-model-choice]] |
| 4 | **Midpoint:** project presentations | none | Students' semester plans + setup as it stands. [[sessions/04-project-presentations-and-plans]] |
| 5 | Vault practice, phone, Discord, MCP | How dangerous is AI really? | Personalise the agent; phone sync; Discord bridge; MCP basics and one server. [[sessions/05-knowledge-base-phone-discord]] · [[what-is-mcp]] |
| 6 | Agent as interface, material, canvas | The ecology of AI | Setup, skills and tools as artistic material; interface score. [[sessions/06-agent-as-interface]] |
| 7 | Coding with agents across creative stacks (*proposal, TBD*) | Privacy: what happens with the data? | Vibe coding critically; code, node, GUI, 3D/CAD, fab. [[sessions/07-coding-and-creative-stacks]] |
| 8 | **Final presentations** (*proposal*) | none | Architecture + use + reflection; closing check-in. [[sessions/08-final-presentations]] |

Rhythm and student groups: [[course-rhythm]]. Cut sessions from the earlier 13-session plan (authorship and labour, ecology and when not, studio and critique, MCP and tools, models and install) are kept in [[sessions/archive-13-session-plan/README]].

---

## Software and platforms (default stack)

| Role | Default | Notes |
|---|---|---|
| Agent | [Hermes Agent](https://hermes-agent.nousresearch.com/docs/) (MIT) | Not the Hermes 4 chat models. Installed in Session 02 |
| Free model to start | NVIDIA Nemotron 3 Ultra via OpenRouter's free tier | Open weights (OpenMDW 1.1); rate-limited; runs in the cloud. [[lectures/01-welcome-landscape-deep-dives/default-setup]] §4 |
| Notes / wiki | [Obsidian](https://obsidian.md/) + LLM Wiki habit | Phone sync via personal cloud (e.g. Nextcloud) |
| Harness concept | Agent = Model + Harness | [[what-is-harness]] · Session 02 |
| Protocol for apps | [MCP](https://modelcontextprotocol.io/) (Model Context Protocol) | Calendar, browser, **CAD/3D**, etc. Session 05 |
| Optional | Discord bridge; Nextcloud Context Agent (one MCP) | Not required student infra |

Install guides (Windows / macOS / Linux): [[howto-hermes-setup]] · [[howto-obsidian-setup-and-sync]] · optional [[howto-silverbullet-setup-and-sync]]

Creative AI tool survey (extra): [[ai-tools-creative-processes]]

Local hardware (Session 03): [[../../research/local-gpu-hardware-for-llms]] · [[howto-local-llm-hardware]]

Class rhythm: [[course-rhythm]]

Student materials pack (do not share the full vault): [[student-share-structure]]

---

## Core readings (short)

Full list: [[references]].

| Theme | Starter |
|---|---|
| LLM Wiki method | [Karpathy, `llm-wiki.md` gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) |
| Political economy / bubble | [[lectures/01-welcome-landscape-deep-dives/bubble-economy]] · research note [[../../research/ai-bubble-productivity-datacenter]]; Tooze / BIS as cited there; Verdegem, *Dismantling AI capitalism* (2022) |
| Authorship & labour | [[lectures/01-welcome-landscape-deep-dives/labour]] · jobs evidence [[../../research/ai-jobs-rising-tide-productivity]] |
| Flattening, AI and patriarchy | [[lectures/01-welcome-landscape-deep-dives/flattening-and-the-norm]] |
| Ecology / data centres / when not | [[lectures/01-welcome-landscape-deep-dives/ecology]] · [[../../research/data-centers-energy-ecology-economy]]; IEA; Be Smart overview video |
| Local hardware / open weights | Session 03 + [[../../research/local-gpu-hardware-for-llms]] · [[howto-local-llm-hardware]] |

Peer-course patterns (not required texts): HKUST AMCC6500; Birkbeck Critical and Creative AI; HM Munich *Our Br00d*. See [[timeline#peer-courses-web-research-2026-10-18]].

---

## Still open (*todo*)

- Exact calendar, room, ECTS, grading weights
- Session 07 focus (proposal: coding with agents) and Session 08 (proposal: finals): Sebastian to approve
- Student group size for the five input slots
- Model cost guidance for students
- Whether a shared class wiki sits beside personal vaults
