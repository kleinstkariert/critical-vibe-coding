---
title: Student-facing share structure (not the whole vault)
date: 2026-10-20
tags:
  - course
  - teaching
  - nextcloud
---

# Student-facing share structure

The teacher Obsidian vault (`KnowledgeBaseObsidian` + full CVC research + clippings + private emails) is **too large and too mixed** to share as-is. Students need a **course pack**, not your second brain.

Labels: *technical suggestion* (how other practice-based programmes often do it).

---

## What other lecturers typically do

| Pattern | Who / vibe | What students get |
|---|---|---|
| **Week folder + PDF outline** | HKUST AMCC6500-style | One outline PDF + weekly topic list; readings linked out |
| **Public git course repo** | SFPC, many IMA/ITP courses | Sessions, how-tos, assignments; no private research dump |
| **LMS / Moodle unit** | Universities | Handouts + submission; heavy UI, fine for grades |
| **Shared cloud “Course” space** | Collectives / Nextcloud / Drive | Small curated tree; teacher pushes releases |
| **Reader / zotero group** | Theory-heavy seminars | Citations only; PDFs via library |

CVC fits **git repo and/or Nextcloud course folder** + optional Moodle for admin. Keep the fat vault private.

**Platform choice (UFG / Teams / Moodle / GitHub Pages):** full research + recommendation → [[platform-and-course-site]].

---

## Recommended split

| Layer | Where | Contents |
|---|---|---|
| **A — Student kit** (share) | Nextcloud team folder *or* public/private git | Outline, sessions, how-tos, short research handouts |
| **B — Teacher vault** (private) | Your Obsidian | Clippings, emails, admission, raw bubble notes, talk image archives |
| **C — Optional reader** | Links only | DOI / URL list in [[references]] — students fetch themselves |

---

## Proposed Nextcloud (or Drive) tree

Publish something like:

```text
CriticalVibeCoding-Students/          ← share this folder only
  00-START-HERE.md                    ← link to outline + install order
  course-outline.md                   ← short syllabus sheet
  timeline.md                         ← session map (can omit teacher todos)
  sessions/
    01-welcome-and-landscape.md
    02-agent-harness-and-wiki-architecture.md
    03-… 
    13-final-presentations.md
  howtos/
    howto-hermes-setup.md
    howto-obsidian-setup-and-sync.md
    what-is-harness.md
    what-is-mcp.md
    what-is-lint.md
    llm-wiki-standard-files.md
  handouts/                           ← curated, short
    ai-tools-creative-processes.md
    prompting-and-model-choice.md
    academic-ai-austria.md
    eu-ai-act-and-datenschutz.md
    local-gpu-hardware-for-llms.md    ← from research/ (student-safe copy)
    presentation-style.md             ← optional
  lectures/                           ← only if you want them to see notes
    01-welcome-landscape-lecture.md   ← or export PDF without teacher-only paths
  references.md
  assets/                             ← images you cleared for teaching
    01-lecture/
```

**Do not put in the student kit**

- `course/emails/`, admission criteria with names  
- Full `research/ai-bubble-productivity-datacenter.md` if you consider it prep-only — *or* put a **2-page handout** extract instead  
- Vault `Clippings/` wholesale (Tooze transcripts, etc.) — link URLs in references  
- `.cursor/`, agent stores, personal Nextcloud other projects  
- High-res talk photo archives from `_QUADRATURE/…`

---

## Release rhythm (*technical suggestion*)

| When | Action |
|---|---|
| Before semester | Publish outline + how-tos + sessions 1–3 |
| Weekly | Drop next session file + any new handout |
| After class | Optional: slide PDF / recording link in that week’s folder |
| Never | “Sync entire Obsidian vault to students” |

Versioning: either **git tags** (`week-03`) or dated zip (`CVC-student-kit-2026-10-20.zip`) so late joiners get a snapshot.

---

## Obsidian for students (their machines)

Each student keeps a **personal** vault (phone sync). The student kit is **source material to copy or link**, not a shared multiplayer vault (unless you later open a Collectives space for group notes).

*technical suggestion:* In session 1, say: “Clone or download the kit into `Obsidian/CVC-course/`; your LLM Wiki lives beside it or in `wiki/`.”

---

## GitHub / Codeberg option

If the department is fine with public teaching materials:

- Repo = student kit only  
- Teacher research stays private (this Nextcloud path)  
- Matches SFPC / many media-art courses  

Private git also works with invite-only students.

---

## Status (2026-10-22)

- [x] GitHub repo is the student kit (`README` + `course/START-HERE.md`)  
- [x] Private files gitignored (`StudentList.md`, `course/emails/`, `.cursor/`)  
- [x] Instructor prep moved behind [[todo-teacher-prep]] (not the main student path)  
- [ ] Optional: enable GitHub Pages / Docsify for a prettier URL  
- [ ] Pin repo URL in Teams + UFG online  
- [ ] Exact semester dates on [[timeline]] when known  
