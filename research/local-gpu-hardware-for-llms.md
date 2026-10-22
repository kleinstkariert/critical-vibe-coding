---
title: Local hardware for larger LLMs
date: 2026-10-20
tags:
  - research
  - hardware
  - local-llm
  - course
---

# Local hardware for larger LLMs

Research note for Critical Vibe Coding. Labels: *verified fact* | *street-price estimate* | *technical suggestion*.  
Prices move weekly — re-check before telling students a number. Currency roughly **USD street / MSRP class, mid–late 2026** unless noted.

Use in: session [[../course/sessions/03-models-prompting-install]] (landscape) · [[../course/sessions/10-local-ecology-when-not]] (local as choice) · lecture [[../course/lectures/01-welcome-landscape-lecture]] (preview only).

---

## What “larger model” means for memory

Rule of thumb for **weights only** (plus KV-cache / context needs more):

| Precision | Approx. GB per billion parameters |
|---|---|
| FP16 / BF16 | ~2 GB |
| 8-bit | ~1 GB |
| 4-bit (Q4) | ~0.5 GB |

Examples (*order of magnitude*):

| Model class | Q4 weights | Practical machine memory |
|---|---|---|
| 7–9B | ~4–6 GB | Laptop GPU / 16–24 GB unified OK |
| 27–34B | ~16–20 GB | 24 GB discrete GPU or 32–48 GB unified |
| 70B | ~40–44 GB | **≥48–64 GB** usable GPU/unified; 128 GB comfortable |
| 70B Q8 / larger MoE | 80 GB+ | 96–192 GB unified or multi-GPU |

*nuance:* Advertised RAM ≠ usable for weights. Discrete GPUs lose some VRAM to the display driver; unified-memory machines share RAM with the OS (often plan ~70–80% of the sticker for the model).

Inference stack examples: **llama.cpp / Ollama / LM Studio** (easy); **vLLM / TensorRT-LLM** (NVIDIA serving); **MLX** (Apple). Training/LoRA is a harder memory problem than chat inference.

---

## Path A — Self-built NVIDIA (discrete GPU)

Best when you want **CUDA**, maximum tok/s per euro at mid size, and are willing to assemble a PC.

### Typical build tiers (*street-price estimate*)

| Tier | Example GPU | VRAM | Fits (Q4 chat, rough) | GPU street | Whole PC ballpark |
|---|---|---|---|---|---|
| Entry local | RTX 4060 / 4060 Ti | 8–16 GB | 7–13B comfortable | €300–500 | €900–1 400 |
| Sweet spot used/new | RTX 3090 / 4090 | 24 GB | ~30–34B; 70B only with offload (slow) | 3090 used varies; 4090 often €1 500–2 200 | €2 000–3 500 |
| Current high consumer | RTX 5090 | 32 GB | larger 30B-class; 70B still tight | check live | €3 000–4 500+ |
| Multi-GPU | 2×24–48 GB | 48–96 GB pool | 70B Q4 if software supports split | 2× GPU + big PSU | €4 000–8 000+ |

**Build checklist**

- PSU headroom (4090-class ~450 W TDP + CPU); quality cables  
- Case airflow; GPU length  
- Fast NVMe for model files (70B Q4 is tens of GB on disk)  
- Linux or Windows; Linux usually nicer for CUDA servers  
- Power / heat / noise — studio apartments matter  

**Pros:** Fast for models that fit in VRAM; CUDA ecosystem.  
**Cons:** VRAM ceiling per card; multi-GPU complexity; power draw; Austria/EU electricity cost for always-on.

Links: [NVIDIA GeForce](https://www.nvidia.com/en-us/geforce/) · community trackers e.g. [llmhardware.io/compare](https://llmhardware.io/compare)

---

## Path B — Ready-made NVIDIA “AI PCs”

### NVIDIA DGX Spark (GB10, deskside)

- **What:** Small deskside / workstation-class box, **128 GB** unified LPDDR5x, Grace Blackwell GB10, DGX OS (Ubuntu), CUDA / TensorRT-LLM path.  
- **MSRP class:** often cited around **~$4 000–4 700** (confirm on [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) / local reseller).  
- **Fits:** 70B Q4 comfortably in memory terms; bandwidth (~273 GB/s class) is **lower** than top Apple Ultra — expect solid CUDA workflow, not always the tok/s king vs Mac Studio.  
- **Pros:** Official NVIDIA stack; less DIY; path toward networked Spark setups in docs.  
- **Cons:** Price; Linux-first; less “normal laptop” than a Mac.

### Other NVIDIA / OEM

- Older **DGX Station** / enterprise boxes: budget usually **beyond student/artist** (tens of k€).  
- OEM “AI mini PCs” with mobile Blackwell/Ada — verify real VRAM/unified numbers, not marketing FLOPS.

---

## Path C — Apple Silicon (unified memory)

Apple does **not** have a separate GPU VRAM pool the way discrete NVIDIA cards do. CPU + GPU share **unified memory**. For local LLMs this is the feature: a **128 GB Mac Studio** can load model weights that a 24 GB GeForce cannot, using MLX / llama.cpp Metal / Ollama.

| Config (examples) | Unified memory | Rough fit | Price class (*estimate*) |
|---|---|---|---|
| Mac mini M4 Pro | 24–64 GB | 7–34B; 70B Q4 only at high memory configs | check Apple |
| Mac Studio M4 Max | up to ~128 GB class | 70B Q4 comfortable at 64–128 GB | often ~$2 k–$4 k+ depending on RAM |
| Mac Studio M4 Ultra | high bandwidth (~800 GB/s class), large RAM options | 70B Q8 experiments; larger quants | often **$5 k–$9 k+** fully loaded |

*verified direction:* Higher **memory bandwidth** on Ultra vs DGX Spark is why many tok/s comparisons favour Mac for pure local chat; NVIDIA wins on CUDA training/serving ecosystem.

**Pros:** Quiet, low power, strong laptop/desktop continuity, easy for artists already on Mac.  
**Cons:** No CUDA; some Python ML stacks are second-class; RAM soldered (buy the memory you need on day one).

Links: [Apple Mac Studio](https://www.apple.com/mac-studio/) · MLX: https://github.com/ml-explore/mlx

---

## Path D — AMD unified / Strix Halo mini PCs

Examples: mini PCs with **Ryzen AI Max+ 395** and **128 GB** LPDDR5x (~$2 000–3 500 class).  

- Memory capacity competes with Spark/Mac for *loading* 70B Q4.  
- Software (ROCm / Vulkan llama.cpp) is more brittle than CUDA or MLX.  
- *technical suggestion:* Interesting if budget-constrained and Linux-curious; not the class default.

---

## Path E — Don’t buy: rent or share

| Option | When |
|---|---|
| Cloud GPU hour (RunPod, Vast, Lambda, etc.) | Occasional 70B experiments |
| University / lab machine | If access exists — say so clearly in class |
| Class one shared box | *technical suggestion:* one DGX Spark or 4090 workstation in the studio for booked slots |
| Strong cloud API + small local model | Default for most students |

Ecology session: local always-on 4090 can lose to shared efficient inference if utilisation is low — measure use, don’t moralise hardware alone.

---

## Decision guide for students

| Goal | Prefer |
|---|---|
| Learn agents + wiki, little money | Cloud API + laptop; no GPU purchase |
| Private / offline 7–13B | Any recent laptop; or used 3060/4060 |
| Serious local 70B chat | Mac Studio 64–128 GB **or** DGX Spark **or** multi-GPU NVIDIA |
| CUDA training / fine-tune | NVIDIA self-build or Spark |
| Quiet desk, Apple already home | Mac Studio / Mac mini high RAM |
| Lowest €/GB to *load* large quants | Watch used 3090 pairs vs mini-PC 128 GB deals |

---

## Course placement (*technical suggestion*)

| Session | What to cover |
|---|---|
| **03** | 10 min landscape: cloud vs local vs EU host; point here; no one must buy |
| **10** | Local as political/aesthetic choice; power; when renting wins |
| **11 studio** | Optional bookable machine if the department can host one |

Do **not** make purchasing hardware a course requirement.

---

## Sources (re-check before lecture)

- NVIDIA DGX Spark product page: https://www.nvidia.com/en-us/products/workstations/dgx-spark/  
- Apple Mac Studio: https://www.apple.com/mac-studio/  
- Comparative write-ups (street prices, May–Oct 2026): https://gpuinsights.net/unified-memory-ai-showdown-2026/ · https://www.compute-market.com/blog/nvidia-dgx-spark-vs-mac-studio-m4-max-local-ai-2026 · https://llmhardware.io/compare  
- VRAM rules of thumb: https://www.compute-market.com/tools/vram-requirements  

*todo:* add Austrian/EU shop links and watt-cost example (kWh × hours × €) before session 10.
