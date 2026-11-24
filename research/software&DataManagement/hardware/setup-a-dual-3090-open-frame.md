---
title: Setup A, dual RTX 3090 open frame
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

# Setup A: dual RTX 3090 (48 GB split)

Dated research. Read the [hardware README](README.md) for the price date, the evidence labels and the shared assumptions. Prices here are not a current offer.

**Cost:** €4,990–6,750 including 10% contingency.
**Use:** fast 27–70B inference.
**Limitation:** the memory is split, not unified. gpt-oss-120b does not fit. See [shared technical notes](README.md#shared-technical-notes-for-the-diy-builds).
**Role:** DIY alternative. The [recommended option](spark-gb10-recommended-system.md) is the Spark class system.

## Parts and estimates

| Part | Estimate | Evidence |
|---|---:|---|
| 2 × RTX 3090, invoiced, 12-month warranty | €3,100–3,500 | *dealer listing*, 2026-10-29 |
| Aluminium frame (check the 32 cm GPU length limit) | €80–230 | *estimate, no source recorded* |
| AM4 board with two usable full-length PCIe slots | €150–280 | *estimate, no source recorded* |
| Ryzen 7 5700X-class CPU | €150–280 | *estimate, no source recorded* |
| Cooler | €35–55 | *estimate, no source recorded* |
| 64 GB DDR4 | €400–560 | *dealer listing*, 2026-10-29 |
| 1200–1300 W quality PSU | €180–280 | *estimate, no source recorded* |
| Separate PCIe cables | €20–40 | *estimate, no source recorded* |
| 2 TB NVMe | €230–340 | *estimate, no source recorded* |
| Risers | €25–90 | *estimate, no source recorded* |
| Fans | €40–90 | *estimate, no source recorded* |
| Network and OS | €10–90 | *estimate, no source recorded* |
| Safety cage, guards, metered PDU | €120–300 | *estimate, no source recorded* |
| **Subtotal** | **€4,540–6,135** | Sum of the rows above (checked) |
| Contingency 10% | €454–614 | |
| **Total** | **€4,990–6,750** | |

Optional NVLink bridge: €160–300 (*dealer listing*, 2026-10-29). It is not needed for llama.cpp layer split, and it limits the card spacing.

**Power:** about 700–900 W at load. General power-cable and circuit rules are in the [README cautions](README.md#procurement-and-operation-cautions).

**Software:** Ubuntu LTS, NVIDIA driver, llama.cpp or Ollama, and optional vLLM. Split modes are explained in the [README](README.md#shared-technical-notes-for-the-diy-builds).

Which models fit: [capability matrix](llm-coding-capability-matrix.md). The request text for this build and for Setup C: [DIY request draft](diy-request-draft.md).
