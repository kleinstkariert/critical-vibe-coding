---
title: Why this install
date: 2026-11-25
tags:
  - course
  - howto
  - install
status: current
canonical: true
---

# Why this install

Read this page once. Then follow only your operating-system guide:

- Windows: [install windows](install-windows.md)
- Linux: [install linux](install-linux.md)
- macOS: [install mac](install-mac.md)

Do not copy this page into those guides.

## Your laptop

You install Hermes on your own laptop. Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

The notes stay on your laptop. The phone copy is a separate sync. That path is [howto obsidian setup and sync](../02-knowledge-bases/howto-obsidian-setup-and-sync.md).

## The local model

A local model runs on a computer you control. It is optional. The default for class is a free cloud model ([providers and keys](howto-hermes-providers-and-keys.md)). A local model is a home project: [howto local models](../03-models-and-providers/howto-local-models.md). For model types, task fit, apps and who builds and sells each model, see [model types and local model tiers](../03-models-and-providers/model-types-and-local-model-tiers.md).

Small local models are weaker at agent tasks than cloud models. They make more tool-call mistakes, lose the thread of a long task sooner, and are often slower. *verified fact*, vendor numbers from the Gemma 4 model card, checked 25 Nov 2026: on the Tau2 tool-use test the 31B model scores 76.9%, the 26B A4B model 68.2%, the E4B model 42.2%, and the E2B model 24.5%. No Tau2 number is listed for the 12B model (not verified). Use a small model to learn how the parts fit.

VRAM is the memory on the graphics card. The Windows test machine for this course has an NVIDIA GeForce RTX 5080 with 16 GB of VRAM (Windows 11 Enterprise 25H2). The room demo card, an NVIDIA GeForce RTX 4080 Super, also has 16 GB. 27B means 27 billion parameters.

System memory is the normal RAM in the computer. Offload means Hermes puts part of the model in that RAM. The model can run. It can also be slow.

### What Hermes needs

*verified fact*, Hermes docs checked 25 Nov 2026:

- Hermes needs at least 64,000 tokens of context for agent work with tools. It rejects smaller windows at start.
- Models that Hermes loads itself (the Local Models page) get at least 64K context. Hermes chooses the context and memory placement. Hermes does not offer builds below 4-bit.
- Ollama starts with 4,096 tokens when the card has less than 24 GB of VRAM. Raise it with `OLLAMA_CONTEXT_LENGTH=64000`, then check with `ollama ps`.
- In LM Studio, load with `lms load <model> --context-length 64000`. Add `--estimate-only` to see the memory estimate first.
- If the model prints raw tool text instead of running the tool, the server is usually not set up for tool calls. The model is usually not the cause.

A larger context needs more VRAM. The sources below give file sizes, not the VRAM at 64K context. That number is not verified. *technical suggestion*: choose a file about 70% of your VRAM or smaller, then read the fit label or the estimate.

### Small models that list tool calls

Sizes are download sizes shown on the model pages, checked 25 Nov 2026. "Tools" and "reasoning" are the marks on the Ollama and LM Studio pages. This course did not run these models with Hermes (not verified).

| VRAM tier | Model (ids) | Download | Context | Tools | Reasoning | Trade-offs |
|---|---|---|---|---|---|---|
| 8 GB | Qwen3.5 4B (`qwen3.5:4b`) | 3.3 GB (Ollama), 3.75 GB (LM Studio) | 256K | Yes | Yes | Safe fit. Weak at long tasks |
| 8 GB | Gemma 4 E4B (`gemma4:e4b`, `google/gemma-4-e4b`) | 6.6 GB (Ollama), 5.9 GB (LM Studio) | 128K | Yes | Yes | Tight at 64K context. Tau2 42.2% |
| 8 GB | Granite 4.1 3B (`ibm/granite-4.1-3b`) | 2.1 GB (LM Studio) | not listed | Yes | No mark | Very small. No reasoning mark |
| 12 GB | Gemma 4 12B (`gemma4:12b`, `google/gemma-4-12b`) | 8.0 GB (Ollama), 7.4 GB (LM Studio) | 256K | Yes | Yes | Good first choice. No Tau2 number |
| 12 GB | Qwen3.5 9B (`qwen3.5:9b`, `qwen/qwen3.5-9b`) | 6.6 GB (Ollama), 7.0 GB (LM Studio) | 256K | Yes | Yes | Smaller file than Gemma 4 12B |
| 12 GB | Granite 4.1 8B (`ibm/granite-4.1-8b`) | 5.3 GB (LM Studio) | not listed | Yes | No mark | Tool-call focus. No reasoning mark |
| 16 GB | Qwen3.5 9B, 8-bit (`qwen3.5:9b-q8_0`) | 10 GB (Ollama) | 256K | Yes | Yes | More exact than 4-bit. Less room for context |
| 16 GB | Gemma 4 12B, 8-bit (`gemma4:12b-it-q8_0`) | 13 GB (Ollama) | 256K | Yes | Yes | Tight with a long context |
| 16 GB | MiMo V2.6 9B (`mimo-v2.6:9b`) | 6.6 to 8.7 GB (Ollama) | 256K | Yes | Yes | Made for code and agent work (vendor text). Newer. Less tested |
| 16 GB | Gemma 4 26B A4B (`gemma4:26b`) | 15.6 GB (LM Studio), 16 to 19 GB (Ollama) | 256K | Yes | Yes | Only 3.8B parameters active. File is at the VRAM limit, so it spills. Tau2 68.2% |
| 24 GB | Qwen3.8 27B (Hermes catalog `qwen3.8-27b`) | 16.5 GB, 18.5 GB with image and draft files | 256K | Yes | Yes | Best all-round model in the catalog (vendor text) |
| 24 GB | Gemma 4 31B (`gemma4:31b`) | 19 to 20 GB | 256K | Yes | Yes | The Hermes Ollama guide calls it reliable for tools. Tau2 76.9% |

The Hermes Ollama guide, checked 25 Nov 2026, names only Gemma 4 31B as reliable for tool calls in its own list. That list also holds older models (Gemma 2, Llama 3.2) that have no tool calls. It does not test the small models above. Treat the table as candidates to try, not as a promise.

Ternary and 1-bit builds (for example Bonsai 2) are very small. Hermes offers nothing below 4-bit in its own catalog because quality drops. This course does not recommend them.

### The Hermes catalog

*verified fact*, checked 25 Nov 2026: the catalog file lists five models. It lists no model smaller than 27B. The first entry is **Qwen3.8 27B**, catalog id `qwen3.8-27b`. The catalog text calls it the best all-round agent model. The 4-bit weights file `UD-Q4_K_M` is about 16.5 GB (15.3 GiB). The same entry also downloads an image file and a draft file. Those three files are about 18.5 GB (17.3 GiB) before the context cache. The other four models (Qwen3.6 35B-A3B, Nemotron 3.5 Bolt, Qwen3.8 Flash Next, DeepSeek V4 Flash) need 22 GB or more.

The Hermes docs say a GPU with 8 GB or more runs the small catalog models comfortably, and 16 GB or more runs the 27B to 35B models at high quality. The catalog has no small model, so the first part has nothing to run today. On a 16 GB card the Qwen3.8 27B file is larger than the VRAM, so the fit label can say it uses system RAM. Read the label on the computer you use. This course did not check it on the 5080 (not verified).

For a small model, use one of these:

1. The Find more models box on the Local Models page. It searches Hugging Face and gives a fit check per file. Hermes does not test those models.
2. LM Studio. Hermes lists it as a model provider.
3. Ollama, with a custom endpoint.

The short steps are in [howto local models](../03-models-and-providers/howto-local-models.md). The runtime steps are below.

### Local runtime steps

*technical suggestion*. This order was not run on a real machine for this course (not verified).

LM Studio. Install it from https://lmstudio.ai/download. Search for a model from the table and download it. In a terminal, check the fit, for example `lms load google/gemma-4-12b --context-length 64000 --estimate-only`. If the estimate is more than your VRAM, choose a smaller model. Then load it with `lms load google/gemma-4-12b --context-length 64000` and start the server with `lms server start`. Type `hermes model`, choose LM Studio, press Enter to use `http://localhost:1234/v1`, and pick the model.

Ollama. Hermes needs a 64,000 token context there. Set it before you start the server. Windows PowerShell: `$env:OLLAMA_CONTEXT_LENGTH = 64000`, then `ollama serve`. macOS and Linux: `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`. If the Ollama app already runs in the tray or menu bar, quit it first, or the setting may not apply (not verified). Type `ollama ps` and read the CONTEXT column. In `hermes model`, choose Custom endpoint and use `http://localhost:11434/v1`.

On the first reply, a local model can stay silent for minutes. Hermes sends a large fixed prompt each time. This is expected. If a download is not done after 5 minutes, use a cloud model.

Catalog file: https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

*verified fact* from the course research note: a 27B to 34B model at 4-bit needs about 16 to 20 GB for the weights. Runtime, cache, and context need more. Source: [local gpu hardware for llms](../../../research/software&DataManagement/local-gpu-hardware-for-llms.md).

Tool calling means the model asks Hermes to run a tool. Use a model that lists tools.

Sources, checked 25 Nov 2026:

- Hermes providers (Ollama, LM Studio, 64K context): https://hermes-agent.nousresearch.com/docs/integrations/providers
- Hermes Ollama guide: https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup
- Ollama models with tools: https://ollama.com/search?c=tools
- Ollama pages: https://ollama.com/library/gemma4/tags and https://ollama.com/library/qwen3.5/tags and https://ollama.com/library/mimo-v2.6/tags
- LM Studio pages: https://lmstudio.ai/models/gemma-4 and https://lmstudio.ai/models/qwen3.5 and https://lmstudio.ai/models/granite-4.1
- LM Studio and Hermes: https://lmstudio.ai/docs/integrations/hermes

Free cloud models already chosen for this course are not listed again here. Read [default setup](default-setup.md) §4 and [providers and keys](howto-hermes-providers-and-keys.md).

## The model provider and key

A local model can be too big for a laptop, or too slow for a short task. A cloud model is the fallback that still supports tool calling. No single provider is the course default. The beginner guides use OpenRouter in Desktop Settings. The full table (key pages, cards, `.env`) is in [providers and keys](howto-hermes-providers-and-keys.md). Provider list: https://hermes-agent.nousresearch.com/docs/integrations/providers

## Obsidian and the wiki

Obsidian is the note app. The vault is the folder of notes it opens. An LLM Wiki is that folder with standing orders, an index, and a log, so the agent and you share the same files.

Why this store, and which other stores are allowed: [knowledge store options](../02-knowledge-bases/knowledge-store-options.md). Do not copy that comparison into the install.

Folder jobs and file names: [llm wiki standard files](../02-knowledge-bases/llm-wiki-standard-files.md). The copy-paste tree is [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).

## Rules before extra software

The agent can read files and run commands on a personal laptop. That is the reason for a first `SCHEMA.md`, for approvals, and for keys outside the vault.

The course already wrote those rules. Use them. Do not start a second security essay.

- Course repo rules: [AGENTS.md](../../../AGENTS.md)
- Project copy: [agents md template](agents-md-template.md)
- The safety rules that all install guides share, in one place: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md)
- Short Hermes limits: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md)
- Personal-laptop baseline: read-only inspection, a disposable project, command approvals (the default mode is `smart`; type `hermes config set approvals.mode manual` to be asked every time), a Git or filesystem snapshot before write tasks (Hermes writes files without asking), a narrow work folder as a habit, and no private vault. The steps are in the [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md). On Windows, an Administrators-group account is fine if you use a normal, non-elevated terminal. Hermes needs no elevation on any system.
- Docker is an advanced safety module, not the two-hour baseline: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md)
- Mounts, secrets, and the rule list: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §§9 to 14
- Repair limit and the coding loop: [howto hermes efficient coding](howto-hermes-efficient-coding.md)

## Examples, not requirements

vvvv on Windows, and TouchDesigner on macOS, show one external program and one MCP. An MCP is a connector that lets Hermes talk to another program. Steps: [howto example mcp servers](../06-mcp-and-tools/howto-example-mcp-servers.md).

Read the permissions and capability rule before you add a server: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

Those programs are examples. You can replace them with a program you already use. The connector is optional.

What an MCP is: [what is mcp](../06-mcp-and-tools/what-is-mcp.md).
