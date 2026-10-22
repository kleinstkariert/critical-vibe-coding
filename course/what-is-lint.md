---
title: What is “lint” in an LLM Wiki?
date: 2026-10-18
tags:
  - course
  - llm-wiki
---

# What is “lint” in an LLM Wiki?

Short teaching note for Critical Vibe Coding. Labels: *verified fact* | *technical suggestion*.

## One sentence

*verified fact:* In Karpathy’s LLM Wiki pattern, **lint** is a periodic **health-check** of the wiki: the agent audits the markdown for structural and knowledge problems, reports them, and (when you ask) suggests or applies fixes. It is not a programming-language linter alone — though the metaphor is the same: “find smells before they harden.”

Primary source: [Karpathy, `llm-wiki.md`](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (section *Operations → Lint*). Hermes implements the same third operation in its bundled skill: [Hermes llm-wiki skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki).

## How it sits next to ingest and query

| Operation | Job |
|---|---|
| **Ingest** | Add a source; update many wiki pages; update `index.md` and `log.md` |
| **Query** | Answer from the compiled wiki; optionally file the answer as a new page |
| **Lint** | Audit the wiki itself; list issues by severity; append a lint entry to `log.md` |

You usually lint **less often** than you ingest — after a batch of sources, weekly, or when the wiki feels “off.”

## What lint looks for

From Karpathy’s gist (paraphrased) and the Hermes skill checklist (*verified fact* via Hermes docs):

1. **Orphan pages** — no inbound `[[wikilinks]]` from other pages  
2. **Broken wikilinks** — `[[Link]]` targets that do not exist  
3. **Index completeness** — every wiki page listed in `index.md`  
4. **Frontmatter** — required fields present; tags only from the schema taxonomy  
5. **Stale content** — pages not updated while newer sources touch the same entities  
6. **Contradictions** — conflicting claims; pages marked `contested: true`  
7. **Quality signals** — `confidence: low`, single-source pages without a confidence field  
8. **Source drift** — `raw/` files whose `sha256` no longer matches (raw should be immutable)  
9. **Page size** — pages over ~200 lines (split candidates)  
10. **Tag audit** — tags used but not declared in `SCHEMA.md`  
11. **Log rotation** — `log.md` too long → rotate  

Hermes asks the agent to **report with file paths and suggested actions**, grouped by severity, then append:

`## [YYYY-MM-DD] lint | N issues found`

to `log.md`.

## Lint vs “the model being wrong”

Lint does **not** prove truth. It finds **consistency and maintenance** problems. A page can lint clean and still be wrong about the world. A contested flag is a prompt for *you* to decide.

*technical suggestion for the course:* Treat a student lint report like a studio critique of the knowledge base — not like an exam grade.

## How students run it

**With Hermes (filesystem agent):**

- Say: “Lint my wiki” / “Health-check the wiki”  
- Or follow the skill’s lint section after orientation (`SCHEMA.md` → `index.md` → recent `log.md`)  
- Docs: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki  

**With the Obsidian plugin (Karpathy LLM Wiki / `karpathywiki`):**

- The plugin advertises a **lint health scan** (and “Smart Fix All”) inside Obsidian  
- Marketplace: https://community.obsidian.md/plugins/karpathywiki  
- Repo: https://github.com/GD4AI/obsidian-llm-wiki  

Class default remains **Hermes + folder wiki**; the plugin is an alternate / complementary path (see [[references]]).

## Course habits

- After several ingests → one lint before the next class  
- Midpoint (session 7): show a lint report as proof the setup is maintained  
- Schema should say how often to lint and who approves mass fixes  

Related: [[llm-wiki-standard-files]] · [[references]] · [[../research/karpathy-llm-wiki-and-openclaw]]
