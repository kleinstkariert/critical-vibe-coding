---
title: AI and jobs — rising tide, early-career canaries, productivity by experience
date: 2026-10-26
tags:
  - research
  - labour
  - jobs
  - course
---

# AI and jobs — rising tide, early-career canaries, productivity by experience

Course handout for Session 01, Block 6 ([[../course/lectures/01-welcome-landscape-deep-dives/labour]]); earlier unit archived: [[../course/sessions/archive-13-session-plan/10-authorship-labour-platforms]]. Labels: *verified fact* | *nuance* | *claim*.

**Do not** teach Amodei “20% unemployment” or Goldman “300 million jobs” as settled forecasts. Prefer the papers below.

Cross-refs: [[../course/topics/visions-fears-regulation]] · IMF “exposed ≠ replaced” · [[ai-bubble-productivity-datacenter]] (macro CapEx ≠ labour outcomes).

---

## 1. Shape of automation — crashing wave vs rising tide (MIT FutureTech)

**Paper:** Mertens, Kuzee, Harris, Lyu, Li, Rosenfeld, Anto, Fleming, Thompson — *Crashing Waves vs. Rising Tides: Findings on AI Automation from Thousands of Worker Evaluations of Labor Market Tasks* (MIT FutureTech, July 2026).

| Link | Use |
|---|---|
| arXiv | https://arxiv.org/abs/2604.01363 |
| PDF (author site / CDN) | https://cdn.prod.website-files.com/6501f77fe3413fa9dbfbd69d/6a60d8d26a565e0d6983744a_Crashing_Waves_vs_Rising_Tides_%2021July26.pdf |
| Project page | https://futuretech.mit.edu/publication/crashing-waves-vs-rising-tides-preliminary-findings-on-ai-automation-from-thousands-of-worker-evaluations-of-labor-market-tasks |
| MIT Sloan explainer | https://mitsloan.mit.edu/ideas-made-to-matter/how-will-ai-automation-hit-a-crashing-wave-or-a-rising-tide |

**Frame (*verified fact* from abstract / intro):**

| Metaphor | Meaning | Labour implication |
|---|---|---|
| **Crashing wave** | Capability jumps: long tasks go from “almost never works” → “almost always works” overnight | Sudden occupation shocks; little adaptation time |
| **Rising tide** | Performance lifts **broadly** across short *and* long tasks; success–duration curve stays relatively **flat** | Gradual, diffuse pressure across many text-based jobs |

**Main empirical claims (*verified fact* — paper):**

- &gt;6,000 O*NET LLM-addressable tasks; &gt;60,000 expert worker evaluations; 41 models.
- Little evidence of crashing waves; **rising tides** dominate.
- 2024-Q2 → 2025-Q3: ~60% → &gt;70% success on ~1.5-hour text tasks (minimally sufficient, no human edit).
- If recent rates persist: by **2030**, most such tasks at minimally sufficient quality with **88–97%** success (*projection / upper-bound scenario* — authors flag possible slowdown).

**Class line:** Dario/Sam-style “entry-level wiped in five years” sounds like a **wave**. MIT’s map looks more like a **tide** — still serious, but not a one-year occupation wipeout.

**Nuance:** Rising tide ≠ “no labour impact.” Authors: institutions still need to respond to **broad**, multi-year change. Text/LLM-addressable tasks only — not robots on shop floors.

---

## 2. Who is already hit — Stanford “Canaries” (employment, not vibes)

**Paper:** Brynjolfsson, Chandar & Chen — *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence* (Stanford Digital Economy Lab).

| Link | Use |
|---|---|
| Lab page | https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/ |
| PDF (Nov 2025 vintage) | https://digitaleconomy.stanford.edu/app/uploads/2025/11/CanariesintheCoalMine_Nov25.pdf |
| Aug 2026 update note | https://digitaleconomy.stanford.edu/news/canariesaug26/ |
| Author primer | https://bharatchandar.substack.com/p/a-primer-on-canaries-in-the-coal |

**Core facts (*verified fact* — lab summary):**

1. **No** economy-wide mass displacement yet.
2. **Young workers (≈22–25)** in highly AI-exposed occupations fall behind: employment gap ~**19%** below the path of similarly aged workers in less-exposed jobs (June 2026 update; was ~15% mid-2025).
3. Gap **widens** over time.
4. Mechanism: mainly **less hiring**, not mass firings.
5. Declines concentrated where AI **automates** tasks; **augmenting** uses → flat/rising employment (esp. experienced).
6. Adjustment shows more in **employment** than base pay so far.

**Software / student-relevant:** ADP payroll — employment for **22–25 software developers** down ~**20%** from late-2022 peak through mid-2025 (author primer); older cohorts in same occupation stable or growing.

**Charts to show in class:** employment index by **age band** for software developers / customer service (Canaries figures; primer has a clear software-by-age chart).

**Class line:** Paradox for students — juniors **gain most productivity from AI tools** (next section) while **entry hiring** in AI-exposed white-collar tracks is the canary that falters.

---

## 3. Productivity by experience — the chart students care about

YouTube that stacks these claims (~13:20 onward): https://www.youtube.com/watch?v=UGVz615AQLA  
**Attribution cleanup:** the video mixes papers. Use the table — do not say “one Stanford paper” for all three.

### A. Call centres — *this* is the Stanford(-led) paper

**Brynjolfsson, Li & Raymond**, *Generative AI at Work*, NBER w31161 → *QJE* 2025.

- https://www.nber.org/papers/w31161 · PDF https://www.nber.org/system/files/working_papers/w31161/w31161.pdf  
- Published: https://academic.oup.com/qje/article/140/2/889/7990658  

| Result | Number |
|---|---|
| Average productivity (issues resolved / hour) | **+14–15%** |
| Novice / lower-skilled | about **+30–34%** |
| Experienced / high-skilled | **minimal** / small |

**Chart:** figure of treatment effect by pre-AI skill / tenure in that paper (novice bar ≫ experienced bar).

### B. Programmers — field RCTs (MIT / multi-firm) — best “junior vs senior” chart

**Cui, Demirer, Jaffe, Musolff, Peng, Salz**, *The Effects of Generative AI on High-Skilled Work: Evidence from Three Field Experiments with Software Developers*, *Management Science* (2026).

- DOI: https://doi.org/10.1287/mnsc.2025.00535  
- Author PDF: https://www.mertdemirer.com/Papers/Demirer_AI_productivity.pdf  
- MIT Sloan write-up: https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-affects-highly-skilled-workers  

| Result | Number |
|---|---|
| Pooled completed tasks (Copilot access) | **~+26%** |
| Short-tenure / junior | about **+27–39%** (IV; noisy) / junior level **~+21–40%** |
| Long-tenure / senior | about **+8–13%** / **~+7–16%** |

**Chart to project:** **Figure 6** in Demirer et al. (heterogeneity by tenure / level / pre-productivity) — junior bars taller than senior. Supplement ITT Figure 7 if needed.

### C. Programmers — early Copilot lab task (often mislabeled “Stanford”)

**Peng, Kalliamvakou, Cihon, Demirer**, *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*, arXiv:2302.06590 (Microsoft / GitHub).

- https://arxiv.org/abs/2302.06590  
- GitHub blog summary: https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/  

| Result | Number |
|---|---|
| Task completion time (JS HTTP server) | **~55.8% faster** with Copilot |
| Heterogeneity | **Less** professional experience → **larger** benefit (Table 1; *p*≈0.06 on years of experience) |

**Not Stanford.** Same co-author Demirer later on the multi-firm paper.

### D. Counterweight — experienced OSS can *slow down*

**METR**, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* — experienced maintainers on mature repos: AI allowed → **~19% slower**, against forecasts of speedup.

- https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf  

**Class line:** “AI makes juniors faster” is real in many RCTs; **context** (greenfield task vs giant mature codebase) flips the result. Seniors often gain less — and sometimes lose time reviewing AI.

---

## 4. How to talk about jobs in 60–90 seconds (Session 01)

1. **Shape:** rising tide (MIT), not overnight wave — still a fast tide.  
2. **Who:** early-career in exposed occupations = canary (Stanford ADP); overall employment still grows.  
3. **Paradox:** tools raise junior **output** most; firms hire fewer juniors in automating occupations.  
4. **Macro:** Acemoglu — modest TFP over ~10 years ([NBER w32487](https://www.nber.org/system/files/working_papers/w32487/w32487.pdf)); IMF “40% exposed” ≠ “40% unemployed.”

---

## 5. IMF / Spiegel reminder (from fact-check)

| Phrase | Means |
|---|---|
| **Exposed** | Tasks could be done *with* or *by* AI |
| **Replaced** | Job gone |

IMF: https://www.imf.org/en/blogs/articles/2024/01/14/ai-will-transform-the-global-economy-lets-make-sure-it-benefits-humanity  

Of exposed jobs in advanced economies: roughly half may **complement**, half may face **lower demand** — not a single unemployment number.

---

## Sources checklist (prefer primary)

| Theme | Cite |
|---|---|
| Wave vs tide | MIT FutureTech / arXiv:2604.01363 |
| Early-career employment | Stanford Canaries (Brynjolfsson–Chandar–Chen) |
| Productivity × experience (support) | Brynjolfsson–Li–Raymond QJE |
| Productivity × experience (code) | Demirer et al. *Management Science*; Peng et al. Copilot |
| Experienced slowdown | METR Early 2025 OSS RCT |
| Modest macro | Acemoglu *Simple macroeconomics of AI* |
