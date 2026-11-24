---
title: Hardware research, DIY multi-GPU builds and a DGX Spark class system
status: current
canonical: true
date: 2026-10-29
updated: 2026-11-23
last_verified: 2026-10-29
price_status: dated 2026-10-29, not rechecked on 2026-11-23
tags:
  - research
  - hardware
  - procurement
  - dated-prices
---

# Hardware research: DIY multi-GPU builds and a DGX Spark class system

This folder holds dated research on machines for local LLM work. It compares one ready-made system (a DGX Spark class machine) with four build options of consumer GPUs in an open frame. It also holds a model-fit table.

**No one must buy hardware for this course.** These notes are optional reading and an advanced path. See [how-to local LLM hardware](../../../course/PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md) and [minimum path](../../../course/PROJECT-WORK/01_minimum-path.md).

## Read this first: these numbers are dated

- Every price and specification in this folder is a **dated research snapshot**, not a current offer and not a guarantee.
- The price date is **29 October 2026**. The notes were copied into this repository on 23 November 2026. That edit changed structure and wording only. It did **not** recheck any price, benchmark or model size.
- Prices move weekly. Check live prices before you quote a number to anyone.
- Where a note recorded no date or source, this folder says so. It does not add one.

## Evidence labels

Labels follow the [source types](../../../course/REFERENCES/bibliography.md#source-types) of the course. A label names the kind of source. It is not independent verification.

| Label used here | Meaning | Source type |
|---|---|---|
| *vendor specification* | A figure from the maker's own page, as recorded in the note | Primary evidence (as recorded, not reopened) |
| *dealer listing* | A price shown on a dealer or price-comparison page (Geizhals.at) on the date given | Secondary reporting, dated |
| *community measurement* | A speed figure from forum or repository posts. It is not a controlled benchmark | Secondary reporting |
| *estimate, no source recorded* | A price or size with no source in the note | Course interpretation, unverified |
| *technical suggestion* | A design choice that the note recommends | Course interpretation |
| *claim* | A statement about a service or product that the note does not source | Speaker claim or unverified lead |

## Shared assumptions

These assumptions hold for all build options. The option pages do not repeat them.

| Assumption | Value | Evidence |
|---|---|---|
| Budget envelope | €6,000–10,000 | Planning input, no source |
| VAT | Prices include 20% VAT (Austria) | Planning input |
| Price date | Late October 2026 (29 October 2026) | As recorded |
| GPU, RAM, NVLink bridge and Spark prices | Rechecked on 29 October 2026 | *dealer listing* |
| Board, CPU, PSU, fan, frame and safety-part prices | Not rechecked. They need 2–3 current quotations | *estimate, no source recorded* |
| Contingency | 10% added to each build subtotal | Planning input |
| Price risk | Ask for quote validity, or allow ±15% | *technical suggestion* |

## Options at a glance

| Option | Memory | Total including contingency | Load power | Best at | Verdict in the source note |
|---|---|---:|---|---|---|
| [Spark class system (Acer Veriton GN100)](spark-gb10-recommended-system.md) | 128 GB unified | System €6,299; request ceiling €7,800 | Low hundreds of W (240 W supply) | Capacity, watts, warranty, broad model support | Recommended |
| [Setup A, dual RTX 3090](setup-a-dual-3090-open-frame.md) | 48 GB split | €4,990–6,750 | About 700–900 W | Fast 27–70B inference | DIY alternative |
| [Setup C, triple RTX 3090](setup-c-triple-3090-open-frame.md) | 72 GB split | €7,050–9,280 | About 1.1–1.3 kW | Fast 120B-class inference | DIY alternative |
| [Setup B, dual RTX 4090](setup-b-dual-4090-open-frame.md) | 48 GB split | €8,030–11,130 | About 1.0–1.2 kW | Same capacity as A, faster per card | Not recommended |
| [Setup D, dual RTX 5090](setup-d-dual-5090-ceiling.md) | 64 GB split | €13,300–18,000 | Not recorded | Ceiling case only | Excluded |

Model fit for A, C and the Spark system: [LLM coding capability matrix](llm-coding-capability-matrix.md). The request draft for the DIY options: [DIY request draft](diy-request-draft.md).

Setup C is shown as €7,050–9,280. The older index and the request draft rounded the same figure to €9.3k and €9,300.

## Efficiency-only conclusion

*technical suggestion, from the source notes.* If teaching value is left out, the Spark class system is generally the more cost-effective purchase for capacity and operating efficiency.

- **Capacity.** 128 GB unified memory for about €6,300 (2 TB, Acer, 3-year warranty, Austria) against 48 GB split VRAM for Setup A at €4,990–6,750.
- **Cost per GB.** About €49 per GB for the Spark system against €104–141 per GB for Setup A. The arithmetic checks: 6,299 ÷ 128 ≈ 49, and 4,990 ÷ 48 ≈ 104, 6,750 ÷ 48 ≈ 141.
- **Power.** The Spark system uses up to a few hundred watts. Dual 3090 uses about 700–900 W under inference.
- **Model reach.** The Spark system can load models that do not fit in 48 or 72 GB.
- **Risk.** Warranty, integration and maintenance risk are lower.

The DIY builds win on **interactive speed for models that fit**:

| Measurement | Value | Evidence |
|---|---|---|
| Llama 3.3 70B Q4, dual 3090 | About 18 tok/s | *community measurement*, source not recorded |
| Llama 3.3 70B Q4, Spark | About 2–5 tok/s per stream | *community measurement*, see sources on the [Spark page](spark-gb10-recommended-system.md) |
| gpt-oss-120b, three 3090 | About 73–130 tok/s | *community measurement*, source not recorded |
| gpt-oss-120b, Spark | About 59 tok/s (llama.cpp, February 2026) | *community measurement*, see the Spark page |

None of these is a controlled comparison. On mixture-of-experts models such as Qwen3-Coder-Next and gpt-oss-120b, the Spark system is competitive. The large gap is on dense 70B models.

| System | Capacity | Typical load power | Best at |
|---|---:|---:|---|
| Spark class | 128 GB unified | Low hundreds of W | Capacity, watts, maintenance |
| Dual 3090 (A) | 48 GB split | 700–900 W | 70B latency and throughput |
| Triple 3090 (C) | 72 GB split | 1.1–1.3 kW | Fast 120B-class inference |

In short:

- **Capacity, watts, warranty and broad model support:** Spark class.
- **Lowest latency and highest tok/s on models that fit:** multi-3090.

## Shared technical notes for the DIY builds

- **Memory is split, not unified.** Software splits the model across cards. Two 24 GB cards give about 48 GB of weight capacity, not one 48 GB GPU. The longer explanation is in [local GPU hardware for LLMs](../local-gpu-hardware-for-llms.md#4-path-c-diy-multi-gpu-rack-workstation).
- **Split mode.** llama.cpp layer split (`-sm layer`) is the default and works over PCIe. Tensor split (`-sm tensor`) is still experimental. An NVLink bridge is not needed for layer split.
- **Power cables.** Use one PSU cable per GPU connector. Never daisy-chain GPU power cables. Power-limit the cards where practical, and meter consumption.
- **Reasoning settings.** "Thinking off" applies only to models that support it. See the note in the [capability matrix](llm-coding-capability-matrix.md).

## Procurement and operation cautions

These cautions apply to all DIY options. They are *technical suggestions*.

| Concern | Measure |
|---|---|
| Used GPUs | Buy from an invoiced dealer with the 12-month statutory warranty. Burn in for 24–72 hours during the return window |
| Electrical safety | Use a lockable, ventilated cage or machine room, fan guards, an electrical inspection and a dedicated 16 A circuit |
| Power | Meter consumption. Power-limit the GPUs |
| Maintenance | Name a responsible person for hardware, OS, drivers and security |
| Procurement | Confirm the university's Austrian procurement threshold and the NVIDIA GeForce licence terms before purchase |
| Price volatility | Require quote validity, or allow ±15% |

## How this folder relates to other pages

| Page | What it holds | Do not duplicate here |
|---|---|---|
| [Local GPU hardware for LLMs](../local-gpu-hardware-for-llms.md) | General research: memory math, ready-made machines, single-GPU tiers, how multi-GPU works, tutorials | Memory math and the multi-GPU explanation |
| [How-to local LLM hardware](../../../course/PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md) | Student steps for software and a first machine | Setup steps |
| [Dated models, prices, limits and hardware](../../../course/REFERENCES/dated-models-prices-limits-and-hardware.md) | Index of volatile claims with check dates | Row-level price tracking |
| [Academic AI in Austria](../../../course/PRACTICE/03-models-and-providers/academic-ai-austria.md) | What campus services offer | The "no API key for agents" background |

**Price ranges differ between notes.** The older general note gives "dual 3090 used workstation often €3–6k" and "dual 4090 new €5–9k+". This folder gives €4,990–6,750 for Setup A and €8,030–11,130 for Setup B. The older ranges record no basis. This folder's totals include invoiced dealers with warranty, a safety cage, 64 GB RAM, 2 TB NVMe and 10% contingency. Treat both as dated and compare them only with that in mind (*uncertainty*).

## Known gaps

- No source is recorded for the 18 tok/s and the 73–130 tok/s figures.
- No power figure is recorded for Setup D.
- Model sizes in the capability matrix have no per-row source. Verify on Hugging Face at purchase time.
- Board, CPU, PSU, fan and frame prices are estimates with no date.
- The claim that a campus service has no API key for agents is not sourced in the Spark note. The course page on [Academic AI in Austria](../../../course/PRACTICE/03-models-and-providers/academic-ai-austria.md) says the same, with its own caveats.

## Reading order

1. This page.
2. [Spark class system](spark-gb10-recommended-system.md), the recommended option.
3. [Setup A](setup-a-dual-3090-open-frame.md) and [Setup C](setup-c-triple-3090-open-frame.md), the DIY alternatives.
4. [Setup B](setup-b-dual-4090-open-frame.md) and [Setup D](setup-d-dual-5090-ceiling.md), the rejected options.
5. [Capability matrix](llm-coding-capability-matrix.md).
6. [DIY request draft](diy-request-draft.md).
