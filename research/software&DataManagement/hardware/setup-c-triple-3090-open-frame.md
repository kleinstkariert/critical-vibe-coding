---
title: Setup C, triple RTX 3090 open frame
audience: student
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

# Setup C: triple RTX 3090 (72 GB split)

Dated research. Read the [hardware README](README.md) for the price date, the evidence labels and the shared assumptions. Prices here are not a current offer.

**Cost:** €7,050–9,280 including 10% contingency.
**Use:** gpt-oss-120b, and long-context or concurrent projects.
**Evidence:** *community measurement*. About 73–130 tok/s for gpt-oss-120b against about 59 tok/s on the Spark system. It is not a controlled comparison. The source for the 73–130 figure is not recorded. See [efficiency conclusion](README.md#efficiency-only-conclusion).
**Role:** DIY alternative. The [recommended option](spark-gb10-recommended-system.md) is the Spark class system.

## Parts and estimates

| Part | Estimate | Evidence |
|---|---:|---|
| 3 × RTX 3090, invoiced, 12-month warranty | €4,650–5,250 | *dealer listing*, 2026-10-29 |
| Aluminium frame | €100–230 | *estimate, no source recorded* |
| Board with three usable PCIe connections | €250–450 | *estimate, no source recorded* |
| CPU and cooler | €220–520 | *estimate, no source recorded* |
| 64 GB DDR4 | €400–560 | *dealer listing*, 2026-10-29 |
| 1600 W PSU, or a synchronised dual PSU | €300–500 | *estimate, no source recorded* |
| Cables, 2 TB NVMe, fans and risers | €360–620 | *estimate, no source recorded* |
| Safety cage, guards, metered PDU and OS | €130–310 | *estimate, no source recorded* |
| **Subtotal** | **€6,410–8,440** | Sum of the rows above (checked) |
| Contingency 10% | €641–844 | |
| **Total** | **€7,050–9,280** | |

If you use two PSUs, use a sync adapter and one shared PDU, one circuit and one ground. The general rule not to daisy-chain GPU power cables is in the [README](README.md#shared-technical-notes-for-the-diy-builds).

Wall draw: about 1.1–1.3 kW (*estimate, no source recorded*). A dedicated 16 A circuit is required. More cautions: [README](README.md#procurement-and-operation-cautions).

Which models fit: [capability matrix](llm-coding-capability-matrix.md). The request text: [DIY request draft](diy-request-draft.md).
