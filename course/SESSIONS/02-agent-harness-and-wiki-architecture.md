---
title: Session 02. Agent harness, wiki architecture, model landscape, Hermes install
session: 2
updated: 2026-11-10
status: current
canonical: true
---

# Session 02. Agent harness, LLM Wiki structure, model landscape, install Hermes

*reference implementation.* The lecturer will install Hermes with the class. That install is a *demonstration*. It is *not required for assessment*. The assessed object is the student-designed system in [minimum path](../PROJECT-WORK/01_minimum-path.md). Claude Code, Cursor, OpenCode, a local script, or another agent are valid systems. The flattening input presentation is required. Other tools are compared in the [tool comparison](../../research/software&DataManagement/vibe-coding-tools-and-agent-environments.md).

Parent: [timeline](overview/timeline.md) · Outline: [course outline](overview/course-outline.md) · Rhythm: [course rhythm](overview/course-rhythm.md)

First **practice** session after Session 01. A student group opens with the **flattening** input; harness, wiki structure, model landscape and the Hermes install are the teacher's. Prompting and chat versus reasoning: Session 03. Phone, Discord and MCP: Session 05.

**Slot:** 10:00 to 12:00.

## Goals

- Define **harness** in plain language: Agent = Model + Harness
- Map harness parts to what students will actually configure (not vendor mythology)
- Then specialise: **LLM Wiki + knowledge store** as the durable filesystem half of our harness
- Short **model landscape**: what students can use, and what it costs (moved here from the old Session 03)
- **Install Hermes**, point it at the vault, and run it on one free-to-use hosted endpoint ([default setup](../PRACTICE/01-harness-and-agents/default-setup.md) §4)
- Leave with a mental diagram they can redraw for the midpoint and the final

## Clock

| Clock | Block |
|---|---|
| **10:00 to 10:20** | Check-in (listen only) |
| **10:20 to 10:35** | Student input: **flattening** ([course rhythm](overview/course-rhythm.md)) |
| **10:35 to 10:55** | Teacher: harness (general), then LLM Wiki / store structure |
| **10:55 to 11:05** | Break |
| **11:05 to 11:15** | Teacher: model landscape and the free-to-use endpoint |
| **11:15 to 12:00** | Install Hermes, connect that endpoint, vault smoke test |

If the install runs long, the diagram practice moves to homework.

## Check-in

Listen only: [course rhythm](overview/course-rhythm.md#1-check-in-every-session).

## Student input (theory / humanities): Flattening

Group (about 15 min). Thesis to test: **AI kills the underground and it kills diversity.**

Flattening is not only taste or style moving toward the popular voice. A statistical model reproduces what is shown most online, so it generates an average of the most displayed content, not of reality. That average becomes a norm, skewed toward the most visible: male, English-speaking, young, commercial. Include **AI and patriarchy** and **feminism and AI**.

Deep dive and sources: [flattening and the norm](../THEORY/04-bias-flattening/flattening-and-the-norm.md). Not "what is a harness".

## Teacher input, Part A: Harness (general), *practice*

Course note: [what is harness](../PRACTICE/01-harness-and-agents/what-is-harness.md)
Read (teacher, optional students): [LangChain, *The Anatomy of an Agent Harness*](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) (2026-03-10).

### Core sentence

> The model contains the intelligence; the **harness** is the system that makes that intelligence useful.
> If you're not the model, you're the harness.

### Layers (reuse vocabulary from the Session 01 lecture)

| Layer | What |
|---|---|
| **Model** | Weights: token in, token out |
| **Thin harness** | Chat UI + history loop (ChatGPT-style) |
| **Thick harness** | Files, tools, skills, MCP, sandboxes, verify loops (Hermes, Cursor Agent, Claude Code...) |

### Derive harness from desired behaviour (*teaching pattern from the article*)

| We want... | Harness provides... |
|---|---|
| Work that survives tomorrow | Filesystem / vault (not only chat scrollback) |
| Agent can act, not only talk | Tools, bash/code, MCP kitchens |
| Safe enough to try | Sandbox, allow-lists, human-only folders |
| Knowledge past the cutoff | Search, MCP, *your* notes |
| Long tasks without melting | Compaction, skills (progressive disclosure), plan files |
| "Did it actually work?" | Lint, tests, eyes-on for fab |

Emphasise: **harness engineering is design**. Choosing tools, schemas and kill switches is already interface work (Session 06 treats it as material and canvas).

### Why we invest in structure before model shopping

Research check: [structure vs model quality](../../research/software&DataManagement/structure-vs-model-quality.md) · short version in [what is harness](../PRACTICE/01-harness-and-agents/what-is-harness.md#why-structure--harness-often-beats-just-a-better-model).

Teach carefully:

1. **SE / coding-agent evidence:** same model, different harness, different scores and token costs; rankings can reverse (scaffold / model-harness papers, 2026). Repo context and retrieval often beat "just use a bigger model".
2. **The ~70/30 rumour:** *nuance:* not a productivity study. The closest published split (~70% from provided context, ~30% from model weights in the answer) is Wadhwa et al. 2024. Useful as "the model leans on what you feed it", not as a pie chart of student success.
3. **Within limits:** there is still a model floor; structure multiplies capability, it does not create it.

Classroom bet for CVC: spend the semester on **wiki + schema + tools** (structure), not on chasing the newest API name.

### Image / board suggestions

- One slide: `Agent = Model + Harness`
- Sparse tech-flow (Quadrature style): You → Harness → Model → Tools/Files → World
- Contrast slide: "Bigger model" versus "Better index / SCHEMA / tools" (two doors)
- Avoid neon "AI brain" stock; avoid a fake 70/30 productivity pie unless you label it *misheard*

## Teacher input, Part B: LLM Wiki + Obsidian (our harness specialisation)

After the general frame, land in the course default.

*reference implementation.* "Course default" here means the Hermes example for this class. It is not the assessed system. See [minimum path](../PROJECT-WORK/01_minimum-path.md).

### Why a folder wiki is harness, not "just notes"

- Context windows are scarce → durable state on disk
- Humans and agents share the same files (collaboration surface)
- Schema / index / log = memory files the harness injects or the agent learns to read first

### Structure to teach (walk the tree)

Point at [llm wiki standard files](../PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md) and draw:

```text
vault/  (or wiki/)
  SCHEMA.md     ← standing orders / limits (harness memory)
  index.md      ← map of the territory
  log.md        ← what happened
  raw/          ← immutable sources
  entities/ concepts/ comparisons/ queries/
```

Habits: ingest → query → **lint** ([what is lint](../PRACTICE/02-knowledge-bases/what-is-lint.md)). A structured wiki does not make the notes true: [llm wiki standard files](../PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md#what-structure-improves).
Karpathy pattern: [karpathy llm wiki and openclaw](../../research/software&DataManagement/karpathy-llm-wiki-and-openclaw.md) · gist in [references](../REFERENCES/bibliography.md).

### Obsidian's job

- Human IDE for the filesystem (graph, mobile, clipper)
- Sync to phone = harness reaches the street (Session 05)
- The agent does **not** need Obsidian open to edit files; Obsidian is the viewer and editor for you

How-to: [howto obsidian setup and sync](../PRACTICE/02-knowledge-bases/howto-obsidian-setup-and-sync.md)

### Diagram to leave with

```text
[You]
   ↓ prompts / veto
[Harness: Hermes + SCHEMA + tools/MCP]
   ↓ context engineering
[Model]
   ↓ tool calls
[Filesystem: Obsidian / LLM Wiki]  ←→  [optional MCP apps]
```

Students redraw this in their own words for homework.

## Teacher input, Part C: Model landscape (short), *practice*

Ten minutes, honest access notes:

- **Proprietary cloud** (OpenAI, Anthropic, Google): strongest models, paid, your data leaves. Choose by strengths: [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md).
- **Open weights** (Llama, Qwen, DeepSeek, Mistral, Nemotron): weights published; can run locally if small enough, or through a hosted provider. Closed versus open as power: student input in Session 03.
- **Local**: preview only. Hardware paths and memory math: Session [03](03-practical-install.md).
- **European hosting**: usually no agent API key; HPC / AI Factory is not a daily Hermes backend. **Austrian academic AI**: students have the web chat, not an agent endpoint for student projects. Administrators can create API clients. The course author states that this is restricted to certified employees and that students cannot create or use these clients: [API access in academic AI](../PRACTICE/03-models-and-providers/academic-ai-austria.md#api-access-in-academic-ai). Say explicitly what students can and cannot use.
- Cloud or local, where the notes go: the flowchart in [default setup](../PRACTICE/01-harness-and-agents/default-setup.md) §3. Privacy and AI Act pointer: [eu ai act and datenschutz](../THEORY/05-privacy-regulation/eu-ai-act-and-datenschutz.md).

### The free-to-use endpoint for today

*technical suggestion* (page consulted 10 Nov 2026): **NVIDIA Nemotron 3 Ultra through OpenRouter's free tier**, model ID `nvidia/nemotron-3-ultra-550b-a55b:free`.

- Openly distributed materials under OpenMDW-1.1 (weights, and NVIDIA's claim of data and recipes). The endpoint is free to use: $0 per token. Tool calling and up to 1 million tokens of context (Hermes needs at least 64,000 and tool calling).
- Limits: 20 requests per minute and 50 per day on a free account. Enough for a smoke test and light daily use, not for long agent runs. Prompts may be logged. Too large for most student machines. Do not send private notes through it until you have checked the data policy. The route is a hosted cloud service: [default setup](../PRACTICE/01-harness-and-agents/default-setup.md) §4.
- Fallback: the free plan of Nous Portal (`hermes setup --portal`, free-to-use hosted models only), or students' own subscriptions or keys.

## Practical: install Hermes (≥45 min)

1. Install Hermes on student machines: [howto hermes setup](../PRACTICE/01-harness-and-agents/howto-hermes-setup.md) (Windows, macOS, Linux).
2. Create a free OpenRouter account and key. Put it in `~/.hermes/.env` as `OPENROUTER_API_KEY`, never in the vault.
3. `hermes model` → OpenRouter → `nvidia/nemotron-3-ultra-550b-a55b:free` (or the student's own access).
4. Point Hermes at the Obsidian vault path (`WIKI_PATH` / `OBSIDIAN_VAULT_PATH`).
5. Smoke test: the agent creates one note, then lists the vault. Check the note in Obsidian.
6. Optional: create a `SCHEMA.md` stub with three lines: may edit / must ask / never touch.

If the install fails, label Model versus Harness on a product the student already uses (ChatGPT versus Cursor versus a local GGUF in a random UI) and sketch the future vault folders on paper. Finish the install as homework.

## Homework

- Finish the Hermes install and smoke test if class time ran out: [howto hermes setup](../PRACTICE/01-harness-and-agents/howto-hermes-setup.md)
- One-page diagram: Model / Harness / Wiki folders (phone photo OK)
- Skim the Karpathy gist **or** the LangChain harness article (pick one)
- Next week: hardware paths, locally runnable models, prompting, chat versus reasoning ([03 practical install](03-practical-install.md))

## Materials / References

| What | Link |
|---|---|
| Course: what is a harness | [what is harness](../PRACTICE/01-harness-and-agents/what-is-harness.md) |
| Structure versus model quality (research) | [structure vs model quality](../../research/software&DataManagement/structure-vs-model-quality.md) |
| LangChain: Anatomy of an agent harness | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness |
| LLM Wiki standard files | [llm wiki standard files](../PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md) |
| What is lint | [what is lint](../PRACTICE/02-knowledge-bases/what-is-lint.md) |
| Karpathy research note | [karpathy llm wiki and openclaw](../../research/software&DataManagement/karpathy-llm-wiki-and-openclaw.md) |
| Hermes install | [howto hermes setup](../PRACTICE/01-harness-and-agents/howto-hermes-setup.md) · https://hermes-agent.nousresearch.com/docs/getting-started/installation |
| Hermes efficient coding (harness tips) | [howto hermes efficient coding](../PRACTICE/01-harness-and-agents/howto-hermes-efficient-coding.md) · [agents md template](../PRACTICE/01-harness-and-agents/agents-md-template.md) |
| Hermes vs coding agents (comparison) | [hermes vs coding agents](../PRACTICE/01-harness-and-agents/hermes-vs-coding-agents.md) |
| OpenCode setup and Hermes pairing | [howto opencode setup](../PRACTICE/01-harness-and-agents/howto-opencode-setup.md) · [howto hermes opencode pairing](../PRACTICE/01-harness-and-agents/howto-hermes-opencode-pairing.md) |
| Session 02 Obsidian slides | [02 agent harness and hermes](lectures/02-agent-harness-slideshow/02-agent-harness-and-hermes.md) |
| Architecture overview | [Local LLM Coding with Hermes](../PRACTICE/08-verification-and-provenance/local-llm-coding-with-hermes.md) |
| Hermes install (Desktop + CLI) | [howto hermes setup](../PRACTICE/01-harness-and-agents/howto-hermes-setup.md) |
| Hermes providers | https://hermes-agent.nousresearch.com/docs/integrations/providers |
| Free-to-use endpoint (OpenRouter) | https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free |
| Model choice, academic access | [Prompting Guide for Critical Vibe Coding](../PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md) · [academic ai austria](../PRACTICE/03-models-and-providers/academic-ai-austria.md) |
| Flattening deep dive (student input) | [flattening and the norm](../THEORY/04-bias-flattening/flattening-and-the-norm.md) |
| Session 01 lecture (model versus product versus agent) | [01 welcome landscape lecture](lectures/01-welcome-landscape-lecture.md) |
| Presentation style | [presentation style](lectures/presentation-style.md) |
