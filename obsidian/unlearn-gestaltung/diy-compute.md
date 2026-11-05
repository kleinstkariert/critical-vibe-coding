---
title: DIY Compute — condensed note
date: 2026-11-04
slug: ro8j5asv
tags:
  - research
  - kitegg
  - hardware
---

# DIY Compute: Rolling Your Own GPU Node from Cheap Hardware

**Author:** Anton Koch  
**URL:** https://unlearn.gestaltung.ai/article/ro8j5asv  
**Language:** English

## Main points

1. **Why:** HGX/DGX-class servers are expensive; for **small concurrent staff/user counts**, ~**€3000** barebone nodes with up to **six PCIe GPUs** (repurposed workstation/VR/mining cards) can open access.
2. **Example build:** IPC **4W2 mining rack** (~€150) + PWM fan swap + **reversed airflow** to match datacenter front→back; ASRock **ROMED8** server board with BMC/IPMI (~€700); **Epyc 7513** 32-core (~€800); start **128 GB RAM**; dual 2 TB NVMe; **1500 W** PSU; Phanteks PCIe risers.
3. **Sizing idea:** ~four interactive users each with a GPU (Jupyter-style) or four parallel worker tasks — Mini-PC/VPS-like per-user thinking, not hyperscale.
4. **Cooling caveat:** passively cooled datacenter cards need real HVAC; blower workstation cards heat the room hard.
5. **Assembly culture:** torque specs, don’t trust trays, expect metal burr (“blood in the machine”); reverse airflow is most of the fab work.
6. **Role in KITeGG ecology:** cheap end of the spectrum complementary to the main A100 HGX cluster — same software story possible, weaker MIG/multi-instance story on consumer cards.

## vs CVC hardware path

- Aligns in spirit with CVC Session 04 DIY / research note Paths B–C and teacher hardware-procurement thinking.
- Still **multi-GPU rack server** for lab concurrency — larger than CVC’s default “Ollama on your laptop / one gaming GPU / optional Mac Studio or Spark.”
- Useful citation when teaching **own metal without HGX money**.

## Related

- [[article-how-to-kitegg]] · [[article-kitegg-cluster]] · [[comparison-vs-cvc]]
