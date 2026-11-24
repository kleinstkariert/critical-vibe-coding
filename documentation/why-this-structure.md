---
title: Why this structure
status: draft
canonical: false
---

# Why this structure

This page gives the reasons and the doubts. It does not list moves or checks. The record of what moved, and what was checked, is [structure move history](structure-move-history.md).

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
- Project work is where each student documents their own practice. Templates hold the blank forms.
- Sessions are the timeline.
- References hold sources and facts that change.
- Research notes stay outside the course pages and are sorted by purpose.

The idea comes from a proposal note. The note is no longer in the repository. Its reasoning is on this page.
Students were asked about the change, and they wanted it.
That is a reason to try it. It is not proof that it works.

## One rule for all pages: position says purpose

A page has no label for its reader. We removed the old `audience` field. A reader should learn what a page is for from three things: where it sits, its title, and its short description. A page keeps `status` and `canonical` only where they help, for example to mark a draft or the one page that holds a fact.

Weak point: this works only if the folders and titles are honest. If a note sits in the wrong folder, nothing else tells the reader.

## Reasons, folder by folder

These are arguments, not facts. Each one has a weak point.

**README.** It links to a short list of pages. We hoped a short list would show the shape of the course at once.
Weak point: a reader may still skip the seminar page.

**START-HERE.** A short orientation page. It is not an install page.
Weak point: it has to be short, and short pages leave things out.

**SEMINAR.** It describes what the group does together: check-in, screen-free discussion, student inputs, group agreements, ways to take part without AI.
We want this page to feel more important than the install guides.
Weak point: a page cannot make a discussion good. The room does that.

**THEORY.** The critical and humanities notes, sorted by topic: political economy, labour, ecology, bias and flattening, privacy, danger and risk, refusal.
The point is a common surface for discussion, not a fixed curriculum.
Weak point: topics overlap. A note about data centres belongs to ecology, economy and labour at once. We had to choose one folder.

**PRACTICE.** The technical notes, sorted by question: what can an agent do, how is knowledge organised, which model, where does it run, where can it read and write, how are tools connected, what about creative stacks, how is work checked.
It also holds the install guides and the [install order](../course/PRACTICE/install-order.md). That page only gives the order for the Hermes example. It does not repeat the course.
We sorted by question because we did not want to suggest a mandatory setup path.
Weak point: a beginner may miss a clear order outside the install example.

**SESSIONS.** The eight session notes stay the main timeline. Syllabus pages and lectures sit here, because they describe the meetings.
Weak point: this makes the folder mixed. Slideshows and generators live inside it.
We did not make one template for all session pages.

**PROJECT-WORK and templates.** The guide pages are numbered in the order a student meets them. The README explains the sequence. The blank forms are in a separate `templates/` folder, so that a guide page explains and a template only asks.
Weak point: two folders mean two places to look. A numbered list also suggests an order that a student with another plan may not follow.

**REFERENCES.** Bibliography, primary sources, peer courses, a tools and documentation page, a dated page for models, prices, limits and hardware, and English translations of guidelines and handbooks.
Keeping unstable facts apart from the seminar texts should make updates easier.
Weak point: the dated page holds only a first set of rows, and nobody owns the updates yet. A translation can drift from its original.

**research/.** Research notes sorted by main purpose, not by the words they contain. A note about a tool, a store or a machine is in `software&DataManagement/`. A note about what a technology does to people, work or the planet stays in `research/`. Notes by other groups are in `externalReferences/`.
Weak point: some notes serve both purposes. We used the primary purpose, and the choice is partly arbitrary. The `&` in a folder name is unusual and can need care in some tools.

**archive/.** Old navigation text, kept for reference. Nothing is deleted from history.
The old 13-session files were removed from the repository. Their reusable parts moved into current pages.

**documentation/.** Why we did this, and the record of the move. We merged the old separate folder for the record into this one, because both explain the structure. They should not repeat each other: this page argues, the record states facts.

## Arguments against, and doubts

- A new structure costs readers time. People who knew the old paths must learn new ones.
- Technical and critical work are not really separate. Splitting them in folders may hide how they connect.
- Numbered folders and numbered files suggest an order, even if we say there is none.
- Some files could sit in two places. Our choices are partly arbitrary.
- We moved files and fixed links, but we did not rewrite most texts. Some old texts still describe the old layout.
- The structure was designed by the teacher. Students approved the idea, but not each file location.

## What we did not decide

- Whether all session pages should follow one template.
- Whether the numbered topic folders in THEORY and PRACTICE should stay.
- Who keeps the dated models, prices, limits and hardware page up to date, and how often.

## What would make us change it

- Students cannot find things.
- The seminar page is not used.
- Technical notes still feel like the "real" course.
- Links break often.
- A better idea comes from the group.

## How to tell us

Say it in class, use the class Teams channel, or send an email to the instructor.
A short note is enough: what you looked for, where you went first, and what you found.
