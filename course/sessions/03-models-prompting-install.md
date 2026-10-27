---
title: Session 03 — Models, prompting, install
session: 3
---

# Session 03 — Model landscape, prompting, install agents

Parent: [[../timeline]]

## Goals

- Compare open-source, Chinese, local-GPU, EU-hosted, and academic Austrian AI options (clarity on what students can use)
- Show real practitioner setups (schemes from contacts — *todo*)
- Prompting habits that matter for agents, not only chat — ICAO clearances + tip list with research *why* ([[../prompting-and-model-choice]])
- Chat / instruct vs **reasoning** models; when thinking-on is worth the monologue tokens; thinking-off / effort knobs (OpenRouter, Ollama, Gemini budget 0) — same handout §§4–6
- Evidence: skillset / knowledge base vs. raw model quality
- Get agents installing on student machines (**cloud / API first**; local hardware = session 04)
- Confirm **10 student pairs** + input slots ([[../course-rhythm]])

## Check-in

Listen only — [[../course-rhythm#check-in-every-session]] (morning + AI since last met). Friction/sync can appear in the AI answer.

## Input — systems landscape

Cover, with honest access notes:

- Proprietary cloud (OpenAI, Anthropic, etc.) — choose by strengths: [[../prompting-and-model-choice]] (Azure catalog, Kaggle Game Arena)
- **Reasoning vs chat** — default instruct/flash with thinking **off**; escalate for hard multi-step; cheap hybrids with a switch (Qwen3, DeepSeek hybrid, Gemini Flash `thinkingBudget: 0`) — [[../prompting-and-model-choice#4-chat-llms-vs-reasoning-models]]
- Open weights / Chinese model ecosystems (examples current at teaching time) — good source of toggleable thinking + local 8B class
- Local models **preview only** (~5–10 min) — deep dive next week [[04-local-hardware-and-open-llms]] · [[../../research/local-gpu-hardware-for-llms]] · [[../prompting-and-model-choice#6-cheap--local-lightweight-options]]
- Servers hosting models in Europe
- **Austrian academic AI** — usually **no agent API key**; HPC / AI Factory ≠ daily Hermes backend — [[../academic-ai-austria]] (*say explicitly what students can/cannot use*)
- Privacy / AI Act pointer: [[../eu-ai-act-and-datenschutz]]

## Input — practitioner setups

Introduce 2–4 setup schemes collected from people in the field (diagrams preferred).

*todo before this class:* chase contacts for schemes — see [[../timeline#teacher-todo-setup-schemes--prep]].

## Input — prompting + knowledge vs model

- **Prompting handout** (ICAO tips + chat packs → agent briefs + reasoning/thinking): [[../prompting-and-model-choice]]  
- Hermes ICAO skills: `icao-prompting` · `icao-project-comms` (vault `KnowledgeBaseObsidian/skills/`)  

  OpenAI Academy: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role
- Agent habits: goals, constraints, file paths, “do not invent”, verify
- **Structure / harness vs model quality** — [[../../research/structure-vs-model-quality]] · [[../what-is-harness]] · session [[02-agent-harness-and-wiki-architecture]]
- *Classroom line:* within a usable model tier, invest in wiki + schema + tools before paying for the next model upgrade; treat **thinking** as a Token Cost knob (Tip C), not a status symbol
- Preview standard wiki files: [[../llm-wiki-standard-files]] · lint: [[../what-is-lint]]
- Link: [[../knowledge-store-options]], [[../../research/obsidian-vs-joplin-hermes-llmwiki]], [[../references]]

## Practical

- Install Hermes (or chosen agent) on student machines
- Point agent at Obsidian vault path
- Smoke test: create one note via agent
- Optional: same micro-task on two models (Game Arena / catalog pick) → log in `comparisons/`
- Optional: **thinking on vs off** on one model (Ollama `--think=false` or OpenRouter `reasoning.effort: none`) — same hard question; note latency / tokens / quality

How-to: [[../howto-hermes-setup]] · [[../howto-obsidian-setup-and-sync]]  
Hardware: [[../../research/local-gpu-hardware-for-llms]]  
Academic AI: [[../academic-ai-austria]]  
Student kit (not full vault): [[../student-share-structure]]

## Homework / student inputs

Pair roster and themes: [[../course-rhythm#2-student-inputs-from-session-2]]. Optional extra demos (not instead of the roster): VS Code Copilot/Continue, git for vaults, a local model already running, Discord bridge.

## Materials

| What | Link |
|---|---|
| Prompting + model choice | [[../prompting-and-model-choice]] |
| Academic AI (Austria) | [[../academic-ai-austria]] |
| EU AI Act + Datenschutz | [[../eu-ai-act-and-datenschutz]] |
| Local hardware | [[../../research/local-gpu-hardware-for-llms]] |
| Harness / MCP preview | [[../what-is-harness]] · [[../what-is-mcp]] (session 5) |
| Setup schemes | folder TBD |
