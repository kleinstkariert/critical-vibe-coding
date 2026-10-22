---
title: LLM Wiki — standard files and folders
date: 2026-10-18
tags:
  - course
  - llm-wiki
---

# LLM Wiki — standard files and folders

What lives in a Karpathy-style wiki directory. Labels: *verified fact* | *technical suggestion*.

Canonical pattern: [Karpathy gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).  
Hermes layout (names below): [llm-wiki skill](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki).  
Naming essay: [The Schema Is the Product](https://cozypet.github.io/llm-wiki-schema/).

## Tree (Hermes / course default)

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

*verified fact:* Hermes names this file `SCHEMA.md`. Karpathy’s gist allows `CLAUDE.md` / `AGENTS.md` — same job, different filename.

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

*verified fact:* Content catalog. Every wiki page listed under its type with a **one-line summary**. The agent reads this **first** when querying.

**Scaling (Hermes):** Split sections after ~50 entries; topic map after ~200 pages.

### `log.md` (history)

*verified fact:* Append-only chronological record. Hermes format:

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
- **Lint** → health-check; see [[what-is-lint]]

## Tools that implement this

| Tool | Link | Notes |
|---|---|---|
| Hermes Agent skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki | Filesystem agent; class default with Obsidian as viewer |
| Hermes skill source | https://github.com/NousResearch/hermes-agent/blob/HEAD/skills/research/llm-wiki/SKILL.md | Full `SKILL.md` |
| Obsidian plugin `karpathywiki` | https://community.obsidian.md/plugins/karpathywiki · https://github.com/GD4AI/obsidian-llm-wiki | Ingest/query/lint inside Obsidian; Apache-2.0 |
| Dexio guide | https://dexio.wiki/guides/llm-wiki-obsidian/ | Obsidian-oriented walkthrough |

Setup in this repo: [[howto-hermes-setup]] · [[howto-obsidian-setup-and-sync]] · [[references]]
