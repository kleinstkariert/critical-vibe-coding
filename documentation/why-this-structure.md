---
title: Why this structure
audience: student
status: draft
canonical: false
---

# Why this structure

## Status of this page

This is a dynamic experiment. We do not know if this structure is good.
It may change during the semester, or after it.
We do not claim it is the best structure. It is our current attempt.
If it does not work for you, please say so. See the last section.

## The problem we saw

The repository began as a pack of install guides and session notes.
The first page a student saw was about installing software.
That gave a wrong picture of the course.

The course is a seminar. Much of the work is group discussion without screens.
Technical setups are personal. They differ, and some students use no AI at all.
When technical notes come first, they can look like the "real" course.
The group conversation then looks like an introduction.
We worry about that, but we are not sure it is the main cause of confusion.

## The idea we tried

We separated shared critical work from optional technical support.
The two sit side by side. Neither one is a mandatory track.

- The seminar (how we meet, how we talk) is the centre.
- Theory and practice are two parallel resources for the seminar.
- Project work is where each student documents their own practice.
- Sessions are the timeline.
- References hold sources and facts that change.

The idea comes from a proposal note. That note is kept in the [archive](../archive/potential-structure-change.md).
Students were asked about the change, and they wanted it.
That is a reason to try it. It is not proof that it works.

## The layout

```text
README.md
course/
  START-HERE.md
  SEMINAR.md
  THEORY/
  PRACTICE/
  SESSIONS/
  PROJECT-WORK/
  REFERENCES/
research/
UnlearGestaltungAI_Mainz/
archive/
documentation/
migrations/
```

## Reasons, folder by folder

These are arguments, not facts. Each one has a weak point.

**README.** It links to seven pages only. We hoped a short list would show the shape of the course at once.
Weak point: seven links may still be too many, and a reader may skip the seminar page.

**START-HERE.** A short orientation page. It is not an install page.
Weak point: it has to be short, and short pages leave things out.

**SEMINAR.** It describes what the group does together: check-in, screen-free discussion, student inputs, group agreements, ways to take part without AI.
We want this page to feel more important than the install guides.
Weak point: a page cannot make a discussion good. The room does that.

**THEORY.** The critical and humanities notes, sorted by topic: political economy, labour, ecology, bias and flattening, privacy, danger and risk, refusal.
The point is a common surface for discussion, not a fixed curriculum.
Weak point: topics overlap. A note about data centres belongs to ecology, economy and labour at once. We had to choose one folder.

**PRACTICE.** The technical notes, sorted by question: what can an agent do, how is knowledge organised, which model, where does it run, where can it read and write, how are tools connected, what about creative stacks, how is work checked.
It also holds the install guides for Windows, Linux and macOS and the starter knowledge base. Session 03 uses them.
We sorted by question because we did not want to suggest a mandatory setup path.
Weak point: a beginner may miss a clear order. The old install-order page is still there for that reason.

**SESSIONS.** The eight session notes stay the main timeline. Session 03 is a practical install session: check-in, student input, break, and an optional join-in install. It has no Docker baseline.
We moved the syllabus pages (outline, rhythm, timeline, brief) and the lectures here, because they describe the meetings.
Weak point: this makes the folder mixed. Slideshows and generators now live inside it.
The proposal also asked for one template for all session pages. We did not do that yet.

**PROJECT-WORK.** The documents students need for their own practice.
The minimum path is the required work. The project path covers proposal, midpoint and final in one page. Provenance includes the process log. Verification and reflection are short templates. The interface score is an optional scaffold for later.
Weak point: the templates mostly link to older notes and add little new teaching. We may have merged pages that students would rather read apart.

**REFERENCES.** Bibliography, primary sources, peer courses, a tools and documentation page, and a dated page for models, prices, limits and hardware.
Keeping unstable facts apart from the seminar texts should make updates easier.
Weak point: the dated page holds only a first set of rows. Most volatile facts are still inside the older notes, and nobody owns the updates yet.

**research/ and UnlearGestaltungAI_Mainz/.** Both stay as they were. They are research material, not course pages.
The proposal asked why the Mainz notes are not inside research. We did not answer that question. We left them where they were, because links point there.

**archive/.** Old structure and the old README. Nothing is deleted from history.
The old 13-session files were removed from the repository. Their reusable parts moved into current pages.

## Arguments against, and doubts

- A new structure costs readers time. People who knew the old paths must learn new ones.
- Technical and critical work are not really separate. Splitting them in folders may hide how they connect.
- Numbered folders suggest an order, even if we say there is none.
- Some files could sit in two places. Our choices are partly arbitrary.
- We moved files and fixed links, but we did not rewrite the texts. Some old texts still describe the old layout.
- The structure was designed by the teacher. Students approved the idea, but not each file location.

## Later changes on the same branch

After the first move, we added material from two open pull requests: the install guides and the starter knowledge base from one, a tool comparison from the other. The comparison is now one canonical page in `research/`. We also removed the lecturer's first name from tracked text and file names, and merged the stub pages that had no content of their own. The full list is in the [migration report](../migrations/2026-structure-move.md).

## What we did not decide

- Whether all session pages should follow one template.
- Whether the numbered topic folders in THEORY and PRACTICE should stay.
- Who keeps the dated models, prices, limits and hardware page up to date, and how often.
- Whether `research/` and the Mainz notes should be merged.

## What would make us change it

- Students cannot find things.
- The seminar page is not used.
- Technical notes still feel like the "real" course.
- Links break often.
- A better idea comes from the group.

## How to tell us

Say it in class, use the class Teams channel, or send an email to the instructor.
A short note is enough: what you looked for, where you went first, and what you found.
