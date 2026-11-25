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
| The Hermes Local Models catalog has five models. None is smaller than 27B. For a small model, use the Find more models box, LM Studio, or Ollama. | 25 Nov 2026 | [catalog file](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json) | Hermes catalog only. Other runtimes, such as Ollama, list other models | *vendor documentation* |
| The catalog lists Qwen3.8 27B (`qwen3.8-27b`) first and calls it the best all-round agent model. The 4-bit weights file `UD-Q4_K_M` is about 16.5 GB (15.3 GiB). With the image file and the draft file the download is about 18.5 GB (17.3 GiB), before the context cache. | 25 Nov 2026 | Same catalog file | Hermes catalog entry. The "best" wording is the vendor's own | *vendor documentation* |
| Hermes needs at least 64,000 tokens of context for agent work with tools. Ollama starts at 4,096 tokens on a card with less than 24 GB of VRAM, so the user must raise it. In LM Studio, `lms load <model> --context-length 64000 --estimate-only` shows the memory estimate. | 25 Nov 2026 | [Hermes providers](https://hermes-agent.nousresearch.com/docs/integrations/providers) | Hermes docs on that date. The VRAM used at 64K context is not published (not verified) | *vendor documentation* |
| Small models that list tool calls and fit 8 to 16 GB: Qwen3.5 4B (3.3 GB), Gemma 4 E4B (6.6 GB), Gemma 4 12B (8.0 GB), Qwen3.5 9B (6.6 GB), MiMo V2.6 9B (6.6 to 8.7 GB). Download sizes are for 4-bit files on Ollama. The full table is in install why. | 25 Nov 2026 | [Ollama Gemma 4](https://ollama.com/library/gemma4/tags) · [Ollama Qwen3.5](https://ollama.com/library/qwen3.5/tags) · [Ollama MiMo](https://ollama.com/library/mimo-v2.6/tags) · [LM Studio Gemma 4](https://lmstudio.ai/models/gemma-4) | Marks come from the model pages. This course did not run these models with Hermes (not verified) | *vendor documentation* |
| Gemma 4 model card, Tau2 tool-use test: 31B 76.9%, 26B A4B 68.2%, E4B 42.2%, E2B 24.5%. No number for the 12B model. | 25 Nov 2026 | [Ollama Gemma 4](https://ollama.com/library/gemma4) | Vendor numbers for one model family. They show that small models are weaker at tool-use tasks | *vendor documentation* |
| The Hermes Ollama guide names only Gemma 4 31B as reliable for tool calls in its own model list. | 25 Nov 2026 | [Hermes Ollama guide](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup) | The guide may be older than the Ollama model pages | *vendor documentation* |
| NVIDIA Nemotron 3 Ultra through OpenRouter (`nvidia/nemotron-3-ultra-550b-a55b:free`) is a free hosted route: $0 per token, tool calling, up to 1 million tokens of context. The limit is 20 requests per minute and 50 per day on a free account. Prompts may be logged. | 10 Nov 2026 | [Hermes guide](https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free) · [OpenRouter](https://openrouter.ai) | Free account only. A hosted cloud service, so the data leaves your computer | *vendor documentation* plus *course author's suggestion* |

## Prices and plan limits

| Claim | Checked | Source | Scope | Independence |
|---|---|---|---|---|
| ChatGPT Plus does not include OpenAI API credits. An API key is a separate account with its own billing. | 20 Nov 2026 | [What is ChatGPT Plus](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus) | OpenAI plans only | *vendor documentation* |
| OpenAI standard API list prices per million tokens, input and output, short context: `gpt-6-luna` US $0.10 and $0.50. `gpt-6.1-terra` US $1.00 and $5.00. `gpt-6.2-sol` US $2.00 and $10.00. `gpt-6.2-astra` US $8.00 and $40.00. | 25 Nov 2026 | [OpenAI price page](https://developers.openai.com/api/docs/pricing) | Standard tier, short context. Batch, flex, fast, long-context and cached prices differ. Taxes are not covered | *vendor price page* |
| OpenRouter models whose id ends in \:free\ need no credit purchase. Limits: 20 requests a minute and 50 a day. After US \ of credit, 1,000 a day. | 25 Nov 2026 | [OpenRouter limits](https://openrouter.ai/docs/api_reference/limits) | Failed requests count. A negative balance blocks free models | *vendor documentation* |
| Gemini API free tier needs no billing account. Free-tier content can be used to improve Google products. Gemini 3.5 Flash-Lite paid price: US \.30 and \.50 per million tokens. | 25 Nov 2026 | [Gemini billing](https://aistudio.google.com/docs/billing) · [Flash-Lite page](https://aistudio.google.com/docs/models/gemini-3.5-flash-lite) | Free-tier limits change by model | *vendor documentation* |
| Claude API: a key can be created without credit, but requests fail until prepaid credit is bought. Claude Haiku 5.5 costs US \.10 and \.50 per million tokens for prompts up to 100,000 tokens. | 25 Nov 2026 | [Claude billing help](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage) · [Claude pricing](https://platform.claude.com/docs/en/about-claude/pricing) | Longer prompts cost more | *vendor documentation* |
| `gpt-5.4-mini` is still on the price page, in the table of older models: US $0.75 input and $4.50 output per million tokens. The newest family is `gpt-6.x`. Which OpenAI models the Hermes model picker lists on 25 Nov 2026: not verified. | 25 Nov 2026 | [OpenAI price page](https://developers.openai.com/api/docs/pricing) | Older model, list price. Taxes, tiers, batch and cached prices are not covered | *vendor price page* |
| Hermes can log in with a ChatGPT subscription for Codex models. That login is not an API key. The Hermes docs do not say which Plus limits it uses. | 20 Nov 2026 | [Hermes providers](https://hermes-agent.nousresearch.com/docs/integrations/providers) | Hermes docs on that date | *vendor documentation* |

## Hardware and fit

| Claim | Checked | Source | Scope | Independence |
|---|---|---|---|---|
| A 27B to 34B model at 4-bit needs about 16 to 20 GB for the weights. Runtime, cache and context need more. A practical machine is a 24 GB graphics card, or 32 to 48 GB of unified memory. | 27 Oct 2026 (research note update) | [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) | Rule of thumb for weights only. Context length can make a model unusable even when the weights fit | *course research note* |
| The Windows test machine has an NVIDIA GeForce RTX 5080 with 16 GB of VRAM (Windows 11 Enterprise 25H2). The room demo card, an RTX 4080 Super, also has 16 GB. A 16 GB card does not prove that a 27B model fits in VRAM. | 25 Nov 2026 | [install why](../PRACTICE/01-harness-and-agents/install-why.md) | One room machine. Your computer can differ | *course author's suggestion* |
| First local model by VRAM: 8 GB, Qwen3.5 4B or Gemma 4 E4B. 12 GB, Gemma 4 12B or Qwen3.5 9B. 16 GB, a 9B to 12B model at 8-bit, or a 26B to 27B model that may spill into system RAM. 24 GB, Qwen3.8 27B or Gemma 4 31B. Small models are weaker at agent tasks. | 25 Nov 2026 | [install why](../PRACTICE/01-harness-and-agents/install-why.md) | A starting suggestion, not a benchmark | *course author's suggestion* |
| Prices and specifications of one DGX Spark class system and four DIY multi-GPU builds, with a model-fit table. Dealer prices are Austrian, with 20% VAT. | 29 Oct 2026 (source note dates, not rechecked on 23 Nov 2026) | [hardware research](../../research/software&DataManagement/hardware/README.md) | Dated research. Parts other than GPU, RAM and the Spark system are estimates with no source. Not a current offer | *course research note*, mixed with *dealer listing* and *community measurement* |
| Street prices for GPUs, Mac Studio and DGX Spark class machines. Prices move weekly. | 27 Oct 2026 | [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) · [howto local llm hardware](../PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md) | Street-price estimates, mid to late 2026. No purchase is required | *course research note* |

## Installers and checksums

| Claim | Checked | Source | Scope | Independence |
|---|---|---|---|---|
| Hermes Desktop is Apple Silicon only. Intel Macs use the command-line script or another machine. | 18 Oct 2026 | [Hermes install docs](https://hermes-agent.nousresearch.com/docs/getting-started/installation) | macOS Desktop package | *vendor documentation* |
| The Hermes install page publishes no checksum for `install.sh` or `install.ps1`. The course does not invent one. | 20 Nov 2026 | [Hermes install docs](https://hermes-agent.nousresearch.com/docs/getting-started/installation) | The two scripts only | *vendor documentation* |
| The scripts' changes to the system, listed per system. | 20 Nov 2026 | [advanced Hermes config](../PRACTICE/01-harness-and-agents/howto-hermes-advanced-config.md) · [install linux](../PRACTICE/01-harness-and-agents/install-linux.md) §1 · [install mac](../PRACTICE/01-harness-and-agents/install-mac.md) §1 | Read from the script text and the install layout on that date | *course author's reading of vendor scripts* |
| The OpenCode install script at `https://opencode.ai/v2/install` publishes no checksum of itself. Release v2.3.2 has a `SHA256SUMS` file for archives, from v2.2.0 on. That file does not check the script. | 20 Nov 2026 | [OpenCode release v2.3.2](https://github.com/anomalyco/opencode/releases/tag/v2.3.2) | Archives only | *vendor documentation* |
| TDMCP, the official TouchDesigner MCP from Derivative, is in public beta. Its README names the local URL `http://127.0.0.1:13316/mcp`. | 20 Nov 2026 | [howto example mcp servers](../PRACTICE/06-mcp-and-tools/howto-example-mcp-servers.md) | One example MCP | *vendor documentation* |

## Where other volatile facts live

These notes keep their own dates. They are not copied here.

- Academic AI access in Austria (research date 21 Oct 2026): [Academic AI in Austria](../PRACTICE/03-models-and-providers/academic-ai-austria.md)
- Install commands and endpoints: [Windows](../PRACTICE/01-harness-and-agents/install-windows.md) · [macOS](../PRACTICE/01-harness-and-agents/install-mac.md) · [Linux](../PRACTICE/01-harness-and-agents/install-linux.md) · [Default setup](../PRACTICE/01-harness-and-agents/default-setup.md)
- Legal timelines: [EU AI Act and Datenschutz](../THEORY/05-privacy-regulation/eu-ai-act-and-datenschutz.md)
- Data centre and investment figures: [Data centres, energy, ecology](../../research/data-centers-energy-ecology-economy.md) and [Economy and the AI bubble](../THEORY/01-political-economy/bubble-economy.md)

## Rule for new rows

Add one row per claim. Give the checked date, a source link, the scope, and the independence label. If you cannot check the source, do not add the row.
