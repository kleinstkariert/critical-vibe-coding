---
title: Install order
date: 2026-10-22
tags:
  - course
  - students
  - install
status: current
canonical: true
---

# Install order

*reference implementation. Optional extension. Not required for assessment.* This page gives the order in which to set up the Hermes example. If you use another system, you can skip it. The required work is in the [minimum path](../PROJECT-WORK/01_minimum-path.md). Other tools are compared in the [tool comparison](../../research/software&DataManagement/vibe-coding-tools-and-agent-environments.md).

## Order

1. Knowledge store with **phone sync**: default Obsidian; **alternatives allowed**. See [knowledge store options](02-knowledge-bases/knowledge-store-options.md) and [Obsidian setup and sync](02-knowledge-bases/howto-obsidian-setup-and-sync.md).
2. Note which **LLM access** you already have. Campus academic AI has **no API for agents**. See [academic AI in Austria](03-models-and-providers/academic-ai-austria.md).
3. **Hermes Agent**, installed together in Session 03. A free-to-use hosted endpoint to start: Nemotron 3 Ultra on OpenRouter. See [Hermes setup](01-harness-and-agents/howto-hermes-setup.md) section 3. Words and the classroom route: [default setup](01-harness-and-agents/default-setup.md) section 4.
4. Skim **harness**: [what is a harness](01-harness-and-agents/what-is-harness.md) (Session 02).
5. Prompting and chat versus reasoning: [prompting guide](03-models-and-providers/prompting-guide-for-critical-vibe-coding.md) (Session 03).
6. Optional **local** models and hardware: [local LLM hardware](04-local-and-cloud/howto-local-llm-hardware.md) (Session 03).

Keep API keys out of synced notes.

## Step-by-step guides

| Need | Guide |
|---|---|
| Hermes Desktop on Windows, Linux or macOS | [install-windows.md](01-harness-and-agents/install-windows.md) · [install-linux.md](01-harness-and-agents/install-linux.md) · [install-mac.md](01-harness-and-agents/install-mac.md) |
| Why this order | [install-why.md](01-harness-and-agents/install-why.md) |
| First folders and `SCHEMA.md` | [starter knowledge base](02-knowledge-bases/starter-knowledge-base.md) |
| Local GPU, Mac, DGX, multi-GPU | [local LLM hardware](04-local-and-cloud/howto-local-llm-hardware.md) · [hardware research](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) |

## Where to keep this repository

*technical suggestion:* Clone or download this repository into a folder next to (or inside) your personal vault, for example `Obsidian/CVC-course/`. Your **LLM Wiki** (`wiki/` or agent-writable folders) stays in *your* vault. This repository is the course pack, not your diary.

GitHub renders Markdown in the browser. You do not need Obsidian to *read* the course pack.
