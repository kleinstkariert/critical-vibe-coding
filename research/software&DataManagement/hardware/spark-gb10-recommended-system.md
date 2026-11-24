---
title: Recommended production system, GB10 / DGX Spark class, 128 GB / 2 TB (Acer Veriton GN100)
audience: student
status: current
canonical: true
date: 2026-10-29
updated: 2026-11-23
last_verified: 2026-10-29
price_status: dated 2026-10-29 17:40, not rechecked on 2026-11-23
tags:
  - research
  - hardware
  - procurement
  - production
  - hermes
  - dated-prices
---

# Recommended departmental AI production system

Dated research. The source note was rechecked on **29 October 2026, 17:40**. Its price source was Geizhals.at (*dealer listing*). It also used the Hermes documentation and community Spark benchmarks. Read the [hardware README](README.md) for the evidence labels and the shared assumptions. Prices and specifications here are not current guarantees. Check them before any purchase.

## 1. What changed in the recheck

| Earlier draft | Result of the recheck |
|---|---|
| ASUS GX10 **4 TB**, €8,280 | **Not the best buy.** The 4 TB model costs **about €1,900 more** than 2 TB (ASUS 2 TB €6,551 against 4 TB €8,199) |
| ASUS 1-year warranty | The vendor page says 1 year. Geizhals lists 2 years for ASUS and Dell. **Acer lists 3 years (Bring-In)** |
| Budget ceiling €9,500 | **Ceiling €7,800** including UPS, cable and optional external model storage |
| "gpt-oss-120b about 42 tok/s" | Newer llama.cpp and vLLM results: **about 59 tok/s decode, about 2,400 tok/s prefill**. Qwen3-Coder-Next about **60–75 tok/s** |
| "Llama 3.3 70B Q4" as a target | **Drop for production.** Dense 70B is bandwidth-bound (about 2–5 tok/s on Spark). Use mixture-of-experts models |
| Hermes setup sketch | Needs `--jinja`, at least 64k context **per user slot**, an authenticated proxy, keep-alive and a long timeout. See section 6 |

## 2. Recommendation

**1 × Acer Veriton GN100 (NVIDIA DGX Spark platform), 128 GB LPDDR5x, 2 TB SSD, DGX OS.**

- Acer article: **DT.R6LEH.004**. Geizhals.at listing name: "Veriton GN100 (DGX Spark), GB10, 128GB RAM, 2TB SSD".
- Price (Geizhals.at, 29 October 2026, including VAT): **€6,299** at Cyberport.at, in stock in 2–4 working days. Other Austrian dealers were up to €6,898.
- Warranty: **3 years (Bring-In)**.

Alternatives with the same silicon (*dealer listing*, 29 October 2026):

| Option | 128 GB / SSD | Price AT | Warranty (Geizhals) |
|---|---|---:|---|
| **Acer Veriton GN100** | 2 TB | **€6,299** | **3 years** |
| ASUS Ascent GX10 GX10-GG0026BN | 2 TB | €6,551 | 2 years |
| Dell Pro Max GB10 FCM1253 | 2 TB | €6,779 | 2 years |
| ASUS GX10-GG0003BN | 1 TB | €6,251 | 2 years |
| NVIDIA Founders Edition | 4 TB | about €8,092 | per dealer |
| ASUS GX10-GG0027BN | 4 TB | €8,199 | 2 years |
| MSI EdgeXpert | 4 TB | €8,085 | not recorded |

**Why 2 TB, not 1 or 4 TB.** 1 TB is too small: gpt-oss-120b is about 65 GB, Qwen3-Coder-Next is about 46 GB at Q4, and you need room for several variants, the OS and containers. 4 TB costs €1,900 more. An external 4 TB NVMe enclosure or a NAS over 10 GbE gives the same cold storage for much less. Keep hot models on the internal 2 TB. (The cost of the external kit is in section 4.3. The older draft's figure was wrong.)

**Why Acer.** Lowest price and the longest warranty. Acer has **one** QSFP port, where ASUS and Dell have two. This does not matter unless you cluster four units.

Sources (dealer listings): [Acer GN100](https://geizhals.at/acer-veriton-gn100-dgx-spark-dt-r6leh-004-a3962656.html) · [ASUS Ascent](https://geizhals.at/asus-ascent-v219542.html) · [Dell Pro Max GB10](https://geizhals.at/dell-pro-max-with-gb10-dgx-spark-fcm1253-v226544.html)

## 3. Technical specification of the platform

*vendor specification* (NVIDIA pages, as recorded in the source note, not reopened on 23 November 2026).

| Component | Specification |
|---|---|
| SoC | NVIDIA **GB10 Grace Blackwell Superchip**, TDP 140 W |
| CPU | **20-core Arm**: 10 × Cortex-X925 and 10 × Cortex-A725 (Arm v9.2-A) |
| GPU | Blackwell, 5th-generation Tensor cores, 4th-generation RT cores |
| AI compute | Up to 1 PFLOP FP4 (sparse; vendor figure) |
| Memory | **128 GB LPDDR5x coherent unified**, 256-bit, **273 GB/s**, not upgradable |
| Storage | **2 TB M.2 NVMe PCIe** (this configuration) |
| Network | 10 GbE RJ-45; ConnectX-7 QSFP56 up to 200 Gb/s; Wi-Fi 7; Bluetooth 5.4 |
| I/O | 3–4 × USB-C 20 Gb/s (DP 2.1), HDMI 2.1, Kensington lock |
| OS | **NVIDIA DGX OS 7.6** (Ubuntu 24.04.5 base, Arm64), driver 580.x, CUDA 13.0 |
| Power | External **240 W** PSU |
| Size and weight | 150 × 150 × 50.5 mm, about 1.2 kg |
| Noise (NVIDIA declared) | 35 dB(A) sound power under load, 19 dB idle |

Sources: [NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/) · [DGX Spark hardware documentation](https://docs.nvidia.com/dgx/dgx-spark/hardware.html)

## 4. Purchase package, product links and ceiling

Prices: Geizhals Österreich, late October 2026, including VAT (*dealer listing*). Check again before ordering. The source note prefers invoiceable Austrian dealers (Cyberport.at, e-tec.at, galaxus.at and others).

### 4.1 Main system (required)

| Item | Exact product | Link | € |
|---|---|---|---:|
| **AI workstation** | Acer Veriton GN100, GB10, 128 GB, **2 TB**, article **DT.R6LEH.004** | [Geizhals listing](https://geizhals.at/acer-veriton-gn100-dgx-spark-dt-r6leh-004-a3962656.html) | **6,299** (Cyberport.at) |

### 4.2 Surrounding hardware (required or strongly recommended)

| Role | Exact product | Why this one | Link | € |
|---|---|---|---|---:|
| **UPS (lead)** | Digitus Professional Line Interactive **DN-170074**, 1000 VA / 600 W, USB and serial, **4× Schuko**, LCD | The GN100 uses an AC adapter brick, so Schuko outlets fit without adapters. 600 W real power covers the 240 W supply with margin. USB allows safe shutdown with Linux NUT | [Geizhals listing](https://geizhals.at/digitus-professional-line-interactive-1000va-dn-170074-a1928654.html) | **about 107** |
| **UPS (institutional alternative)** | APC Smart-UPS C **SMC1000IC**, 1000 VA / 600 W, USB and LAN, **8× C13** | Better management (SmartConnect, LAN). Needs C13 to Schuko adapters or IEC power cords for the brick. More than a single mini-PC needs | [Geizhals listing](https://geizhals.at/apc-smart-ups-c-1000va-smartconnect-smc1000ic-a1806897.html) | **about 523** |
| **Network cable, 2 m** | InLine slim Cat6a S/FTP LSZH patch cable, **2 m**, article **74902** | Cat6A for the 10 GbE port. LSZH for office or lab. Short desk run | [Geizhals listing](https://geizhals.at/inline-patchkabel-slim-lszh-flexibel-cat6a-s-ftp-rj-45-rj-45-2m-grau-74902-a3843088.html) | **about 8** |
| **Network cable, 5 m** | InLine slim Cat6a S/FTP LSZH patch cable, **5 m**, article **74905R** | Same specification, longer run to a rack or switch | [Geizhals listing](https://geizhals.at/inline-patchkabel-slim-lszh-flexibel-cat6a-s-ftp-rj-45-rj-45-5m-rot-74905r-a3843131.html) | **about 10** |

Buy **one** cable length, not both. Confirm that the switch port is Cat6A and 10 GbE capable. If it is not, the GN100 falls back to 1 GbE and still works.

**UPS note.** The Digitus unit is enough for this box. Choose APC only if the university already standardises on APC or NUT monitoring. Use USB shutdown with Network UPS Tools (NUT) on DGX OS or Ubuntu.

### 4.3 Optional external model storage (cold archive)

The internal 2 TB holds the OS and 2–3 large models. Extra cold storage is optional.

| Role | Exact product | Link | € |
|---|---|---|---:|
| **4 TB NVMe (lead)** | Samsung SSD **990 EVO Plus 4 TB**, M.2 2280, MZ-V9S4T0BW | [Geizhals listing](https://geizhals.at/samsung-ssd-990-evo-plus-4tb-mz-v9s4t0bw-mz-v9s4t0b-a3316847.html) | **about 614** |
| **4 TB NVMe (alternative)** | WD Black **SN850X 4 TB**, WDS400T2X0E (no heatsink) | [Geizhals listing](https://geizhals.at/western-digital-wd-black-sn850x-v106796.html) | **about 651** |
| **USB4 enclosure** | Lindy USB4 NVMe M.2 enclosure **43394** (2280/2260/2242, 40 Gb/s) | [Geizhals listing](https://geizhals.at/lindy-usb4-nvme-m-2-ssd-enclosure-43394-a3593513.html) | **about 55** |
| **Enclosure (alternative)** | DeLOCK USB4 M.2 NVMe enclosure **42034** | [Geizhals listing](https://geizhals.at/delock-externes-gehaeuse-fuer-m-2-nvme-ssd-42034-a3840301.html) | **about 89** |

**Recommended optional kit:** Samsung 990 EVO Plus 4 TB and Lindy 43394, about **€670**. Plug it into a GN100 USB-C port (USB4 or 20 Gb/s class). Use it for cold GGUF archives. Keep hot models on the internal 2 TB.

An earlier draft said €350–450 for this kit. That was **wrong at the prices of 29 October 2026**. A 4 TB NVMe drive alone was about €600 or more.

### 4.4 Totals

| Bundle | € |
|---|---:|
| Acer GN100 alone | 6,299–6,898 |
| Plus Digitus UPS and one Cat6A cable | **about 6,415–7,015** |
| Plus optional 4 TB external kit | **about 7,085–7,685** |
| APC UPS instead of Digitus | add about 416 against the Digitus path |
| **Request ceiling (Digitus path)** | **€7,800** |
| **Request ceiling (APC and external kit)** | **€8,300** |

Ask for a quote with: the written configuration (128 GB / 2 TB), the 3-year warranty and a price validity of at least 30 days.

## 5. Justification points in the draft

These points are the arguments of the original request. Some are *claims* that the note does not source.

1. **Autonomy.** *claim.* Another department's Spark is used mainly for training, so the department cannot rely on it for production. A departmental unit runs on the department's own schedule.
2. **No agent access to Academic AI.** *claim, not sourced in this note.* Academic AI has **no API key**, so Hermes (tool calling, scheduled, multi-step) cannot use it. Only a department-controlled OpenAI-compatible endpoint makes agents possible. The course page [Academic AI in Austria](../../../course/PRACTICE/03-models-and-providers/academic-ai-austria.md) describes the same limit with its own caveats.
3. **Privacy and data sovereignty.** Prompts, code, unpublished research and student work stay on university-controlled hardware. Access and logging are set locally. Local does not mean automatically compliant: access control, retention and data-protection assessment still apply.
4. **Long-term cost.** Routine and bulk agent work moves off Academic AI and commercial token budgets. The system is a fixed cost, and the marginal cost of local tokens is electricity. See section 5a.
5. **Reproducibility.** Pinned model, quantisation, context and server version. Results do not change when a cloud model is retired or updated.
6. **Capacity per euro and per watt.** The numbers are in the [README efficiency section](README.md#efficiency-only-conclusion).
7. **Resilience.** Outages, quota changes or price changes of cloud or Academic AI services do not stop department work. A fallback is optional (section 6).

### 5a. Long-term cost model (illustrative, replace with real numbers)

**Three-year fixed cost** (approximate):

| Item | € |
|---|---:|
| System, Digitus UPS and Cat6A cable | about 6,415–7,015 |
| Electricity: assumed 100 W average × 8,760 h = 876 kWh per year × €0.25 × 3 years (measure on the UPS or a metered PDU) | about 660 |
| **Total for 3 years** (without staff time and without the optional external SSD) | **about 7,100–7,700** |

**Break-even.** €7,400 ÷ 36 months is about **€205 per month**. If local inference replaces more than about €205 per month of Academic AI or commercial token use, the system is cheaper over three years.

Illustration only: the Hermes documentation estimates about USD 0.80 per heavy coding-agent session on a commercial model (about USD 24 per month for daily use per person). At about €0.75 per session, about **280 sessions per month** (for example 20 users × 14 sessions) equals break-even. The actual Academic AI tariff or quota and the monthly usage were not available when the note was written. Insert them before you use this calculation.

| Avoided token spend per month | Months to recover about €7,400 |
|---:|---:|
| €150 | about 49 |
| €205 | 36 |
| €300 | about 25 |
| €500 | about 15 |
| €1,000 | about 7 |

Limits, as the note says: local open-weight models do not match the best frontier models on the hardest tasks. The saving applies to the routine and bulk share. If Academic AI tokens are not charged to the department's budget, the benefit is capacity relief on the shared service, not cash. Staff time for operation is not costed.

**Inconsistency in the source note.** The example text in section 8 gives a three-year total of about €7,200–8,000 and a break-even of about €210 per month. The worked calculation above gives about €7,100–7,700 and about €205 per month. The source does not explain the difference. The calculation above matches its own arithmetic (*uncertainty* for the section 8 figures).

## 6. Hermes production setup

Checked in the source note against the Hermes documentation (Local Models and the Local Ollama guide). Hermes needs an OpenAI-compatible endpoint, **tool calling**, **at least 64k context** and long timeouts for prefill. The desktop "Local Models" button manages llama.cpp **on the user's own machine**. A **shared server uses a custom endpoint**.

**Architecture**

```text
Hermes (staff and student machines)
   |  HTTPS + internal token (campus LAN or VPN)
   v
Reverse proxy (TLS, auth, rate limit)  -->  llama-server  -->  models on the Spark NVMe
```

**Server** (a systemd service on the Spark system). This is a starting point to validate in the acceptance test.

```bash
llama-server \
  -hf Qwen/Qwen3-Coder-Next-GGUF:Q4_K_M \
  --jinja \
  --host 127.0.0.1 --port 8080 \
  -fa on --no-mmap \
  -np 4 -c 262144
```

- Pick the quantisation on the model page. Q4_K_M is about 46 GB.
- `--jinja` is **required**. Without it, tool calls appear as plain text.
- `-c` is the **total** context. With `-np N` slots, each user gets `c/N`. Here: 4 slots × 64k. Hermes needs at least 64k per session.
- Bind to localhost. Expose the server only through the authenticated reverse proxy. Do not open the model port to the network.
- Ollama is an alternative. Set `num_ctx` to at least 64000 and `OLLAMA_KEEP_ALIVE=24h`.
- vLLM (NVFP4 or MXFP4 builds) gives better aggregate throughput. Qwen3-Coder-Next reached about 289 tok/s aggregate at 8 concurrent streams in community tests. It needs Arm64-specific containers. Evaluate it after the llama.cpp baseline works.

**Hermes client configuration** (`hermes setup`, then Custom Endpoint, or `~/.hermes/config.yaml`):

```yaml
model:
  default: "qwen3-coder-next"
  provider: "custom"
  base_url: "https://llm.<department-host>/v1"   # internal URL
```

- The API key field holds an **internal access token**, not a commercial key.
- In `~/.hermes/.env`: `HERMES_API_TIMEOUT=1800` (long prefill with the fixed Hermes system and tool prompt).
- Use `hermes prompt-size` and `hermes tools` to trim the fixed prompt.
- **Fallbacks** (`fallback_providers`) send data to an external provider. **Disable them for confidential projects.** Enable them only for non-sensitive work.
- Optional: run `hermes gateway` (Discord or Telegram bots) on the Spark system for always-on department agents. Use separate service accounts.

**Models** (mixture-of-experts preferred, because decode speed is limited by the 273 GB/s bandwidth). The fit table for other setups is in the [capability matrix](llm-coding-capability-matrix.md).

| Role | Model | Size | Expected decode (*community measurement*) |
|---|---|---:|---|
| Primary coding agent | Qwen3-Coder-Next 80B-A3B (non-thinking) | about 46 GB Q4 | about 60–75 tok/s, single stream |
| Large reasoning and agent | gpt-oss-120b (MXFP4; lowest reasoning effort for agents) | about 59–65 GB | about 59 tok/s; prefill about 2,400 tok/s |
| Fast small agent | GLM-4.7-Flash 30B-A3B | about 18 GB | high (no figure recorded) |
| Alternative | Devstral Small 2 24B, Qwen3.6 27B (dense, slower) | 15–17 GB | no figure recorded |
| Avoid in production | Dense 70B (Llama 3.3 70B) | about 40 GB | about 2–5 tok/s |

Practical memory is about 110 GB usable. Run **one large model and one small model**, not two large ones.

Sources (benchmarks are community measurements, not controlled tests): [llama.cpp discussion 16578](https://github.com/ggml-org/llama.cpp/discussions/16578) · [gpuwerk benchmarks](https://gpuwerk.com/docs/benchmarks/) · [Hermes Local Ollama guide](https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup) · [Hermes Local Models](https://hermes-agent.nousresearch.com/docs/user-guide/local-models)

**Operations**

- Fixed hostname or IP. Firewall to the campus LAN or VPN. TLS. Per-user or per-project tokens.
- No raw prompt logging by default. Document diagnostic logging and retention.
- Monthly DGX OS and container updates after a short staging test. Keep configuration in Git and secrets outside it.
- Monitoring: availability, memory, temperature, disk, request volume, metered power.
- A named responsible person. A UPS with safe shutdown. A backup of configuration and project data (models can be downloaded again).

## 7. Arm64 acceptance test (before or right after purchase)

The GB10 is **Arm64**. llama.cpp (CUDA arm64) and Hermes (arm64 Linux) are supported, but some third-party binaries and containers have no Arm64 build.

1. Ask the other department for a **1–2 hour test slot**, or agree test and return terms with the dealer.
2. Run `llama-server` with the flags above. Connect Hermes through the custom endpoint.
3. Test tool calls (file edit, shell, web), 64k or more context, and 4 concurrent sessions.
4. Record time to first token, tok/s, memory use and stability for Qwen3-Coder-Next and gpt-oss-120b.
5. Test every container and package that your projects need on Arm64.

## 8. Example justification text

This is the text of the original draft. The price is the one of 29 October 2026. Insert the Academic AI figures where marked. See the note on inconsistent totals in section 5a.

> We request one dedicated NVIDIA DGX Spark-class system (Acer Veriton GN100, GB10 Grace Blackwell, 128 GB unified memory, 2 TB SSD, 3-year warranty; Geizhals.at €6,299 including VAT, 29 October 2026) for local AI production and Hermes agent infrastructure in our department. The DGX Spark owned by another department is used mainly for model training and cannot provide the continuous availability needed for our production work. The university's Academic AI service provides no API key, so it cannot be used by Hermes or other automated, tool-using applications.
>
> A departmental system gives us operational autonomy and a controlled OpenAI-compatible inference endpoint. Source code, unpublished research and student work remain on university-controlled infrastructure with locally defined access and retention rules. Routine and bulk agent workloads run locally instead of consuming Academic AI or commercial token budgets; after the one-time purchase, the marginal cost is electricity. Over three years the total cost is approximately €7,200–8,000 including UPS and electricity, which is recovered if the system replaces about €210 per month of token consumption [insert Academic AI quota or tariff and expected usage]. The 128 GB unified memory runs current coding and agent models (for example Qwen3-Coder-Next, gpt-oss-120b) that do not fit on 48–72 GB consumer-GPU workstations, at a 240 W power supply instead of 0.7–0.9 kW.
>
> We request a ceiling of **€7,800 including VAT** for the system, UPS, network cable and optional external model storage, and will validate the Hermes and Arm64 software stack on delivery.

## 9. Decision requested in the draft

Approve **1 × Acer Veriton GN100 (DT.R6LEH.004), 128 GB / 2 TB, 3-year warranty**, plus UPS, network cable and optional external storage, with a **ceiling of €7,800 including VAT** and a quote validity of at least 30 days.
