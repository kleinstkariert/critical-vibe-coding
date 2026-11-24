---
title: Session 03. Practical install
session: 3
updated: 2026-11-23
audience: student
status: current
canonical: true
---

# Session 03. Practical install: a light Hermes Desktop install, with hardware and prompting as reading

*optional extension. Not required for assessment.* The install is a *demonstration* of one *reference implementation*. Any one agent plus one folder meets [minimum path](../PROJECT-WORK/01_minimum-path.md). The input on closed versus open weights is required. *Locally runnable* is defined in [default setup](../PRACTICE/01-harness-and-agents/default-setup.md) §4.

Parent: [timeline](overview/timeline.md) · Outline: [course outline](overview/course-outline.md) · Rhythm: [course rhythm](overview/course-rhythm.md) · Slides: [03 practical install slides](lectures/03-practical-install-slideshow/03-practical-install.md)

This session was first planned as "Hardware paths, locally runnable models, prompting, chat versus reasoning". The hardware and prompting sections stay in this file as reading and as practice for later. The live class is: check-in, the student input, a break, and then a light install that you can join or skip.

**Buying hardware is optional**: this session teaches *how*, so students can choose later. Prompting and chat versus reasoning are in this file as reading.

**Slot:** 10:00 to 12:00.

## Goals

- Join, if you want to, a light install: Hermes Desktop, one small model or one API key, one wiki folder. **Docker is not part of the baseline.**
- Leave with a personal "fits / does not fit" note for local models
- Map three hardware paths: **ready-made unified** (Apple / DGX Spark) · **single GPU DIY** · **multi-GPU rack** (split ≠ fused RAM)
- Prompting habits for agents: [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md)
- **Chat / instruct versus reasoning**; thinking-off knobs (guide §28)

## Clock

| Clock | Block |
|---|---|
| **10:00 to 10:20** | Check-in (listen only) |
| **10:20 to 10:35** | Student input: **closed versus open weights as power** ([course rhythm](overview/course-rhythm.md)) |
| **10:35 to 10:55** | Bridge: why this install, what is optional, and the safety baseline ([install why](../PRACTICE/01-harness-and-agents/install-why.md)) |
| **10:55 to 11:05** | Break |
| **11:05 to 12:00** | **Optional join-in install**: light Hermes Desktop install, one guide for your system. No Docker. |

If you do not want to install, you can read the hardware section below, write the "fits / does not fit" note, or help a neighbour. The install is not required for assessment.

## Check-in

Listen only: [course rhythm](overview/course-rhythm.md#1-check-in-every-session).

## Student input (theory / humanities): Closed versus open weights as power

Group (about 15 min). Who holds the power when the weights are secret, and who when they are public? Is "open" open if only a few labs can afford to train? Who can afford local privacy? Starting points: [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md) · [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) · Verdegem's commons essay ([bubble economy](../THEORY/01-political-economy/bubble-economy.md) §10). **Not** a GPU shopping list.

## The light install

Follow one guide, from top to bottom. Do not copy the steps into notes. The guides are the single source.

- Windows: [install windows](../PRACTICE/01-harness-and-agents/install-windows.md)
- Linux: [install linux](../PRACTICE/01-harness-and-agents/install-linux.md)
- macOS: [install mac](../PRACTICE/01-harness-and-agents/install-mac.md)

Why this order: [install why](../PRACTICE/01-harness-and-agents/install-why.md). Starter folders and the first `SCHEMA.md`: [starter knowledge base](../PRACTICE/02-knowledge-bases/starter-knowledge-base.md).

What "light" means here:

| Guide section | Light install |
|---|---|
| 1. Install Hermes Desktop | Do |
| 2. Load one local model | Start with a small model (7B to 8B for 8 to 16 GB of VRAM). A 27B model is advanced |
| 3. Connect an OpenAI API key | Do, if the local model is too big or too slow |
| 4. Install Obsidian and the LLM wiki | Do. Hermes points at the `wiki/` folder, not the whole vault |
| 5. Rules and the first `SCHEMA.md` | Do |
| 6. Personal laptop | Do. Read-only first, a disposable folder, manual approvals, one write folder, a snapshot, no private vault |
| 7. Example MCP (vvvv on Windows, TouchDesigner on macOS) | Skip unless time is left. Read the [MCP permissions rule](../PRACTICE/06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary) first |

The first Hermes request reads one small file that you create in a disposable folder named `hermes-smoke-test`. It does not list the vault.

Docker is an advanced workshop, not today's baseline: [howto hermes docker sandbox](../PRACTICE/05-security-and-privacy/howto-hermes-docker-sandbox.md).

## Reading: hardware (formerly teacher input, Part A, about 10 min), *practice*

1. Memory math (Q4 ≈ 0.5 GB per billion parameters): board table from [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md)
2. **Unified memory** (Apple, Spark) versus **VRAM** (GeForce) versus **multi-GPU split** (layer/tensor, not one big VRAM)
3. Open models that make sense for agents (**tool calling** > raw chat), thinking off by default: [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md#28-chat-versus-reasoning-models)
4. Hermes paths: Local Models one-click · Ollama endpoint ([docs](https://hermes-agent.nousresearch.com/docs/user-guide/local-models))

## Reading: prompting and chat versus reasoning (formerly teacher input, Part B, about 10 min), *practice*

- **Prompting guide** (task structure, chat packs → agent briefs, reasoning/thinking, STE80): [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md)
- ICAO prompting skills are retired. Use STE80 and plain English status words (guide §§26 to 27).
- OpenAI Academy: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role
- Agent habits: goals, constraints, file paths, "do not invent", verify; Hermes context: [agents md template](../PRACTICE/01-harness-and-agents/agents-md-template.md)
- **Reasoning versus chat:** default instruct/flash with thinking **off**; escalate for hard multi-step tasks; cheap hybrids with a switch (Qwen3, DeepSeek hybrid, Gemini Flash `thinkingBudget: 0`): [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md#28-chat-versus-reasoning-models)
- **Structure / harness versus model quality:** [structure vs model quality](../../research/software&DataManagement/structure-vs-model-quality.md) · [what is harness](../PRACTICE/01-harness-and-agents/what-is-harness.md) · Session [02 agent harness and wiki architecture](02-agent-harness-and-wiki-architecture.md)
- *Classroom line:* within a usable model tier, invest in wiki + schema + tools before paying for the next model upgrade; treat **thinking** as a token-cost knob, not a status symbol

## Practice for later: hardware tracks (≥45 min)

The live install is the clock above. These tracks are hardware practice for later or for home.

Pick **one** track (pairs OK):

| Track | Do |
|---|---|
| **A: Laptop only** | Install Ollama or Hermes Local; pull ≤8B; one agent smoke test on the vault |
| **B: Has NVIDIA/Apple** | Pull the largest model that still feels interactive; note tokens per second + RAM |
| **C: Paper design** | Spec a dual-GPU or Spark/Mac build from the research note + one tutorial link; no purchase |

Then, on any model: **thinking on versus off** (Ollama `--think=false` or OpenRouter `reasoning.effort: none`), same hard question; note latency, tokens, quality.

Log under `comparisons/local-hardware.md` in the personal vault: path chosen · model · memory · would I buy? why/why not.

Howto: [howto local llm hardware](../PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md)

## Homework

- Finish the software setup at home if class time ran out (flipped: deep DIY reading at home): [install windows](../PRACTICE/01-harness-and-agents/install-windows.md) · [install linux](../PRACTICE/01-harness-and-agents/install-linux.md) · [install mac](../PRACTICE/01-harness-and-agents/install-mac.md)
- Optional: skim one multi-GPU tutorial linked in the research note
- Prepare a short project idea for Session 04 (project presentations and semester plans)

## Materials

| What | Link |
|---|---|
| Install guides | [install windows](../PRACTICE/01-harness-and-agents/install-windows.md) · [install linux](../PRACTICE/01-harness-and-agents/install-linux.md) · [install mac](../PRACTICE/01-harness-and-agents/install-mac.md) · [install why](../PRACTICE/01-harness-and-agents/install-why.md) |
| Starter knowledge base | [starter knowledge base](../PRACTICE/02-knowledge-bases/starter-knowledge-base.md) |
| Session 03 slides | [03 practical install slides](lectures/03-practical-install-slideshow/03-practical-install.md) |
| Dated model and hardware claims | [dated models, prices, limits and hardware](../REFERENCES/dated-models-prices-limits-and-hardware.md) |
| Research (ready-made, DIY, multi-GPU, models) | [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) |
| Dated build options (DIY multi-GPU, DGX Spark class) | [hardware research](../../research/software&DataManagement/hardware/README.md) |
| Student howto | [howto local llm hardware](../PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md) |
| Hermes Local Models | https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Hermes + Ollama | https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup |
| Ollama GPU | https://docs.ollama.com/gpu |
| llama.cpp multi-GPU | https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md |
| Prompting / thinking-off | [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md) |
| Academic AI (not daily local) | [academic ai austria](../PRACTICE/03-models-and-providers/academic-ai-austria.md) |
