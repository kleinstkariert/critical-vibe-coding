---
title: Session 08 — Midpoint demo and proposal
session: 8
---

# Session 08 — Midpoint: working setup demo + project proposal

Parent: [[../timeline]]

## Goals

- Everyone demos a **working** personal agent setup (even if rough)
- Pitch how the setup enters an art / semester project
- Peer feedback; adjust trajectory for second half

## Check-in

Energy check before demos; timebox rules.

## Format (suggested)

Per student (~8–12 min including feedback):

1. **Setup walkthrough** — vault layout (`SCHEMA.md`, `index.md`, `log.md`, `raw/` — [[../llm-wiki-standard-files]]), schema/skills, model, tools/MCP (session 5 diagram); harness from session 2, phone/Discord if any
2. **Lint report** (*requirement*) — show the most recent **lint** entry in `log.md` (Hermes: `## [date] lint | N issues found`) or the Obsidian plugin’s health scan, **or** explain why lint is still pending (no ingests yet, setup broke, plugin not installed…). What lint is and is not: [[../what-is-lint]]. Read the report as a studio critique of the knowledge base, not as a grade.
3. **Live micro-task** — agent does something real (ingest, query, edit, tool call)
4. **Proposal** — how *agent as interface* appears in a project (not only “AI will generate my visuals”)
5. **Peer notes** — one strength, one risk, one question

Inspired by the [HKUST AMCC6500](https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf) midterm proposal review pattern ([[../timeline]]).

## Teacher role

- Catch missing safety (secrets in vault, double sync, two writers on the same pages — Hermes *and* the Obsidian plugin)
- Check the three backbone files exist and are used (`SCHEMA.md` has human-only paths; `index.md` lists the pages; `log.md` has ingest + lint entries)
- Push vague proposals toward concrete interface decisions

## Homework

- Update schema from feedback; fix at least the high-severity lint issues (or write into `SCHEMA.md` why they stay)
- Choose focus theme for sessions 8–9 reading/discussion (labour vs ecology vs regulation) and pick **one** optional reading from the session 8 or 9 list

## Materials / References

| What | Link |
|---|---|
| What lint checks (orphans, broken links, index completeness, frontmatter, stale, contested…) | [[../what-is-lint]] |
| Standard files the walkthrough should show | [[../llm-wiki-standard-files]] |
| Hermes llm-wiki skill — ingest / query / lint | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki |
| Obsidian plugin `karpathywiki` — in-app lint health scan | https://community.obsidian.md/plugins/karpathywiki |
| Karpathy gist — *Operations → Lint* | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Peer pattern — HKUST midterm proposal review | https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf |
