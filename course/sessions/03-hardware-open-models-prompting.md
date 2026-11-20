---
title: Session 03. Hardware paths, locally runnable models, prompting, chat versus reasoning
session: 3
updated: 2026-11-10
audience: student
status: current
canonical: true
---

# Session 03. Hardware paths, locally runnable models versus RAM, prompting, chat versus reasoning

*advanced path* for a local model or new hardware. *optional extension. Not required for assessment.* Any one agent plus one folder meets [minimum path](../minimum-path.md). The input on closed versus open weights is required. *Locally runnable* is defined in [default setup](../lectures/01-welcome-landscape-deep-dives/default-setup.md) §4.

Parent: [timeline](../syllabus/timeline.md) · Outline: [course outline](../syllabus/course-outline.md) · Rhythm: [course rhythm](../syllabus/course-rhythm.md)

After the Hermes install in Session 02. **Buying hardware is optional**: this session teaches *how*, so students can choose later. Prompting and chat versus reasoning are in this session.

**Slot:** 10:00 to 12:00.

## Goals

- Map three hardware paths: **ready-made unified** (Apple / DGX Spark) · **single GPU DIY** · **multi-GPU rack** (split ≠ fused RAM)
- Match a **locally runnable model** to memory; leave with a personal "fits / doesn't fit" note
- Prompting habits for agents: [Prompting Guide for Critical Vibe Coding](../setup/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md)
- **Chat / instruct versus reasoning**; thinking-off knobs (guide §28)
- Connect Hermes / Ollama / MLX to whatever students actually own (often: laptop + small model)

## Clock

| Clock | Block |
|---|---|
| **10:00 to 10:20** | Check-in (listen only) |
| **10:20 to 10:35** | Student input: **closed versus open weights as power** ([course rhythm](../syllabus/course-rhythm.md)) |
| **10:35 to 10:55** | Teacher: memory math + hardware paths, then prompting and chat versus reasoning |
| **10:55 to 11:05** | Break |
| **11:05 to 12:00** | Practical tracks A/B/C below, plus one thinking on/off comparison |

## Check-in

Listen only: [course rhythm](../syllabus/course-rhythm.md#1-check-in-every-session).

## Student input (theory / humanities): Closed versus open weights as power

Group (about 15 min). Who holds the power when the weights are secret, and who when they are public? Is "open" open if only a few labs can afford to train? Who can afford local privacy? Starting points: [Prompting Guide for Critical Vibe Coding](../setup/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md) · [local gpu hardware for llms](../../research/local-gpu-hardware-for-llms.md) · Verdegem's commons essay ([bubble economy](../lectures/01-welcome-landscape-deep-dives/bubble-economy.md) §10). **Not** a GPU shopping list.

## Teacher input, Part A: hardware (~10 min), *practice*

1. Memory math (Q4 ≈ 0.5 GB per billion parameters): board table from [local gpu hardware for llms](../../research/local-gpu-hardware-for-llms.md)
2. **Unified memory** (Apple, Spark) versus **VRAM** (GeForce) versus **multi-GPU split** (layer/tensor, not one big VRAM)
3. Open models that make sense for agents (**tool calling** > raw chat), thinking off by default: [Prompting Guide for Critical Vibe Coding](../setup/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md#28-chat-versus-reasoning-models)
4. Hermes paths: Local Models one-click · Ollama endpoint ([docs](https://hermes-agent.nousresearch.com/docs/user-guide/local-models))

## Teacher input, Part B: prompting and chat versus reasoning (~10 min), *practice*

- **Prompting guide** (task structure, chat packs → agent briefs, reasoning/thinking, STE80): [Prompting Guide for Critical Vibe Coding](../setup/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md)
- ICAO prompting skills are retired. Use STE80 and plain English status words (guide §§26 to 27).
- OpenAI Academy: https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role
- Agent habits: goals, constraints, file paths, "do not invent", verify; Hermes context: [agents md template](../setup/agents-md-template.md)
- **Reasoning versus chat:** default instruct/flash with thinking **off**; escalate for hard multi-step tasks; cheap hybrids with a switch (Qwen3, DeepSeek hybrid, Gemini Flash `thinkingBudget: 0`): [Prompting Guide for Critical Vibe Coding](../setup/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md#28-chat-versus-reasoning-models)
- **Structure / harness versus model quality:** [structure vs model quality](../../research/structure-vs-model-quality.md) · [what is harness](../concepts/what-is-harness.md) · Session [02 agent harness and wiki architecture](02-agent-harness-and-wiki-architecture.md)
- *Classroom line:* within a usable model tier, invest in wiki + schema + tools before paying for the next model upgrade; treat **thinking** as a token-cost knob, not a status symbol

## Practical (≥45 min)

Pick **one** track (pairs OK):

| Track | Do |
|---|---|
| **A: Laptop only** | Install Ollama or Hermes Local; pull ≤8B; one agent smoke test on the vault |
| **B: Has NVIDIA/Apple** | Pull the largest model that still feels interactive; note tokens per second + RAM |
| **C: Paper design** | Spec a dual-GPU or Spark/Mac build from the research note + one tutorial link; no purchase |

Then, on any model: **thinking on versus off** (Ollama `--think=false` or OpenRouter `reasoning.effort: none`), same hard question; note latency, tokens, quality.

Log under `comparisons/local-hardware.md` in the personal vault: path chosen · model · memory · would I buy? why/why not.

Howto: [howto local llm hardware](../setup/howto-local-llm-hardware.md)

## Homework

- Finish the software setup at home if class time ran out (flipped: deep DIY reading at home)
- Optional: skim one multi-GPU tutorial linked in the research note
- Prepare a short project idea for Session 04 (project presentations and semester plans)

## Materials

| What | Link |
|---|---|
| Research (ready-made, DIY, multi-GPU, models) | [local gpu hardware for llms](../../research/local-gpu-hardware-for-llms.md) |
| Student howto | [howto local llm hardware](../setup/howto-local-llm-hardware.md) |
| Hermes Local Models | https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Hermes + Ollama | https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup |
| Ollama GPU | https://docs.ollama.com/gpu |
| llama.cpp multi-GPU | https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md |
| Prompting / thinking-off | [Prompting Guide for Critical Vibe Coding](../setup/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md) |
| Academic AI (not daily local) | [academic ai austria](../setup/academic-ai-austria.md) |
