---
title: Agent. General skills and STE80
date: 2026-11-25
status: current
canonical: true
---

# Agent. General skills and STE80

No official Hermes skill slug for STE was found (not verified). Put STE rules in `AGENTS.md`. Human detail: [prompting guide §26](../../03-models-and-providers/prompting-guide-for-critical-vibe-coding.md#26-course-writing-default-ste80).

## Skills commands

```bash
hermes skills browse
hermes skills search <term>
hermes skills list
hermes skills install official/research/llm-wiki
```

- Review third-party skills before install.
- Hub docs: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills

## STE80 rules (write this way)

- Short sentences. Active voice. One instruction per sentence.
- Common words. One term for one concept.
- No em dashes. Use commas, colons, or a new sentence.
- Number ranges with "to" (example: 8 to 16).
- Prefer lists for steps.
- State limits. Mark not verified when untested.
- Keep each sentence near 20 words when practical.
- About 80% ASD-STE100. Preserve code, paths, proper names.

## Put STE in AGENTS.md

Add a short block:

```markdown
## Writing
Write replies and new course text in STE ~80%.
No em dashes. Short sentences. Active voice.
```

## Check

1. `hermes skills list` shows installed skills.
2. Ask Hermes to restate the STE rules from `AGENTS.md`.
