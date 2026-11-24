---
title: Session 04. Project presentations and semester plans (midpoint)
session: 4
updated: 2026-11-10
status: current
canonical: true
---

# Session 04. Midpoint: project presentations and semester plans

The presentation is required. Show the system in [minimum path](../PROJECT-WORK/01_minimum-path.md): knowledge store, access boundary, model endpoint, tool set, verification method, and provenance. Hermes, a wiki file set, and lint are a *reference implementation*. They are *not required for assessment*.

Parent: [timeline](overview/timeline.md) · Rhythm: [course rhythm](overview/course-rhythm.md)

**Slot:** 10:00 to 12:00. Presentations dominate; no student input this session.

## Goals

- Everyone presents their **semester plan**: the project and how the agent setup enters it
- Show the setup as it stands (even if rough): vault, Hermes, model
- Peer feedback; adjust the trajectory for the second half

## Clock

| Clock | Block |
|---|---|
| **10:00 to 10:15** | Check-in (listen only; slightly shorter) |
| **10:15 to 10:55** | Presentations round 1 |
| **10:55 to 11:05** | Break |
| **11:05 to 12:00** | Presentations round 2 + wrap |

## Check-in

Listen only: [course rhythm](overview/course-rhythm.md#1-check-in-every-session). Then timebox rules for the presentations.

## Format (suggested)

Per student (about 5 to 8 min including feedback, for about 20 students):

1. **Semester plan:** the project, and how *agent as interface* appears in it (not only "AI will generate my visuals"). Students who do not want to use AI present their research or investigative plan instead.
2. **Setup walkthrough:** vault layout (`SCHEMA.md`, `index.md`, `log.md`, `raw/`: [llm wiki standard files](../PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md)), model, harness from Session 02; local path if any (Session 03).
3. **Provenance note** (draft): which model, which tools, who decided (how), where it ran. Template idea in [media art workflows](../PRACTICE/07-creative-stacks/media-art-workflows.md).
4. **Lint report** (optional at this point): the most recent lint entry in `log.md`, or why lint is still pending. What lint is and is not: [what is lint](../PRACTICE/02-knowledge-bases/what-is-lint.md).
5. **Peer notes:** one strength, one risk, one question.

Inspired by the [HKUST AMCC6500](https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf) midterm proposal review pattern ([timeline](overview/timeline.md)).

With about 20 students, 5 to 8 minutes each fills the session. If the group is larger, parallel rooms or shorter slots may be needed.

## Homework

- Update the schema and plan from the feedback
- Prepare for Session 05: phone sync and the Discord bridge need the vault in a syncable place

## Materials / References

| What | Link |
|---|---|
| What lint checks | [what is lint](../PRACTICE/02-knowledge-bases/what-is-lint.md) |
| Standard files the walkthrough should show | [llm wiki standard files](../PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md) |
| Hermes llm-wiki skill (ingest / query / lint) | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki |
| Obsidian plugin `karpathywiki` (in-app lint health scan) | https://community.obsidian.md/plugins/karpathywiki |
| Karpathy gist (*Operations → Lint*) | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Peer pattern: HKUST midterm proposal review | https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf |
| Provenance and authorship (archived session) | [10 authorship labour platforms](../THEORY/02-labour-authorship/labour.md#retired-session-10-prompts-readings-and-practical) |
