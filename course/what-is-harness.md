---
title: What is an agent harness?
date: 2026-10-20
tags:
  - course
  - concepts
---

# What is an agent harness?

Course concept note for session [[sessions/02-agent-harness-and-wiki-architecture]].  
Primary external text: [LangChain — *The Anatomy of an Agent Harness*](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) (Trivedy, 2026-03-10).

## One line

**Agent = Model + Harness.**  
The model is the intelligence; the harness is everything else that makes that intelligence *do work*.

If you are not training or swapping the weights, you are designing the harness.

## What counts as harness

| Piece | Role |
|---|---|
| System prompt / schema | Standing instructions, voice, hard limits |
| Tools, skills, MCP | What the agent can call; how tools are described |
| Filesystem / workspace | Durable state outside the context window |
| Orchestration | Loops, subagents, handoffs, model routing |
| Hooks / middleware | Compaction, lint, tests, “don’t stop yet” continuations |
| Sandbox / runtime | Where code runs, what is allowed |

A chat product is already a thin harness (message history + while-loop). A coding or research agent is a thick harness (files, bash, verify, skills).

## Why models need harnesses

Out of the box, a model mostly maps context → tokens. It does **not** by itself:

- keep durable state across days  
- execute code or open apps  
- fetch live knowledge after its cutoff  
- enforce your studio rules  

Those are harness jobs. Desired behaviour → harness feature (LangChain’s derivation pattern).

## Course mapping (Hermes + Obsidian)

| Harness idea | Our default stack |
|---|---|
| Filesystem workspace | Obsidian vault / `WIKI_PATH` |
| Memory files | `SCHEMA.md`, `index.md`, `log.md` |
| Skills | Hermes bundled skills (llm-wiki, …) + your procedures |
| Tools / MCP | Filesystem tools first; apps via MCP later ([[what-is-mcp]]) |
| Verification | Lint pass, human review, tests before fab |
| Context management | Small index + pull pages; don’t paste the whole vault |

Deep structure: [[llm-wiki-standard-files]] · [[what-is-lint]] · Karpathy gist via [[../research/karpathy-llm-wiki-and-openclaw]].

---

## Why structure / harness often beats “just a better model”

*technical suggestion for teaching:* In software-engineering-style agent work, **information structure + harness design** frequently move outcomes more than swapping to the next bigger LLM — *within a usable model tier*. Research note with citations: [[../research/structure-vs-model-quality]].

### What is actually true

| Claim | Status |
|---|---|
| Structure / context / harness matter a lot for coding agents | *verified direction* — harness papers (SWE-Bench / Terminal-Bench): same model, different scaffold → different accuracy and huge cost gaps; model rankings can **reverse** across harnesses |
| Repo / retrieval context can beat raw scale | *verified direction* — RepoFusion-class and RAG datastore scaling: smaller model + good context ≈ larger model without it, on knowledge-heavy or repo tasks |
| “Productivity is 70% knowledge base, 30% model” | **Misheard number** — do not teach as productivity law. Closest paper (~70% context / ~30% parametric) measures **where answer content comes from** when context is provided (Wadhwa et al., arXiv:2409.08435), not % of human productivity |

### Classroom one-liner

> Don’t buy a fancier model before you have a readable wiki, a schema, and a harness that can find files. The model is the engine; the structure is the road.

### Within limits

A floor still exists: a too-weak model fails hard SE tasks even with a perfect vault. Structure does not replace capability — it multiplies it.
