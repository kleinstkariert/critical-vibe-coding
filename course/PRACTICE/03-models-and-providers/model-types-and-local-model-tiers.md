---
title: Model types and local model tiers
date: 2026-11-25
tags:
  - course
  - models
  - local
  - reference
status: current
canonical: true
---

# Model types and local model tiers

*optional extension.* *not required for assessment.* Any model endpoint meets the [minimum path](../../PROJECT-WORK/01_minimum-path.md).

This page answers one question: which kind of model, and which small local model, for which job? Facts were checked on 25 Nov 2026. Model pages change fast. Read the source page again before you download or pay.

Other pages do other jobs. This page does not repeat them.

- Tools, editors and agents: [vibe-coding tools and agent environments](../../../research/software&DataManagement/vibe-coding-tools-and-agent-environments.md).
- Prices and limits, one row per claim: [dated models, prices, limits and hardware](../../REFERENCES/dated-models-prices-limits-and-hardware.md).
- Install steps, context rules and file sizes: [why this install](../01-harness-and-agents/install-why.md).
- Bigger machines (48 GB and more): [LLM coding capability matrix](../../../research/software&DataManagement/hardware/llm-coding-capability-matrix.md).

How to read the marks:

- *verified fact*: a source page said it on the check date.
- *vendor numbers*: the model maker reported the score. Nobody independent checked it here.
- *not verified*: this course did not read it or did not run it. No model on this page was run by the course on 25 Nov 2026.

## 1. Model types in use now

A model carries several labels at once. The training label says how it was tuned: base, instruction, reasoning. The job label says what it is for: coding, multimodal. The build label says how it is made: dense or mixture of experts (MoE). The place label says where it runs: hosted or small local. One model can have all four. Example: Qwen3.8 27B has reasoning, vision input and a dense build, and it can run locally. Gemma 4 26B A4B is a MoE model.

| Type | What it is | Made for | Watch for |
|---|---|---|---|
| Base | Trained only to predict the next token. It continues text. It does not answer. | Fine-tuning. Text continuation. Code completion inside a line. | A chat app on a base model gives odd output. |
| Instruction (chat) | A base model plus training on instructions and answers. | The default for chat, summaries, extraction and tool calls. | Names differ: `-it` (Gemma), `-Instruct` (Qwen, Meta, Mistral). A name with no suffix is often the instruction model. |
| Reasoning ("thinking") | An instruction model trained to write a chain of thought before the answer. | Multi-step maths, planning, debugging. | Slower. It uses more tokens. It adds little on simple lookups. Hosted APIs can bill the thinking tokens as output. |
| Coding | Tuned on code and on agent work in repositories. | Repository work, tool loops, terminal tasks. | The word "coding" in a name is a vendor label. Test it on your own task. |
| Multimodal | Takes images, and in some models audio or video, as well as text. | Screenshots, documents, interface references. | It needs more memory. Gemma 4: images on all sizes, audio on E2B and E4B only. |
| Mixture of experts (MoE) | Many small expert sub-networks. A router picks a few for each token. | Large knowledge at a lower compute cost per token. | All weights must still fit in memory. Speed follows the active parameters, not the total. Gemma 4 26B A4B: 25.2B total, 3.8B active. |
| Small local | A model small enough for one consumer card or a laptop. Often 2B to 14B parameters, 4-bit. | Privacy, offline work, no bill per token. | Weaker, smaller context, fewer tokens per second than a frontier model. Zed's blog (19 May 2026) says so in plain words. |

Open weights means the files are public. You can download them. A hosted copy is a service: someone else runs the model and sells you access. The `cloud` mark on an Ollama page means Ollama hosts it.

Sources, checked 25 Nov 2026:

- Base, instruction and reasoning types (two explainers): https://sameralqaisi.me/ai-models/foundations/base-instruction-tuned-and-reasoning-models/ and https://inferbase.ai/blog/instruct-vs-thinking-vs-base-models
- MoE ("capacity depends on total parameters, speed depends on active parameters"): https://huggingface.co/blog/moe-transformers, published 26 Feb 2026. Memory rule: https://github.com/guruswami-ai/mlx-benchmarks/blob/main/docs/MODEL_TYPES.md
- Gemma 4 sizes, MoE counts and modalities: https://ollama.com/library/gemma4
- Qwen3.8 reasoning levels and vision: https://lmstudio.ai/models/qwen3.8
- Coding labels: https://ollama.com/library/mimo-v2.6 and https://lmstudio.ai/models (Qwen3-Coder-Next, Flint)
- Small local models are weaker: https://zed.dev/blog/local-ai-in-zed
- The marks `tools`, `thinking`, `vision` and `cloud`: https://ollama.com/search

## 2. Local model tiers: 8, 12, 16 and 24 GB

VRAM is the memory on the graphics card. The Windows test machine for this course has an NVIDIA GeForce RTX 5080 with 16 GB of VRAM. It uses the 16 GB set below. Sizes are download sizes of 4-bit files unless the row says 8-bit. Hermes needs a context of at least 64,000 tokens, and that needs extra VRAM. The sources do not give that number (not verified). The rules and steps are in [why this install](../01-harness-and-agents/install-why.md).

All models below carry the `tools` mark on their Ollama or LM Studio page. This course did not run any of them with Hermes (not verified).

| Tier | Model | Labels | Download | Context |
|---|---|---|---|---|
| 8 GB | Qwen3.5 4B | reasoning, vision | 3.3 GB | 256K |
| 8 GB | Gemma 4 E4B | instruction, reasoning, vision and audio | 6.6 GB (Ollama), 5.9 GB (LM Studio) | 128K |
| 8 GB | Granite 4.1 3B | instruction, text only, no reasoning mark | 2.1 GB | 128K |
| 12 GB | Gemma 4 12B | instruction, reasoning, vision | 8.0 GB (Ollama), 7.4 GB (LM Studio) | 256K |
| 12 GB | Qwen3.5 9B | reasoning, vision, dense | 6.6 GB (Ollama), 7.0 GB (LM Studio) | 256K |
| 12 GB | Granite 4.1 8B | instruction, text only, no reasoning mark | 5.3 GB | 128K |
| 16 GB (5080 set) | Qwen3.5 9B, 8-bit | as above | 10 GB | 256K |
| 16 GB (5080 set) | Gemma 4 12B, 8-bit | as above | 13 GB | 256K |
| 16 GB (5080 set) | MiMo V2.6 9B | coding and agent tuned, reasoning, vision | 6.6 to 8.7 GB | 256K |
| 16 GB (5080 set) | Gemma 4 26B A4B | MoE, reasoning, vision | 15.6 GB (LM Studio), 16 to 19 GB (Ollama) | 256K |
| 24 GB | Qwen3.8 27B | reasoning, vision, dense | 16.1 GB (LM Studio), 16.5 GB (Hermes catalog, 18.5 GB with image and draft files), 18 GB (Ollama) | 256K |
| 24 GB | Gemma 4 31B | dense, reasoning, vision | 19 to 20 GB | 256K |

On 16 GB, the Gemma 4 26B A4B file is about as large as the VRAM. Part of it will sit in system RAM, and the model will slow down. Qwen3.8 27B can be tried on 16 GB too. Its fit label in Hermes may say it uses system RAM (not verified on the 5080).

### 2.1 Pros, cons and apps

The apps column uses these short names: H is Hermes, Z is Zed, O is OpenCode, C is OpenClaw. Each Ollama model page lists `ollama launch` commands for Hermes, OpenCode and OpenClaw (verified on the pages for Gemma 4, Qwen3.5, Qwen3.8, MiMo and Granite 4.1). Zed connects to Ollama and LM Studio in general. None of these combinations was run here (not verified).

| Model | Pros | Cons | Apps |
|---|---|---|---|
| Qwen3.5 4B | Small and quick to download. Long listed context. Reads images. | The weakest in this table for agent work (not verified, no score read). | H, Z, O, C |
| Gemma 4 E4B | Small. Audio and image input. Thinking mode. Native function calling (model card). | Tau2 42.2% (vendor numbers). Tight on 8 GB at 64K context. | H, Z, O, C |
| Granite 4.1 3B and 8B | Very small files. Built for tool use, JSON and RAG (model page). Fill-in-the-middle code completion. | Text only. No reasoning mark. No agent score read (not verified). | H, Z, O, C |
| Gemma 4 12B | Fits 12 GB at 4-bit. 256K context. Reasoning and vision. | No benchmark in the model card (not verified). | H, Z, O, C |
| Qwen3.5 9B | Smaller file than Gemma 4 12B. Reasoning and vision. | Scores in the MiMo table are modest (see 2.2). | H, Z, O, C |
| MiMo V2.6 9B | Tuned for code and agent work (Xiaomi). Beats its Qwen3.5-9B base on Xiaomi's agent tests. | Newer, so less tested by others. Use restrictions in its card. Xiaomi's own numbers. | H, Z, O, C |
| Gemma 4 26B A4B | Only 3.8B active parameters, so it can be quick. Strong Tau2 for its size. | The file is as large as 16 GB of VRAM. Part of it spills to RAM. | H, Z, O, C. In LM Studio too |
| Qwen3.8 27B | The highest coding scores in this table, as reported by Qwen. In the Hermes catalog, so Hermes loads it and sets the context. | The largest download. The 16 GB fit is not verified. | H (catalog, Ollama, LM Studio), Z, O, C |
| Gemma 4 31B | Best Tau2 here. The Hermes Ollama guide calls it reliable for tools. | 19 to 20 GB. It needs a 24 GB card. | H, Z, O, C |

### 2.2 Scores by task

Scores come from the model makers. Different makers use different test setups. Do not compare a Gemma score with a Qwen score as if one lab ran both.

| Model | Chat (MMLU-Pro) | Code | Tool use | Long context | Speed |
|---|---|---|---|---|---|
| Gemma 4 E4B | 69.4% | LiveCodeBench v6 52.0% | Tau2 42.2% | MRCR 128K 25.4% | not verified |
| Gemma 4 12B | not listed | not listed | not listed | 256K listed | not verified |
| Gemma 4 26B A4B | 82.6% | LiveCodeBench v6 77.1% | Tau2 68.2% | MRCR 128K 44.1% | not verified. Active parameters set speed, but the spill to RAM slows it |
| Gemma 4 31B | 85.2% | LiveCodeBench v6 80.0% | Tau2 76.9% | MRCR 128K 66.4% | not verified |
| Qwen3.5 9B (Xiaomi table) | not read | SWE-bench Verified 60.0, SWE-bench Pro 32.0 | Terminal Bench 2.1 27.0, Toolathlon 25.9 | not read | not verified |
| MiMo V2.6 9B (Xiaomi) | not read | SWE-bench Verified 61.1, SWE-bench Pro 44.6 | Terminal Bench 2.1 37.1, Toolathlon 35.2 | not read | not verified |
| Qwen3.8 27B (Qwen) | not read | LiveCodeBench v6 90.3, SWE-bench Pro 61.7 | Terminal Bench 2.1 73.0 | 262K native | not verified |
| Qwen3.5 4B, Granite 4.1 3B and 8B | not read | not read | not read | 256K and 128K listed | not verified |

What the numbers say, in plain words:

- Scores fall with size inside one family. Gemma 4 on Tau2: 76.9% (31B), 68.2% (26B A4B), 42.2% (E4B), 24.5% (E2B).
- Long context is weaker in small models. Gemma 4 MRCR at 128K: 66.4% (31B) and 25.4% (E4B).
- Hermes docs give CPU speeds only: about 10 tokens per second for a 9B model on an 8-core CPU, and 2 to 5 for a 31B model. GPU speeds for these models were not measured here. Hermes recommends a model only when it predicts 20 tokens per second or more.
- Chat is the easiest job for a small model. Agent work is the hardest: many steps, tool calls and a long context.

### 2.3 What the apps need

| App | What it is | Local path | Watch for |
|---|---|---|---|
| Hermes Agent | An agent that edits files and runs commands. MIT licence. | Local Models page (llama.cpp, managed), LM Studio provider, or Ollama as a custom endpoint at `http://localhost:11434/v1` | At least 64,000 tokens of context. Ollama starts at 4,096 on cards below 24 GB. |
| Zed (Zed Agent) | A code editor with its own agent. | Ollama, LM Studio, llama.cpp, or any OpenAI-compatible local server | Zed shows "No tools" when a model has no tool support. Zed sends 4,096 tokens to Ollama by default, so raise `context_window`. External agents in Zed need their own local setup. |
| OpenCode | A terminal coding agent. MIT licence. | Finds Ollama at `http://127.0.0.1:11434` and LM Studio at `http://127.0.0.1:1234/v1` by itself | Models found on a vLLM server start with tools turned off. For Ollama and LM Studio, check the tools mark. Read its provider docs. |
| OpenClaw | A real, current, self-hosted gateway. It links chat apps (WhatsApp, Slack, Telegram and more) to agents. It is not a code editor. | Ollama through the native API, and an LM Studio provider | Do not use the Ollama `/v1` URL. Its docs say that breaks tool calls. Use `http://host:11434`. Licence: not verified. |

Sources, checked 25 Nov 2026:

- Hermes: https://hermes-agent.nousresearch.com/docs/user-guide/local-models and https://hermes-agent.nousresearch.com/docs/integrations/providers
- Zed: https://zed.dev/docs/ai/use-a-local-model and https://zed.dev/docs/ai/agent-panel
- OpenCode: https://opencode.ai/docs/providers
- OpenClaw: https://docs.openclaw.ai/start/openclaw and https://docs.openclaw.ai/providers/ollama
- Benchmarks: https://ollama.com/library/gemma4 (Gemma 4 card), https://lmstudio.ai/models/qwen3.8 (Qwen), https://ollama.com/library/mimo-v2.6 (Xiaomi)
- CPU speeds: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup

## 3. Who builds, pays, sells and profits

The sources do not publish training cost or profit for these models. This table records only what a source states: who builds the model, the licence, the price you pay, who sells hosted access, and which revenue path the sources name. A local run is free of per-token fees. You pay for the graphics card, the power and the disk space.

| Model | Get it | Price | Builder and licence | Hosted access, and who sells it | Revenue path in the sources |
|---|---|---|---|---|---|
| Qwen3.5 (4B, 9B) | [Ollama](https://ollama.com/library/qwen3.5) · [LM Studio](https://lmstudio.ai/models/qwen3.5) | Free, local | Qwen team at Alibaba. Apache 2.0 (LM Studio page) | Not read | Not stated |
| Qwen3.8 27B | [Ollama](https://ollama.com/library/qwen3.8) · [LM Studio](https://lmstudio.ai/models/qwen3.8) · [Hermes catalog](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json) | Free, local | Qwen team at Alibaba. Apache 2.0. The Hermes catalog file comes from the Unsloth GGUF repository `unsloth/Qwen3.8-27B-GGUF` | Not read | Not stated |
| Gemma 4 (E4B, 12B, 26B A4B, 31B) | [Ollama](https://ollama.com/library/gemma4) · [LM Studio](https://lmstudio.ai/models/gemma-4) | Free, local | Google DeepMind. Apache 2.0 (LM Studio page) | Ollama Cloud sells `gemma4` at US $0.14 input and $0.40 output per million tokens. The size is not stated | Ollama's paid cloud plans and pay per token. Google's own income from Gemma: not stated |
| MiMo V2.6 9B | [Ollama](https://ollama.com/library/mimo-v2.6) · [Hugging Face](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B) | Free, local | Xiaomi MiMo. MIT in the card. A fine-tune of Qwen3.5-9B (Apache 2.0). The card lists use restrictions, such as no military use | Ollama Cloud sells other MiMo models (`mimo-v2.6-flash` US $0.14 and $0.28, `mimo-v2.6-pro` US $0.435 and $0.87 per million tokens). Those are not this 9B file | Xiaomi calls the 9B file a start for open research. Its own income path: not stated on the card |
| Granite 4.1 (3B, 8B) | [Ollama](https://ollama.com/library/granite4.1) · [LM Studio](https://lmstudio.ai/models/granite-4.1) | Free, local | IBM Granite team. Apache 2.0. Marked "enterprise-ready" on the Ollama page | Not read | Not stated |

The runtimes and apps are businesses too.

| Product | Who makes it | Price | What is sold | Source |
|---|---|---|---|---|
| Ollama | Ollama | Local use is free and unlimited. Paid plans start at US $20 per month. Pay-as-you-go cloud has no subscription. | Hosted open models, per token or by plan credits. The page says prompts are not logged or trained on. | https://ollama.com/pricing |
| LM Studio | Element Labs, Inc. | The app is free for personal and work use. Bionic+ is US $20 per month. Pro is US $100 per month. | Cloud-hosted models and plans. The app is proprietary. The terms bar resale. | https://lmstudio.ai/pricing · https://lmstudio.ai/blog/free-for-work · https://lmstudio.ai/app-terms |
| Hermes Agent | Nous Research | Free. MIT licence. | The course guides name the Nous Portal as a hosted route. Its price was not rechecked on 25 Nov 2026 (not verified). | [default setup](../01-harness-and-agents/default-setup.md) |
| Zed | Zed Industries | The editor is US $0. Pro is US $10 per month with US $5 of hosted tokens. Hosted use above that is list price plus 10%. | Hosted models and edit predictions. Your own keys and local models are not charged by Zed. | The tools page, read 23 Nov 2026. Not rechecked on 25 Nov 2026 |
| OpenCode | OpenCode | The tool is free. MIT licence. | Not read | The tools page, read 23 Nov 2026 |
| OpenClaw | Not read | Not read | Not read | https://docs.openclaw.ai (not verified) |

## 4. Limits

- Small models make more tool-call mistakes and lose a long task sooner. Zed's blog says to watch them closely, and to edit your last message rather than send a correction.
- A size that fits on disk does not always fit with a 64,000-token context. Check the Hermes fit label or `lms load <model> --context-length 64000 --estimate-only`.
- Benchmark scores come from the makers, on their own setups. Qwen3.8 numbers use the Claude Code harness. Xiaomi compares its fine-tune with its own base model.
- A `tools` mark means the model can emit tool calls. It does not mean it does so well in every app. Zed, OpenCode and OpenClaw each have their own setup notes.
- This course did not run any model here. Speed on the 5080 is not verified.
- Model names and sizes change monthly. The Hermes Ollama guide still names only Gemma 4 31B as reliable for tools. Its list may be older than the Ollama model pages.

## 5. Not verified

- Every model run in Hermes, Zed, OpenCode and OpenClaw.
- Speed in tokens per second on a 16 GB RTX 5080.
- VRAM use at a 64,000-token context.
- Scores for Gemma 4 12B, Qwen3.5 4B, Granite 4.1 3B and 8B.
- Who hosts these exact models and what they charge, except the Ollama Cloud rows above.
- The OpenClaw licence and price.
- Training cost and profit for every model.
