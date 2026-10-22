---
title: Course platforms and website-like structure
date: 2026-10-20
tags:
  - course
  - teaching
  - platforms
---

# Course platforms and website-like structure

Research + recommendation for Critical Vibe Coding. Labels: *verified fact* | *technical suggestion*.  
Constraints from you: UFG online, Microsoft Teams, Moodle (slow/buggy); no large uploads; prefer existing git; want a website-like place.

Related: [[student-share-structure]] · git remote already: `https://github.com/kleinstkariert/critical-vibe-coding.git`

---

## What comparable courses actually use

| Pattern | Who / examples | What it is good for |
|---|---|---|
| **Public git repo + README as “site”** | NYU ITP (e.g. Code Your Way on GitHub), SFPC session repos, many creative-coding classes | Syllabus, week pages, links; students already live in browsers; version history |
| **GitHub Pages (static HTML/MD site)** | ITP / HCI instructors; ACM note *GitHub Pages as an LMS Alternative* (2024) | Real URL, nicer navigation than raw repo; still no gradebook |
| **Department class web / WordPress** | NYU ITP `itp.nyu.edu/classes/…` | Branded URL; often still redirects to GitHub |
| **LMS only (Moodle / Canvas / Brightspace)** | Default university path | Enrolment, grades, assignment dropbox — weak as a *readable* syllabus site |
| **Teams / Discord as hub** | Design studios, COVID-era hybrids | Chat, meetings, files — poor as the only syllabus (search dies, structure decays) |
| **Outline PDF + week list** | HKUST AMCC6500-style | Printable; not a living site |

*verified fact / pattern:* Practice-based tech+art programmes (ITP, SFPC-adjacent) routinely put the **syllabus on the open web or GitHub**, and keep the institutional LMS only for admin/submissions if required. ITP faculty helpdesk explicitly allows GitHub redirects.

---

## Your three institutional options (honest)

| Platform | Fit for CVC | Verdict |
|---|---|---|
| **UFG online** | Enrolment, official notices, closed “nerdy” portal | Keep as **admin pointer** (“materials live here →”) — not the reading site |
| **Microsoft Teams** | Chat, calendar, optional file tab, hybrid meetings | Good as **announcements + talk channel**; bad as the only syllabus (no clean session URLs, markdown hell) |
| **Moodle** | Grades, assignment boxes | Use **only if** the university forces submissions/grades there. Do not make it the front door if it is slow/broken for your cohort |

None of these give you a pleasant, linkable, versioned course website by themselves.

---

## Decision (2026-10-22)

**Primary (student-facing course pack):** this GitHub repo — `kleinstkariert/critical-vibe-coding` — with [`README.md`](../README.md) + [`START-HERE.md`](START-HERE.md). GitHub’s Markdown rendering is enough; optional GitHub Pages later.

**Secondary (communication):** Microsoft Teams — announcements, session reminders.

**Tertiary (admin only):** UFG online (and Moodle *only* if grades/uploads are required).

Private teacher material (student lists, emails, Cursor skills) stays **gitignored** / off this remote.

### Why not Moodle/Teams as the main site

- You already distrust Moodle performance.  
- Teams buries documents in chat/files; no stable public URL for session 02.  
- CVC materials are mostly markdown — git displays them; LMS fights them.

---

## Can git embed HTML-like pages?

**Yes — three levels:**

| Level | Effort | What students see |
|---|---|---|
| **A. Repo as site** | Lowest | GitHub renders `README.md` and every `.md` as a formatted page. Good enough for a class of artists who can click folders. |
| **B. GitHub Pages** | Low–medium | Enable Pages on the repo → `https://kleinstkariert.github.io/critical-vibe-coding/` (name may vary). Can serve **plain HTML**, or Markdown via Jekyll, or a zero-build tool (Docsify / Just the Docs / MkDocs). |
| **C. Static generator** | Medium | Quartz / VitePress / Eleventy builds a real multi-page site from your `course/` markdown on each push. |

Important nuances:

- **Git itself** stores files; it does not “host” a website. **GitHub (or Codeberg/GitLab) Pages** does.  
- You can commit `index.html` + CSS; Pages serves them as a normal website.  
- You can also keep writing **only Markdown** and let Docsify/Jekyll turn it into HTML in the browser or on build — no need to hand-author HTML for every session.  
- Private teacher stuff (`emails/`, admission, full vault) must **not** be on the public branch — use the student-kit split in [[student-share-structure]].

*technical suggestion for CVC:* start with **A** (public `docs/` or `student/` tree + strong README), add **B** (Pages + Docsify or plain HTML shell) when you want a single nice URL. Skip a heavy CMS.

### Minimal Docsify-style layout (optional later)

```text
docs/
  index.html          ← Docsify shell (loads .md)
  README.md           ← home
  outline.md
  sessions/
  howtos/
```

One `index.html`, rest stays markdown — website feel, git-native editing.

---

## Alternatives if GitHub Pages is awkward

| Option | When |
|---|---|
| **Codeberg Pages** | Prefer EU/non-Microsoft git host |
| **Cloudflare Pages** | Free static host from git push |
| **Nextcloud Collectives** (student-only collective) | Want login + collaborative wiki; not as pretty as Pages |
| **Obsidian Publish** (paid) | Mirror a small student vault publicly |
| **Teams “Website” tab** | Embed the Pages URL inside Teams so students who only open Teams still land on the real site |
| **UFG webspace** (if any CGI/static quota) | Only if IT gives a stable HTTPS URL; usually more hassle than Pages |

---

## Suggested operating model

| Need | Where |
|---|---|
| Syllabus, session pages, how-tos, diagrams | **GitHub Pages / docs** |
| “Class starts in room X” / weather backup | **Teams** announcement |
| Official enrolment list | **UFG online** |
| Assignment upload / grades (if forced) | **Moodle** stub links from the site |
| Private teacher research | Stay offline / private vault — never push |

Release rhythm: push student-safe markdown weekly; tag `week-03` if you want snapshots.

---

## Todo (when you decide)

- [ ] Decide public vs private GitHub repo (public is normal for ITP-style; private + invite also fine)
- [ ] Move/copy student kit into `docs/` or `student/` and strip emails/admission
- [ ] Write root `README.md` as the landing page (outline + session table + install order)
- [ ] Enable GitHub Pages (branch `main` / folder `/docs`) **or** add Docsify `index.html`
- [ ] Pin the Pages URL in Teams + UFG online
- [ ] Optional: Moodle empty course with one link button only

---

## Sources

- ACM ITiCSE / related: *GitHub Pages as an LMS Alternative* — https://dl.acm.org/doi/fullHtml/10.1145/3660650.3660667  
- How to Teach Online — content delivery (Canvas/Moodle vs GitHub/Pages) — https://niema.net/How-to-Teach-Online/content_delivery.html  
- NYU ITP faculty — class web space allows GitHub redirects — https://itp.nyu.edu/help/faculty/class-web-space/  
- Example ITP course on GitHub — https://github.com/ellennickles/code-your-way-s26  
- Example GitHub Pages course — https://hmason.github.io/datastorytelling/  
- Peer outline PDF pattern — HKUST AMCC6500 (linked in [[timeline]])  
