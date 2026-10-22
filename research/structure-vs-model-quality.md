---
title: Structure / harness vs model quality — research check
date: 2026-10-20
tags:
  - research
  - harness
  - software-engineering
  - course
---

# Structure / harness vs model quality — research check

Claim circulating in the course: *the information structure around an agent matters more than LLM quality (within limits); someone said productivity is ~70% knowledge/structure and ~30% model.*

Domain: mainly **software engineering / coding agents**, with supporting RAG results.  
Labels: *verified fact* | *nuance / caveat* | *technical suggestion*.

Course home for this argument: [[../course/what-is-harness]] · session [[../course/sessions/02-agent-harness-and-wiki-architecture]].

---

## Verdict (teach this)

1. **Direction of the claim is well supported** in SE and RAG: repository context, retrieval corpus, and **harness/scaffold** design often move scores as much as (or more than) swapping to a bigger model — *within a capability band* (a tiny model still fails hard tasks).
2. **The neat “70% / 30% productivity” split is not a productivity study.** The closest published ~70/30 figure measures something else (see below). Do **not** present 70/30 as an established productivity law.
3. For class: say **structure + harness first, model second (with a floor)** — and cite SE harness papers + repo-context work, not a fake pie chart.

---

## Where the ~70% / ~30% figure actually comes from

*verified fact:* Wadhwa et al., *When Context Leads but Parametric Memory Follows in Large Language Models* (arXiv:2409.08435, 2024).

- Setting: open-ended QA when **context is knowledge-consistent** with what the model “knows.”
- Finding: across nine LLMs, answers draw **roughly ~70% from the provided context** and **~30% from parametric (in-weights) knowledge**; more context → fewer hallucinations; models never use context 100%.
- This is about **where tokens in the answer come from**, not about “70% of a developer’s productivity.”

*nuance / caveat:* Easy to mis-hear as a productivity split. In class, either cite it correctly (“when you give context, the model leans on it ~70%”) or skip the numbers and keep the qualitative claim.

Link: https://arxiv.org/abs/2409.08435 · https://doi.org/10.48550/arxiv.2409.08435

---

## Software engineering — stronger evidence for “structure > raw model”

### A. Harness / scaffold changes outcomes with the model fixed

| Study | Finding (compressed) |
|---|---|
| Fan et al., *An Empirical Study of Harness Design for Coding Agents* (arXiv:2609.20804, 2026) | On SWE-Bench Verified & Terminal-Bench 2.1: **context management**, planning, and action space (tools vs bash) each matter; same model, different harness components → different accuracy/cost. Context management especially valuable under tight windows. |
| *The Scaffold Effect in Coding Agents* (arXiv:2607.22585, 2026) | Same models across Goose / OpenCode / OpenHands: harness can change **tokens per solved task by up to ~40×**; pass-rate gaps smaller (often 0–8 pp). Failure modes track the **harness**, not only the model. |
| Li et al., *Finding the Right Fit: Model–Harness Interactions* (arXiv:2610.00917, 2026) | **Model rankings reverse across harnesses** (e.g. Claude ahead of GPT in one harness, far behind in another on Terminal-Bench). Evaluate **model–harness–task** together. |

These are the cleanest “your friend’s claim, but for coding agents” papers: **the wrapper is not a detail**.

### B. Repository / knowledge context beats scale (completion & repair)

| Study | Finding (compressed) |
|---|---|
| RepoFusion (arXiv:2306.10998) | Models trained/used with **repository context** beat much larger code models *without* that context (~70× size gap class results on single-line completion). |
| RepoExec / context ablation (arXiv:2406.11927) | **Full dependency context** best for repo-level generation; context level changes correctness and dependency use. |
| REPOFORGE-style repo agents (2025 survey write-ups) | Retrieval + agent loop lifts Pass@1 sharply over no-retrieval; **retrieval can dominate scale** at repo level. |

### C. RAG / datastore (knowledge-intensive; not only SE)

| Study | Finding (compressed) |
|---|---|
| Shao et al., MassiveDS / retrieval scaling (arXiv:2407.12854) | Larger inference datastore → gains without obvious saturation; **smaller LM + large datastore can beat larger LM-only** on knowledge-heavy tasks. |
| *Less LLM, More Documents* (arXiv:2510.02657) | **Corpus scaling** often substitutes for moving up a model tier; mid-size models gain most. |
| Pinecone RAG study (industry) | With enough retrieved data, smaller open models can approach GPT-4-class faithfulness on their metrics — treat as *directional*, not peer-reviewed gospel. |

---

## Limits (say aloud)

- A weak model + perfect wiki still fails multi-step SE tasks that need strong reasoning / tool use.  
- Garbage structure hurts any model (wrong index, no schema, noisy vault).  
- “Structure” here means: **repo/wiki layout, retrieval, schema/skills, tools, context policy** — the harness — not mystical vibes.  
- Most hard numbers are from **coding / QA benchmarks**, not from a controlled study of artists’ media pipelines. Transfer by analogy; don’t overclaim.

---

## How to phrase it in Critical Vibe Coding

**Preferred classroom sentence:**

> Within a usable model tier, **how you structure information and the agent harness often moves results more than swapping to the next bigger LLM** — especially in software-engineering-style work. A famous ~70/30 split in one paper is about *context vs weights in the answer*, not productivity percentages.

**Maps to our stack:**

| “Structure” | CVC object |
|---|---|
| Repo / project truth | Files the agent can read |
| Curated memory | LLM Wiki: `SCHEMA.md`, `index.md`, `raw/`, lint |
| Harness | Hermes skills, tools, MCP, kill-switches |
| Model | Whatever API / local weights they attach |

Karpathy LLM Wiki bet is the same intuition at small scale: a maintained folder beats dumping everything into a larger context window.

---

## Sources (quick list)

- https://arxiv.org/abs/2409.08435 — context ~70% / parametric ~30% in answers  
- https://arxiv.org/abs/2609.20804 — harness components, SWE-Bench / Terminal-Bench  
- https://arxiv.org/abs/2607.22585 — scaffold effect, token cost  
- https://arxiv.org/abs/2610.00917 — model–harness interactions, ranking reversals  
- https://arxiv.org/abs/2306.10998 — RepoFusion  
- https://arxiv.org/abs/2406.11927 — RepoExec contexts  
- https://arxiv.org/abs/2407.12854 — datastore scaling  
- https://arxiv.org/abs/2510.02657 — less LLM, more documents  
- LangChain harness essay (course): https://www.langchain.com/blog/the-anatomy-of-an-agent-harness  
