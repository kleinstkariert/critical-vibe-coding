---
title: Academic AI in Austria — access for this course
date: 2026-10-21
tags:
  - course
  - academic-ai
  - austria
---

# Academic AI in Austria — access for this course

English course note. Official portals may be German/English. Labels: *verified fact* | *technical suggestion* | *todo*.

Use with: session [[sessions/03-models-prompting-install]] · hardware [[../research/local-gpu-hardware-for-llms]] · regulation [[eu-ai-act-and-datenschutz]].

---

## What “academic AI” means here

| Path | Typical offer | Fits Hermes / agents? |
|---|---|---|
| **University chat / web portal** | Browser UI for a hosted model (campus login) | Usually **no** — no API key for agents |
| **Academic API / gateway** | Keyed endpoint for research projects | Rare; often proposal-gated |
| **HPC / AI Factory GPU hours** | Train / fine-tune on EuroHPC or national systems | **Not** a drop-in ChatGPT replacement; batch jobs, not daily agent chat |
| **Commercial API** (OpenAI, Anthropic, …) | Keys students buy or get via credits | Yes — default agent path in this course |
| **Local / own hardware** | Run open weights yourself | Yes — see [[../research/local-gpu-hardware-for-llms]] |

*requirement for class honesty:* If Kunstuni / UFG academic AI is **chat-only** and has **no agent API**, say so in session 3. Do not pretend Hermes can “just use” it.

---

## Current working assumption (update after contacts)

*technical suggestion until verified:*

- Students should plan on **personal / commercial API keys**, **EU-hosted commercial**, or **local models** for agent work.
- Campus academic AI (if any) is a **bonus for interactive exploration**, not the agent backbone — unless we confirm an API or self-hosted endpoint.
- Kunstuniversität Linz is **not** listed among ASC free partner universities (TU Wien, Uni Wien, BOKU, Innsbruck, TU Graz, Uni Graz, JKU, …). Access to ASC would likely be **pay-per-use** or via a partner project — inquire; do not promise free HPC.

ASC access overview: https://asc.ac.at/access/

---

## AI Factory Austria (AI:AT) — check this

National AI Factory under EuroHPC JU (AIT + Advanced Computing Austria + university consortium). English site: https://ai-at.eu/en/  
*(German root https://ai-at.eu/ may be temporarily offline for PHP security patches — use `/en/`.)*

### What they advertise (*verified fact* from AI:AT English pages, research date 2026-10-21)

- Free / facilitated access to **European HPC** (e.g. LUMI, Leonardo, MareNostrum 5, JUPITER) for AI training and fine-tuning  
- Tracks such as **AI for Science**, Development, Playground, Fast Lane, Large Scale (GPU-hour bands and durations vary)  
- Inference mainly for **testing**; **production hosting not supported** (per their infrastructure page)  
- Contact: **info@ai-at.eu**  
- Consortium includes TU Wien, Uni Wien, BOKU, Innsbruck, TU Graz, JKU, ISTA, ÖAW, … — **not** Kunstuni Linz as a named consortium partner on the About page (as of research date)

HPC access service page: https://ai-at.eu/en/services/exclusive-access-to-the-european-hpc-infrastructure/  
FAQ: https://ai-at.eu/en/faq/

### Relevance for Critical Vibe Coding

| Use | Fit |
|---|---|
| Fine-tune / train a small open model for a semester project | Possible *if* a project application succeeds — weeks of lead time |
| Daily Hermes agent chat | **Poor fit** — HPC is not a Chat Completions API for students |
| Run “our own” weights on EU machines | Closer — still ops-heavy; not the class default |

*technical suggestion:* Treat AI:AT as a **teacher/research contact** for optional advanced projects, not as week-2 install path.

---

## Teacher todos (*todo*)

- [ ] **Contact AI Factory Austria** — email `info@ai-at.eu`: Can Interface Cultures / Kunstuniversität Linz students or a course project get **AI for Science** or Development access? Is there any **inference API / shared endpoint** suitable for teaching agents, or only batch HPC? Ask for onboarding kit + timelines.
- [ ] **Contact Kunstuni / UFG IT or digital teaching** — Is there a campus AI chat? Any API? Terms for student artwork / personal data?
- [ ] **Contact ASC** (`support@asc.ac.at`) — Conditions for non-partner art university (pay-per-use? teaching project?).
- [ ] After answers: rewrite the one-sentence “student access” line in session 3 and [[todo-teacher-prep]].
- [ ] If an academic endpoint appears: document how (or whether) Hermes can point at a custom OpenAI-compatible base URL — see Hermes provider docs.

Also listed in [[todo-teacher-prep]].

---

## Classroom talking points

1. Academic ≠ automatically agent-ready.  
2. Sovereignty / EU compute is real — but **bureaucracy and job scripts**, not “paste key in Hermes.”  
3. Course default remains: personal stack + optional local GPU + structure/harness ([[what-is-harness]]).  
4. Privacy: sending student/artwork data to campus vs US cloud — pair with [[eu-ai-act-and-datenschutz]].
