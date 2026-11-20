---
title: Why this install
date: 2026-11-20
tags:
  - course
  - howto
  - install
---

# Why this install

Read this page once. Then follow only your operating-system guide:

- Windows: [[install-windows]]
- Linux: [[install-linux]]
- macOS: [[install-mac]]

Do not copy this page into those guides.

## Your laptop

You install Hermes on your own laptop. Hermes Agent is the program that uses a model to read files and call tools. Hermes Desktop is the app window for that program.

The notes stay on your laptop. The phone copy is a separate sync. That path is [[howto-obsidian-setup-and-sync]].

## The local model

A local model runs on a computer you control. One reference GPU for the model below is an NVIDIA GeForce RTX 4080 Super with 16 GB of VRAM. VRAM is the memory on the graphics card.

*technical suggestion*, checked 20 Nov 2026 against the Hermes local catalog: use **Qwen3.8 27B**, catalog id `qwen3.8-27b`.

Why this one:

- Hermes lists it first in the local catalog. The catalog text calls it the best all-round agent model. Source: the catalog file in [Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/hermes_cli/local_runtime/catalog.json).
- Hermes agent work needs tool calling. Tool calling means the model asks the harness to run a tool, in a fixed format. This catalog entry is the agent model Hermes ships for that job. Docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models
- The weights file in that catalog entry is the 4-bit build `UD-Q4_K_M`, about 15.3 GB. Hermes docs say a GPU with 16 GB or more runs the 27 to 35 billion parameter catalog models at high quality. 27B means 27 billion parameters.
- The same entry also downloads an image file and a draft file. Those files, plus the context cache, can be larger than 16 GB together. Hermes may place the overflow in normal computer memory. The fit label in the app tells you which case you have.
- Hermes does not offer a copy smaller than 4-bit. If the label says the model is too big, do not hunt for a smaller file. Use the API model in your operating-system guide.

Your computer may have less than 16 GB of VRAM. Read the fit label on the computer you are using.

Free cloud models already chosen for this course are not listed again here. Read [[../lectures/01-welcome-landscape-deep-dives/default-setup]] §4 and [[howto-hermes-setup]] §3.

## The API key

A local model can be too big for a laptop, or too slow for a short task. An API model is the fallback that still supports tool calling.

ChatGPT Plus does not include OpenAI API credits. Create an OpenAI API key and select a small model. Details and the model name are in your operating-system guide. Provider page: https://hermes-agent.nousresearch.com/docs/integrations/providers

## Obsidian and the wiki

Obsidian is the note app. The vault is the folder of notes it opens. An LLM Wiki is that folder with standing orders, an index, and a log, so the agent and you share the same files.

Why this store, and which other stores are allowed: [[knowledge-store-options]]. Do not copy that comparison into the install.

Folder jobs and file names: [[llm-wiki-standard-files]]. The copy-paste tree is [[starter-knowledge-base]].

## Rules before extra software

The agent can read files and run commands on a personal laptop. That is the reason for a first `SCHEMA.md`, for approvals, and for keys outside the vault.

The course already wrote those rules. Use them. Do not start a second security essay.

- Course repo rules: [AGENTS.md](../../AGENTS.md)
- Project copy: [[agents-md-template]]
- Short Hermes limits: [[howto-hermes-setup]] §5d
- Personal-laptop sandbox and approvals: [[howto-hermes-docker-sandbox]]
- Mounts, secrets, and the rule list: [[Local LLM Coding with Hermes]] §§9 to 14
- Repair limit and the coding loop: [[howto-hermes-efficient-coding]]

## Examples, not requirements

vvvv on Windows, and TouchDesigner on macOS, show one external program and one MCP. An MCP is a connector that lets Hermes talk to another program.

Those programs are examples. You can replace them with a program you already use. Linux has no MCP example in its guide for the same reason: the connector is optional.

What an MCP is: [[../concepts/what-is-mcp]].
