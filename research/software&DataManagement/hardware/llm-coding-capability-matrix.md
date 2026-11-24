---
title: LLM coding capability matrix, model fit on DIY setups and a Spark class system
status: current
canonical: true
date: 2026-10-29
updated: 2026-11-23
last_verified: 2026-10-29
price_status: not a price page. Model names and sizes dated 2026-10-29, not rechecked on 2026-11-23
tags:
  - research
  - hardware
  - models
  - dated-specs
---

# Model fit: DIY setups and a Spark class system

Dated research. Model names and quantisation sizes age quickly. Verify them on Hugging Face at purchase time. The sizes below have no per-row source recorded (*estimate, no source recorded*). Shared labels and assumptions are in the [hardware README](README.md).

Memory for the DIY setups is split, not fused. See [shared technical notes](README.md#shared-technical-notes-for-the-diy-builds). The setups are [A, 48 GB](setup-a-dual-3090-open-frame.md), [C, 72 GB](setup-c-triple-3090-open-frame.md) and the [Spark class system, 128 GB](spark-gb10-recommended-system.md).

| Model | Approximate need | Setup A: 48 GB | Setup C: 72 GB | Spark: 128 GB |
|---|---:|---|---|---|
| Qwen3.6 27B | ~17 GB Q4 | Excellent; one GPU | Excellent | Excellent |
| GLM-4.7-Flash 30B-A3B | ~18 GB Q4 | Excellent | Excellent | Excellent |
| Devstral Small 2 24B | ~15 GB | Excellent | Excellent | Excellent |
| gpt-oss-20b | ~14–16 GB | Excellent | Excellent | Excellent |
| Qwen3-Coder-Next 80B-A3B | ~46 GB Q4 plus context | Tight, short context | Good | Good |
| Llama 3.3 70B Q4 | ~40 GB weights plus KV | Yes, short or moderate context | Good | Good |
| gpt-oss-120b | ~59–65 GB | No | Yes | Yes |
| Devstral 2 123B | ~75 GB | No | No | Yes |

## Long context on a 48 GB system

Llama-3.3-70B Q4_K_M is about 39.6 GiB in weights. It is approximately 43 GiB at 8k context and about 50 GiB at 32k context with an f16 KV cache. On a 48 GB system, shorten the context or quantise the KV cache.

## Reasoning settings

"Thinking off" applies only to models that support it. gpt-oss uses reasoning-effort levels. Qwen3-Coder-Next is non-thinking.

## Efficiency

The capacity, power and "best at" comparison of the three systems is in the [README](README.md#efficiency-only-conclusion).

## Software references

- [llama.cpp multi-GPU documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md)
- [vLLM parallelism and scaling](https://docs.vllm.ai/en/stable/serving/parallelism_scaling/)
- [Ollama GPU documentation](https://docs.ollama.com/gpu)

These are vendor and project documentation (*primary evidence* for what the software does). Their text changes. No check date is recorded.
