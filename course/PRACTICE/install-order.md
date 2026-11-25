---
title: Install order
date: 2026-11-25
tags:
  - course
  - students
  - install
status: current
canonical: true
---

# Install order

*reference implementation. Optional extension. Not required for assessment.* This page gives the order for the Hermes example. If you use another system, you can skip it. The required work is in the [minimum path](../PROJECT-WORK/01_minimum-path.md). Other tools are compared in the [tool comparison](../../research/software&DataManagement/vibe-coding-tools-and-agent-environments.md).

## Start here

Pick your OS beginner guide first. Follow that file from top to bottom.

| OS | Beginner guide |
|---|---|
| Windows | [install-windows.md](01-harness-and-agents/install-windows.md) |
| macOS | [install-mac.md](01-harness-and-agents/install-mac.md) |
| Linux | [install-linux.md](01-harness-and-agents/install-linux.md) |

Each guide covers: install Desktop (or the Linux terminal install), add an OpenRouter key in Settings, first chat, one smoke test. Why this order: [install-why.md](01-harness-and-agents/install-why.md). Safety: [safe install rules](05-security-and-privacy/howto-hermes-safe-install-rules.md).

## Order (Hermes example)

1. **Pick your OS guide** and finish the smoke test (Session 03). Class default model: free OpenRouter route. Words: [default setup](01-harness-and-agents/default-setup.md) section 4. Providers table: [providers and keys](01-harness-and-agents/howto-hermes-providers-and-keys.md).
2. Note which **LLM access** you already have. Campus academic AI is a web chat for students. It is **not an agent endpoint for student projects**. See [API access in academic AI](03-models-and-providers/academic-ai-austria.md#api-access-in-academic-ai).
3. Knowledge store with **phone sync** (homework): default Obsidian; **alternatives allowed**. See [knowledge store options](02-knowledge-bases/knowledge-store-options.md) and [Obsidian setup and sync](02-knowledge-bases/howto-obsidian-setup-and-sync.md).
4. Skim **harness**: [what is a harness](01-harness-and-agents/what-is-harness.md) (Session 02).
5. Prompting and chat versus reasoning: [prompting guide](03-models-and-providers/prompting-guide-for-critical-vibe-coding.md) (Session 03).
6. Optional **local** models: [howto local models](03-models-and-providers/howto-local-models.md) · [local LLM hardware](04-local-and-cloud/howto-local-llm-hardware.md).

Keep API keys out of synced notes.

## Advanced guides

| Need | Guide |
|---|---|
| Why this order | [install-why.md](01-harness-and-agents/install-why.md) |
| Providers and keys (all rows, .env) | [providers and keys](01-harness-and-agents/howto-hermes-providers-and-keys.md) |
| CLI install, vault paths, skills, gateway | [advanced Hermes config](01-harness-and-agents/howto-hermes-advanced-config.md) |
| Local models | [howto local models](03-models-and-providers/howto-local-models.md) |
| MCP examples (vvvv, TouchDesigner) | [howto example mcp servers](06-mcp-and-tools/howto-example-mcp-servers.md) |
| Docker sandbox | [howto hermes docker sandbox](05-security-and-privacy/howto-hermes-docker-sandbox.md) |
| Efficient coding | [howto hermes efficient coding](01-harness-and-agents/howto-hermes-efficient-coding.md) |
| Safety rules | [safe install rules](05-security-and-privacy/howto-hermes-safe-install-rules.md) |
| First folders and SCHEMA.md | [starter knowledge base](02-knowledge-bases/starter-knowledge-base.md) |
| Local GPU, Mac, DGX, multi-GPU | [local LLM hardware](04-local-and-cloud/howto-local-llm-hardware.md) · [hardware research](../../research/software&DataManagement/local-gpu-hardware-for-llms.md) |

## Where to keep this repository

*technical suggestion:* Clone or download this repository into a folder next to (or inside) your personal vault, for example Obsidian/CVC-course/. Your **LLM Wiki** (wiki/ or agent-writable folders) stays in *your* vault. This repository is the course pack, not your diary.

GitHub renders Markdown in the browser. You do not need Obsidian to *read* the course pack.
