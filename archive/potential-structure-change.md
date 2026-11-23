---
title: Potential Structure Change
audience: teacher
status: proposal
canonical: false
---

This is a proposal, not the current course. Students will be asked separately.

The repository needs clearer entry points, but not a hierarchical “student path.” The course is a seminar and shared inquiry space. Students may use different tools, combine several setups, or decide not to use AI. The structure should separate **shared critical work** from **optional technical support**, without turning the technical material into a set of mandatory tracks.

## Alternative structure: shared seminar, parallel resources

```text
README.md
└── course/
    ├── START-HERE.md
    ├── SEMINAR.md
    ├── THEORY/
    ├── PRACTICE/
    ├── SESSIONS/
    ├── PROJECT-WORK/
    └── REFERENCES/
```

## 1. `README.md`

The repository landing page should explain the overall character of the course:

- This is a seminar, not a software-certification course.
- Large chunk of the work is collective discussion without screens.
- Technical setups are personal and may differ.
- Students may use AI, use it critically, or work through research and refusal.
- The repository contains shared questions, session materials, technical notes, and references.

The README should link only to:

- [[course/START-HERE]]
- [[course/SEMINAR]]
- [[course/THEORY/README|THEORY]]
- [[course/PRACTICE/README|PRACTICE]]
- [[course/SESSIONS/README|SESSIONS]]
- [[course/PROJECT-WORK/README|PROJECT-WORK]]
- [[course/REFERENCES/README|REFERENCES]]

## 2. `course/START-HERE.md`

This should be a short orientation page, not an installation page.

It should answer:

- What is this course?
- How is each session organised?
- What should students read before the first meeting?
- Where are the shared discussions documented?
- Where are the technical notes?
- What is required for the midpoint and final?
- Where can students ask questions or report setup problems?

Suggested structure:

```text
START HERE
├── The course in one page
├── How we work together
├── Session overview
├── Shared questions and student inputs
├── Technical materials
├── Project work and documentation
└── References
```

The first paragraph should make the social format explicit:

> This course is a shared space for talking, experimenting, and thinking about AI in artistic practice. Technical work supports the discussion. No single software stack is required.

## 3. `course/SEMINAR.md`

This is the central course document. It should describe the common activity of the group.

Include:

- check-in format;
- screen-free discussion periods;
- student inputs;
- collective questions;
- group agreements;
- how disagreement is handled;
- how experiences and fears are discussed;
- when technical demonstrations or workshops occur;
- how students may participate without using AI.

Suggested sections:

```text
# Seminar

## How the sessions work
## Check-in
## Screen-free discussion
## Student inputs
## Group agreements
## Questions we are carrying
## Ways to participate
## Confidentiality and care
```

This document should be more prominent than the install guide. It represents the actual course.

## 4. `course/THEORY/`

This folder contains the critical and humanistic material.

Possible sections:

```text
THEORY/
├── 01-political-economy/
├── 02-labour-authorship/
├── 03-ecology-infrastructure/
├── 04-bias-flattening/
├── 05-privacy-regulation/
├── 06-danger-and-risk/
└── 07-refusal-and-alternatives/
```

The current deep dives can remain largely intact, but the folder should distinguish:

- readings;
- discussion prompts;
- research notes;
- lecture notes;
- claims requiring current verification.

For example:

```text
THEORY/
├── readings.md
├── discussion-prompts.md
├── political-economy.md
├── labour-and-authorship.md
├── ecology-and-infrastructure.md
├── flattening-and-the-norm.md
├── privacy-and-regulation.md
└── danger-and-risk.md
```

The point is not to create a fixed theory curriculum. It is to give the group a common surface for discussion.

## 5. `course/PRACTICE/`

This folder contains technical material without implying that every student must follow the same sequence.

Suggested sections:

```text
PRACTICE/
├── 01-harness-and-agents/
├── 02-knowledge-bases/
├── 03-models-and-providers/
├── 04-local-and-cloud/
├── 05-security-and-privacy/
├── 06-mcp-and-tools/
├── 07-creative-stacks/
└── 08-verification-and-provenance/
```

Each technical note should state:

```yaml
audience: student
status: current | draft | optional | advanced
requires:
  - ...
alternatives:
  - ...
```

The technical materials should be organised by **questions and functions**, not by mandatory setup paths:

- What can an agent do?
- Where can it read and write?
- Where does the model run?
- How can knowledge be organised?
- How can tools be connected?
- How can work be checked?
- How can the process be documented?

This reflects the course’s complexity better than “choose cloud, local, or existing tools.”

## 6. `course/SESSIONS/`

Keep the sessions as the main timeline of the course:

```text
SESSIONS/
├── 01-welcome-and-landscape.md
├── 02-harness-and-wiki.md
├── 03-models-hardware-and-prompting.md
├── 04-project-presentations.md
├── 05-vault-phone-and-tools.md
├── 06-agent-as-interface.md
├── 07-creative-stacks-and-privacy.md
└── 08-final-presentations.md
```

Each session page should use the same structure:

```text
# Session title

## What we are doing together
## Screen-free discussion
## Student input
## Technical material
## Questions to carry forward
## Optional preparation
## Project work
```

This format places discussion first and technical work in context.

It also prevents the technical material from becoming the hidden “real course” while the group conversation appears as an introduction.

## 7. `course/PROJECT-WORK/`

This folder should collect the documents students need for their own practices:

```text
PROJECT-WORK/
├── project-proposal.md
├── interface-score.md
├── provenance.md
├── process-log.md
├── verification.md
├── critical-reflection.md
└── final-presentation.md
```

These should be templates, not instructions to use one agent architecture.

A student working with Hermes, Cursor, a local script, a visual tool, or no AI should be able to use the same documentation framework.

## 8. `course/REFERENCES/`

Move bibliography and external research here:

```text
REFERENCES/
├── bibliography.md
├── primary-sources.md
├── peer-courses.md
├── tools-and-documentation.md
└── current-claims.md
```

`current-claims.md` (find more intuitive name) should contain volatile information such as:

- model availability;
- prices;
- installation commands;
- hardware;
- provider policies;
- legal timelines;
- current data-centre figures.

That keeps unstable material separate from the more durable seminar texts.

## Suggested top-level relationship

```text
                 ┌─────────────────────┐
                 │       SEMINAR       │
                 │ collective inquiry  │
                 │ discussion and care │
                 └──────────┬──────────┘
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
┌─────────▼─────────┐               ┌─────────▼─────────┐
│      THEORY       │               │      PRACTICE     │
│ readings, claims, │               │ tools, setups,    │
│ questions, debate │               │ security, methods │
└─────────┬─────────┘               └─────────┬─────────┘
          │                                   │
          └─────────────────┬─────────────────┘
                            │
                 ┌──────────▼──────────┐
                 │    PROJECT WORK     │
                 │ personal practice,  │
                 │ documentation,      │
                 │ reflection          │
                 └─────────────────────┘
```

## What should remain at repository root

Keep only:

```text
README.md
AGENTS.md
course/
research/
UnlearGestaltungAI_Mainz/    -> why not at research? linked...?
```

But revise `README.md` so it does not present the repository primarily as an installation pack.

The first visible message should be:

> Critical Vibe Coding is a seminar about living and working with AI in media-art practice. The course combines screen-free group discussion, critical research, technical experiments, and individual project work. The technical materials support different practices. They do not define one correct setup.

This structure preserves the horizontal, collective character of the course while still solving the navigation problem.
