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

- Changed paths against `main`: **133** (81 renamed, 28 added, 20 modified, 4 removed).
- Moves use `git mv`. Each move commit has at most 30 changed files. Links were updated in the same commit group.
- `course/sessions/` became `course/SESSIONS/` in two commits through a temporary name, because Windows and macOS folders ignore case.
- Four old 13-session files were removed from the repo after a copy was kept outside the repo in the teacher vault. See "Removed files".
- Three entry points are drafts: `README.md`, `course/START-HERE.md`, `course/SEMINAR.md`. They were the last commit of the first move series.
- Later commits on the same branch: Session 03 became the practical install session (`03-practical-install.md`), the practical class material of pull request 17 was integrated, the tool comparison of pull request 18 became one canonical research page, old paths in deck speaker notes were patched, the lecturer first name was removed from tracked content and file names, and the stub pages were filled or merged.

## New layout

| Folder | Holds |
|---|---|
| `course/THEORY/` | Six topic folders plus an index for refusal and alternatives |
| `course/PRACTICE/` | Eight technical folders, install guides for Windows, Linux and macOS, the starter knowledge base, and the earlier install-order page |
| `course/SESSIONS/` | Sessions 01 to 08, `overview/`, `lectures/` |
| `course/PROJECT-WORK/` | Minimum path, project path (proposal, midpoint, final), provenance with process log, verification, reflection, interface score |
| `course/REFERENCES/` | Bibliography, primary sources, peer courses, tools and documentation, dated models, prices, limits and hardware |
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
| `course/sessions/03-hardware-open-models-prompting.md` | `course/SESSIONS/03-practical-install.md` |
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
| `course/lectures/01-welcome-landscape-slideshow/patch_<author-first-name>_edit.py` | `course/SESSIONS/lectures/01-welcome-landscape-slideshow/patch_lecturer_edit.py` |
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

## Pages merged or renamed during the later work

These stub pages never existed on `main`. They were created in the first series.

- `course/PROJECT-WORK/proposal.md` is now `course/PROJECT-WORK/project-path.md`.
- `course/PROJECT-WORK/final.md` was merged into `project-path.md` and removed.
- `course/PROJECT-WORK/process-log.md` was merged into `provenance.md` and removed.
- `course/REFERENCES/current-claims.md` is now `course/REFERENCES/dated-models-prices-limits-and-hardware.md`.
- `course/SESSIONS/03-hardware-open-models-prompting.md` is now `course/SESSIONS/03-practical-install.md`. It is listed in the rename table.

## Added files

- `archive/README-before-seminar-first.md`
- `archive/README.md`
- `course/PRACTICE/01-harness-and-agents/install-linux.md`
- `course/PRACTICE/01-harness-and-agents/install-mac.md`
- `course/PRACTICE/01-harness-and-agents/install-why.md`
- `course/PRACTICE/01-harness-and-agents/install-windows.md`
- `course/PRACTICE/02-knowledge-bases/starter-knowledge-base.md`
- `course/PRACTICE/README.md`
- `course/PRACTICE/install-order-and-first-week.md`
- `course/PROJECT-WORK/README.md`
- `course/PROJECT-WORK/interface-score.md`
- `course/PROJECT-WORK/project-path.md`
- `course/PROJECT-WORK/provenance.md`
- `course/PROJECT-WORK/reflection.md`
- `course/PROJECT-WORK/verification.md`
- `course/REFERENCES/README.md`
- `course/REFERENCES/dated-models-prices-limits-and-hardware.md`
- `course/REFERENCES/peer-courses.md`
- `course/REFERENCES/tools-and-documentation.md`
- `course/SEMINAR.md`
- `course/SESSIONS/README.md`
- `course/SESSIONS/lectures/03-practical-install-slideshow/03-practical-install.md`
- `course/SESSIONS/lectures/03-practical-install-slideshow/README.md`
- `course/THEORY/07-refusal-and-alternatives/README.md`
- `course/THEORY/README.md`
- `documentation/why-this-structure.md`
- `research/vibe-coding-tools-and-agent-environments.md`
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
- `research/README.md`
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

The course author approved this removal. The four files below were copied to the teacher vault first. The copies are byte-identical (SHA-256 checked). They sit in a sibling folder next to the course folder, outside the repo. The removal is its own commit.

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
| Link check, default mode, final tree | PASS | 92 files scanned. 0 broken links in current student files. 0 broken links in other files. 73 notices (wikilinks that only work in Obsidian). Before the move: 0 current, 7 other broken, 102 notices |
| Link check, `--strict` | PASS | 0 broken links anywhere, including `archive/`, `research/`, `documentation/`, `migrations/`. Before the move: 54 broken links in 5 files. Every commit after the first series was checked before it was made |
| Case-exact paths in links | PASS | The checker compares case. 0 case mismatches |
| No lowercase `sessions` folder | PASS | 0 tracked files under `course/sessions/`. The on-disk folder is `SESSIONS` |
| Course map generator | PASS | `generate-course-map.py` ran. 76 rows. It scans `course/`, `archive/`, `documentation/` |
| README has exactly 7 internal links | PASS | 7 links, 0 wikilinks, 0 external links. All 7 targets exist |
| Stub pages | PASS | 0 pages with an empty body or the text "Stub". `course/REFERENCES/README.md` and `archive/README.md` are deliberate short indexes. `THEORY/07-refusal-and-alternatives/README.md` is a deliberate index |
| Old paths in text | PASS | 0 matches for `course/sessions`, `course/lectures`, `course/setup`, `course/concepts`, `course/syllabus`, `course/teacher`, `current-claims`, `03-hardware-open-models-prompting`, `PROJECT-WORK/proposal`, `final`, `process-log` outside `archive/` and this report |
| Old paths in deck speaker notes | PASS | 0 old-path strings in the 15 patched notes slides of the pptx and in the odp `content.xml`. Method: only the notes XML was rewritten, all other zip entries copied unchanged. `testzip` passed for both files. python-pptx still reads 57 slides. The odp (56 pages) was patched directly, not rebuilt from the pptx |
| Lecturer first name removed | PASS | 0 case-insensitive matches in tracked file names, in tracked text and in deck XML. This report names the old script as `patch_<author-first-name>_edit.py`. Git history was not changed |
| Teacher machine paths in student text | PASS | 0 local absolute paths in tracked `.md` and `.py` files |
| No em dashes in new text | PASS | 0 in text written for this branch. Moved and merged files keep their own wording, and some older lines still have em dashes |
| Commit size | PASS | At most 30 changed files in any commit. Author of every commit: `kleinstkariert` |
| Scripts compile | PASS | `check-course-links.py`, `generate-course-map.py`, `build_deck.py`, `patch_lecturer_edit.py` compile. Decks were not rebuilt (see AGENTS.md) |

The checker is `course/scripts/check-course-links.py`. It now scans `course/`, `research/`, `archive/`, `documentation/`, `migrations/`, `README.md` and `AGENTS.md`. It compares path case exactly. `--strict` fails on any broken link anywhere.

## Remaining risks

- The pptx and odp were patched in the speaker notes only. The odp has 56 pages and the pptx has 57 slides, so the two decks were not in sync before the patch and still are not. A full rebuild was not run, as AGENTS.md asks.
- The ignored local folder `archive/` inside the first slideshow folder is not tracked. Move it by hand in each existing checkout.
- The teacher vault is not updated. 19 vault-only files exist (teacher notes, hardware notes, the pull request 18 note, three old decks). Sync it additively. A mirror-style sync would delete teacher-only files.
- About 24 wikilinks in teacher-only vault notes point to old paths. They break until the vault is updated.
- Many moved pages still describe the old layout in their prose. Only links and paths were changed, as the safety rule requires.
- The Session 03 page, the dated models, prices, limits and hardware page, and the PROJECT-WORK pages are new text written for this branch. They have not been tested in class.
- Rows of the dated page and the tool comparison were not all rechecked on 23 Nov 2026. Each row shows its own check date. Prices, star counts and model names change.
- The AgentCraft section rests on two READMEs and the GitHub API. Its safety claims are marked as claims and were not tested.
- Session 03 has no Docker baseline. The Docker guide is for an advanced workshop. If you want it back in class, change `03-practical-install.md`.
- The install guides come from pull request 17 and were merged by hand with a 3-way merge. They were not run on a clean machine again.
- The project-path, provenance, verification, reflection and interface-score pages mostly link to older notes. They are short on purpose.
- The eight session pages do not use one common template yet.
- The three entry points are drafts. SEMINAR contains rules that are new and not found in older repo text: laptops closed during check-in and discussion, starting points for group agreements, how disagreement is handled, confidentiality. Two of them are marked to confirm with the group.
- Case-only rename: a case-sensitive file system or a Nextcloud sync client may keep the old lowercase folder next to `SESSIONS`. Check each checkout after the pull.
- Pull requests 17 and 18 were not touched or closed. Their content is integrated here, so they are superseded. Pull request 16 was not touched and may conflict with the new paths.
- The course-repo-structure skill outside the repo still describes the old layout and the delete rule.
- Placeholders such as `C:/path/to/lo-profile` and `C:/Windows/Fonts` remain. They are not teacher paths.

## Human approval required

- Review and edit the three entry points: `README.md`, `course/START-HERE.md`, `course/SEMINAR.md`.
- Decide whether the removal of the four archive files stays.
- Merge. Nobody opened or merged a pull request from this branch.
- Decide whether the teacher vault is synced, and how (additive only). Nothing was synced or deleted in the vault.
- Pull requests 17 and 18 are superseded by the integrated content. Pull request 16 was not touched. Decide whether to close them.
