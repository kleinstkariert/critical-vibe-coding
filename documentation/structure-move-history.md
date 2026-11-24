---
title: Structure move history
date: 2026-11-23
status: draft
canonical: false
---

# Structure move history

This page is the factual record of the seminar-first move: what moved, what was added or removed, which checks ran, and which risks remain. It belongs to one branch. A human must review it before merge.

The reasons for the structure, and its doubts, are on [why this structure](why-this-structure.md). This page does not repeat them.

## Summary

- Changed paths against `main`: **164** (94 renamed, 51 added, 12 modified, 7 removed). Git pairs a rename only when the files stay at least 30% alike, so some heavily rewritten pages count as added.
- Moves use `git mv`. Each commit has at most 30 changed files. Links, wikilinks and inline paths were updated in the same commit group.
- `course/sessions/` became `course/SESSIONS/` in two commits through a temporary name, because Windows and macOS folders ignore case.
- Seven files were removed from the repo: four old 13-session files, the structure proposal and two Academic AI source files (a PDF and a PPTX). A copy of each is kept outside the repo. See "Removed files".
- First series: the seminar-first layout, three draft entry points (`README.md`, `course/START-HERE.md`, `course/SEMINAR.md`), Session 03 as the practical install session, the install guides, the tool comparison as one canonical page, and the removal of the lecturer first name from tracked text and file names.
- Second series: the changes listed in "Second series of moves".

## Layout now

| Folder | Holds |
|---|---|
| `course/THEORY/` | Six topic folders plus an index for refusal and alternatives |
| `course/PRACTICE/` | Eight technical folders, install guides for Windows, Linux and macOS, the starter knowledge base, and the [install order](../course/PRACTICE/install-order.md) |
| `course/SESSIONS/` | Sessions 01 to 08, `overview/`, `lectures/` |
| `course/PROJECT-WORK/` | Numbered guide pages `01_` to `06_` and an index that explains the sequence |
| `course/templates/` | Blank forms for the required documents, and an index |
| `course/REFERENCES/` | Bibliography, primary sources, peer courses, tools and documentation, dated models, prices, limits and hardware, and `guidelines-and-handbooks/` |
| `research/` | Humanistic, social and conceptual research notes |
| `research/software&DataManagement/` | Tool, data, store and hardware research, including the one canonical tool comparison and `hardware/` |
| `research/externalReferences/` | Notes by other groups: `UnlearGestaltungAI_Mainz/` |
| `archive/` | The previous navigation page |
| `documentation/` | This record and the reasons for the structure |

## Second series of moves

| Change | Detail |
|---|---|
| Record merged into `documentation/` | `migrations/2026-structure-move.md` became `documentation/structure-move-history.md`. The `migrations/` folder is gone |
| Reader label removed | The reader-label field was removed from the frontmatter of every tracked page. The link checker and the course map generator no longer read it. The map has the columns Page, Status and Canonical |
| Research split by purpose | Tool, data, store and hardware notes moved to `research/software&DataManagement/`, hardware notes to `.../hardware/`. Four humanistic notes stayed in `research/` |
| External notes moved | `UnlearGestaltungAI_Mainz/` moved to `research/externalReferences/UnlearGestaltungAI_Mainz/` (9 files) |
| Guidelines and handbooks | New folder `course/REFERENCES/guidelines-and-handbooks/` with an index and English translations of the Academic AI user manual and presentation. See "Guidelines and handbooks" |
| Archive page renamed | `archive/README-before-seminar-first.md` became `archive/former-repository-navigation.md` |
| Spaced file names | `Prompting Guide for Critical Vibe Coding.md` and `Local LLM Coding with Hermes.md` became kebab-case names. Links, deck-note paths and the map were updated |
| Install order | `course/PRACTICE/install-order-and-first-week.md` became `course/PRACTICE/install-order.md`. It now holds the install order only |
| PROJECT-WORK sequence | Pages got the prefixes `01_` to `06_` in the order a student meets them. `README.md` stays the index |
| Templates | New folder `course/templates/` with nine blank forms and an index. Blank tables moved out of the guide pages |
| Tool comparison links | One link to the canonical comparison was added where Hermes is optional or alternatives are valid (see "Tool comparison audit") |
| Deck speaker notes | The pptx and odp notes point to the moved hardware research note. Only the notes XML was patched |
| Python cache | One accidental `.pyc` file was removed from the index. `.gitignore` now ignores Python caches |

## Renamed and moved files

Old path, then new path.

| Old | New |
|---|---|
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
| `course/setup/academic-ai-austria.md` | `course/PRACTICE/03-models-and-providers/academic-ai-austria.md` |
| `course/setup/Prompting Guide for Critical Vibe Coding.md` | `course/PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md` |
| `course/setup/howto-local-llm-hardware.md` | `course/PRACTICE/04-local-and-cloud/howto-local-llm-hardware.md` |
| `course/setup/howto-hermes-docker-sandbox.md` | `course/PRACTICE/05-security-and-privacy/howto-hermes-docker-sandbox.md` |
| `course/concepts/what-is-mcp.md` | `course/PRACTICE/06-mcp-and-tools/what-is-mcp.md` |
| `course/topics/ai-tools-creative-processes.md` | `course/PRACTICE/07-creative-stacks/ai-tools-creative-processes.md` |
| `course/lectures/01-welcome-landscape-deep-dives/media-art-workflows.md` | `course/PRACTICE/07-creative-stacks/media-art-workflows.md` |
| `course/setup/Local LLM Coding with Hermes.md` | `course/PRACTICE/08-verification-and-provenance/local-llm-coding-with-hermes.md` |
| `course/minimum-path.md` | `course/PROJECT-WORK/01_minimum-path.md` |
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
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/00-index.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/00-index.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/article-how-to-kitegg.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/article-how-to-kitegg.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/article-kitegg-cluster.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/article-kitegg-cluster.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/comparison-vs-cvc.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/comparison-vs-cvc.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/diy-compute.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/diy-compute.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/systems-labs-overview.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/systems-labs-overview.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/vol1-approaching.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/vol1-approaching.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/vol2-navigating.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/vol2-navigating.md` |
| `UnlearGestaltungAI_Mainz/unlearn-gestaltung/vol3-integrating.md` | `research/externalReferences/UnlearGestaltungAI_Mainz/unlearn-gestaltung/vol3-integrating.md` |
| `research/karpathy-llm-wiki-and-openclaw.md` | `research/software&DataManagement/karpathy-llm-wiki-and-openclaw.md` |
| `research/llmwiki-obsidian-vs-nextcloud-collectives.md` | `research/software&DataManagement/llmwiki-obsidian-vs-nextcloud-collectives.md` |
| `research/local-gpu-hardware-for-llms.md` | `research/software&DataManagement/local-gpu-hardware-for-llms.md` |
| `research/obsidian-vs-joplin-hermes-llmwiki.md` | `research/software&DataManagement/obsidian-vs-joplin-hermes-llmwiki.md` |
| `research/structure-vs-model-quality.md` | `research/software&DataManagement/structure-vs-model-quality.md` |

## Pages merged or renamed during the later work

These pages never existed on `main`. They were created in the first series.

- `course/PROJECT-WORK/proposal.md` became `project-path.md`, now `02_project-path.md`.
- `course/PROJECT-WORK/final.md` was merged into the project path page and removed.
- `course/PROJECT-WORK/process-log.md` was merged into the provenance page and removed.
- `course/REFERENCES/current-claims.md` is now `course/REFERENCES/dated-models-prices-limits-and-hardware.md`.
- `course/SESSIONS/03-hardware-open-models-prompting.md` is now `course/SESSIONS/03-practical-install.md`. It is in the rename table.

## Hardware research

Eight hardware-procurement notes existed only in the teacher vault. They were copied into the repo as student-visible research. They now sit in `research/software&DataManagement/hardware/`. Local paths, wikilinks, the "private, ignored by Git" markers, the "send this" workflow text and the author name were removed. Prices and specifications are labelled as dated research (29 Oct 2026). No price, benchmark or model size was rechecked. Where a note recorded no date or source, the page says so.

| Vault note | Repo file (in `hardware/`) | Treatment |
|---|---|---|
| `00-index-budget-vs-spark.md` | `README.md` | Entry point. Shared assumptions, options table, efficiency conclusion, shared technical notes and cautions |
| `01-budget-letter.md` | `diy-request-draft.md` | Kept the request, ceilings, purpose and decision. The cost table, the Spark comparison and the risk table became links |
| `02-recommended-spark-production-hermes.md` | `spark-gb10-recommended-system.md` | Kept all sections. Fixed two wording problems. Marked unsourced claims |
| `A-dual-3090-open-frame.md` | `setup-a-dual-3090-open-frame.md` | Kept the parts table. Shared prose became links |
| `B-dual-4090-open-frame.md` | `setup-b-dual-4090-open-frame.md` | Kept in full, plus evidence column |
| `C-triple-3090-open-frame.md` | `setup-c-triple-3090-open-frame.md` | Kept the parts table. Shared prose became links |
| `D-dual-5090-ceiling.md` | `setup-d-dual-5090-ceiling.md` | Kept in full, plus evidence column |
| `llm-coding-capability-matrix.md` | `llm-coding-capability-matrix.md` | Kept the matrix and the long-context note. The efficiency table moved to the README |

Redundancy decisions:

- Overview, envelope, VAT, price date and the contingency rule appeared in the index, the letter and the setup notes. They now live once in the README.
- The efficiency summary appeared in the index and in the matrix. It is one table in the README. The matrix links to it.
- The Spark versus DIY comparison and the speed figures appeared in four notes. The figures are in one README table. The other pages link to it.
- "Memory is split, not unified", the llama.cpp split modes and the power-cable rule appeared in Setups A and C and in the matrix. They are in one README section.
- The letter's risk table and the index cautions overlapped. They are one README table. The two items that only the letter had were kept.
- Not merged: the five build options, the capability matrix and the long Spark note. They hold different content.
- Overlap with older pages: the older pages keep the general explanation, the new pages link to it.
- Source inconsistency kept and labelled, not resolved: the Spark note gives a three-year total of about 7,100 to 7,700 euros in the cost model and about 7,200 to 8,000 euros in the example text.

## Teacher notes check

- `course/teacher/` has no tracked file on this branch. 0 tracked paths contain `teacher` in a folder or file name.
- Seven vault teacher notes have no copy in the repo (0 byte-identical, 0 shared text lines of length over 40 against any tracked Markdown file).
- The structure proposal was the one teacher note tracked on `main`. It is removed from the repository (see Removed files).
- 0 tracked files have a reader-label frontmatter field.

## Tool comparison audit

- `research/software&DataManagement/vibe-coding-tools-and-agent-environments.md` is the one full comparison. `course/REFERENCES/tools-and-documentation.md` is a pointer with a documentation link table. No other page repeats licences, prices or star counts.
- The comparison names Hermes, OpenCode, Claude Code, Cursor, VS Code with Copilot, Continue, Cline, Windsurf and Devin, Zed AI, Codex CLI, Aider, Gemini CLI, AgentCraft and Antigravity. Its Words table separates editor, assistant, coding agent, harness or runtime, and model provider.
- Pages that link to it: `README.md`, `course/START-HERE.md`, `course/SEMINAR.md`, `course/PRACTICE/README.md`, `course/PRACTICE/install-order.md`, `course/PROJECT-WORK/01_minimum-path.md`, the Hermes install pages, the harness pages, the models and providers pages, Sessions 02 and 03, `course/REFERENCES/tools-and-documentation.md` and `research/software&DataManagement/README.md`.
- `course/PRACTICE/01-harness-and-agents/hermes-vs-coding-agents.md` compares jobs, not licences or prices. It stays and points to the comparison.

## Guidelines and handbooks

The two source documents were in a folder `RichtlinienUndLeitblaetter/` outside `course/`. Each now has an English Markdown translation in `course/REFERENCES/guidelines-and-handbooks/`. The course author approved the removal of both source files from Git on 24 Nov 2026. Copies stay outside the repo. No public URL was verified for either source, and nobody has independently checked the translations against the originals.

| Source used for the translation | English Markdown | Public source | Source file |
|---|---|---|---|
| Academic AI user manual, German, version V 2.1 of 09.09.2026 | `academic-ai-user-manual.md` | No public URL of V 2.1 was found. The page links the older official V 2.0 (27.07.2026): `https://www.kunstuni-linz.at/fileadmin/media/KI/0726_Benutzerhandbuch_Academic_AI_3.0-V2.0.pdf` | Removed from Git (old path `RichtlinienUndLeitblaetter/Benutzerhandbuch Academic AI 3.0 - V2.1.pdf`) |
| Academic AI presentation, German, October 2026 | `academic-ai-presentation.md` | No publisher and no public original URL were found | Removed from Git (old path `RichtlinienUndLeitblaetter/Academic_AI_Vortrag_10_2026.pptx`) |

The translation headers and the folder README say this. The V 2.0 link is for orientation only and does not confirm the text of V 2.1. The files stay in the Git history of `main`.

## Added files

- `archive/README.md`
- `archive/former-repository-navigation.md`
- `course/PRACTICE/01-harness-and-agents/install-linux.md`
- `course/PRACTICE/01-harness-and-agents/install-mac.md`
- `course/PRACTICE/01-harness-and-agents/install-why.md`
- `course/PRACTICE/01-harness-and-agents/install-windows.md`
- `course/PRACTICE/02-knowledge-bases/starter-knowledge-base.md`
- `course/PRACTICE/README.md`
- `course/PRACTICE/install-order.md`
- `course/PROJECT-WORK/02_project-path.md`
- `course/PROJECT-WORK/03_provenance.md`
- `course/PROJECT-WORK/04_verification.md`
- `course/PROJECT-WORK/05_interface-score.md`
- `course/PROJECT-WORK/06_reflection.md`
- `course/PROJECT-WORK/README.md`
- `course/REFERENCES/README.md`
- `course/REFERENCES/dated-models-prices-limits-and-hardware.md`
- `course/REFERENCES/guidelines-and-handbooks/README.md`
- `course/REFERENCES/guidelines-and-handbooks/academic-ai-presentation.md`
- `course/REFERENCES/guidelines-and-handbooks/academic-ai-user-manual.md`
- `course/REFERENCES/peer-courses.md`
- `course/REFERENCES/tools-and-documentation.md`
- `course/SEMINAR.md`
- `course/SESSIONS/README.md`
- `course/SESSIONS/lectures/03-practical-install-slideshow/03-practical-install.md`
- `course/SESSIONS/lectures/03-practical-install-slideshow/README.md`
- `course/THEORY/07-refusal-and-alternatives/README.md`
- `course/THEORY/README.md`
- `course/templates/README.md`
- `course/templates/critical-reflection.md`
- `course/templates/final-presentation.md`
- `course/templates/group-input-presentation.md`
- `course/templates/interface-score.md`
- `course/templates/manifesto.md`
- `course/templates/midpoint-check.md`
- `course/templates/project-proposal.md`
- `course/templates/provenance-note-and-log.md`
- `course/templates/verification-plan.md`
- `documentation/structure-move-history.md`
- `documentation/why-this-structure.md`
- `research/externalReferences/README.md`
- `research/software&DataManagement/README.md`
- `research/software&DataManagement/hardware/README.md`
- `research/software&DataManagement/hardware/diy-request-draft.md`
- `research/software&DataManagement/hardware/llm-coding-capability-matrix.md`
- `research/software&DataManagement/hardware/setup-a-dual-3090-open-frame.md`
- `research/software&DataManagement/hardware/setup-b-dual-4090-open-frame.md`
- `research/software&DataManagement/hardware/setup-c-triple-3090-open-frame.md`
- `research/software&DataManagement/hardware/setup-d-dual-5090-ceiling.md`
- `research/software&DataManagement/hardware/spark-gb10-recommended-system.md`
- `research/software&DataManagement/vibe-coding-tools-and-agent-environments.md`

## Modified in place

- `.gitignore`
- `AGENTS.md`
- `README.md`
- `course/START-HERE.md`
- `course/course-map.md`
- `course/scripts/check-course-links.py`
- `course/scripts/generate-course-map.py`
- `research/README.md`
- `research/ai-brains-critical-thinking.md`
- `research/ai-bubble-productivity-datacenter.md`
- `research/ai-jobs-rising-tide-productivity.md`
- `research/data-centers-energy-ecology-economy.md`

## Removed files

The course author approved each removal. Seven files are listed below.

- The four `archive-13-session-plan` files were copied to the teacher vault first. The copies are byte-identical (SHA-256 checked). They sit outside the repo.
- The two Academic AI source files (`RichtlinienUndLeitblaetter/`) are covered under "Guidelines and handbooks".
- `course/teacher/potential-structure-change.md` is the structure proposal. The course author approved its removal on 24 Nov 2026. A copy stays in the teacher vault, outside the repo. Its reasoning is on [why this structure](why-this-structure.md).

- `RichtlinienUndLeitblaetter/Academic_AI_Vortrag_10_2026.pptx`
- `RichtlinienUndLeitblaetter/Benutzerhandbuch Academic AI 3.0 - V2.1.pdf`
- `course/sessions/archive-13-session-plan/06-mcp-and-tools.md`
- `course/sessions/archive-13-session-plan/10-authorship-labour-platforms.md`
- `course/sessions/archive-13-session-plan/11-local-ecology-when-not.md`
- `course/sessions/archive-13-session-plan/README.md`
- `course/teacher/potential-structure-change.md`

Content that current pages relied on was moved first, then the files were removed:

- The CAD and 3D servers table, the practical and the links from old Session 06 went verbatim to `course/PRACTICE/06-mcp-and-tools/what-is-mcp.md`.
- The prompts, readings and practical from old Session 10 went to `course/THEORY/02-labour-authorship/labour.md`.
- The prompts, readings and practical from old Session 11 went to `course/THEORY/03-ecology-infrastructure/ecology.md`.
- The table of where the old sessions went moved to `course/SESSIONS/overview/timeline.md`.

## Checks

Pass 1 ran in the working tree. Pass 2 ran independently in a fresh clone of the committed branch. The script is `course/scripts/check-course-links.py`. It compares path case exactly. `--strict` fails on any broken link and resolves wikilinks by path only.

| Check | Result | Pass 1 | Pass 2 |
|---|---|---|---|
| Strict link check (links, wikilinks by path, heading anchors, exact case) | PASS | 123 files, 0 broken links, 111 notices (Obsidian-only wikilinks) | 123 files, 0 broken links, 111 notices (Obsidian-only wikilinks) |
| Independent link pass (separate script, GitHub heading slugs, exact case) | PASS | 123 Markdown files, 1423 relative links, 0 broken. A first run found 4 broken heading anchors, repaired once. After the two source files were removed: 1419 links, 0 broken | 123 Markdown files, 1419 relative links, 0 broken |
| Stale old-path scan | PASS | 3 pattern matches, all reviewed, 0 stale (one vault note name, two link labels) | 3 pattern matches, all reviewed, 0 stale (one vault note name, two link labels) |
| Frontmatter scan (reader-label field, malformed blocks) | PASS | 0 reader-label fields, 0 malformed blocks | 0 reader-label fields, 0 malformed blocks |
| Name scan (case-insensitive, text, file names, deck XML) | PASS | 0 in 129 text files, 159 file names and 2 deck packages | 0 in 129 text files, 159 file names and 2 deck packages |
| Local machine path scan | PASS | 0 (one match is the word OneDrive, a cloud product) | 0 (one match is the word OneDrive, a cloud product) |
| Duplicate canonical content scan | PASS with notes | 54 sentences repeated across files, mostly between the three OS install guides, by design. One page holds the tool comparison | 54 sentences repeated across files, mostly between the three OS install guides, by design. One page holds the tool comparison |
| Content loss scan against `origin/main` | PASS | 229 old lines are not in the new tree. All sit in rewritten entry pages, removed files, the Session 03 rewrite, name removal or link-label edits | 229 old lines are not in the new tree. All sit in rewritten entry pages, removed files, the Session 03 rewrite, name removal or link-label edits |
| Course map generator | PASS | 89 rows, 0 reader-label columns | 89 rows. One stale page title found and regenerated |
| Deck packages (zip test, python-pptx, old paths in notes XML) | PASS | zip test OK (pptx 291 entries, odp 40), 57 slides, 0 old paths in notes XML | zip test OK (pptx 291 entries, odp 40), 57 slides, 0 old paths in notes XML |
| README entry points | PASS | 7 internal links (START-HERE, SEMINAR, THEORY, PRACTICE, SESSIONS, PROJECT-WORK, REFERENCES), 0 wikilinks, 0 external links | 7 internal links (START-HERE, SEMINAR, THEORY, PRACTICE, SESSIONS, PROJECT-WORK, REFERENCES), 0 wikilinks, 0 external links |
| Stub pages, `teacher` paths, lowercase `sessions` | PASS | 0 stub pages, 0 `teacher` paths, 0 files under `course/sessions/` | 0 stub pages, 0 `teacher` paths, 0 files under `course/sessions/` |
| Em dashes in new text | PASS with notes | 0 in text written for this branch. 2 moved pages carry old ones | 0 in text written for this branch. 2 moved pages carry old ones |
| Tracked binary scan (guideline originals removed) | PASS | Only the lecture deck pair (pptx, odp) remains as tracked document binaries. 0 guideline originals tracked, 0 references to their file names | Only the lecture deck pair (pptx, odp) remains as tracked document binaries. 0 guideline originals tracked, 0 references to their file names |
| Scripts compile | PASS | 5 files compile | 5 files compile |
| Commit size and author | PASS | At most 30 files per commit. One author: `kleinstkariert` | At most 30 files per commit. One author: `kleinstkariert` |

## Remaining risks

- The English translations rest on a German manual V 2.1 (09.09.2026) and a German presentation (October 2026). No public URL of V 2.1, and no publisher or public URL of the presentation, was found. The older official V 2.0 manual is linked for orientation only. The two source files are no longer in the repo. They stay in the Git history of main and outside the repo.
- The two English translations were written for this branch. Nobody has compared them with the originals line by line. The manual figures appear as captions only. Check them before class.
- The official manual says institution admins can create API clients, and it points to API documentation. `course/PRACTICE/03-models-and-providers/academic-ai-austria.md` and the install order say campus academic AI has no API for agents. This was not changed. Ask the campus admin.
- The pptx and odp were patched in the speaker notes only. The odp has 56 pages and the pptx has 57 slides, so the two decks were not in sync before and still are not. Several notes use short paths such as `course/what-is-mcp.md` that never resolved. A full rebuild was not run, as AGENTS.md asks.
- The ignored local folder `archive/` inside the first slideshow folder is not tracked. Move it by hand in each existing checkout.
- The teacher vault is not updated. It still holds 19 vault-only files. Eight hardware notes are now also in the repo, so their vault originals are duplicates until the course author decides. Sync additively. A mirror-style sync would delete teacher-only files.
- Hardware research lives under `research/software&DataManagement/hardware/`. The placement is a judgment call. The `&` in the folder name needs quoting in some shells and sync tools.
- The hardware notes keep source inconsistencies and gaps as labels. They do not resolve them. No price was rechecked. They contain procurement arguments, marked as claims. Review them before you show them to students.
- Many moved pages still describe the old layout in their prose, because only links and paths were changed. One example: `howto-hermes-efficient-coding.md` names `Local LLM Coding with Hermes.md` as the vault note, and that is still the vault file name.
- The Session 03 page, the dated page, the PROJECT-WORK pages, the templates and the install order are new text. They have not been tested in class.
- Rows of the dated page and the tool comparison were not all rechecked on 23 Nov 2026. Each row shows its own check date. Prices, star counts and model names change.
- The AgentCraft section rests on two READMEs and the GitHub API. Its safety claims are marked as claims and were not tested.
- Four heading links did not work on GitHub, because GitHub keeps double hyphens when a heading has a dash or slash. They were repaired, and the checker now uses the same slug rule. Other tools may slug differently.
- Case-only rename: a case-sensitive file system or a Nextcloud sync client may keep the old lowercase folder next to `SESSIONS`. Check each checkout after the pull.
- Pull requests 17 and 18 were not touched or closed. Their content is integrated here. Pull request 16 was not touched and may conflict with the new paths.
- The course-repo-structure skill outside the repo still describes the old layout and the delete rule.
- Older moved text still holds about 440 em dashes in 36 files. Two added pages carry old em dashes in titles of external works: `archive/former-repository-navigation.md` and `course/REFERENCES/peer-courses.md`. New text written for this branch has none.
- The three OS install guides repeat many sentences on purpose, because each guide stands alone.
- The eight session pages do not use one common template. This was not decided.
- Placeholders such as `C:/path/to/lo-profile` and `C:/Windows/Fonts` remain. They are not machine paths of the teacher.

## Human approval required

- Supply an official URL for the V 2.1 manual or the presentation if one becomes known. Until then the pages keep their present wording.
- Confirm the folder name `research/software&DataManagement/` and the placement of `hardware/` inside it.
- Review the three entry points: `README.md`, `course/START-HERE.md`, `course/SEMINAR.md`.
- Decide whether the removal of the four archive files and the structure proposal stays.
- Merge. Nobody opened or merged a pull request from this branch.
- Decide whether the teacher vault is synced, and how (additive only). Nothing was synced or deleted in the vault.
- Decide whether to close pull requests 17 and 18.
