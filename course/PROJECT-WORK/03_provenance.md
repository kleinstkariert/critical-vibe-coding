---
title: Provenance and process log
status: current
canonical: true
---

# Provenance and process log

Provenance is the record of where a result came from. [Minimum path](01_minimum-path.md) asks for "a record of the task, the model, the tools, and the outcome". This page covers the project note and the running log in one place.

## 1. Provenance note

Write one short `provenance.md` per project, in your own words. Keep it in your knowledge store. Answer these questions.

| Question | Your answer |
|---|---|
| Which task did the agent do? | |
| Which model? Name the version and the date. | |
| Which tools, skills, and MCP servers? | |
| Who decided what? Say where you decided and where the agent decided. | |
| Where did it run? Local, cloud, or both. | |
| Who was paid, and for what? Subscription, API key, none. | |
| What was the outcome? Which files or works changed. | |

The source of this list is the provenance note in the course lecture and in [media art workflows](../PRACTICE/07-creative-stacks/media-art-workflows.md). Session 04 asks for a draft. Session 08 asks for the final note.

## 2. Process log

The process log is the running record. The note above is the summary of it.

Use the `log.md` file of your wiki: [llm wiki standard files](../PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md). It is append-only. Add one entry each time the agent does real work.

| Field | Example |
|---|---|
| Date | The day of the task |
| Task | One line |
| Mode | coding, production, or hybrid (see [AGENTS.md template](../PRACTICE/01-harness-and-agents/agents-md-template.md)) |
| Checks | Which check ran, and PASS or FAIL. See [verification](04_verification.md) |
| Human approval | What you approved, and what you rejected |
| Remaining risks | What is still unchecked |

A lint entry also goes into the log. What lint is and is not: [what is lint](../PRACTICE/02-knowledge-bases/what-is-lint.md).

## 3. Keep private notes out

The log and the note can be shared with the class. Do not write secrets, keys, or private vault content into them.
