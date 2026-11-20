---
title: Session 03 — Models, prompting, install
session: 3
---

# Session 03 — Model landscape, prompting, install agents

Parent: [[../timeline]] · Rhythm: [[../course-rhythm]]

**Slot:** 10:00–12:00.

## Goals

- Compare open-source, Chinese, local-GPU, EU-hosted, and academic Austrian AI options (clarity on what students can use)
- Prompting habits for agents — [[../../setup/Prompting Guide for Critical Vibe Coding]]
- Chat / instruct vs **reasoning**; thinking-off knobs — guide §28
- Evidence: skillset / knowledge base vs raw model quality
- Get agents installing (**cloud / API first**; local hardware = session 04)

## Clock

| Clock | Block |
|---|---|
| **10:00–10:20** | Check-in (listen only) |
| **10:20–10:35** | Student pair G2 — bias / corpus / taste flattening — [[../course-rhythm]] |
| **10:35–10:55** | Teacher — model landscape + prompting (incl. reasoning knobs) |
| **10:55–11:05** | Break |
| **11:05–12:00** | Install Hermes → vault smoke test |

## Check-in

Listen only — [[../course-rhythm#1-check-in-every-session]].

## Student input (theory / humanities)

Pair G2: bias / whose training data? flattening toward popular voice/style? closed vs open as power — not a model-shopping talk.

## Teacher — systems landscape (*practice*)

Cover, with honest access notes:

- Proprietary cloud (OpenAI, Anthropic, etc.) — choose by strengths: [[../../setup/Prompting Guide for Critical Vibe Coding]] (Azure catalog, Kaggle Game Arena)
- **Reasoning vs chat** — default instruct/flash with thinking **off**; escalate for hard multi-step; cheap hybrids with a switch (Qwen3, DeepSeek hybrid, Gemini Flash `thinkingBudget: 0`) — [[../../setup/Prompting Guide for Critical Vibe Coding#28-chat-versus-reasoning-models]]
- Open weights / Chinese model ecosystems (examples current at teaching time) — good source of toggleable thinking + local 8B class
- Local models **preview only** (~5–10 min) — deep dive next week [[04-local-hardware-and-open-llms]] · [[../../research/local-gpu-hardware-for-llms]] · [[../../setup/howto-local-llm-hardware]]
- Servers hosting models in Europe
- **Austrian academic AI** — usually **no agent API key**; HPC / AI Factory ≠ daily Hermes backend — [[../../setup/academic-ai-austria]] (*say explicitly what students can/cannot use*)
- Privacy / AI Act pointer: [[../../topics/eu-ai-act-and-datenschutz]]

## Teacher — practitioner setups (*if ready*)

Introduce 2–4 setup schemes from the field (diagrams preferred) when available.

## Teacher — prompting + knowledge vs model

- **Prompting guide** (chat packs → agent briefs + reasoning/thinking + STE80): [[../../setup/Prompting Guide for Critical Vibe Coding]]
- ICAO prompting skills are retired. Use STE80 and plain English status words (guide §§26 to 27).

  OpenAI Academy: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role
- Agent habits: goals, constraints, file paths, “do not invent”, verify; Hermes context: [[../../setup/agents-md-template]]
- **Structure / harness vs model quality** — [[../../research/structure-vs-model-quality]] · [[../../concepts/what-is-harness]] · session [[../02-agent-harness-and-wiki-architecture]]
- *Classroom line:* within a usable model tier, invest in wiki + schema + tools before paying for the next model upgrade; treat **thinking** as a Token Cost knob, not a status symbol
- Preview standard wiki files: [[../../setup/llm-wiki-standard-files]] · lint: [[../../concepts/what-is-lint]]
- Link: [[../../setup/knowledge-store-options]], [[../../research/obsidian-vs-joplin-hermes-llmwiki]], [[../../syllabus/references]]

## Practical

- Install Hermes (or chosen agent) on student machines
- Point agent at Obsidian vault path
- Smoke test: create one note via agent
- Optional: same micro-task on two models (Game Arena / catalog pick) → log in `comparisons/`
- Optional: **thinking on vs off** on one model (Ollama `--think=false` or OpenRouter `reasoning.effort: none`) — same hard question; note latency / tokens / quality

How-to: [[../../setup/howto-hermes-setup]] · [[../../setup/howto-obsidian-setup-and-sync]]  
Hardware: [[../../research/local-gpu-hardware-for-llms]]  
Academic AI: [[../../setup/academic-ai-austria]]  
## Homework / student inputs

Pair roster and themes: [[../../syllabus/course-rhythm#2-student-inputs-from-session-2]]. Optional extra demos (not instead of the roster): VS Code Copilot/Continue, git for vaults, a local model already running, Discord bridge.

## Materials

| What | Link |
|---|---|
| Prompting guide | [[../../setup/Prompting Guide for Critical Vibe Coding]] |
| Academic AI (Austria) | [[../../setup/academic-ai-austria]] |
| EU AI Act, and GDPR (separate topics) | [[../../topics/eu-ai-act-and-datenschutz#decision-questions]] |
| Local hardware | [[../../research/local-gpu-hardware-for-llms]] |
| Harness / MCP preview | [[../../concepts/what-is-harness]] · [[../../concepts/what-is-mcp]] (session 5) |
| Setup schemes | folder TBD |
