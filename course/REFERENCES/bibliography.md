---
title: Critical Vibe Coding — references
date: 2026-10-18
tags:
  - course
  - references
audience: student
status: current
canonical: true
---

# References

Working bibliography for the seminar. Prefer primary evidence in class. YouTube is optional prep. A URL that loaded on 2026-10-18 is not, by itself, a checked claim.

## Source types

*Verified fact* in older notes often meant only that a web page existed, or that a claim appeared in a source. It did not always mean the claim was checked against primary evidence. Do not read an old *verified fact* tag as independent verification.

| Type | What it is |
|---|---|
| Primary evidence | A filing, a law, an official specification, a peer-reviewed paper, or an original dataset. |
| Institutional summary | An agency, a university, a research institution, or an official explanatory page. |
| Secondary reporting | Reputable journalism or analysis. |
| Speaker claim | A podcast, a talk, an interview, or a keynote. |
| Course interpretation | The instructor's synthesis. |
| Unverified lead | A source was found. It was not checked. |
| Outdated / historical snapshot | The source is no longer current. |

A label names the kind of source. It does not, by itself, mean the claim was independently verified.

Copy this source record:

```yaml
source_type: primary | institutional | secondary | speaker | course
checked_on: YYYY-MM-DD
independent_verification: yes | no
current_as_of: YYYY-MM-DD
claim_scope: exact | paraphrase | interpretation
```

`checked_on` is the date the source was opened. Leave it empty if you do not have that date. `independent_verification: yes` means the claim was checked against primary evidence, not only that a page opened. Do not invent a date. For an unverified lead, or for an outdated snapshot, say so in the prose next to the record.

## LLM Wiki — primary

| Source | URL |
|---|---|
| Andrej Karpathy, `llm-wiki.md` gist (2026-04-04) | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f |
| Mirror / readable site | https://llm-wiki.md/ |
| Schema-focused reading | https://cozypet.github.io/llm-wiki-schema/ |
| Dexio — LLM Wiki in Obsidian guide | https://dexio.wiki/guides/llm-wiki-obsidian/ |

## Hermes Agent

| Source | URL |
|---|---|
| Hermes docs home | https://hermes-agent.nousresearch.com/docs/ |
| Bundled **llm-wiki** skill (ingest / query / lint) | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki |
| Skill source `SKILL.md` | https://github.com/NousResearch/hermes-agent/blob/HEAD/skills/research/llm-wiki/SKILL.md |
| Obsidian note-taking skill | https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian |
| MCP feature | https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp |
| Discord setup (bot, DMs vs mention-only channels, per-user sessions). Added 2026-10-18. *institutional summary*. The page loaded. The claims were not independently verified. | https://hermes-agent.nousresearch.com/docs/user-guide/messaging/discord |
| Installation | https://hermes-agent.nousresearch.com/docs/getting-started/installation |

Course how-to (Win / macOS / Linux): [howto hermes setup](../PRACTICE/01-harness-and-agents/howto-hermes-setup.md)  
Short syllabus sheet: [course outline](../SESSIONS/overview/course-outline.md)  
What is a harness: [what is harness](../PRACTICE/01-harness-and-agents/what-is-harness.md)  
Prompting guide (chat versus reasoning, STE80, Hermes context): [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/Prompting%20Guide%20for%20Critical%20Vibe%20Coding.md)  
Academic AI Austria: [academic ai austria](../PRACTICE/03-models-and-providers/academic-ai-austria.md)  
Drivers / visions / fears / regulation (Session 01, 10–15 min): [visions fears regulation](../THEORY/06-danger-and-risk/visions-fears-regulation.md)  
AI jobs — rising tide, Canaries, productivity × experience: [ai jobs rising tide productivity](../../research/ai-jobs-rising-tide-productivity.md)  
AI, brains, critical thinking (MIT EEG + recent clippings): [ai brains critical thinking](../../research/ai-brains-critical-thinking.md)  
Curated vault clipping links (scan 2026-11-11): [links from clippings](primary-sources.md)  
EU AI Act, and GDPR (separate topics): [eu ai act and datenschutz](../THEORY/05-privacy-regulation/eu-ai-act-and-datenschutz.md#decision-questions)  
AI creative tools survey: [ai tools creative processes](../PRACTICE/07-creative-stacks/ai-tools-creative-processes.md)  
Session 01 lecture draft: [01 welcome landscape lecture](../SESSIONS/lectures/01-welcome-landscape-lecture.md)  
Session 02 harness + wiki: [02 agent harness and wiki architecture](../SESSIONS/02-agent-harness-and-wiki-architecture.md)  
Local GPU / Apple / DGX research: [local gpu hardware for llms](../../research/software&DataManagement/local-gpu-hardware-for-llms.md)  
Bubble / productivity / DC financing: [ai bubble productivity datacenter](../../research/ai-bubble-productivity-datacenter.md)  
Data centres: energy, ecology, US/world economy (Session 01 Block 5; student input Session 06): [data centers energy ecology economy](../../research/data-centers-energy-ecology-economy.md)  
Presentation style: [presentation style](../SESSIONS/lectures/presentation-style.md)

## Obsidian auto LLM Wiki plugin

| Source | URL |
|---|---|
| Community plugin **Karpathy LLM Wiki** (`karpathywiki`) | https://community.obsidian.md/plugins/karpathywiki |
| GitHub `GD4AI/obsidian-llm-wiki` | https://github.com/GD4AI/obsidian-llm-wiki |
| Project site / blog | https://llmwiki.greenerai.top/ · https://llmwiki.greenerai.top/blog/ |
| Sister CLI | https://github.com/green-dalii/obsidian-llm-wiki-cli |

*technical suggestion:* Class default = Hermes writing a folder + Obsidian as viewer. The plugin is the “auto wiki inside Obsidian” path (ingest/query/**lint health scan** in-app). Students may try either; do not run two writers on the same pages without a clear rule.

## YouTube (optional watching)

| Title | URL | Use |
|---|---|---|
| Karpathy's LLM Wiki — Full Beginner Setup Guide (Teachers Tech / Jamie) | https://www.youtube.com/watch?v=iXd0t60YmMw | Beginner folder + agent walkthrough |
| Karpathy's LLM Wiki: What It Means & How to Build One | https://www.youtube.com/watch?v=zVEb19AwkqM | Concept intro |
| Build a Hermes Knowledge Base That Self-Improves | https://www.youtube.com/watch?v=D3dQqqDx2V4 | Hermes-focused KB |
| AI Just Unlocked UNLIMITED Knowledge! Hermes & LLMWiki | https://www.youtube.com/watch?v=YUz2CLLmdjA | Hermes + wiki skill hype/overview — critique the claims in class |
| Building an LLM Wiki in Obsidian (Beomsu Koh) | https://www.youtube.com/watch?v=sQSFeqeLKtU | Live Obsidian session |
| I Built Karpathy’s LLM Wiki in Obsidian | https://www.youtube.com/watch?v=bgXEDymiZCc | Obsidian practice narrative |
| Be Smart, *The Real Cost of AI Will Shock You* | https://www.youtube.com/watch?v=YgoiujmwLKI | Prep overview for the ecology input, Session 06 (energy, water, neighbours); handout [data centers energy ecology economy](../../research/data-centers-energy-ecology-economy.md) |
| Jon Stewart — AI monologue (Daily Show) | https://www.youtube.com/watch?v=S18jxWZntUo | Session 01: pick-a-lane / jobs / capitalism→socialism gag — [visions fears regulation](../THEORY/06-danger-and-risk/visions-fears-regulation.md) |
| Jacob Coxon — *Existential Threat of AI from the Inside* (Daily Show) | https://www.youtube.com/watch?v=lnLDjXy2kRA | Session 01: utopia vs incentives / misuse — teacher clip |
| Salim Ismail — *Jon Stewart Is Right About AI And Wrong* | https://www.youtube.com/watch?v=ionrjPXLIYg | Amplifier / regulate outcomes — then counter in [visions fears regulation](../THEORY/06-danger-and-risk/visions-fears-regulation.md) |
| HealthyGamerGG — *How AI is Killing Your Potential* | https://www.youtube.com/watch?v=BzsLbHoNXTs | Optional prep: MIT “brain rust” framing — pair with [ai brains critical thinking](../../research/ai-brains-critical-thinking.md) |
| Huberman Lab Clips — *Mental Health Risks of Using AI* (Dr K) | https://www.youtube.com/watch?v=sqYLH72eCg0 | Optional; sycophancy / psychosis risk — content warning |
| Ezra Klein Show — *Is There an A.I. Bubble? A Debate.* | https://www.youtube.com/watch?v=9GLdGc9OX-A | Session 01 bubble / CapEx debate |
| Richard Campbell — *After the AI Hype* (2026) | https://www.youtube.com/watch?v=uWnUnMphmPM | Skeptical build-out keynote |
| YouTube — *MCP vs API Explained* | https://www.youtube.com/watch?v=kn6dxL53NkM | Session 05 / [what is mcp](../PRACTICE/06-mcp-and-tools/what-is-mcp.md) |
| YouTube — *Stop Prompting Claude. Use Karpathy's Method Instead.* | https://www.youtube.com/watch?v=7zZy1QTvokM | STE / aircraft-manual prompting beat |

## Cognition / critical thinking (AI and brains)

Appended 2026-11-11 from a teacher vault scan. Research note: [ai brains critical thinking](../../research/ai-brains-critical-thinking.md). Full curated link list: [links from clippings](primary-sources.md).

| Source | URL | One-line note |
|---|---|---|
| Kosmyna et al., *Your Brain on ChatGPT* (arXiv:2506.08872, 2025) | https://arxiv.org/abs/2506.08872 | MIT Media Lab EEG essay study; preprint; order-of-use matters |
| MIT Media Lab publication page | https://www.media.mit.edu/publications/your-brain-on-chatgpt/ | Author abstract; peer-review caveat |
| Lee et al., CHI 2025 (Microsoft + CMU) | https://dl.acm.org/doi/full/10.1145/3706598.3713778 | AI confidence ↔ less critical thinking (self-report survey) |
| Lacuna — *AI and Critical Thinking: The Research* (2026-10-08) | https://learnwithlacuna.com/articles/ai-critical-thinking-research | Careful secondary read of Lee / Kosmyna / Fan / Gerlich |
| Abrams / APA Monitor (2026-07) — *How AI is reshaping human skills and thinking* | https://www.apa.org/monitor/2026/07-08/ai-job-skills-thinking | Structured vs passive use; skill decay examples |
| Haber — *Emerging realities of AI and mental health* | https://pmc.ncbi.nlm.nih.gov/articles/PMC13576966/ | Therapy bots, sycophancy, delusional spirals |

## MCP

| Source | URL |
|---|---|
| Model Context Protocol intro | https://modelcontextprotocol.io/docs/getting-started/intro |
| Architecture | https://modelcontextprotocol.io/specification/2026-07-28/architecture |
| Course note | [what is mcp](../PRACTICE/06-mcp-and-tools/what-is-mcp.md) |

## Nextcloud / Collectives / Context Agent (comparison track)

| Source | URL |
|---|---|
| Collectives | https://github.com/nextcloud/collectives |
| Collectives markdown files | https://docs.nextcloud.com/server/stable/user_manual/en/collectives/markdown_files.html |
| Context Agent + MCP endpoint | https://docs.nextcloud.com/server/stable/admin_manual/ai/app_context_agent.html |
| Context Agent repo | https://github.com/nextcloud/context_agent |
| Research note | [llmwiki obsidian vs nextcloud collectives](../../research/software&DataManagement/llmwiki-obsidian-vs-nextcloud-collectives.md) |

## Peer courses (timeline inspiration)

| Course | URL |
|---|---|
| HKUST AMCC6500 Critical AI and Artistic Creation | https://amc.hkust.edu.hk/upload/2026-27%20Fall%20Course%20Info/AMCC6500I-Course_Outline.pdf |
| Birkbeck Critical and Creative AI | https://www.bbk.ac.uk/courses/modules/sc04/SC04023S7 |
| HM Munich — Our Br00d (agentic AI in artistic research) | https://mediapool.hm.edu/media/dachmarke/dm_lokal/hm_international/sprachen/coursesinenglish_1/courses_in_english_ss_26/muc_dai_5/CiE_Kursbeschreibung_Our_Br00d_Technical_Development_of_Agentic_AI_in_Artistic_Research_Geaendert.pdf |
| SFPC Handmade Datasets | https://sfpc.study/sessions/summer-26/handmade-datasets |
| NYU IMA Chatbots for Art’s Sake | https://itp.nyu.edu/ima_course_listings/chatbots-for-arts-sake/ |
| Gray Area Creative Code Intensive | https://grayarea.org/course/creative-code-intensive/ |

Full mapping: [timeline](../SESSIONS/overview/timeline.md)

## Critical readings: primary, free to read (Session 01 deep dives and student inputs)

Appended 2026-10-18 after a URL check. The page loaded and the description matched. That is not independent verification. See [Source types](#source-types). No paywalled-only items. Session tables (archived with the 13-session plan): [10 authorship labour platforms](../THEORY/02-labour-authorship/labour.md#retired-session-10-prompts-readings-and-practical) · [11 local ecology when not](../THEORY/03-ecology-infrastructure/ecology.md#retired-session-11-prompts-readings-and-practical). Current use: Session 01 deep dives and the student inputs ([course rhythm](../SESSIONS/overview/course-rhythm.md)).

## Agent harness

| Source | URL |
|---|---|
| LangChain — *The Anatomy of an Agent Harness* (2026-03-10) | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness |
| Zyte — *Harness Engineering, part 1* | https://www.zyte.com/blog/harness-engineering-part-1-what-is-an-agent-harness-and-why-it-matters/ |
| Course note | [what is harness](../PRACTICE/01-harness-and-agents/what-is-harness.md) |
| Session 02 | [02 agent harness and wiki architecture](../SESSIONS/02-agent-harness-and-wiki-architecture.md) |
| Structure vs model quality (research check, SE + RAG) | [structure vs model quality](../../research/software&DataManagement/structure-vs-model-quality.md) |
| Wadhwa et al. — context ~70% / parametric ~30% *in answers* (not productivity) | https://arxiv.org/abs/2409.08435 |
| Fan et al. — harness design for coding agents (SWE-Bench / Terminal-Bench) | https://arxiv.org/abs/2609.20804 |
| Scaffold effect — harness as hidden variable | https://arxiv.org/abs/2607.22585 |
| Model–harness interactions (ranking reversals) | https://arxiv.org/abs/2610.00917 |
| RepoFusion — repo context vs larger models | https://arxiv.org/abs/2306.10998 |
| Less LLM, more documents (RAG corpus vs model size) | https://arxiv.org/abs/2510.02657 |

| Source | URL | Session · one-line note |
|---|---|---|
| Kate Crawford & Vladan Joler, *Anatomy of an AI System* (2018) | https://anatomyof.ai/ | 8, 9 · Amazon Echo mapped as labour, data and material extraction; essay in 21 parts + diagram |
| Crawford & Joler, *Calculating Empires* (2023) | https://calculatingempires.net/ | 8 · interactive long-timeline of technology and power (browser-heavy site) |
| Luccioni, Jernite & Strubell, *Power Hungry Processing* (ACM FAccT 2024) | https://arxiv.org/abs/2311.16863 | 9 · inference energy of 88 models; general-purpose vs task-specific |
| IEA, *Energy and AI* (2025-04-10, CC BY 4.0) | https://www.iea.org/reports/energy-and-ai | 9 · data-centre electricity projections, supply, emissions |
| U.S. Copyright Office, *Copyright and Artificial Intelligence* (Parts 1–3, 2024–2025) | https://www.copyright.gov/ai/ | 8 · copyrightability of AI outputs (Part 2), training (Part 3 pre-pub); US position |
| OpenAI, *Sycophancy in GPT‑4o* (2025-04-29) | https://openai.com/index/sycophancy-in-gpt-4o/ | 5 · vendor post-mortem of the rolled-back “overly agreeable” update |
| Cory Doctorow, *Tiktok’s enshittification* (2023-01-21) | https://pluralistic.net/2023/01/21/potemkin-ai/ | 8 · platform lifecycle argument behind “platform dependency” |
| Billy Perrigo / TIME, *OpenAI Used Kenyan Workers…* (2023-01-18) | https://time.com/6247678/openai-chatgpt-kenya-workers/ | 8 · outsourced toxic-text labelling via Sama; pay and harm claims — **content warning** (graphic labour). PDF mirror: https://cse.buffalo.edu/mlsoc/assets/files/openai_kenyan_worker.pdf |
| Data Workers’ Inquiry (project site) | https://data-workers.org/ | 8 · worker-led accounts of annotation / moderation; method: https://data-workers.org/about/the-method/ |

## Hermes — local / custom models

| Source | URL |
|---|---|
| Local Models (user guide) | https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Providers — custom & self-hosted endpoints | https://hermes-agent.nousresearch.com/docs/integrations/providers |
| Guide: Run Hermes with Ollama | https://hermes-agent.nousresearch.com/docs/guides/local-ollama-setup |
| FAQ — offline / local models | https://hermes-agent.nousresearch.com/docs/reference/faq |

## Course notes in this repo

| Topic | Note |
|---|---|
| Lint explained | [what is lint](../PRACTICE/02-knowledge-bases/what-is-lint.md) |
| `SCHEMA.md` / `index.md` / `log.md` / folders | [llm wiki standard files](../PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md) |
| Knowledge store options | [knowledge store options](../PRACTICE/02-knowledge-bases/knowledge-store-options.md) |
| Karpathy vs OpenClaw research | [karpathy llm wiki and openclaw](../../research/software&DataManagement/karpathy-llm-wiki-and-openclaw.md) |
| Obsidian vs Joplin | [obsidian vs joplin hermes llmwiki](../../research/software&DataManagement/obsidian-vs-joplin-hermes-llmwiki.md) |
| AI / brains / critical thinking | [ai brains critical thinking](../../research/ai-brains-critical-thinking.md) |
| Vault clippings → student links | [links from clippings](primary-sources.md) |
