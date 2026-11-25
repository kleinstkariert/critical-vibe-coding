---
title: How-to. Load one local model
date: 2026-11-25
tags:
  - course
  - howto
  - models
  - local
audience: student
status: current
canonical: true
last_verified: 2026-11-25
---

# How-to. Load one local model (optional)

*optional extension.* *not required for assessment.* The install guides use a free cloud model. A local model runs on your own computer. It needs no key and no card, and nothing leaves your computer after download. Do this after your first chat works, or at home. A download is about 2 to 20 GB.

Primary path: **Hermes Desktop → Settings → Providers → Local Models** (official docs, checked 25 Nov 2026). Ollama and LM Studio are alternates. CLI is advanced.

Small models are weaker at agent work than large cloud models. They make more tool-call mistakes and lose a long task sooner. Why, and more models: [model types and local model tiers](model-types-and-local-model-tiers.md). Free cloud comparison: [free cloud models for class](free-cloud-models-for-class.md).

## 1. Find your memory

- Windows: open Task Manager, then the Performance tab, then your GPU. Read "Dedicated GPU memory". This is VRAM.
- Linux with an NVIDIA card: type `nvidia-smi` in a terminal and read the memory line (output not verified for this course).
- Mac: a Mac uses unified memory, shared by the processor and the graphics. macOS and your other apps use part of it. Read the table with your unified memory in place of VRAM, and pick one row lower (*technical suggestion*, not verified).

## 2. Pick a model size

Pick a row at or below your memory. Sizes are download sizes from model pages (checked 25 Nov 2026). Hermes Desktop shows a **fit label** (green / amber / red) before you download. Prefer that label over this table when they disagree.

| VRAM (guide) | Example size | Notes |
|---|---|---|
| 8 GB | about 2 to 4B | Small agent trials only |
| 12 GB | about 9 to 12B | Better tools than 4B |
| 16 GB | about 12 to 26B | Still tight for large MoE |
| 24 GB | about 27B catalog row | Hermes catalog lists Qwen3.8 27B for this class of machine |

Full Ollama / LM Studio id table (alternate path): see section 4.

## 3. Primary: Hermes Desktop Local Models

Official docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models (checked 25 Nov 2026).

Menu path (verified in docs): **Settings → Providers → Local Models**. Onboarding can also say **Run models locally** (exact onboarding wording: not verified on a class machine).

1. Open Hermes Desktop.
2. Open **Settings**, then **Providers**, then **Local Models**.
3. Click **Install runtime**. Wait until it finishes. Hermes downloads a pinned llama.cpp build for your hardware.
4. Pick a catalog model. Read the fit label. Click **Download** only when the label says the model fits (green), or when you accept amber (uses system RAM, slower).
5. Click **Use**. New chats run on that local model.
6. Optional: **Find more models** searches Hugging Face with a per-file fit check. Community models have no Hermes "validated" badge.
7. Optional: **Add model file** links a `.gguf` you already have on disk.

Pause and Resume work on engine and model downloads (docs). If a download is not done after 5 minutes and you need class time, stop. Use a free cloud model from [free cloud models for class](free-cloud-models-for-class.md).

Linux note from the Hermes docs: NVIDIA CUDA needs a CUDA 13 driver for the managed runtime. If the runtime refuses the GPU, stop. Do not install a random driver.

### Advanced: same flow in the terminal

Type `hermes model`, choose **Local models**, and follow the prompt. Ctrl+C pauses a download; choose the model again to resume. Use this when Desktop is not available (some Linux or Intel Mac setups).

## 4. Alternates: LM Studio or Ollama

Use these only when you want a server Hermes did not manage, or when Local Models is not available.

*technical suggestion*. This alternate order was not run on a real machine for this course (not verified).

Hermes needs a context of at least 64,000 tokens for tool work. Models that Hermes Local Models loads get at least 64K. Ollama starts with 4,096 tokens when the card has less than 24 GB of VRAM, so you must raise it. A larger context needs more VRAM. Choose a file about 70% of your memory or smaller, then check the fit.

Example ids (checked 25 Nov 2026; Hermes did not test these with tools):

| VRAM | Model | Get |
|---|---|---|
| 8 GB | Qwen3.5 4B | [Ollama](https://ollama.com/library/qwen3.5:4b) · [LM Studio](https://lmstudio.ai/models/qwen3.5) |
| 8 GB | Granite 4.1 3B | [Ollama](https://ollama.com/library/granite4.1:3b) · [LM Studio](https://lmstudio.ai/models/granite-4.1) |
| 12 GB | Gemma 4 12B | [Ollama](https://ollama.com/library/gemma4:12b) · [LM Studio](https://lmstudio.ai/models/gemma-4) |
| 12 GB | Qwen3.5 9B | [Ollama](https://ollama.com/library/qwen3.5:9b) · [LM Studio](https://lmstudio.ai/models/qwen3.5) |
| 16 GB | Gemma 4 12B, 8-bit | [Ollama](https://ollama.com/library/gemma4:12b-it-q8_0) |
| 16 GB | MiMo V2.6 9B | [Ollama](https://ollama.com/library/mimo-v2.6:9b) · [Hugging Face](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B) |
| 24 GB | Qwen3.8 27B | [Hermes catalog](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json) · [Ollama](https://ollama.com/library/qwen3.8:27b) · [LM Studio](https://lmstudio.ai/models/qwen3.8) |

**LM Studio.** Install from https://lmstudio.ai/download. Search, download, then estimate fit, for example `lms load google/gemma-4-12b --context-length 64000 --estimate-only`. Load with `--context-length 64000`, then `lms server start`. In Hermes: Desktop model picker or `hermes model` → LM Studio → `http://localhost:1234/v1` (Desktop custom-endpoint labels: not verified).

**Ollama.** Set context before the server starts. Windows PowerShell: `$env:OLLAMA_CONTEXT_LENGTH = 64000`, then `ollama serve`. macOS and Linux: `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`. Quit the tray app first if it already runs (not verified). Check `ollama ps` CONTEXT. In Hermes: Custom endpoint `http://localhost:11434/v1` (Desktop path: not verified; CLI: `hermes model`).

On the first reply, a local model can stay silent for minutes. Hermes sends a large fixed prompt each time. This is expected. If the model prints raw tool text such as `{"name": ...}`, the server is not set up for tool calls (Hermes docs: usually the server, not the model). Stop and use a cloud model.

## Sources, checked 25 Nov 2026

- Hermes local models (Desktop Local Models UI): https://hermes-agent.nousresearch.com/docs/user-guide/local-models
- Hermes Ollama guide: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
- Hermes providers (Ollama, LM Studio, 64K context): https://hermes-agent.nousresearch.com/docs/integrations/providers
- LM Studio and Hermes: https://lmstudio.ai/docs/integrations/hermes
- Catalog file: https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json
- Free cloud comparison: [free cloud models for class](free-cloud-models-for-class.md)
- Hardware background: [local gpu hardware for llms](../../../research/software&DataManagement/local-gpu-hardware-for-llms.md)
