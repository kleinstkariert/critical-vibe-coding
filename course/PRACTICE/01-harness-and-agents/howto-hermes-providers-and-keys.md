---
title: How-to. Hermes providers and keys
date: 2026-11-25
tags:
  - course
  - howto
  - providers
  - keys
status: current
canonical: true
---

# How-to. Hermes providers and keys

*optional extension.* *not required for assessment.* Beginners: use your OS install guide and add an OpenRouter key in Desktop Settings. This page is for other providers, cards, and the terminal or `.env` path.

Hermes itself is free (MIT). Model use is separate. Class free picks and ethics notes: [free cloud models for class](../03-models-and-providers/free-cloud-models-for-class.md). Full Hermes provider list: https://hermes-agent.nousresearch.com/docs/integrations/providers

## Prefer the Desktop path

In Hermes Desktop:

- Cloud key: **Settings → Providers → OpenRouter → add API key** (exact labels: not verified). For another provider, open that row in the same Providers list and paste the key there.
- Local models: **Settings → Providers → Local Models → Install runtime → Download → Use** (labels from official docs, checked 25 Nov 2026). Guide: [howto local models](../03-models-and-providers/howto-local-models.md).

Never type a key in a shell command. Terminal and `.env` are advanced.

## Provider table

| Provider | Get a key | Card needed | Key name in the env file | Notes |
|---|---|---|---|---|
| OpenRouter, free route | [openrouter.ai/settings/keys](https://openrouter.ai/settings/keys) | No, for models whose id ends in `:free` | `OPENROUTER_API_KEY` | Free models: 20 requests a minute and 50 a day. After you buy US $10 of credit, 1,000 a day. Prefer Gemma `:free` or `openrouter/free`. Nemotron free burns quota fast and may train. Comparison: [free cloud models for class](../03-models-and-providers/free-cloud-models-for-class.md) · [Free models](https://openrouter.ai/collections/free-models) |
| OpenAI API | [platform.openai.com/api-keys](https://platform.openai.com/api-keys) | Yes. Prepaid credit | `OPENAI_API_KEY` | ChatGPT Plus has no API credit. [Billing help](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) |
| Anthropic (Claude API) | [platform.claude.com/settings/keys](https://platform.claude.com/settings/keys) | Yes. Prepaid credit. A key without credit fails | `ANTHROPIC_API_KEY` | Hermes cannot log in with a Claude Pro plan. Use a key. [Billing help](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage) |
| Google Gemini | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | No, for the free tier | `GOOGLE_API_KEY` (or `GEMINI_API_KEY`) | Google can use free-tier prompts to improve its products. Hermes docs: a free key can run out after a few agent turns. [Billing](https://aistudio.google.com/docs/billing) |
| Nous Portal | [portal.nousresearch.com](https://portal.nousresearch.com) | Subscription. Card: not verified | None. Log in with `hermes model` | One login for many models. Price: not verified. `nous/welcome` is a separate one-shot free path in setup |
| Local (Hermes Desktop) | No key | No | None | **Settings → Providers → Local Models**. Primary local path. [howto local models](../03-models-and-providers/howto-local-models.md) |
| Local, with Ollama or LM Studio | [ollama.com/download](https://ollama.com/download) or [lmstudio.ai/download](https://lmstudio.ai/download) | No | None | Alternate when Local Models is not available. Same howto |

Key pages ask you to sign in. The links load (checked 25 Nov 2026). The page labels can change (not verified).

## Class free OpenRouter models

*technical suggestion* (re-checked 25 Nov 2026). Prefer open weights and hosts that OpenRouter does not mark as may-train. Full table: [free cloud models for class](../03-models-and-providers/free-cloud-models-for-class.md).

1. Create a free account and API key at https://openrouter.ai
2. Prefer Desktop Settings (above). Or add the key to the Hermes env file (below).
3. In OpenRouter privacy, turn off free-model training if you can (exact label: not verified).
4. Choose OpenRouter, then prefer `google/gemma-4-26b-a4b-it:free` or `openrouter/free`.

**Nemotron (still listed, demoted):** `nvidia/nemotron-3-ultra-550b-a55b:free`. Strong for agents and Hermes has a guide. The free quota (50 requests a day) burns fast with tool loops. OpenRouter marks NVIDIA as may train. Prefer Gemma, `openrouter/free`, or a local model when you care about quota or training. Hermes guide: https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free

Limits: 20 requests per minute and 50 per day on a free account (checked 25 Nov 2026). Keep private notes away from free cloud hosts. Fallback: local models, or Nous Portal (`hermes setup --portal`).

## Terminal: `hermes model`

Type `hermes model` in a normal terminal. Paste the key at its prompt. Choose a small model that says it supports tools.

Optional OAuth path: `hermes setup --portal` (Nous Portal).

## Env file (advanced)

Do this only if Desktop Settings and `hermes model` are not available.

| Platform | Env file | Open example |
|---|---|---|
| Windows | `%LOCALAPPDATA%\hermes\.env` | `notepad "$env:LOCALAPPDATA\hermes\.env"` |
| macOS / Linux | `~/.hermes/.env` | `nano ~/.hermes/.env` |

Add one line with the key name from the table, for example:

```env
OPENROUTER_API_KEY=your-key
```

On Windows: click File, then Save. Do not use Save As. On macOS and Linux with nano: Control+O, Return, Control+X.

Do not put the key in the vault, in chat, or in Git. Why, and what to do after a leak: [safe install rules](../05-security-and-privacy/howto-hermes-safe-install-rules.md#5-secrets).

## Related

- OS beginner guides: [Windows](install-windows.md) · [macOS](install-mac.md) · [Linux](install-linux.md)
- Local models: [howto local models](../03-models-and-providers/howto-local-models.md)
- Vault paths and CLI: [advanced Hermes config](howto-hermes-advanced-config.md)
