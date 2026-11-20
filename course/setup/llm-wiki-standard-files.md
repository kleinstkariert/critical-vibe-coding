---
title: LLM Wiki — standard files and folders
date: 2026-10-18
tags:
  - course
  - llm-wiki
audience: student
status: current
canonical: true
---

# LLM Wiki — standard files and folders

*reference implementation. Optional extension. Not required for assessment.* This tree is the Hermes example. Your knowledge store can use other names. A full wiki file set is not required. See [minimum path](../minimum-path.md).

Source types: [references](../syllabus/references.md#source-types). A label names the source kind. It is not independent verification. What lives in a Karpathy-style wiki directory. Labels: *technical suggestion*.

Canonical pattern: [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).  
Hermes layout (names below): [llm-wiki skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki).  
Naming essay: [The Schema Is the Product](https://cozypet.github.io/llm-wiki-schema/).

## Tree (Hermes / course default)

*reference implementation.* The heading means the Hermes example, not the assessed file names.

```text
wiki/   (or your vault root / a subfolder)
├── SCHEMA.md          # rules for the agent (sometimes AGENTS.md / CLAUDE.md)
├── index.md           # catalog of pages + one-line summaries
├── log.md             # append-only action history
├── raw/               # immutable sources
│   ├── articles/
│   ├── papers/
│   ├── transcripts/
│   └── assets/
├── entities/          # people, orgs, products, models…
├── concepts/          # topics, ideas
├── comparisons/       # side-by-side analyses
└── queries/           # filed answers worth keeping
```

*technical suggestion:* For Critical Vibe Coding, keep artistic voice notes **outside** agent-writable folders (or mark them human-only in `SCHEMA.md`).

## The three backbone files

### `SCHEMA.md` (Layer 3 — the contract)

*institutional summary:* Hermes names this file `SCHEMA.md`. Karpathy’s gist allows `CLAUDE.md` / `AGENTS.md` — same job, different filename.

**What it is:** The instructions the agent must follow: domain, naming, frontmatter, tag taxonomy, when to create/split/archive pages, how to handle contradictions, who may edit what.

**Why it matters:** Without a schema, every session invents a new house style. With a schema, ingest/query/lint stay consistent. See also [cozypet on schema](https://cozypet.github.io/llm-wiki-schema/).

**Minimum contents (course):**

- Domain (one paragraph)
- Conventions (filenames, wikilinks, update dates)
- Tag taxonomy (10–20 tags; add new tags *here* before use)
- Page thresholds (when to create / merge / split)
- Human-only vs agent-writable paths
- Lint frequency / approval for mass edits

### `index.md` (navigation)

*unverified lead:* Content catalog. Every wiki page listed under its type with a **one-line summary**. The agent reads this **first** when querying.

**Scaling (Hermes):** Split sections after ~50 entries; topic map after ~200 pages.

### `log.md` (history)

*institutional summary:* Append-only chronological record. Hermes format:

`## [YYYY-MM-DD] action | subject`

Actions include: `ingest`, `update`, `query`, `lint`, `create`, `archive`, `delete`.

**Scaling:** Rotate after ~500 entries (`log-YYYY.md`).

## Layers again

| Layer | Path | Who writes |
|---|---|---|
| 1 Raw | `raw/` | Human drops sources; agent **reads only** (never edits) |
| 2 Wiki | `entities/`, `concepts/`, … | Agent creates/updates |
| 3 Schema | `SCHEMA.md` | Human + agent co-evolve |

## Frontmatter (pages)

Hermes expects YAML on wiki pages, roughly:

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from-taxonomy]
sources: [raw/articles/example.md]
confidence: high | medium | low   # optional
contested: true                   # optional
contradictions: [other-slug]      # optional
---
```

Raw files get a smaller block (`source_url`, `ingested`, `sha256`) so re-ingest can detect drift.

## Name variants you will see

| Role | Hermes | Karpathy gist / other agents | Obsidian plugin |
|---|---|---|---|
| Schema | `SCHEMA.md` | `AGENTS.md`, `CLAUDE.md` | Plugin settings + conventions |
| Catalog | `index.md` | `index.md` | Generated wiki index |
| Log | `log.md` | `log.md` | Plugin activity / lint scan |
| Sources | `raw/` | `raw/` | often `sources/` or `wiki/sources/` |

Same idea; do not mix two layouts in one folder without teaching the agent.

## Three operations (reminder)

- **Ingest** → touches many pages + index + log  
- **Query** → reads index (then pages); may file into `queries/`  
- **Lint** → health-check; see [what is lint](../concepts/what-is-lint.md)

## Tools that implement this

| Tool | Link | Notes |
|---|---|---|
| Hermes Agent skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki | Filesystem agent; Hermes example. Obsidian is one viewer |
| Hermes skill source | https://github.com/NousResearch/hermes-agent/blob/HEAD/skills/research/llm-wiki/SKILL.md | Full `SKILL.md` |
| Obsidian plugin `karpathywiki` | https://community.obsidian.md/plugins/karpathywiki · https://github.com/GD4AI/obsidian-llm-wiki | Ingest/query/lint inside Obsidian; Apache-2.0 |
| Dexio guide | https://dexio.wiki/guides/llm-wiki-obsidian/ | Obsidian-oriented walkthrough |

Setup in this repo: [howto hermes setup](howto-hermes-setup.md) · [howto obsidian setup and sync](howto-obsidian-setup-and-sync.md) · [references](../syllabus/references.md)

## What structure improves

A structured knowledge base does not make information true. Its value is that it makes information easier to inspect, connect, use, and revise.

A structured base can improve these things:

| Improvement | Question |
|---|---|
| Traceability | Can a claim be followed back to a source, version, passage, or production decision? |
| Consistency | Are related pages using compatible terms, categories, dates, and conventions? |
| Discoverability | Can a person or agent find the relevant material without reading the entire collection? |
| Maintainability | Can the knowledge base be updated, corrected, split, archived, or transferred to another tool? |
| Comparability | Can competing sources, models, workflows, or interpretations be placed next to one another? |
| Operational usefulness | Can the material support a real task, such as preparing an application, debugging a patch, planning an exhibition, or documenting an installation? |
| Reflexivity | Does the system make its own assumptions, exclusions, uncertainties, and authorship visible? |

These are different forms of quality:

| Form | Question |
|---|---|
| Structural | Are files, links, tags, metadata, and version histories coherent? |
| Evidential | Are claims supported by sources appropriate to their importance and scope? |
| Procedural | Can another person understand how the material was collected, transformed, and updated? |
| Interpretive | Does the analysis distinguish description, inference, comparison, and argument? |
| Contextual | Does the knowledge remain meaningful for the specific artistic, institutional, social, or technical situation? |
| Operational | Does the system help someone make, decide, verify, or revise something in practice? |
| Artistic | Does the work create a meaningful form, experience, relation, or question? |
| Political and ethical | What relations of labour, access, extraction, privacy, and power does the system reproduce or challenge? |

The LLM Wiki mainly supports structural, procedural, and operational quality. It can also support critical work by preserving sources, disagreements, uncertainty, and revision history.

Lint checks structure and maintenance: broken links, missing metadata, orphan pages, stale entries, unresolved contradictions. See [what is lint](../concepts/what-is-lint.md). Lint does not establish truth, settle interpretation, or judge artistic quality.

Structure does not replace critical judgment. It gives critical judgment a better surface to work on.
