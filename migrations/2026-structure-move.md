---
title: Structure move 2026, seminar-first layout
date: 2026-11-23
status: draft
canonical: false
---

# Structure move 2026: seminar-first layout

This report lists what moved, what was added or removed, which checks ran, and which risks remain. It is part of one branch. A human must review it before merge.

Why the structure looks like this, and why it may change: [why this structure](../documentation/why-this-structure.md).

## Summary

- Changed paths against `main`: **126** (81 renamed, 22 added, 19 modified, 4 removed).
- Moves use `git mv`. Each move commit has at most 30 changed files. Links were updated in the same commit group.
- `course/sessions/` became `course/SESSIONS/` in two commits through a temporary name, because Windows and macOS folders ignore case.
- Four old 13-session files were removed from the repo after a copy was kept outside the repo in the teacher vault. See "Removed files".
- Three entry points are drafts: `README.md`, `course/START-HERE.md`, `course/SEMINAR.md`. They are the last commit on the branch.

## New layout

| Folder | Holds |
|---|---|
| `course/THEORY/` | Six topic folders plus a stub for refusal and alternatives |
| `course/PRACTICE/` | Eight technical folders, plus the earlier install-order page |
| `course/SESSIONS/` | Sessions 01 to 08, `overview/`, `lectures/` |
| `course/PROJECT-WORK/` | The minimum path and seven stubs |
| `course/REFERENCES/` | Bibliography, primary sources, peer courses, tool docs stub, current claims |
| `archive/` | The structure proposal and the previous README |
| `documentation/` | Why the structure looks like this |
| `research/`, `UnlearGestaltungAI_Mainz/` | Not changed in place. Links inside were updated where needed |

## Renamed and moved files

Old path, then new path.

| Old | New |
|---|---|
| `course/teacher/potential-structure-change.md` | `archive/potential-structure-change.md` |
| `course/setup/agents-md-template.md` | `course/PRACTICE/01-harness-and-agents/agents-md-template.md` |
| `course/lectures/01-welcome-landscape-deep-dives/default-setup.md` | `course/PRACTICE/01-harness-and-agents/default-setup.md` |
| `course/concepts/hermes-vs-coding-agents.md` | `course/PRACTICE/01-harness-and-agents/hermes-vs-coding-agents.md` |
| `course/setup/howto-hermes-efficient-coding.md` | `course/PRACTICE/01-harness-and-agents/howto-hermes-efficient-coding.md` |
| `course/setup/howto-hermes-opencode-pairing.md` | `course/PRACTICE/01-harness-and-agents/howto-hermes-opencode-pairing.md` |
| `course/setup/howto-hermes-setup.md` | `course/PRACTICE/01-harness-and-agents/howto-hermes-setup.md` |
| `course/setup/howto-opencode-setup.md` | `course/PRACTICE/01-harness-and-agents/howto-opencode-setup.md` |
| `course/concepts/what-is-harness.md` | `course/PRACTICE/01-harness-and-agents/what-is-harness.md` |
| `course/setup/howto-obsidian-setup-and-sync.md` | `course/PRACTICE/02-knowledge-bases/howto-obsidian-setup-and-sync.md` |
| `course/setup/howto-silverbullet-setup-and-sync.md` | `course/PRACTICE/02-knowledge-bases/howto-silverbullet-setup-and-sync.md` |
| `course/setup/knowledge-store-options.md` | `course/PRACTICE/02-knowledge-bases/knowledge-store-options.md` |
| `course/setup/llm-wiki-standard-files.md` | `course/PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md` |
| `course/concepts/what-is-lint.md` | `course/PRACTICE/02-knowledge-bases/what-is-lint.md` |
| `course/setup/Prompting Guide for Critical Vibe Coding.md` | `course/PRACTICE/03-models-and-providers/Prompting Guide for Critical Vibe Coding.md` |
| `course/setup/academic-ai-austria.md` | `course/PRACTICE/03-models-and-providers/academic-ai-austria.md` |
| `course/setup/howto-local-llm-hardware.md` | `course/PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md` |
| `course/setup/howto-hermes-docker-sandbox.md` | `course/PRACTICE/05-security-and-privacy/howto-hermes-docker-sandbox.md` |
| `course/concepts/what-is-mcp.md` | `course/PRACTICE/06-mcp-and-tools/what-is-mcp.md` |
| `course/topics/ai-tools-creative-processes.md` | `course/PRACTICE/07-creative-stacks/ai-tools-creative-processes.md` |
| `course/lectures/01-welcome-landscape-deep-dives/media-art-workflows.md` | `course/PRACTICE/07-creative-stacks/media-art-workflows.md` |
| `course/setup/Local LLM Coding with Hermes.md` | `course/PRACTICE/08-verification-and-provenance/Local LLM Coding with Hermes.md` |
| `course/minimum-path.md` | `course/PROJECT-WORK/minimum-path.md` |
| `course/syllabus/references.md` | `course/REFERENCES/bibliography.md` |
| `course/syllabus/links-from-clippings.md` | `course/REFERENCES/primary-sources.md` |
| `course/sessions/01-welcome-and-landscape.md` | `course/SESSIONS/01-welcome-and-landscape.md` |
| `course/sessions/02-agent-harness-and-wiki-architecture.md` | `course/SESSIONS/02-agent-harness-and-wiki-architecture.md` |
| `course/sessions/03-hardware-open-models-prompting.md` | `course/SESSIONS/03-hardware-open-models-prompting.md` |
| `course/sessions/04-project-presentations-and-plans.md` | `course/SESSIONS/04-project-presentations-and-plans.md` |
| `course/sessions/05-knowledge-base-phone-discord.md` | `course/SESSIONS/05-knowledge-base-phone-discord.md` |
| `course/sessions/06-agent-as-interface.md` | `course/SESSIONS/06-agent-as-interface.md` |
| `course/sessions/07-coding-and-creative-stacks.md` | `course/SESSIONS/07-coding-and-creative-stacks.md` |
| `course/sessions/08-final-presentations.md` | `course/SESSIONS/08-final-presentations.md` |
| `course/lectures/01-welcome-landscape-lecture.md` | `course/SESSIONS/lectures/01-welcome-landscape-lecture.md` |
| `course/lectures/01-welcome-landscape-slideshow/01-welcome-landscape.odp` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/01-welcome-landscape.odp` |
| `course/lectures/01-welcome-landscape-slideshow/01-welcome-landscape.pptx` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/01-welcome-landscape.pptx` |
| `course/lectures/01-welcome-landscape-slideshow/NOTES.md` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/NOTES.md` |
| `course/lectures/01-welcome-landscape-slideshow/README.md` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/README.md` |
| `course/lectures/01-welcome-landscape-slideshow/build_deck.py` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/build_deck.py` |
| `course/lectures/01-welcome-landscape-slideshow/images/04-messy-desk.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/04-messy-desk.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/05-quarto-stato-pellizza.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/05-quarto-stato-pellizza.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/06-datacenter-cooling-tower.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/06-datacenter-cooling-tower.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/11-gw-ranch-heise.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/11-gw-ranch-heise.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/13-meta-el-paso-contentstack.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/13-meta-el-paso-contentstack.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/14-agent-setup-flowchart-medium.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/14-agent-setup-flowchart-medium.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/14-llm-wiki-annotated.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/14-llm-wiki-annotated.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/15-anatomy-of-an-ai-system-joler.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/15-anatomy-of-an-ai-system-joler.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/16-bruegel-tower-of-babel.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/16-bruegel-tower-of-babel.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/20-nyse-crowd-1929.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/20-nyse-crowd-1929.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/21-koehler-der-streik.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/21-koehler-der-streik.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/22-luddite-leader-1812.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/22-luddite-leader-1812.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/23-quadrature-cosmology-of-capital.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/23-quadrature-cosmology-of-capital.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/25-ashburn-data-centers.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/25-ashburn-data-centers.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/27-cloud-vs-local-flowchart.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/27-cloud-vs-local-flowchart.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/27-standard-vs-course-setup.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/27-standard-vs-course-setup.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/28-bigtech-capex-chart.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/28-bigtech-capex-chart.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/29-shiller-cape-chart.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/29-shiller-cape-chart.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/30-bis-labour-share-scenario.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/30-bis-labour-share-scenario.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/31-us-railroad-map-1884.jpg` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/31-us-railroad-map-1884.jpg` |
| `course/lectures/01-welcome-landscape-slideshow/images/32-agentic-ai-loop-bw.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/32-agentic-ai-loop-bw.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/33-bloomberg-circular-ai-deals.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/33-bloomberg-circular-ai-deals.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/34-hype-cycle.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/34-hype-cycle.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/35-us-gdp-tech-capex-chart.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/35-us-gdp-tech-capex-chart.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/36-mag7-sp500-gains-2024.png` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/36-mag7-sp500-gains-2024.png` |
| `course/lectures/01-welcome-landscape-slideshow/images/ATTRIBUTION.md` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/images/ATTRIBUTION.md` |
| `course/lectures/01-welcome-landscape-slideshow/make_images.py` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/make_images.py` |
| `course/lectures/01-welcome-landscape-slideshow/patch_sebastian_edit.py` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/patch_sebastian_edit.py` |
| `course/lectures/02-agent-harness-slideshow/02-agent-harness-and-hermes.md` | `course/SESSIONS/lectures/02-agent-harness-slideshow/02-agent-harness-and-hermes.md` |
| `course/lectures/02-agent-harness-slideshow/README.md` | `course/SESSIONS/lectures/02-agent-harness-slideshow/README.md` |
| `course/lectures/02-agent-harness-slideshow/cvc-slides.css` | `course/SESSIONS/lectures/02-agent-harness-slideshow/cvc-slides.css` |
| `course/presentation-style.md` | `course/SESSIONS/lectures/presentation-style.md` |
| `course/syllabus/00-brief.md` | `course/SESSIONS/overview/00-brief.md` |
| `course/syllabus/course-outline.md` | `course/SESSIONS/overview/course-outline.md` |
| `course/syllabus/course-rhythm.md` | `course/SESSIONS/overview/course-rhythm.md` |
| `course/syllabus/timeline.md` | `course/SESSIONS/overview/timeline.md` |
| `course/lectures/01-welcome-landscape-deep-dives/bubble-economy.md` | `course/THEORY/01-political-economy/bubble-economy.md` |
| `course/lectures/01-welcome-landscape-deep-dives/labour.md` | `course/THEORY/02-labour-authorship/labour.md` |
| `course/lectures/01-welcome-landscape-deep-dives/ecology.md` | `course/THEORY/03-ecology-infrastructure/ecology.md` |
| `course/lectures/01-welcome-landscape-deep-dives/flattening-and-the-norm.md` | `course/THEORY/04-bias-flattening/flattening-and-the-norm.md` |
| `course/topics/eu-ai-act-and-datenschutz.md` | `course/THEORY/05-privacy-regulation/eu-ai-act-and-datenschutz.md` |
| `course/topics/visions-fears-regulation.md` | `course/THEORY/06-danger-and-risk/visions-fears-regulation.md` |

## Added files

- `archive/README-before-seminar-first.md`
- `archive/README.md`
- `course/PRACTICE/README.md`
- `course/PRACTICE/install-order-and-first-week.md`
- `course/PROJECT-WORK/README.md`
- `course/PROJECT-WORK/final.md`
- `course/PROJECT-WORK/interface-score.md`
- `course/PROJECT-WORK/process-log.md`
- `course/PROJECT-WORK/proposal.md`
- `course/PROJECT-WORK/provenance.md`
- `course/PROJECT-WORK/reflection.md`
- `course/PROJECT-WORK/verification.md`
- `course/REFERENCES/README.md`
- `course/REFERENCES/current-claims.md`
- `course/REFERENCES/peer-courses.md`
- `course/REFERENCES/tools-and-documentation.md`
- `course/SEMINAR.md`
- `course/SESSIONS/README.md`
- `course/THEORY/07-refusal-and-alternatives/README.md`
- `course/THEORY/README.md`
- `documentation/why-this-structure.md`
- `migrations/2026-structure-move.md`

## Modified in place

- `.gitignore`
- `AGENTS.md`
- `README.md`
- `UnlearGestaltungAI_Mainz/unlearn-gestaltung/00-index.md`
- `UnlearGestaltungAI_Mainz/unlearn-gestaltung/article-kitegg-cluster.md`
- `UnlearGestaltungAI_Mainz/unlearn-gestaltung/comparison-vs-cvc.md`
- `course/START-HERE.md`
- `course/course-map.md`
- `course/scripts/check-course-links.py`
- `course/scripts/generate-course-map.py`
- `research/ai-brains-critical-thinking.md`
- `research/ai-bubble-productivity-datacenter.md`
- `research/ai-jobs-rising-tide-productivity.md`
- `research/data-centers-energy-ecology-economy.md`
- `research/karpathy-llm-wiki-and-openclaw.md`
- `research/llmwiki-obsidian-vs-nextcloud-collectives.md`
- `research/local-gpu-hardware-for-llms.md`
- `research/obsidian-vs-joplin-hermes-llmwiki.md`
- `research/structure-vs-model-quality.md`

## Removed files

Sebastian approved this removal. The four files below were copied to the teacher vault first. The copies are byte-identical (SHA-256 checked). They sit in a sibling folder next to the course folder, outside the repo. The removal is its own commit.

- `course/sessions/archive-13-session-plan/06-mcp-and-tools.md`
- `course/sessions/archive-13-session-plan/10-authorship-labour-platforms.md`
- `course/sessions/archive-13-session-plan/11-local-ecology-when-not.md`
- `course/sessions/archive-13-session-plan/README.md`

Content that current pages relied on was moved first, then the files were removed:

- The CAD and 3D servers table, the practical and the links from old Session 06 went verbatim to `course/PRACTICE/06-mcp-and-tools/what-is-mcp.md`. Sessions 05 and 07 now link there.
- The prompts, readings and practical from old Session 10 went to `course/THEORY/02-labour-authorship/labour.md`.
- The prompts, readings and practical from old Session 11 went to `course/THEORY/03-ecology-infrastructure/ecology.md`.
- The table of where the old sessions went moved to `course/SESSIONS/overview/timeline.md`.

## Checks

| Check | Result | Numbers |
|---|---|---|
| Link check, default mode, final tree with drafts | PASS | 86 files scanned. 0 broken links in current student files. 0 broken links in other files. 73 notices (wikilinks that only work in Obsidian). Before the move: 0 current, 7 other broken, 102 notices |
| Link check, `--strict` | PASS | 0 broken links anywhere, including `archive/`, `research/`, `documentation/`, `migrations/`. Before the move: 54 broken links in 5 files |
| Case-exact paths in links | PASS | The checker now compares case. 0 case mismatches |
| No lowercase `sessions` folder | PASS | 0 tracked files under `course/sessions/`. The on-disk folder is `SESSIONS` |
| Course map generator | PASS | `generate-course-map.py` ran. 71 rows. It scans `course/`, `archive/`, `documentation/` |
| README has exactly 7 internal links | PASS | 7 links, 0 wikilinks, 0 external links. All 7 targets exist |
| START-HERE shows the 5 required parts | PASS (draft) | Course in one page, how we work, session map, where to find technical notes, midpoint and final |
| SEMINAR explains the 5 required parts | PASS (draft) | Check-in, screen-free discussion, student inputs, group agreements, participation without AI |
| At least 10 files moved into the new folders | PASS | 81 renamed files, with history kept per commit (`git log --follow`) |
| Moved-file content integrity | PASS | Every changed line in a moved or edited file is a link, a path, or an intended new section. No other text was rewritten |
| Old path prefixes left in text | PASS | 0 matches for `course/concepts`, `setup`, `syllabus`, `teacher`, `sessions`, `lectures`, `minimum-path` outside `archive/` and this report |
| Teacher machine paths in student text | PASS | 0 local absolute paths in tracked `.md` and `.py` files |
| No em dashes in new text | PASS | 0 in the new files. Moved files keep their own wording |
| Commit size | PASS | At most 30 changed files in any commit. Author of every commit: `kleinstkariert` |
| Slideshow generator syntax | PASS | `build_deck.py` compiles. Decks were not rebuilt (see AGENTS.md) |

The checker is `course/scripts/check-course-links.py`. It now scans `course/`, `research/`, `archive/`, `documentation/`, `migrations/`, `README.md` and `AGENTS.md`. It compares path case exactly. `--strict` fails on any broken link anywhere.

## Remaining risks

- The binary decks (`.pptx`, `.odp`) were not rebuilt. Their speaker notes still show old paths. Rebuild only when you ask for it.
- The ignored local folder `archive/` inside the first slideshow folder is not tracked. Move it by hand in each existing checkout.
- The vault copy of the course folder is not updated. Sync it additively. A mirror-style sync would delete teacher-only files.
- About 24 wikilinks in teacher-only vault notes point to old paths. They will break until the vault is updated.
- The statement about the G1 to G10 pairing map in `course/SESSIONS/overview/course-rhythm.md` exists only in the vault copy of the old archive files. Check that nothing else is needed from it.
- Many moved pages still describe the old layout in their prose. Only links and paths were changed, as the safety rule requires.
- Rename detection: `08-final-presentations.md` and `what-is-mcp.md` show as delete and add in a single diff against `main`, because many link lines changed. History follows per commit.
- Intermediate commits do not pass `--strict`. Only the last commit does, because the entry points come last by decision.
- `current-claims.md`, `tools-and-documentation.md`, `THEORY/07-refusal-and-alternatives/README.md` and the seven PROJECT-WORK documents are stubs.
- The eight session pages do not use one common template yet.
- The three entry points are drafts. SEMINAR contains rules that are new and not found in older repo text: laptops closed during check-in and discussion, starting points for group agreements, how disagreement is handled, confidentiality. Two of them are marked to confirm with the group.
- Case-only rename: a case-sensitive file system or a Nextcloud sync client may keep the old lowercase folder next to `SESSIONS`. Check each checkout after the pull.
- Open pull requests 16, 17 and 18 were not touched. They still use old paths. 17 and 18 also bring back teacher machine paths that `main` removed. Rebase them on this layout and scrub the paths.
- The course-repo-structure skill outside the repo still describes the old layout and the delete rule.
- Placeholders such as `C:/path/to/lo-profile` and `C:/Windows/Fonts` remain. They are not teacher paths.

## Human approval required

- Review and edit the three entry points: `README.md`, `course/START-HERE.md`, `course/SEMINAR.md`.
- Decide whether the removal of the four archive files stays.
- Merge. Nobody opened or merged a pull request from this branch.
- After merge, rebase the three open pull requests (16, 17, 18) on the new layout.
