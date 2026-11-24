---
title: Dated models, prices, limits and hardware
status: current
canonical: true
---

# Dated models, prices, limits and hardware

Facts on this page change fast. Treat each row as true on its checked date only. Check the source again before you use a number in your own work.

Page created 23 Nov 2026. The rows were copied from the course guides with their original checked dates. They were **not** checked again on 23 Nov 2026.

## How to read the columns

| Column | Meaning |
|---|---|
| Checked | The date the course author or a guide checked the source |
| Source | Where to read the claim yourself |
| Scope | What the claim covers, and what it does not cover |
| Independence | *vendor documentation* (the maker says it), *vendor price page*, *course research note* (a course summary, not independent verification), or *course author's suggestion* |

## Models and catalogs

| Claim | Checked | Source | Scope | Independence |
|---|---|---|---|---|
| The Hermes Local Models catalog has no 7B to 8B model. Do not name a catalog id for that size. | 20 Nov 2026 | [catalog file](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json) | Hermes catalog only. Other runtimes, such as Ollama, list other models | *vendor documentation* |
| The catalog lists Qwen3.8 27B (`qwen3.8-27b`) first and calls it the best all-round agent model. The 4-bit weights file `UD-Q4_K_M` is about 15.3 GB. With the image file and the draft file the download is about 17.3 GB, before the context cache. | 20 Nov 2026 | Same catalog file | Hermes catalog entry. The "best" wording is the vendor's own | *vendor documentation* |
| NVIDIA Nemotron 3 Ultra through OpenRouter (`nvidia/nemotron-3-ultra-550b-a55b:free`) is a free hosted route: $0 per token, tool calling, up to 1 million tokens of context. The limit is 20 requests per minute and 50 per day on a free account. Prompts may be logged. | 10 Nov 2026 | [Hermes guide](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free) · [OpenRouter](https://openrouter.ai) | Free account only. A hosted cloud service, so the data leaves your computer | *vendor documentation* plus *course author's suggestion* |

## Prices and plan limits

| Claim | Checked | Source | Scope | Independence |
|---|---|---|---|---|
| ChatGPT Plus does not include OpenAI API credits. An API key is a separate account with its own billing. | 20 Nov 2026 | [What is ChatGPT Plus](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) | OpenAI plans only | *vendor documentation* |
| `gpt-5.4-mini` costs US $0.75 per million input tokens and US $4.50 per million output tokens. Hermes lists it under the OpenAI API provider. | 20 Nov 2026 | [OpenAI price page](https://developers.openai.com/api/docs/pricing) | One model, list price. Taxes, tiers, batch and cached prices are not covered | *vendor price page* |
| Hermes can log in with a ChatGPT subscription for Codex models. That login is not an API key. The Hermes docs do not say which Plus limits it uses. | 20 Nov 2026 | [Hermes providers](https://hermes-agent.nousresearch.com/docs/integrations/providers) | Hermes docs on that date | *vendor documentation* |

## Hardware and fit

| Claim | Checked | Source | Scope | Independence |
|---|---|---|---|---|
| A 27B to 34B model at 4-bit needs about 16 to 20 GB for the weights. Runtime, cache and context need more. A practical machine is a 24 GB graphics card, or 32 to 48 GB of unified memory. | 27 Oct 2026 (research note update) | [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) | Rule of thumb for weights only. Context length can make a model unusable even when the weights fit | *course research note* |
| The room demo card is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. That card does not prove that a 27B model fits. | 20 Nov 2026 | [install why](../PRACTICE/01-harness-and-agents/install-why.md) | One room machine. Your computer can differ | *course author's suggestion* |
| First local model: 7B to 8B for 8 to 16 GB of VRAM, and 14B to 20B for a 24 GB card. A 27B model only when the fit label says so and you accept system-memory offload. | 20 Nov 2026 | [install why](../PRACTICE/01-harness-and-agents/install-why.md) | A starting suggestion, not a benchmark | *course author's suggestion* |
| Prices and specifications of one DGX Spark class system and four DIY multi-GPU builds, with a model-fit table. Dealer prices are Austrian, with 20% VAT. | 29 Oct 2026 (source note dates, not rechecked on 23 Nov 2026) | [hardware research](../../research/software&DataManagement/hardware/README.md) | Dated research. Parts other than GPU, RAM and the Spark system are estimates with no source. Not a current offer | *course research note*, mixed with *dealer listing* and *community measurement* |
| Street prices for GPUs, Mac Studio and DGX Spark class machines. Prices move weekly. | 27 Oct 2026 | [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) · [howto local llm hardware](../PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md) | Street-price estimates, mid to late 2026. No purchase is required | *course research note* |

## Installers and checksums

| Claim | Checked | Source | Scope | Independence |
|---|---|---|---|---|
| Hermes Desktop is Apple Silicon only. Intel Macs use the command-line script or another machine. | 18 Oct 2026 | [Hermes install docs](https://hermes-agent.nousresearch.com/docs/getting-started/installation) | macOS Desktop package | *vendor documentation* |
| The Hermes install page publishes no checksum for `install.sh` or `install.ps1`. The course does not invent one. | 20 Nov 2026 | [Hermes install docs](https://hermes-agent.nousresearch.com/docs/getting-started/installation) | The two scripts only | *vendor documentation* |
| The scripts' changes to the system, listed per system. | 20 Nov 2026 | [howto hermes setup](../PRACTICE/01-harness-and-agents/howto-hermes-setup.md) §2 (Windows, macOS, Linux) · [install linux](../PRACTICE/01-harness-and-agents/install-linux.md) §1 · [install mac](../PRACTICE/01-harness-and-agents/install-mac.md) §1 | Read from the script text and the install layout on that date | *course author's reading of vendor scripts* |
| The OpenCode install script at `https://opencode.ai/v2/install` publishes no checksum of itself. Release v2.3.2 has a `SHA256SUMS` file for archives, from v2.2.0 on. That file does not check the script. | 20 Nov 2026 | [OpenCode release v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2) | Archives only | *vendor documentation* |
| TDMCP, the official TouchDesigner MCP from Derivative, is in public beta. Its README names the local URL `http://127.0.0.1:13316/mcp`. | 20 Nov 2026 | [install mac](../PRACTICE/01-harness-and-agents/install-mac.md) §7 | One example MCP | *vendor documentation* |

## Where other volatile facts live

These notes keep their own dates. They are not copied here.

- Academic AI access in Austria (research date 21 Oct 2026): [Academic AI in Austria](../PRACTICE/03-models-and-providers/academic-ai-austria.md)
- Install commands and endpoints: [Hermes setup](../PRACTICE/01-harness-and-agents/howto-hermes-setup.md) and [Default setup](../PRACTICE/01-harness-and-agents/default-setup.md)
- Legal timelines: [EU AI Act and Datenschutz](../THEORY/05-privacy-regulation/eu-ai-act-and-datenschutz.md)
- Data centre and investment figures: [Data centres, energy, ecology](../../research/data-centers-energy-ecology-economy.md) and [Economy and the AI bubble](../THEORY/01-political-economy/bubble-economy.md)

## Rule for new rows

Add one row per claim. Give the checked date, a source link, the scope, and the independence label. If you cannot check the source, do not add the row.
