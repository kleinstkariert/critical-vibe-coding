---
title: Session 10 — Local, ecology, when not
session: 10
---

# Session 10 — Local / open infra, ecology, when *not* to use AI

Parent: [[../timeline]]

## Goals

- Ground ecological claims (energy, water, siting) without hand-waving
- Compare cloud convenience vs local/EU/open stacks students can actually run
- Practice deciding **not** to use an agent

## Check-in

What did you *not* automate this week on purpose?

## Student input

Someone with a local GPU or EU host demos if available; else teacher shares contact scheme.

## Teacher input

- Material infrastructure of inference and training (update numbers before class; label sources) — start from the two primary sources below, not from vendor blog posts
- What “run locally” actually costs in hardware: self-build NVIDIA, DGX Spark-class, Apple unified memory — [[../../research/local-gpu-hardware-for-llms]] (when renting/sharing beats owning)
- Open weights + local as political/aesthetic choice ([HM Munich Our Br00d](https://mediapool.hm.edu/media/dachmarke/dm_lokal/hm_international/sprachen/coursesinenglish_1/courses_in_english_ss_26/muc_dai_5/CiE_Kursbeschreibung_Our_Br00d_Technical_Development_of_Agentic_AI_in_Artistic_Research_Geaendert.pdf) pattern: infra as intervention)
- [SFPC “handmade”](https://sfpc.study/sessions/summer-26/handmade-datasets) scale: small knowledge bases you can care for ([[../timeline]]). The LLM Wiki pattern makes the same bet at the technical level: at ~100 sources / a few hundred pages an `index.md` replaces a vector database (Karpathy gist; [[../../research/karpathy-llm-wiki-and-openclaw]])
- Criteria checklist: when AI is useful / unnecessary (*requirement* from brief)

## Optional reading (pick one; all free to read)

URLs checked 2026-10-18 (*verified fact*).

| Reading | Why here |
|---|---|
| Luccioni, Jernite & Strubell, *Power Hungry Processing: Watts Driving the Cost of AI Deployment?* (ACM FAccT 2024) — https://arxiv.org/abs/2311.16863 | Measures **inference** energy across 88 models; finds general-purpose generative models “orders of magnitude” costlier than task-specific ones for the same task. Directly supports the “when *not*” checklist: a small tool may do |
| IEA, *Energy and AI* (2025-04-10, CC BY 4.0) — https://www.iea.org/reports/energy-and-ai | Agency-level projections of data-centre electricity, supply and emissions; the numbers to quote instead of hand-waving |
| Crawford & Joler, *Anatomy of an AI System* (2018) — https://anatomyof.ai/ | Lithium, logistics, e-waste: the material side beyond electricity (also listed for session 8) |

## Practical

- Run the same task: cloud model vs smaller/local/open option (or document why local is impossible on their machine); note energy/latency/quality in a `comparisons/` page
- Write a “kill switch” rule into the schema (tasks the agent must not do) — in `SCHEMA.md` next to the human-only paths ([[../llm-wiki-standard-files]])

## Homework

- Studio prep: list blockers for final; book any needed hardware/time

## Materials / References

| What | Link |
|---|---|
| Optional readings | table above |
| Local hardware (self-build / DGX Spark / Apple unified) | [[../../research/local-gpu-hardware-for-llms]] |
| EU AI Act + Datenschutz (data location / sovereignty) | [[../eu-ai-act-and-datenschutz]] |
| Academic / HPC options (not daily chat) | [[../academic-ai-austria]] |
| Hermes local models | https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Hermes custom / self-hosted endpoints | https://hermes-agent.nousresearch.com/docs/integrations/providers |
| Hermes + Ollama guide | https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup |
| Why small-scale wiki needs no vector DB (Karpathy) | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f · [[../../research/karpathy-llm-wiki-and-openclaw]] |
| Kill-switch rule → `SCHEMA.md` | [[../llm-wiki-standard-files]] |
| Peer courses — HM Munich (infra as artistic decision), SFPC (handmade scale) | [[../references]] |
