---
title: Critical Vibe Coding. Course outline
date: 2026-10-18
updated: 2026-11-10
tags:
  - course
  - outline
audience: student
status: current
canonical: true
---

# Critical Vibe Coding: course outline

Interface Cultures · short public / syllabus sheet. Full session notes: [timeline](timeline.md). Labels: *requirement* | *todo*.

A personal manifesto on how you want to use AI in your practice is required. It names no product. Session 01 introduces it. You develop it through the course and hand it in at the end. It is not a week-1 deliverable. Also required: [minimum path](../minimum-path.md) and the student input presentations.
The technical object is a student-designed agentic production system. Hermes is one *reference implementation*. The class install is a *demonstration*. It is *not required for assessment*. Claude Code, Cursor, OpenCode, a local script, or another agent are valid systems. No purchase is required. Alternatives are allowed.

*Inspired in form by* [HKUST AMCC6500, Critical AI and Artistic Creation](https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf) *(Giannoutakis)*: weekly topic + one-line cover, not a copy of their themes.

---

## Course description

Hands-on seminar: students build and run a personal LLM-agent setup while unpacking the political and economic forces that make these tools feel inevitable. Prompting is the entry into creative coding, node/GUI tools, text frameworks and **3D/CAD** applications, each needing different translation and debugging habits.

"Vibe coding" is not taught as a frictionless shortcut. The course asks when AI helps, when it wastes time, which models and infrastructures fit a task, and how authorship, labour, platform dependency and ecology shift when an **agent** sits between you and the stack. The agent itself is treated as interface material for media-art practice, not only as a means to an output.

**Eight sessions**, each **10:00 to 12:00** (120 min, short break). Each opens with a **listen-only check-in**. In Sessions 02, 03, 05, 06 and 07 a student group (about 15 min) brings a **humanities** question; the teacher leads **technical practice** after. Full rhythm + clocks: [course rhythm](course-rhythm.md). Midpoint (Session 04) and final (Session 08): **working personal setup** + critical reflection. The setup that assessment uses is [minimum path](../minimum-path.md).

*requirement (brief):* visual/node environments, GUI tools, text coding and 3D/CAD; criteria for useful versus unnecessary AI; proprietary cloud versus local/open infra; shared space for hopes, fears and authorship questions.

---

## Learning outcomes

Students will be able to:

1. Run a personal agent (default: Hermes + Obsidian / LLM Wiki) with a clear knowledge store and at least one external tool path (MCP or equivalent).
2. Choose and justify models, tools and infrastructures for a given creative task, including when **not** to use AI.
3. Translate prompts across stacks (code, node, CAD/3D) and document where the agent helps and where it fails.
4. Articulate authorship, labour, platform and ecological questions in relation to their own practice.
5. Present the **setup** (architecture + one artistic/research use) as the main deliverable, not a polished exhibition by default.

Outcome 1 names a *reference implementation*. It is not the assessed architecture. Coding agents and other agents are valid systems. The assessed parts are in [minimum path](../minimum-path.md): knowledge store, access boundary, model endpoint, tool set, verification method, provenance, and critical reflection. The manifesto is also required. Outcome 3, across code, node, and CAD/3D, is an *optional extension*.

---

## Planned assessment (*todo*: weights TBD)

| Assessment | What | % (*todo*) |
|---|---|---|
| Personal manifesto | How you want to use AI in your practice. No required product. Develop it through the course. Hand it in at the end. | TBD |
| Midpoint (Session 04) | Project presentation + semester plan + the system as it stands ([minimum path](../minimum-path.md)) | TBD |
| Final presentation (Session 08) | Architecture walkthrough + one artistic/research use + short critical reflection | TBD |
| Student input | One group input (Sessions 02, 03, 05, 06 or 07) | TBD |
| Seminar participation | Check-ins, studio critique, peer feedback | TBD |

---

## Weekly schedule (session map)

| Week | Topic | Student input | What this session covers |
|---|---|---|---|
| 1 | Welcome + landscape | (groups choose topics) | Outdoor check-in; LLMs and agents; drivers, visions, fears, regulation; economy and the bubble; ecology; labour; media-art workflows; default setup. [01 welcome and landscape](../sessions/01-welcome-and-landscape.md) · [01 welcome landscape lecture](../lectures/01-welcome-landscape-lecture.md) |
| 2 | Harness, wiki architecture, model landscape, **install Hermes** | Flattening | **Agent = Model + Harness**, LLM Wiki / Obsidian structure, what students can use; Hermes install with a free-to-use hosted endpoint. [02 agent harness and wiki architecture](../sessions/02-agent-harness-and-wiki-architecture.md) · [what is harness](../concepts/what-is-harness.md) |
| 3 | Hardware, locally runnable models, prompting | Closed versus open weights as power | Ready-made (Apple/Spark), DIY GPU / multi-GPU split, locally runnable models versus RAM; prompting; chat versus reasoning. [03 hardware open models prompting](../sessions/03-hardware-open-models-prompting.md) · [howto local llm hardware](../setup/howto-local-llm-hardware.md) · [Prompting Guide for Critical Vibe Coding](../setup/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md) |
| 4 | **Midpoint:** project presentations | none | Students' semester plans + setup as it stands. [04 project presentations and plans](../sessions/04-project-presentations-and-plans.md) |
| 5 | Vault practice, phone, Discord, MCP | How dangerous is AI really? | Personalise the agent; phone sync; Discord bridge; MCP basics and one server. [05 knowledge base phone discord](../sessions/05-knowledge-base-phone-discord.md) · [what is mcp](../concepts/what-is-mcp.md) |
| 6 | Agent as interface, material, canvas | The ecology of AI | Setup, skills and tools as artistic material; interface score. [06 agent as interface](../sessions/06-agent-as-interface.md) |
| 7 | Coding with agents across creative stacks (*proposal, TBD*) | Privacy: what happens with the data? | Vibe coding critically; code, node, GUI, 3D/CAD, fab. [07 coding and creative stacks](../sessions/07-coding-and-creative-stacks.md) |
| 8 | **Final presentations** (*proposal*) | none | Architecture + use + reflection; closing check-in. [08 final presentations](../sessions/08-final-presentations.md) |

Rhythm and student groups: [course rhythm](course-rhythm.md). Tables the eight sessions still use are in the [archive](../sessions/archive-13-session-plan/README.md).

---

## Software and platforms (default stack)

*reference implementation. Optional extension. Not required for assessment.* This table is one Hermes example. The assessed system is [minimum path](../minimum-path.md). Coding agents and other agents are valid systems.

| Role | Default | Notes |
|---|---|---|
| Agent | [Hermes Agent](https://hermes-agent.nousresearch.com/docs/) (MIT) | Not the Hermes 4 chat models. Installed in Session 02 |
| Free-to-use hosted endpoint | NVIDIA Nemotron 3 Ultra via OpenRouter | Openly distributed materials (OpenMDW-1.1). Rate-limited. Prompts may be logged. Too large for most student machines. The route is a hosted cloud service. [default setup](../lectures/01-welcome-landscape-deep-dives/default-setup.md) §4 |
| Notes / wiki | [Obsidian](https://obsidian.md/) + LLM Wiki habit | Phone sync via personal cloud (e.g. Nextcloud) |
| Harness concept | Agent = Model + Harness | [what is harness](../concepts/what-is-harness.md) · Session 02 |
| Protocol for apps | [MCP](https://modelcontextprotocol.io/) (Model Context Protocol) | Calendar, browser, **CAD/3D**, etc. Session 05. Permissions and capability boundary: [what is mcp](../concepts/what-is-mcp.md#permissions-and-capability-boundary). |
| Optional | Discord bridge; Nextcloud Context Agent (one MCP) | Not required student infra |

Install guides (Windows / macOS / Linux): [howto hermes setup](../setup/howto-hermes-setup.md) · [howto obsidian setup and sync](../setup/howto-obsidian-setup-and-sync.md) · optional [howto silverbullet setup and sync](../setup/howto-silverbullet-setup-and-sync.md)

Creative AI tool survey (extra): [ai tools creative processes](../topics/ai-tools-creative-processes.md)

Local hardware (Session 03): [local gpu hardware for llms](../../research/local-gpu-hardware-for-llms.md) · [howto local llm hardware](../setup/howto-local-llm-hardware.md)

Class rhythm: [course rhythm](course-rhythm.md)

---

## Core readings (short)

Full list: [references](references.md).

| Theme | Starter |
|---|---|
| LLM Wiki method | [Karpathy, `llm-wiki.md` gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) · what structure improves: [llm wiki standard files](../setup/llm-wiki-standard-files.md#what-structure-improves) |
| Political economy / bubble | [bubble economy](../lectures/01-welcome-landscape-deep-dives/bubble-economy.md) · research note [ai bubble productivity datacenter](../../research/ai-bubble-productivity-datacenter.md); Tooze / BIS as cited there; Verdegem, *Dismantling AI capitalism* (2022) |
| Authorship & labour | [labour](../lectures/01-welcome-landscape-deep-dives/labour.md) · jobs evidence [ai jobs rising tide productivity](../../research/ai-jobs-rising-tide-productivity.md) |
| Flattening, AI and patriarchy | [flattening and the norm](../lectures/01-welcome-landscape-deep-dives/flattening-and-the-norm.md) |
| Ecology / data centres / when not | [ecology](../lectures/01-welcome-landscape-deep-dives/ecology.md) · [data centers energy ecology economy](../../research/data-centers-energy-ecology-economy.md); IEA; Be Smart overview video |
| Local hardware / open weights | Session 03 + [local gpu hardware for llms](../../research/local-gpu-hardware-for-llms.md) · [howto local llm hardware](../setup/howto-local-llm-hardware.md) |

Peer-course patterns (not required texts): HKUST AMCC6500; Birkbeck Critical and Creative AI; HM Munich *Our Br00d*. See [timeline](timeline.md#peer-courses-web-research-2026-10-18).

---

## Still open (*todo*)

- Exact calendar, room, ECTS, grading weights
- Session 07 focus (proposal: coding with agents) and Session 08 (proposal: finals)
- Student group size for the five input slots
- Model cost guidance for students
- Whether a shared class wiki sits beside personal vaults
