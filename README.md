# Critical Vibe Coding

Interface Cultures (Kunstuniversität Linz) — seminar combining **hands-on LLM agents** with **critical inquiry** into authorship, labour, platforms, and ecology.

This GitHub repository is the **student-facing course pack** (syllabus, session notes, how-tos, references). Clone it, browse on GitHub, or copy folders into your Obsidian vault.

|                 |                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| Programme       | Interface Cultures                                                                                        |
| Language        | English                                                                                                   |
| Stack (default) | [Hermes Agent](https://hermes-agent.nousresearch.com/docs/) + [Obsidian](https://obsidian.md/) / LLM Wiki |
| Start here      | [`course/START-HERE.md`](course/START-HERE.md)                                                            |

---

## Quick links

| Need                         | File                                                                           |
|------------------------------|--------------------------------------------------------------------------------|
| Install order + first week   | [`course/START-HERE.md`](course/START-HERE.md)                                 |
| Short syllabus / session map | [`course/syllabus/course-outline.md`](course/syllabus/course-outline.md)                         |
| Full timeline + milestones   | [`course/syllabus/timeline.md`](course/syllabus/timeline.md)                                     |
| Weekly session notes         | [`course/sessions/`](course/sessions/)                                         |
| References & readings        | [`course/syllabus/references.md`](course/syllabus/references.md)                                 |
| Prompting + choosing models  | [`course/concepts/prompting-and-model-choice.md`](course/concepts/prompting-and-model-choice.md) |

---

## Session map (eight sessions; dates TBD)

| # | Topic                                                                                   | Student input                        |
|---|-----------------------------------------------------------------------------------------|--------------------------------------|
| 1 | Welcome + political-economic landscape                                                  | (groups choose topics)               |
| 2 | **Agent harness** → LLM Wiki / Obsidian structure → model landscape; **install Hermes** | Flattening                           |
| 3 | Hardware paths; open models versus RAM; prompting; chat versus reasoning                | Closed versus open weights as power  |
| 4 | **Midpoint:** project presentations, semester plans                                     |                                      |
| 5 | Vault practice, phone sync, Discord bridge, MCP                                         | How dangerous is AI really?          |
| 6 | Agent as interface, as material, as canvas                                              | The ecology of AI                    |
| 7 | *To be decided* (proposal: coding with agents across creative stacks)                   | Privacy: what happens with the data? |
| 8 | **Final** presentations (*proposal*)                                                    |                                      |

Details: [`course/syllabus/timeline.md`](course/syllabus/timeline.md) · [`course/syllabus/course-outline.md`](course/syllabus/course-outline.md) · cut sessions of the earlier 13-session plan: [`course/sessions/archive-13-session-plan/`](course/sessions/archive-13-session-plan/README.md)

---

## How-tos & concepts

| Topic                                       | File                                                                                 |
|---------------------------------------------|--------------------------------------------------------------------------------------|
| Obsidian + phone sync (Win / macOS / Linux) | [`course/setup/howto-obsidian-setup-and-sync.md`](course/setup/howto-obsidian-setup-and-sync.md) |
| Hermes Agent setup                          | [`course/setup/howto-hermes-setup.md`](course/setup/howto-hermes-setup.md)                       |
| What is a **harness**?                      | [`course/concepts/what-is-harness.md`](course/concepts/what-is-harness.md)                             |
| What is **MCP**?                            | [`course/concepts/what-is-mcp.md`](course/concepts/what-is-mcp.md)                                     |
| What is **lint** (LLM Wiki)?                | [`course/concepts/what-is-lint.md`](course/concepts/what-is-lint.md)                                   |
| Wiki standard files                         | [`course/setup/llm-wiki-standard-files.md`](course/setup/llm-wiki-standard-files.md)             |
| Academic AI (Austria)                       | [`course/setup/academic-ai-austria.md`](course/setup/academic-ai-austria.md)                     |
| Drivers / visions / fears / regulation      | [`course/topics/visions-fears-regulation.md`](course/topics/visions-fears-regulation.md)           |
| EU AI Act + Datenschutz                     | [`course/topics/eu-ai-act-and-datenschutz.md`](course/topics/eu-ai-act-and-datenschutz.md)         |
| Creative AI tools survey                    | [`course/topics/ai-tools-creative-processes.md`](course/topics/ai-tools-creative-processes.md)     |
| Local GPU / Apple / DGX hardware            | [`research/local-gpu-hardware-for-llms.md`](research/local-gpu-hardware-for-llms.md) |

---

## Research handouts (optional reading)

| Note                                                   | File                                                                                                 |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Structure / harness vs model quality                   | [`research/structure-vs-model-quality.md`](research/structure-vs-model-quality.md)                   |
| AI bubble, productivity, data centres (finance)        | [`research/ai-bubble-productivity-datacenter.md`](research/ai-bubble-productivity-datacenter.md)     |
| AI jobs — rising tide / Canaries / junior productivity | [`research/ai-jobs-rising-tide-productivity.md`](research/ai-jobs-rising-tide-productivity.md)       |
| Data centres — energy, ecology, US/world economy       | [`research/data-centers-energy-ecology-economy.md`](research/data-centers-energy-ecology-economy.md) |
| Karpathy LLM Wiki                                      | [`research/karpathy-llm-wiki-and-openclaw.md`](research/karpathy-llm-wiki-and-openclaw.md)           |

---

## First steps (students)

1. Star/watch this repo or clone it.
2. Read [`course/START-HERE.md`](course/START-HERE.md).
3. Install **Obsidian**; create a vault in a **phone-syncable** folder.
4. Install **Hermes**; point it at that vault (session 2 lab).
5. Keep secrets (API keys) out of synced notes.

Communication for room changes / announcements: Microsoft Teams (class team) and UFG online as required by the university. **Course content lives here.**

---

## Peer courses (inspiration)

Patterns from theory + practice digital-art / AI seminars (not copies):

- [NYU IMA — Intro to ML for the Arts (GitHub)](https://github.com/ml5js/Intro-ML-Arts-IMA-F25/) — public week schedule + labs
- [HKUST AMCC6500 — Critical AI and Artistic Creation](https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf) — critical weekly themes + studio review
- [HKUST AMCC5170 — Interactive Visual Art with Generative Models](https://amc.hkust.edu.hk/upload/2025-26%20Spring%20Course%20Info/26Spring_AMCC5170_Outline.pdf) — generative tooling → agents → ethics
- [UCLA — Cultural Automation with ML II](https://pkmital.com/home/teaching/ucla-cultural-automation-with-machine-learning-ii/) — theory + generative agents labs
- [SFPC — Handmade Datasets](https://sfpc.study/sessions/summer-26/handmade-datasets) — small cared-for knowledge as practice
- More in [`course/syllabus/timeline.md`](course/syllabus/timeline.md)

---

## Repo policy

- **Public** course materials for enrolled students and peers.
- Private teacher files (student lists, emails, local Cursor skills) are **gitignored** and not published.
- Drafts may change during the semester — check recent commits.

Issues / questions about the materials: use the class Teams channel (or email the instructor).