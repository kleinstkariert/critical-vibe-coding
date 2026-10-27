---
title: Session 04 — Local hardware and open LLMs
session: 4
---

# Session 04 — Local hardware & open downloadable LLMs

Parent: [[../timeline]] · Outline: [[../course-outline]] · Rhythm: [[../course-rhythm]]

After cloud install (session 3). **Buying hardware is optional** — this session teaches *how* so students can choose later; ecology (session 11) asks *whether*.

## Goals

- Map three hardware paths: **ready-made unified** (Apple / DGX Spark) · **single GPU DIY** · **multi-GPU rack** (split ≠ fused RAM)
- Match **open model size** to memory; leave with a personal “fits / doesn’t fit” note
- Connect Hermes / Ollama / MLX to whatever they actually own (often: laptop + small model)

## Class rhythm (*requirement*)

1. **Check-in** (listen only) — [[../course-rhythm#check-in-every-session]]  
2. **Student input** (~15 min) — Group assigned to this theme (hardware or model-scaling)  
3. Teacher framing (~20 min)  
4. **Technical** (≥45 min)

## Teacher input (~20 min)

1. Memory math (Q4 ≈ 0.5 GB/B params) — board table from [[../../research/local-gpu-hardware-for-llms]]  
2. **Unified memory** (Apple, Spark) vs **VRAM** (GeForce) vs **multi-GPU split** (layer/tensor — not one big VRAM)  
3. Open models that make sense for agents (**tool-calling** > raw chat) + thinking off by default — [[../prompting-and-model-choice]]  
4. Hermes paths: Local Models one-click · Ollama endpoint — [docs](https://hermes-agent.nousresearch.com/docs/user-guide/local-models)

## Practical (≥45 min)

Pick **one** track (pairs OK):

| Track | Do |
|---|---|
| **A — Laptop only** | Install Ollama or Hermes Local; pull ≤8B; one agent smoke test on vault |
| **B — Has NVIDIA/Apple** | Pull largest model that still feels interactive; note tok/s + RAM |
| **C — Paper design** | Spec a dual-GPU or Spark/Mac build from the research note + one tutorial link; no purchase |

Log under `comparisons/local-hardware.md` in personal vault: path chosen · model · memory · would I buy? why/why not.

Howto: [[../howto-local-llm-hardware]]

## Homework

- Finish software setup at home if class time ran out (flipped: deep DIY reading at home)  
- Optional: skim one multi-GPU tutorial linked in the research note  
- Prep: wiki personalisation next week (session 05)

## Materials

| What | Link |
|---|---|
| Research (ready-made, DIY, multi-GPU, models) | [[../../research/local-gpu-hardware-for-llms]] |
| Student howto | [[../howto-local-llm-hardware]] |
| Hermes Local Models | https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Hermes + Ollama | https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup |
| Ollama GPU | https://docs.ollama.com/gpu |
| llama.cpp multi-GPU | https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md |
| Prompting / thinking-off | [[../prompting-and-model-choice]] |
| Academic AI (not daily local) | [[../academic-ai-austria]] |
