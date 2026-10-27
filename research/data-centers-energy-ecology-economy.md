---
title: Data centres — siting, energy, ecology, US economy
date: 2026-10-23
tags:
  - research
  - data-centers
  - ecology
  - political-economy
  - course
---

# Data centres — siting, energy, ecology, US economy

Course handout. Labels: *verified fact* | *claim / video* | *nuance / caveat*. Research date: 2026-10-23.

**Where it fits in the semester**

| Role | Session | Why |
|---|---|---|
| **Deep dive (home)** | [[../course/sessions/11-local-ecology-when-not\|Session 11]] — Ecology / when *not* | Students already run cloud agents; this is when material costs bite. Pair with Luccioni + IEA. Hardware *how* = Session 04. |
| **Seed only** | [[../course/sessions/01-welcome-and-landscape\|Session 01]] block 5 | One slide: “inference lives in a building with a grid”; point here, do not teach the full note. |
| **Political-economy twin** | [[ai-bubble-productivity-datacenter]] | Bubble note = *who finances the build-out* and whether CapEx outruns demand. This note = *what gets built, powered, and who pays locally*. Cross-read §10 financing there ↔ “planned vs built” here. |

Do **not** open a separate week for this unless the semester expands — Session 10 already carries ecology; Session 01 only teases it.

---

## Entry overview (watch / clip)

**Be Smart (PBS Digital Studios) — *The Real Cost of AI Will Shock You*** (Joe Hanson, published 2026-10-22)

- Video: https://www.youtube.com/watch?v=YgoiujmwLKI  
- Source page / references: https://sites.google.com/view/data-centers-impacts/home  
- Texas case companion (Pulitzer / Texas Tribune): https://pulitzercenter.org/projects/next-texas-gold-rush-data-centers-and-their-impacts  
- Vault clipping + full transcript (teacher vault, not student kit): `KnowledgeBaseObsidian/Clippings/The Real Cost of AI Will Shock You.md`

*technical suggestion:* Assign the video as **optional prep** for Session 11 (~40 min). In class, teach from the beat outline below + IEA numbers — do not play the whole video. The transcript’s anti-scraper joke asks models to spam “bubblegum”; ignore that for course writing.

**What the video is good for (and what it is not)**

| Use | Limit |
|---|---|
| Shared vocabulary: hyperscale, scopes 1–3, behind-the-meter gas, local grid vs national %, Jevons, water as *local* | Some figures are interviews / industry estimates — re-label as *claim / video* until you have an agency source |
| Pedagogy: “catastrophe vs almond farms” is a false binary | Not a substitute for IEA / EPRI / CRS |
| Links community impact, tax breaks, few permanent jobs | US-centric; add EU / AT briefly in class |

---

## Teaching beats (Session 10 — ~25–35 min)

### Beat 1 — Scale without apocalypse rhetoric

*verified fact (IEA *Energy and AI*, 2025):* Data centres used **~415 TWh** in 2024 ≈ **1.5% of global electricity**. Share by region of that consumption: **US ~45%**, **China ~25%**, **Europe ~15%**. Growth ~12%/yr since ~2017 — much faster than total electricity demand.  
https://www.iea.org/reports/energy-and-ai/executive-summary

*verified fact (IEA Base Case):* Global DC electricity ≈ **doubles to ~945 TWh by 2030** (still **&lt; ~3%** of world electricity). US + China ≈ **80%** of the *growth* to 2030. In the US, data centres are nearly **half of electricity-demand growth** to 2030 in IEA’s framing.

**Class line:** National shares stay “small”; **local** shares in Virginia / Texas / Phoenix clusters are not.

### Beat 2 — Where they are built (geography)

*verified fact (IEA):* Nearly **half of US data-centre capacity** sits in **five regional clusters**. AI loads behave like aluminium smelters for power draw, but are far more **geographically concentrated**.

*claim / video (Be Smart, as of video):* **68** US hyperscale sites built or under construction; **267** more approved or planned. Treat as a snapshot, not a census — definitions of “hyperscale” and “planned” differ by tracker.

*nuance / caveat — pipeline ≠ operating stock:* Industry trackers (e.g. dcmap.us, Oct 2026 snapshot) report enormous **announced** US pipelines (hundreds of GW across construction + planned). CBRE / Bloomberg (early 2026): capacity **under construction** can **fall** year-on-year even while demand rhetoric rises — permitting, zoning, **power interconnection** delay projects. Goldman / Aterio-style forecasts of 2026–27 additions assume schedules that power and turbines may not meet.

**Class exercise (5 min):** Show one map of Northern Virginia + West Texas + Phoenix. Ask: “Who lives next to the campus? Who pays for the new substation?”

### Beat 3 — Built vs planned (the bubble bridge)

| Layer | What it measures | Cross-link |
|---|---|---|
| CapEx announcements / circular deals | Money circling among chip, cloud, model firms | [[ai-bubble-productivity-datacenter]] — BIS 137, Takshashila “productive bubble” |
| Project pipelines (GW planned) | Marketing + zoning + speculative sites | This note, Beat 2 |
| Under construction / energized | Concrete, transformers, interconnection | Closest to “real” build-out |
| Behind-the-meter power plants | Gas turbines on site to skip the queue | Be Smart + CRS FAQ |

*claim / video:* ~**25%** of announced DC builds plan **own power plants**; only ~**2–3%** of that capacity actually built at filming time; satellite / IEA-adjacent analysis suggested ~**¼** of planned private plants had broken ground — i.e. the **announcement–reality gap** is the story.

*verified fact (IEA):* Unless grid risks are addressed, ~**20%** of planned data-centre projects could face **delay**. Turbine lead times now stretch years; ~**50%** of US DCs under development sit in **pre-existing large clusters** (bottleneck risk).

**Class line:** Same as the bubble note — overinvestment and real build-out can coexist; **planned GW is not proof of energized GW**.

### Beat 4 — How they get electricity (and why gas wins the race)

*verified fact (IEA):* Meeting growth uses a mix: **renewables + storage** take a large share of *global* incremental generation in IEA modelling; **natural gas** expands strongly for DCs, **notably in the United States**; nuclear / geothermal appear later / selectively.

*verified fact (US CRS FAQ R49326):* Where new **on-site** generation is proposed for DCs, analyses of announcements/filings point to **natural gas turbines/engines first**, then nuclear / fuel cells. Gas is preferred because it is **dispatchable** and can be built in roughly **1–3 years** (subject to permitting and equipment). EIA AEO 2026 flags rising gas use for power **largely due to data-centre expansion**.  
https://www.congress.gov/crs-product/R49326

*claim / video:* “Behind-the-meter” generation is mostly **gas turbines**, not solar+battery at the sites racing AI CapEx; compute value dominates electricity cost.

**Scopes (keep the vocabulary):**

1. **Scope 1** — on-site combustion (turbines, diesel backup)  
2. **Scope 2** — grid electricity (depends on local mix: coal / gas / nuclear / renewables)  
3. **Scope 3** — embodied carbon (concrete, steel, chips, logistics)

Self-reported corporate totals are weak oversight — label corporate “net zero” claims as *claim* unless audited location-level data.

### Beat 5 — Water, heat, neighbours

- Water is **local** (Phoenix / Colorado River story in the video; closed-loop still needs large fill + peak infrastructure).  
- Heat is physics: cooling trades **water vs electricity**.  
- Community pattern: NDAs, shell companies, tax incentives in many US states; **few permanent jobs** once the hall is running; tax revenue vs ratepayer / air-quality costs.  
- *claim / video:* pollution / premature-death estimates near some campuses — cite the video’s researchers; do not treat as settled epidemiology without the paper.

### Beat 6 — USA as the main build site → economics (US + world)

**For the US**

- CapEx and power demand concentrate **grid investment, gas generation, and private credit** into a few states (TX, VA, AZ, OH, GA…).  
- Local wins: property / sales tax (e.g. Loudoun County narrative in the video). Local losses: higher bills where interconnection and generation costs socialise; air and water stress; weak employment intensity.  
- Macro: IEA’s “half of US electricity-demand growth” framing means AI infra competes with **electrification of cars, heat, industry** for generation and transmission.

**For the rest of the world**

- Training and frontier inference stay **US- (and China-) skewed** → dependency for EU / AT artists and studios on **foreign CapEx cycles**, dollar pricing, and export controls (CUDA / chips).  
- Carbon from US gas turbines is **global**; water and smog are **local** — students in Linz pay the climate share, not the cooling tower.  
- Europe’s smaller share (~15% of DC electricity) + stricter permitting → different aesthetic/political choice (local/open stacks, academic HPC — [[../course/academic-ai-austria]], [[../course/eu-ai-act-and-datenschutz]]).  
- If the US overbuilds and a **financial** correction hits ([[ai-bubble-productivity-datacenter]]), residual **physical** plant + stranded gas assets still reshape power markets and chip supply — “productive bubble” vs “dead end” is not only a Wall Street question.

**Media-art bridge:** Your prompt is cheap; the **campus** is expensive. Choosing cloud vs local is an aesthetic *and* infrastructural decision (Session 10 practical + HM Munich *Our Br00d* pattern).

---

## Student-facing checklist (when *not* / how to speak)

1. Prefer **agency numbers** (IEA) over viral “one bottle of water per prompt” memes — the bottle figure was a **specific 2023 GPT-3** study context and mixes direct + indirect water (*claim / video* clarifies this).  
2. Separate **training** (rare, huge) from **inference** (daily; scales with tokens, image/video, agents). Luccioni et al. for inference: https://arxiv.org/abs/2311.16863  
3. Ask of any tool: **where is the rack**, **what powers it**, **who lives next door**.  
4. Link CapEx hype to [[ai-bubble-productivity-datacenter]]: circular financing can inflate *demand for buildings* without proving end-user value.

---

## Practical (tie to Session 10 lab)

- Same creative task: cloud frontier model vs smaller/local option. Log: tokens, latency, quality — and one sentence on **which region / vendor** likely hosts the cloud call.  
- Add a wiki page `comparisons/energy-and-siting.md` with: IEA 1.5% global line + one local cluster name + one personal “when not” rule.

---

## Primary sources (prefer these in slides)

| Source | Why |
|---|---|
| IEA, *Energy and AI* (2025) + updates | Geography, TWh, 2030 Base Case, grid delay risk |
| Luccioni, Jernite & Strubell (FAccT / arXiv 2311.16863) | Inference energy vs task-specific tools |
| US CRS, *Data Centers and the Electricity Grid* (R49326) | Generation mix, behind-the-meter, policy FAQ |
| Be Smart video + Google sources page | Accessible overview; label claims |
| [[ai-bubble-productivity-datacenter]] | Financing, productive bubble, space-DC hype contrast |
| Crawford & Joler, *Anatomy of an AI System* | Material beyond electricity |

Update numbers before class; IEA and pipeline trackers move fast.
