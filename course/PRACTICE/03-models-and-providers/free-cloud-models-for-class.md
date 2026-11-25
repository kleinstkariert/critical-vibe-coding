---
title: Free cloud models for class
date: 2026-11-25
tags:
  - course
  - models
  - free
  - privacy
audience: student
status: current
canonical: true
last_verified: 2026-11-25
---

# Free cloud models for class

*optional extension.* *not required for assessment.* Any model endpoint meets [minimum path](../../PROJECT-WORK/01_minimum-path.md). This page compares free routes students often use with Hermes. Prefer open weights, clear data policy, and less training on your prompts. EU-hosted free agent endpoints for students were not found (not verified). Local models keep text on your machine: [howto local models](howto-local-models.md).

Labels: *vendor documentation* | *technical suggestion* | *not verified*. Rows can change without notice. Re-check OpenRouter and provider pages before class.

## How to read the table

- **Free limits** for OpenRouter `:free` ids: 20 requests a minute and 50 a day. After you buy US $10 of credit, 1,000 a day. Failed requests count. Source: OpenRouter limits docs, checked 25 Nov 2026.
- **Hosting region**: free OpenRouter routes are usually US hosts. OpenRouter EU in-region routing needs a Business or Enterprise plan (not a free student path). Source: OpenRouter provider-logging docs, checked 25 Nov 2026.
- **Hermes fitness**: needs tool calling and enough context (Hermes docs: at least 64K for tool work). Class did not run every free id with Hermes (*not verified*).
- **Privacy tip**: in OpenRouter account privacy, turn off free-model training if the control is there (exact label: not verified). That skips hosts OpenRouter marks as may-train.

## Comparison (checked 25 Nov 2026)

| Model id | Where to get | Free limits | Hosting region | License / weights | Training / privacy notes | Hermes fitness (tools) | Last checked |
|---|---|---|---|---|---|---|---|
| Local (Hermes Desktop Local Models) | Hermes Desktop: Settings → Providers → Local Models | Disk and RAM only | Your machine | Open weights you download (per model) | Nothing leaves your computer after download (*vendor documentation*, Hermes local-models docs) | Catalog models get ≥64K context; fit labels in UI. Class run: not verified | 25 Nov 2026 |
| `nous/welcome` | Hermes setup / Quickstart (terminal path) | Once per OS user when shown | Not published | Not a durable class model | No OpenRouter key. Shown only when available. Not in containers or scripted runs | First-chat only. Not for ongoing agent work | 25 Nov 2026 |
| `google/gemma-4-26b-a4b-it:free` | OpenRouter | 20/min, 50/day (1,000 after $10) | Google AI Studio host; HQ US (*vendor documentation*) | Gemma 4: Apache 2.0 open weights (*vendor documentation*) | OpenRouter marks Google AI Studio: retain 55 days, does not train. Google Gemini free-tier product terms can say content may improve products (*conflicting summaries*; treat as public text only) | Claims function calling and structured output. Hermes with this free id: not verified | 25 Nov 2026 |
| `google/gemma-4-31b-it:free` | OpenRouter | Same OpenRouter free caps | Same as above | Apache 2.0 open weights | Same privacy notes as Gemma 26B row | Same as above; larger download/host load. Hermes: not verified | 25 Nov 2026 |
| `openrouter/free` | OpenRouter | Same OpenRouter free caps | Depends on routed host | Depends on routed model | Can land on a may-train host unless you deny free-model training in privacy settings | Router picks a free model. Tool fit varies. Not verified | 25 Nov 2026 |
| `particle-ai/particle-1:free` (exact id: not verified; see OpenRouter free list) | OpenRouter free collection | Same OpenRouter free caps | Particle AI: zero retention, does not train (*OpenRouter provider table*) | Post-trained coding model (*vendor blurb*) | Better privacy tags than NVIDIA free on OpenRouter table | Marketed for agentic coding and fewer tokens. Hermes fitness: not verified | 25 Nov 2026 |
| `recursive/flint:free` (exact id: not verified; see OpenRouter free list) | OpenRouter free collection | Same OpenRouter free caps | Recursive: retain unknown period; does not train (*OpenRouter provider table*) | Open-weight MoE (*vendor blurb*) | Hosting region: not verified | Marketed for coding agents. Hermes fitness: not verified | 25 Nov 2026 |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | OpenRouter | Same OpenRouter free caps. **Burns fast** with Hermes tool loops (many requests per task) | NVIDIA host; HQ US | OpenMDW-1.1 open weights (*vendor documentation*) | OpenRouter marks NVIDIA: retain unknown period, **may train**. Prefer Gemma, Particle, or local when you care about training | Strong agent marketing and Hermes guide exists. Still listed for class demos. Demoted as default because of quota burn and may-train tag | 25 Nov 2026 |
| Google AI Studio Gemini free key | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) → Hermes Google provider | Free tier can run out after a few agent turns (*Hermes docs*) | Google; US | Closed Gemini weights; Gemma separate | Free tier may be used to improve Google products (*vendor pricing / terms summaries*) | Hermes supports `GOOGLE_API_KEY`. Quota for agents: weak | 25 Nov 2026 |
| Campus Academic AI (Kunstuni / UFG web chat) | Campus login portal | Campus policy | Often EU campus hosts (*not verified for Kunstuni instance*) | Hosted chat models | Better for private notes than random free US hosts, but **not an agent endpoint for student Hermes projects** | **No** for Hermes. See [academic AI Austria](academic-ai-austria.md) | 25 Nov 2026 |

## Class pick order (*technical suggestion*)

1. **Local** when the laptop has enough memory: [howto local models](howto-local-models.md). Best match to course ethics (control, open weights, no prompt feed to a lab by default).
2. **`nous/welcome`** for the first chat only, if Hermes shows it.
3. **OpenRouter Gemma `:free`** (26B A4B first) with free-model training denied in OpenRouter privacy, when you need a cloud key path.
4. **`openrouter/free`** or Particle / Recursive free ids when Gemma is down. Re-check the live free list.
5. **Nemotron Ultra `:free`**: still valid. Use short prompts. Expect the 50/day cap to end early with tools. Prefer another row for privacy.

## Sources (checked 25 Nov 2026)

- OpenRouter free models: https://openrouter.ai/collections/free-models
- OpenRouter limits: https://openrouter.ai/docs/api_reference/limits
- OpenRouter provider logging / training tags: https://openrouter.ai/docs/guides/privacy/provider-logging
- Hermes local models: https://hermes-agent.nousresearch.com/docs/user-guide/local-models
- Hermes Quickstart (`nous/welcome`): https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- Hermes Nemotron free guide: https://hermes-agent.nousresearch.com/docs/guides/run-nemotron-3-ultra-free
- Providers and keys: [howto Hermes providers and keys](../01-harness-and-agents/howto-hermes-providers-and-keys.md)
- Campus path: [academic AI Austria](academic-ai-austria.md)
