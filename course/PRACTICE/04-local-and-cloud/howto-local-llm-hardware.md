---
title: How-to — Local LLM hardware and software
date: 2026-10-27
tags:
  - course
  - howto
  - local-llm
  - hardware
audience: student
status: current
canonical: true
---

# How-to — Set up your own machine for local LLMs

Student-facing. Deep research tables: [local gpu hardware for llms](../../../research/local-gpu-hardware-for-llms.md). Session: [03 practical install](../../SESSIONS/03-practical-install.md).  
Source types: [references](../../REFERENCES/bibliography.md#source-types). A label names the source kind. It is not independent verification. Labels: *technical suggestion*. **No one must buy hardware for this course.**

*advanced path. Optional extension. Not required for assessment.* Any one agent plus one folder meets [minimum path](../../PROJECT-WORK/minimum-path.md).

---

## 0. Pick a path (5 minutes)

| Your situation | Do this |
|---|---|
| Laptop only, want privacy experiments | Install **Ollama** or Hermes **Local Models** with a **7–8B** quant; accept slow CPU |
| Mac with ≥24 GB unified | Ollama or MLX; aim 8–32B depending on RAM |
| NVIDIA GPU ≥8 GB | Ollama / Hermes Local (CUDA); see https://docs.ollama.com/gpu |
| Want 70B-class without DIY | Consider **Mac Studio** high RAM or **DGX Spark** — research note Path A |
| Building a PC / dual GPU | Research note Paths B–C + tutorials linked there |

---

## 1. Software — three easy stacks

### A. Hermes Desktop — Local Models (*easiest if you already use Hermes*)

1. Settings → Providers → **Local Models** (or onboarding “Run models locally”).  
2. **Install runtime** (managed llama.cpp for your OS/GPU).  
3. Pick a catalog model (Hermes shows fit: green / amber / red).  
4. Download → **Use**.  

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models  

### B. Ollama + Hermes custom endpoint

```bash
# Install: https://ollama.com — then
ollama pull qwen3:8b          # example; pick for your RAM
ollama run qwen3:8b --think=false "ping"
```

Point Hermes at `http://localhost:11434/v1` (custom / Ollama provider).  
Full guide: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup  

**Agent tip:** Raise context (`num_ctx` ≥ 64000). Prefer models with **tool calling**.

### C. Apple MLX / LM Studio

- MLX: https://github.com/ml-explore/mlx · good for Mac Studio  
- LM Studio: GUI download + local OpenAI-compatible server → same Hermes custom URL pattern  

---

## 2. Ready-made hardware (if you buy later)

| System                    | Memory idea                 | Software                                       |
| ------------------------- | --------------------------- | ---------------------------------------------- |
| **Apple** Mac mini/Studio | Unified RAM = model ceiling | Metal / MLX / Ollama                           |
| **NVIDIA DGX Spark**      | 64/128 GB coherent unified  | DGX OS + CUDA; cluster up to 4 via NVIDIA Sync |
| AMD 128 GB mini-PC        | Unified-like capacity       | ROCm/Vulkan — more DIY                         |

Buy for **GB of memory** and **quiet/power**, not FLOPS slides. Details: [local gpu hardware for llms](../../../research/local-gpu-hardware-for-llms.md#2-path-a-ready-made-unified-coherent-memory)

---

## 3. Self-built single GPU

1. Card with enough **VRAM** for your target model (table in research note).  
2. Adequate **PSU**, airflow, NVMe.  
3. Install NVIDIA driver → `nvidia-smi` works → install Ollama or Hermes Local.  
4. Pull a model that **fits** (green in Hermes; or Q4 size ≲ 0.5× VRAM GB as rough start).

---

## 4. Multi-GPU DIY (advanced)

**RAM is not fused.** Software splits layers/tensors across cards.

1. Motherboard with multiple PCIe slots + huge PSU.  
2. `nvidia-smi` · `nvidia-smi topo -m`  
3. Ollama auto-spread **or** llama.cpp `-sm layer` **or** vLLM `--tensor-parallel-size 2`  
4. Tutorials: [local gpu hardware for llms](../../../research/local-gpu-hardware-for-llms.md#4-path-c-diy-multi-gpu-rack-workstation)

NVLink (mostly older 3090 / workstation) helps tensor-parallel serving; **layer split over PCIe** is enough for one-user studio agents.

*Institutional shopping lists and the Spark comparison (teacher only):* the teacher vault. Not required student reading. The public comparison is in [local gpu hardware for llms](../../../research/local-gpu-hardware-for-llms.md#institutional-shopping-lists-teacher-vault-not-public).

---

## 5. Model size vs hardware (cheat sheet)

| Usable GPU/unified memory | Start with |
|---|---|
| 8 GB | 7–8B Q4 |
| 16 GB | 13–14B Q4 |
| 24 GB | 30–34B Q4 |
| 48 GB (e.g. 2×24) | 70B Q4 split |
| 64–128 GB unified | 70B Q4–Q8 comfortable |

Thinking **off** for daily agent work — [Prompting Guide for Critical Vibe Coding](../03-models-and-providers/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md#28-chat-versus-reasoning-models).

---

## 6. Safety / course hygiene

- Do **not** put API keys in synced vault notes.  
- Local ≠ anonymous if the agent still calls web tools.  
- Measure electricity if the box runs 24/7 — ecology session will ask.  
- Prefer **renting** a cloud GPU hour over buying for a one-week experiment.
