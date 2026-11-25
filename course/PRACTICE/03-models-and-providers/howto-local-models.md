---
title: How-to. Load one local model
date: 2026-11-25
tags:
  - course
  - howto
  - models
  - local
status: current
canonical: true
---

# How-to. Load one local model (optional)

*optional extension.* *not required for assessment.* The install guides use a free cloud model. A local model runs on your own computer. It needs no key and no card, and nothing leaves your computer. Do this after your first test works, or at home. A download is 2 to 20 GB.

Small models are weaker at agent work than cloud models. They make more tool-call mistakes and lose a long task sooner. Why, and more models: [model types and local model tiers](model-types-and-local-model-tiers.md).

## 1. Find your memory

- Windows: open Task Manager, then the Performance tab, then your GPU. Read "Dedicated GPU memory". This is VRAM.
- Linux with an NVIDIA card: type `nvidia-smi` in a terminal and read the memory line (output not verified for this course).
- Mac: a Mac uses unified memory, shared by the processor and the graphics. macOS and your other apps use part of it. Read the table with your unified memory in place of VRAM, and pick one row lower (*technical suggestion*, not verified).

## 2. Pick a model

Pick a row at or below your memory. Sizes are download sizes from the model pages (checked 25 Nov 2026). Every model has the `tools` mark on its page. This course did not run these models with Hermes (not verified).

| VRAM | Model | Download | Get |
|---|---|---|---|
| 8 GB | Qwen3.5 4B | 3.3 GB | [Ollama](https://ollama.com/library/qwen3.5:4b) · [LM Studio](https://lmstudio.ai/models/qwen3.5) |
| 8 GB | Granite 4.1 3B | 2.1 GB | [Ollama](https://ollama.com/library/granite4.1:3b) · [LM Studio](https://lmstudio.ai/models/granite-4.1) |
| 12 GB | Gemma 4 12B | 8.0 GB | [Ollama](https://ollama.com/library/gemma4:12b) · [LM Studio](https://lmstudio.ai/models/gemma-4) |
| 12 GB | Qwen3.5 9B | 6.6 GB | [Ollama](https://ollama.com/library/qwen3.5:9b) · [LM Studio](https://lmstudio.ai/models/qwen3.5) |
| 16 GB | Gemma 4 12B, 8-bit | 13 GB | [Ollama](https://ollama.com/library/gemma4:12b-it-q8_0) |
| 16 GB | MiMo V2.6 9B | 6.6 to 8.7 GB | [Ollama](https://ollama.com/library/mimo-v2.6:9b) · [Hugging Face](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B) |
| 16 GB | Gemma 4 26B A4B (tight, may use system RAM) | 16 to 19 GB | [Ollama](https://ollama.com/library/gemma4:26b) · [LM Studio](https://lmstudio.ai/models/gemma-4) |
| 24 GB | Qwen3.8 27B | 16.5 GB | [Hermes catalog](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json) · [Ollama](https://ollama.com/library/qwen3.8:27b) · [LM Studio](https://lmstudio.ai/models/qwen3.8) |
| 24 GB | Gemma 4 31B | 19 to 20 GB | [Ollama](https://ollama.com/library/gemma4:31b) · [LM Studio](https://lmstudio.ai/models/gemma-4) |

## 3. Load it in Hermes Desktop

1. Open Settings, then Providers, then Local Models. Click Install runtime. Wait until it finishes. Terminal only (Linux, or an Intel Mac): type `hermes model`, choose Local models, and follow the prompt.
2. Read the fit label on a model row. Click Download only when the label says the model fits. Then click Use.
3. The Hermes catalog lists only Qwen3.8 27B (the 24 GB row). For the other rows, use the Find more models box (it searches Hugging Face and shows a fit check per file), or use LM Studio or Ollama (section 4). Hermes does not test those models.
4. If a download is not done after 5 minutes, stop. Use the free cloud model from your install guide.

Linux note from the Hermes docs: NVIDIA CUDA needs a CUDA 13 driver for the managed runtime. If the runtime refuses the GPU, stop. Do not install a random driver.

## 4. LM Studio or Ollama

*technical suggestion*. This order was not run on a real machine for this course (not verified).

Hermes needs a context of at least 64,000 tokens for tool work. Models that Hermes loads itself get at least 64K. Ollama starts with 4,096 tokens when the card has less than 24 GB of VRAM, so you must raise it. A larger context needs more VRAM. The sources do not give that size (not verified). Choose a file about 70% of your memory or smaller, then check the fit.

LM Studio. Install it from https://lmstudio.ai/download. Search for a model from the table and download it. In a terminal, check the fit, for example `lms load google/gemma-4-12b --context-length 64000 --estimate-only`. If the estimate is more than your memory, choose a smaller model. Then load it with `lms load google/gemma-4-12b --context-length 64000` and start the server with `lms server start`. Type `hermes model`, choose LM Studio, press Enter to use `http://localhost:1234/v1`, and pick the model.

Ollama. Set the context before you start the server. Windows PowerShell: `$env:OLLAMA_CONTEXT_LENGTH = 64000`, then `ollama serve`. macOS and Linux: `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`. If the Ollama app already runs in the tray or menu bar, quit it first, or the setting may not apply (not verified). Type `ollama ps` and read the CONTEXT column. In `hermes model`, choose Custom endpoint and use `http://localhost:11434/v1`.

On the first reply, a local model can stay silent for minutes. Hermes sends a large fixed prompt each time. This is expected. If the model prints raw tool text such as `{"name": ...}`, the server is not set up for tool calls (Hermes docs: usually the server, not the model). Stop and use the cloud model.

## Sources, checked 25 Nov 2026

- Hermes local models: https://hermes-agent.nousresearch.com/docs/user-guide/local-models
- Hermes Ollama guide: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
- Hermes providers (Ollama, LM Studio, 64K context): https://hermes-agent.nousresearch.com/docs/integrations/providers
- LM Studio and Hermes: https://lmstudio.ai/docs/integrations/hermes
- Catalog file: https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json
- Hardware background: [local gpu hardware for llms](../../../research/software&DataManagement/local-gpu-hardware-for-llms.md)
