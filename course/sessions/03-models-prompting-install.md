---
title: Session 03 — Models, prompting, install
session: 3
---

# Session 03 — Model landscape, prompting, install agents

Parent: [[../timeline]]

## Goals

- Compare open-source, Chinese, local-GPU, EU-hosted, and academic Austrian AI options (clarity on what students can use)
- Show real practitioner setups (schemes from contacts — *todo*)
- Prompting habits that matter for agents, not only chat
- Evidence: skillset / knowledge base vs. raw model quality
- Get agents installing on student machines
- Assign student presentation topics for later sessions

## Check-in

Short round: install friction? first vault sync? anything from last week’s outdoor conversation that stuck?

## Input — systems landscape

Cover, with honest access notes:

- Proprietary cloud (OpenAI, Anthropic, etc.) — choose by strengths: [[../prompting-and-model-choice]] (Azure catalog, Kaggle Game Arena)
- Open weights / Chinese model ecosystems (examples current at teaching time)
- Local models on own GPU / unified-memory machines (Apple, DGX Spark, self-build) — [[../../research/local-gpu-hardware-for-llms]] (*technical suggestion:* ~10 min; no one must buy hardware)
- Servers hosting models in Europe
- **Austrian academic AI** — usually **no agent API key**; HPC / AI Factory ≠ daily Hermes backend — [[../academic-ai-austria]] (*say explicitly what students can/cannot use*)
- Privacy / AI Act pointer: [[../eu-ai-act-and-datenschutz]]

## Input — practitioner setups

Introduce 2–4 setup schemes collected from people in the field (diagrams preferred).

*todo before this class:* chase contacts for schemes — see [[../timeline#teacher-todo-setup-schemes--prep]].

## Input — prompting + knowledge vs model

- **Prompting handout** (chat packs → agent briefs): [[../prompting-and-model-choice]]  
  OpenAI Academy: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role
- Agent habits: goals, constraints, file paths, “do not invent”, verify
- **Structure / harness vs model quality** — [[../../research/structure-vs-model-quality]] · [[../what-is-harness]] · session [[02-agent-harness-and-wiki-architecture]]
- *Classroom line:* within a usable model tier, invest in wiki + schema + tools before paying for the next model upgrade
- Preview standard wiki files: [[../llm-wiki-standard-files]] · lint: [[../what-is-lint]]
- Link: [[../knowledge-store-options]], [[../../research/obsidian-vs-joplin-hermes-llmwiki]], [[../references]]

## Practical

- Install Hermes (or chosen agent) on student machines
- Point agent at Obsidian vault path
- Smoke test: create one note via agent
- Optional: same micro-task on two models (Game Arena / catalog pick) → log in `comparisons/`

How-to: [[../howto-hermes-setup]] · [[../howto-obsidian-setup-and-sync]]  
Hardware: [[../../research/local-gpu-hardware-for-llms]]  
Academic AI: [[../academic-ai-austria]]  
Student kit (not full vault): [[../student-share-structure]]

## Homework / student inputs

Ask students to prepare a short input for a later class. Topics depend on who is in the room, e.g.:

- Open Claude / Copilot / Continue in VS Code
- Git basics for a vault or project
- A local model they already run
- A creative tool + AI workflow they already use
- Discord bot bridging (if someone knows it)

## Materials

| What | Link |
|---|---|
| Prompting + model choice | [[../prompting-and-model-choice]] |
| Academic AI (Austria) | [[../academic-ai-austria]] |
| EU AI Act + Datenschutz | [[../eu-ai-act-and-datenschutz]] |
| Local hardware | [[../../research/local-gpu-hardware-for-llms]] |
| Harness / MCP preview | [[../what-is-harness]] · [[../what-is-mcp]] (session 5) |
| Setup schemes | folder TBD |
