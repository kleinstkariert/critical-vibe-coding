---
title: Why this install
date: 2026-11-20
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

A local model runs on a computer you control.

VRAM is the memory on the graphics card. The room demo card is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. That card does not prove that a 27B model fits in 16 GB. 27B means 27 billion parameters.

*technical suggestion* for the first local experiment:

- 8 to 16 GB of VRAM: a 7B to 8B model
- A 24 GB card: a 14B to 20B model
- A 27B model only when the fit label confirms it, and only when you accept system-memory offload

System memory is the normal RAM in the computer. Offload means Hermes puts part of the model in that RAM. The model can run. It can also be slow.

A long context is a long chat plus the files the agent sends. A long context can make a model unusable even when the weights fit.

*verified fact* from the course research note: a 27B to 34B model at 4-bit needs about 16 to 20 GB for the weights. Runtime, cache, and context need more. A practical machine for that class is a 24 GB graphics card, or 32 to 48 GB of unified memory. Source: [local gpu hardware for llms](../../../research/software&DataManagement/local-gpu-hardware-for-llms.md).

The Hermes catalog checked on 20 Nov 2026 has no 7B to 8B model. This course does not name a catalog id for that size.

1. In Hermes Desktop, open Settings.
2. Open Providers.
3. Open Local Models.
4. Read the row names on that screen.

The same list is the catalog file: https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

Tool calling means the model asks Hermes to run a tool. Download a row only when its text says agent or tool calling.

### Advanced model

*verified fact*, checked 20 Nov 2026: the catalog lists **Qwen3.8 27B** first. The catalog id is `qwen3.8-27b`. The catalog text calls it the best all-round agent model. The 4-bit weights file `UD-Q4_K_M` is about 15.3 GB. The same entry also downloads an image file and a draft file. Those three files are about 17.3 GB before the context cache.

This model is advanced. It is not the first download. Use it only when the fit label says it fits, or when the label says it uses system RAM and you accept the slowdown.

Hermes does not offer a copy of this model smaller than 4-bit. If the label says the model is too big, use the API model in your operating-system guide.

Your computer may have less than 16 GB of VRAM. Read the fit label on the computer you are using.

Free cloud models already chosen for this course are not listed again here. Read [default setup](default-setup.md) §4 and [howto hermes setup](howto-hermes-setup.md) §3.

## The API key

A local model can be too big for a laptop, or too slow for a short task. An API model is the fallback that still supports tool calling.

ChatGPT Plus does not include OpenAI API credits. Create an OpenAI API key and select a small model. Details and the model name are in your operating-system guide. Provider page: https://hermes-agent.nousresearch.com/docs/integrations/providers

## Obsidian and the wiki

Obsidian is the note app. The vault is the folder of notes it opens. An LLM Wiki is that folder with standing orders, an index, and a log, so the agent and you share the same files.

Why this store, and which other stores are allowed: [knowledge store options](../02-knowledge-bases/knowledge-store-options.md). Do not copy that comparison into the install.

Folder jobs and file names: [llm wiki standard files](../02-knowledge-bases/llm-wiki-standard-files.md). The copy-paste tree is [starter knowledge base](../02-knowledge-bases/starter-knowledge-base.md).

## Rules before extra software

The agent can read files and run commands on a personal laptop. That is the reason for a first `SCHEMA.md`, for approvals, and for keys outside the vault.

The course already wrote those rules. Use them. Do not start a second security essay.

- Course repo rules: [AGENTS.md](../../../AGENTS.md)
- Project copy: [agents md template](agents-md-template.md)
- Short Hermes limits: [howto hermes setup](howto-hermes-setup.md) §5d
- Personal-laptop baseline: read-only inspection, a disposable project, manual approvals, one narrow write folder, a Git or filesystem snapshot, and no private vault. The steps are in your operating-system guide, section 6.
- Docker is an advanced safety module. Use it as a demonstration or in a separate workshop: [howto hermes docker sandbox](../05-security-and-privacy/howto-hermes-docker-sandbox.md). Docker adds filesystem sharing, path translation, ownership, network, performance, GPU access, images, and Windows/macOS virtualisation, so it is not the two-hour baseline.
- Mounts, secrets, and the rule list: [Local LLM Coding with Hermes](../08-verification-and-provenance/local-llm-coding-with-hermes.md) §§9 to 14
- Repair limit and the coding loop: [howto hermes efficient coding](howto-hermes-efficient-coding.md)

## Examples, not requirements

vvvv on Windows, and TouchDesigner on macOS, show one external program and one MCP. An MCP is a connector that lets Hermes talk to another program.

Read the permissions and capability rule before you add a server: [what is mcp](../06-mcp-and-tools/what-is-mcp.md#permissions-and-capability-boundary).

Those programs are examples. You can replace them with a program you already use. Linux has no MCP example in its guide for the same reason: the connector is optional.

What an MCP is: [what is mcp](../06-mcp-and-tools/what-is-mcp.md).
