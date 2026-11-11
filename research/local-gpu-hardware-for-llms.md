---
title: Local hardware for larger LLMs
date: 2026-10-20
updated: 2026-10-27
tags:
  - research
  - hardware
  - local-llm
  - course
---

# Local hardware for larger LLMs

Research note + setup map for Critical Vibe Coding. Labels: *verified fact* | *street-price estimate* | *technical suggestion* | *nuance*.  
Prices move weekly — re-check before telling students a number. Currency roughly **USD/EUR street / MSRP class, mid–late 2026** unless noted.

**Session home:** [[../course/sessions/03-hardware-open-models-prompting]] · student howto [[../course/setup/howto-local-llm-hardware]]  
Also pointed from: session [[../course/sessions/02-agent-harness-and-wiki-architecture]] (model landscape preview) · [[../course/sessions/06-agent-as-interface]] (ecology input, not build guide) · [[../course/concepts/prompting-and-model-choice]] §§6 to 7.

Hermes docs (software side): [Local Models](https://hermes-agent.nousresearch.com/docs/user-guide/local-models) · [Ollama guide](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup) · [Providers](https://hermes-agent.nousresearch.com/docs/integrations/providers)

---

## 1. What “fits” — memory math

Rule of thumb for **weights only** (KV-cache / long context needs more):

| Precision | Approx. GB per billion parameters |
|---|---|
| FP16 / BF16 | ~2 GB |
| 8-bit | ~1 GB |
| 4-bit (Q4) | ~0.5 GB |

| Model class | Q4 weights | Practical machine memory |
|---|---|---|
| 7–9B | ~4–6 GB | Laptop GPU / 16–24 GB unified OK |
| 27–34B | ~16–20 GB | 24 GB discrete GPU or 32–48 GB unified |
| 70B | ~40–44 GB | **≥48–64 GB** usable; 128 GB comfortable |
| 70B Q8 / large MoE | 80 GB+ | 96–192 GB unified or multi-GPU |

*nuance:* Advertised RAM ≠ usable for weights. Discrete GPUs lose VRAM to the display driver; unified-memory machines share RAM with the OS (plan ~70–80% of sticker for the model). Hermes Local Models prices catalog builds against your machine and prefers ≥4-bit.

Inference stacks: **llama.cpp / Ollama / LM Studio** (easy) · **Hermes managed llama.cpp** · **vLLM / TensorRT-LLM** (NVIDIA serve) · **MLX** (Apple).

---

## 2. Path A — Ready-made: unified / coherent memory

These machines **share one big memory pool** between CPU and GPU (or GPU-coherent fabric). That is why a 128 GB box can load models a 24 GB GeForce cannot — even if peak FLOPS look lower.

### A1 — Apple Silicon (Mac mini / Studio)

| Config (examples) | Unified memory | Rough fit | Price class (*estimate*) |
|---|---|---|---|
| Mac mini M4/M5 Pro | 24–64 GB | 7–34B; 70B Q4 only at high RAM | check Apple |
| Mac Studio Max | up to ~128 GB | 70B Q4 comfortable at 64–128 GB | often ~$2 k–$5 k+ |
| Mac Studio Ultra | high bandwidth (often **≫** Spark), large RAM | 70B Q8 / larger experiments | often **$5 k–$9 k+** |

- Stack: **MLX**, Ollama Metal, llama.cpp Metal, Hermes `backend: metal`.  
- **Pros:** Quiet, efficient, artists often already on Mac; soldered RAM → buy enough on day one.  
- **Cons:** No CUDA; some training stacks second-class.

Links: [Mac Studio](https://www.apple.com/mac-studio/) · [MLX](https://github.com/ml-explore/mlx)

### A2 — NVIDIA DGX Spark (GB10)

- **What:** Deskside box, **64 or 128 GB** coherent unified LPDDR5x, Grace Blackwell GB10, DGX OS (Ubuntu), CUDA / NIM path. ~240 W class, ~1.2 kg.  
- **MSRP class:** launched ~**$3 999**; later listings often ~**$4 699** (confirm [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)).  
- **Bandwidth:** ~**273 GB/s** — solid, often **below** top Mac Ultra for pure chat tok/s; wins on **CUDA** fine-tune / serve ecosystem.  
- **Networking:** ConnectX-7; docs describe clustering **up to four** Sparks for larger / multi-agent workloads (NVIDIA Sync).  
- **Fits:** 70B Q4 in memory terms; marketing cites up to ~200B-class at aggressive quants — treat as *claim*, verify for your stack.

### A3 — Other ready-mades

| Box | Role | Caution |
|---|---|---|
| OEM “AI mini PCs” (ASUS Ascent-class, etc.) | Spark-like GB10 partners | Check real unified GB, not FLOPS slides |
| Jetson AGX Thor (128 GB class) | **Robotics / edge deploy**, not a cheaper Spark | Same bandwidth class ≠ desktop LLM value; street price can exceed Spark |
| AMD Ryzen AI Max+ 395 + 128 GB mini PCs | Capacity competitor ~$2–3.5 k | ROCm/Vulkan more brittle than CUDA/MLX |

---

## 3. Path B — Self-built discrete GPU (single card)

Best €/tok/s when the **model fits in one card’s VRAM**.

| Tier | Example GPU | VRAM | Fits (Q4, rough) | GPU street | Whole PC ballpark |
|---|---|---|---|---|---|
| Entry | RTX 4060 / 4060 Ti | 8–16 GB | 7–13B | €300–500 | €900–1 400 |
| Sweet used/new | RTX 3090 / 4090 | 24 GB | ~30–34B; 70B only with offload | 3090 used varies; 4090 €1.5–2.2 k | €2–3.5 k |
| Current high | RTX 5090 | 32 GB | larger 30B; 70B still tight | check live | €3–4.5 k+ |

**Build checklist:** PSU headroom · case airflow · GPU length · fast NVMe · Linux preferred for servers · noise/heat/electricity (AT/EU kWh).

Ollama NVIDIA support table (compute capability / drivers): https://docs.ollama.com/gpu

---

## 4. Path C — DIY multi-GPU “rack” / workstation

### What multi-GPU actually does (*verified direction*)

**It does not merge VRAM into one Apple-style unified pool.** Software **splits** the model:

| Mode | Idea | Interconnect |
|---|---|---|
| **Pipeline / layer split** (llama.cpp default `-sm layer`) | Each GPU holds a contiguous slice of layers; activations pass GPU→GPU | Works fine over **PCIe**; NVLink optional |
| **Tensor parallel** (vLLM `--tensor-parallel-size N`; llama.cpp `-sm tensor` experimental) | Each layer’s matrices split across GPUs; more communication per token | Prefers **NVLink** / fast fabric; PCIe works but slower |

So **2×24 GB ≈ 48 GB of weight capacity**, not “one 48 GB GPU.”

### Hardware for a 2–4 GPU rig (*street-price estimate*)

| Part               | Guidance                                                                                                                                                                                                                      |     |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| **GPUs**           | Matched VRAM ideal. Popular: **2× RTX 3090 24 GB** (used; last GeForce with consumer NVLink bridge) · 2× 4090/5090 (PCIe only — NVIDIA dropped NVLink on 40/50 consumer) · workstation A6000-class if budget allows           |     |
| **Motherboard**    | Enough **full-length** PCIe slots at good lane width (x16/x8/x8/x8). Check bifurcation; avoid “x4 decorative” slots for heavy cards. NVIDIA playbook: [Build a Multi-GPU AI PC](https://build.nvidia.com/playbooks/multi-gpu) |     |
| **PSU**            | Sum TDP + CPU + 20–30% headroom; quality cables; often **1200–1600 W** for dual 4090-class                                                                                                                                    |     |
| **Case / cooling** | Open-air or large tower; GPU spacing; dust; noise                                                                                                                                                                             |     |
| **CPU / RAM**      | Enough host RAM for KV spill / OS (64–128 GB system RAM common on serious rigs)                                                                                                                                               |     |
| **Storage**        | Fast NVMe; 70B Q4 is tens of GB per quant                                                                                                                                                                                     |     |
| **Ballpark**       | Dual 3090 used workstation often **€3–6 k**; dual 4090 new **€5–9 k+**; 4-GPU / enterprise beyond most students                                                                                                               |     |

### How to connect and “sync” memory

1. Install drivers; confirm all cards: `nvidia-smi` · topology: `nvidia-smi topo -m`  
2. **Ollama:** auto-spreads when one GPU is too small; limit with `CUDA_VISIBLE_DEVICES` (https://docs.ollama.com/gpu)  
3. **llama.cpp:**  
   - Layer: `llama-server -m model.gguf -ngl all -sm layer`  
   - Unequal cards: `-ts 2,1` style proportions  
   - Docs: https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md  
4. **vLLM:** `vllm serve MODEL --tensor-parallel-size 2` (or pipeline parallel if no NVLink)  
5. Point Hermes at OpenAI-compatible URL (`http://localhost:11434/v1` or llama-server `:8080/v1`)

*nuance:* NVLink helps **tensor-parallel throughput** more than single-user layer-split chat. For art-studio “one agent” workloads, **layer split over PCIe** is usually enough.

### Tutorials (bookmark)

| Resource | URL |
|---|---|
| llama.cpp multi-GPU | https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md |
| CanItRun — split modes & NVLink (2026) | https://canitrun.dev/guides/multi-gpu-setups/ |
| MyAIHardware — vLLM + llama.cpp | https://www.myaihardware.com/tutorial/multi-gpu-setup |
| LLM Hardware Guide — multi-GPU | https://llmhardwareguide.com/multi-gpu-llm |
| NVIDIA multi-GPU PC playbook | https://build.nvidia.com/playbooks/multi-gpu |
| Ollama GPU docs | https://docs.ollama.com/gpu |
| Hermes + Ollama | https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup |

### Institutional shopping lists (teacher vault — not public)

Full **€6–10k** open-frame shopping lists (dual/triple 3090, dual 4090, 5090 ceiling), coding-model matrix, and **DIY vs DGX Spark** justification for budget letters live in the private Obsidian folder:

`KnowledgeBaseObsidian/Teaching/CriticalVibeCoding/hardware-procurement/`  
(start at `00-index-budget-vs-spark.md`)

*nuance for students:* DIY multi-GPU is often best **€/tok/s** for 70B Q4 inference and for **teaching how to build**; Spark wins on **quiet coherent 128 GB** and turnkey training — complements, not clones.

---

## 5. Open downloadable models — what makes sense

Prefer **instruct / tool-calling** builds for Hermes agents (plain chat models cannot drive tools reliably). Names age — check Ollama library / Hugging Face / Hermes catalog at class time.

| Hardware you have | Sensible open models (*examples*) | Role |
|---|---|---|
| 8–16 GB VRAM / 16–24 GB unified | Qwen3 4–8B, Llama 3.x 8B, Gemma 2 9B, Phi-class | Daily chat; light agent if tool-tuned |
| 24 GB / 32–48 GB unified | Qwen3 14–32B, Gemma 27–31B tool models, DeepSeek-R1 **distill 14–32B** | Strong local agent; toggle thinking |
| 48–64 GB (2×24 or 64 GB unified) | 70B Q4 (Llama 3.3 70B, Qwen2.5/3 70B-class) | Serious offline; slower on dual consumer |
| 128 GB unified (Spark / Mac / mini-PC) | 70B Q4–Q8; some MoE / 100B+ at Q4 | Comfortable large local; cluster Sparks for bigger |
| CPU-only | ≤3–8B Q4 | Learning only; slow agent prefill |

**Hermes-specific:** Desktop **Local Models** auto-picks quant vs your GPU; curated catalog + Hugging Face GGUF. Manual Ollama: raise context (`num_ctx` ≥ 64k for agent work), keep-alive, tool-capable model — see Hermes Ollama guide.

**Thinking models:** Use instruct default; enable thinking only for hard tasks ([[../course/concepts/prompting-and-model-choice#5-thinking-on--off--save-monologue-tokens]]).

---

## 6. Decision guide (students)

| Goal                              | Prefer                                                     |
| --------------------------------- | ---------------------------------------------------------- |
| Learn agents + wiki, little money | Cloud API + laptop; **no** GPU purchase                    |
| Private / offline 7–13B           | Laptop or used 3060/4060; Hermes Local / Ollama            |
| Quiet desk, already on Mac        | High-RAM Mac mini/Studio + MLX/Ollama                      |
| CUDA fine-tune / serve            | Self-build NVIDIA or DGX Spark                             |
| Load 70B without DIY pain         | Spark 128 GB **or** Mac Studio 64–128 GB **or** dual 24 GB |
| Lowest €/GB to *load*             | Watch used 3090 pairs vs 128 GB mini-PC deals              |
| Occasional big model              | Rent GPU hour (RunPod / Vast / …)                          |

**Course rule:** Buying hardware is **never** required. Session 03 teaches *how*; the Session 06 ecology input asks *whether*.

---

## 7. Sources (re-check before lecture)

- NVIDIA DGX Spark: https://www.nvidia.com/en-us/products/workstations/dgx-spark/  
- Apple Mac Studio: https://www.apple.com/mac-studio/  
- Ollama GPU: https://docs.ollama.com/gpu  
- Hermes Local Models / Ollama: links at top  
- Comparative landscape write-ups (volatile): https://llmhardware.io/compare · https://presenc.ai/research/local-llm-hardware-landscape-2026  
- VRAM rules of thumb: https://www.compute-market.com/tools/vram-requirements  

*todo:* Austrian/EU shop links + kWh cost example before ecology session.
