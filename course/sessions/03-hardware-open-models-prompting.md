---
title: Session 03. Practical install
session: 3
updated: 2026-11-20
---

# Session 03. Practical install

Parent: [[../timeline]] · Outline: [[../course-outline]] · Rhythm: [[../course-rhythm]]

Check-in, the student input below, then the install only. Slides: [[../lectures/03-practical-install-slideshow/03-practical-install]].

**Buying hardware is optional**: this session teaches *how*, so students can choose later. Prompting and chat versus reasoning come from the old Session 03 ([[archive-13-session-plan/03-models-prompting-install]]). Hardware paths and prompting stay in the sections further down. They are reading for later.

**Slot:** 10:00 to 12:00.

## Goals

- Map three hardware paths: **ready-made unified** (Apple / DGX Spark) · **single GPU DIY** · **multi-GPU rack** (split ≠ fused RAM)
- Match **open model size** to memory; leave with a personal "fits / doesn't fit" note
- Prompting habits for agents: [[../setup/Prompting Guide for Critical Vibe Coding]]
- **Chat / instruct versus reasoning**; thinking-off knobs (guide §28)
- Connect Hermes / Ollama / MLX to whatever students actually own (often: laptop + small model)

## Clock

| Clock | Block |
|---|---|
| **10:00 to 10:20** | Check-in (listen only) |
| **10:20 to 10:35** | Student input: **closed versus open weights as power** ([[../course-rhythm]]) |
| **10:35 to 12:00** | Practical install only. Break about 10:55 to 11:05 ([[../course-rhythm]]). |

One guide, from top to bottom. Do not copy the steps into this note.

- Windows: [[../setup/install-windows]]
- Linux: [[../setup/install-linux]]
- macOS: [[../setup/install-mac]]

Why this order: [[../setup/install-why]]. Starter vault and `SCHEMA.md`: [[../setup/starter-knowledge-base]].

## Check-in

Listen only: [[../course-rhythm#1-check-in-every-session]].

## Student input (theory / humanities): Closed versus open weights as power

Group (about 15 min). Who holds the power when the weights are secret, and who when they are public? Is "open" open if only a few labs can afford to train? Who can afford local privacy? Starting points: [[../setup/Prompting Guide for Critical Vibe Coding]] · [[../../research/local-gpu-hardware-for-llms]] · Verdegem's commons essay ([[../lectures/01-welcome-landscape-deep-dives/bubble-economy]] §10). **Not** a GPU shopping list.

## Teacher input, Part A: hardware (~10 min), *practice*

1. Memory math (Q4 ≈ 0.5 GB per billion parameters): board table from [[../../research/local-gpu-hardware-for-llms]]
2. **Unified memory** (Apple, Spark) versus **VRAM** (GeForce) versus **multi-GPU split** (layer/tensor, not one big VRAM)
3. Open models that make sense for agents (**tool calling** > raw chat), thinking off by default: [[../setup/Prompting Guide for Critical Vibe Coding#28-chat-versus-reasoning-models]]
4. Hermes paths: Local Models one-click · Ollama endpoint ([docs](https://hermes-agent.nousresearch.com/docs/user-guide/local-models))

## Teacher input, Part B: prompting and chat versus reasoning (~10 min), *practice*

- **Prompting guide** (task structure, chat packs → agent briefs, reasoning/thinking, STE80): [[../setup/Prompting Guide for Critical Vibe Coding]]
- ICAO prompting skills are retired. Use STE80 and plain English status words (guide §§26 to 27).
- OpenAI Academy: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role
- Agent habits: goals, constraints, file paths, "do not invent", verify; Hermes context: [[../setup/agents-md-template]]
- **Reasoning versus chat:** default instruct/flash with thinking **off**; escalate for hard multi-step tasks; cheap hybrids with a switch (Qwen3, DeepSeek hybrid, Gemini Flash `thinkingBudget: 0`): [[../setup/Prompting Guide for Critical Vibe Coding#28-chat-versus-reasoning-models]]
- **Structure / harness versus model quality:** [[../../research/structure-vs-model-quality]] · [[../concepts/what-is-harness]] · Session [[02-agent-harness-and-wiki-architecture]]
- *Classroom line:* within a usable model tier, invest in wiki + schema + tools before paying for the next model upgrade; treat **thinking** as a token-cost knob, not a status symbol

## Practical (≥45 min)

The live install is the clock above. This block is hardware practice for later.

Pick **one** track (pairs OK):

| Track | Do |
|---|---|
| **A: Laptop only** | Install Ollama or Hermes Local; pull ≤8B; one agent smoke test on the vault |
| **B: Has NVIDIA/Apple** | Pull the largest model that still feels interactive; note tokens per second + RAM |
| **C: Paper design** | Spec a dual-GPU or Spark/Mac build from the research note + one tutorial link; no purchase |

Then, on any model: **thinking on versus off** (Ollama `--think=false` or OpenRouter `reasoning.effort: none`), same hard question; note latency, tokens, quality.

Log under `comparisons/local-hardware.md` in the personal vault: path chosen · model · memory · would I buy? why/why not.

Howto: [[../howto-local-llm-hardware]]

## Homework

- Finish the software setup at home if class time ran out (flipped: deep DIY reading at home): [[../setup/install-windows]] · [[../setup/install-linux]] · [[../setup/install-mac]]
- Optional: skim one multi-GPU tutorial linked in the research note
- Prepare a short project idea for Session 04 (project presentations and semester plans)

## Materials

| What | Link |
|---|---|
| Install guides | [[../setup/install-windows]] · [[../setup/install-linux]] · [[../setup/install-mac]] · [[../setup/install-why]] |
| Starter knowledge base | [[../setup/starter-knowledge-base]] |
| Session 03 slides | [[../lectures/03-practical-install-slideshow/03-practical-install]] |
| Research (ready-made, DIY, multi-GPU, models) | [[../../research/local-gpu-hardware-for-llms]] |
| Student howto | [[../howto-local-llm-hardware]] |
| Hermes Local Models | https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Hermes + Ollama | https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup |
| Ollama GPU | https://docs.ollama.com/gpu |
| llama.cpp multi-GPU | https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md |
| Prompting / thinking-off | [[../setup/Prompting Guide for Critical Vibe Coding]] |
| Academic AI (not daily local) | [[../academic-ai-austria]] |
| Earlier model-landscape session (archived) | [[archive-13-session-plan/03-models-prompting-install]] |
