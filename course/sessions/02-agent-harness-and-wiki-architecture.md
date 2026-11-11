---
title: Session 02. Agent harness, wiki architecture, model landscape, Hermes install
session: 2
updated: 2026-11-10
---

# Session 02. Agent harness, LLM Wiki structure, model landscape, install Hermes

Parent: [[../timeline]] · Outline: [[../course-outline]] · Rhythm: [[../course-rhythm]]

First **practice** session after Session 01. A student group opens with the **flattening** input; harness, wiki structure, model landscape and the Hermes install are the teacher's. Prompting and chat versus reasoning: Session 03. Phone, Discord and MCP: Session 05.

**Slot:** 10:00 to 12:00.

## Goals

- Define **harness** in plain language: Agent = Model + Harness
- Map harness parts to what students will actually configure (not vendor mythology)
- Then specialise: **LLM Wiki + knowledge store** as the durable filesystem half of our harness
- Short **model landscape**: what students can use, and what it costs (moved here from the old Session 03)
- **Install Hermes**, point it at the vault, and run it on one free, open model
- Leave with a mental diagram they can redraw for the midpoint and the final

## Clock

| Clock | Block |
|---|---|
| **10:00 to 10:20** | Check-in (listen only) |
| **10:20 to 10:35** | Student input: **flattening** ([[../course-rhythm]]) |
| **10:35 to 10:55** | Teacher: harness (general), then LLM Wiki / store structure |
| **10:55 to 11:05** | Break |
| **11:05 to 11:15** | Teacher: model landscape and the free model |
| **11:15 to 12:00** | Install Hermes, connect the free model, vault smoke test |

If the install runs long, the diagram practice moves to homework.

## Check-in

Listen only: [[../course-rhythm#1-check-in-every-session]].

## Student input (theory / humanities): Flattening

Group (about 15 min). Thesis to test: **AI kills the underground and it kills diversity.**

Flattening is not only taste or style moving toward the popular voice. A statistical model reproduces what is shown most online, so it generates an average of the most displayed content, not of reality. That average becomes a norm, skewed toward the most visible: male, English-speaking, young, commercial. Include **AI and patriarchy** and **feminism and AI**.

Deep dive and sources: [[../lectures/01-welcome-landscape-deep-dives/flattening-and-the-norm]]. Not "what is a harness".

## Teacher input, Part A: Harness (general), *practice*

Course note: [[../what-is-harness]]
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

Research check: [[../../research/structure-vs-model-quality]] · short version in [[../what-is-harness#why-structure--harness-often-beats-just-a-better-model]].

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

### Why a folder wiki is harness, not "just notes"

- Context windows are scarce → durable state on disk
- Humans and agents share the same files (collaboration surface)
- Schema / index / log = memory files the harness injects or the agent learns to read first

### Structure to teach (walk the tree)

Point at [[../llm-wiki-standard-files]] and draw:

```text
vault/  (or wiki/)
  SCHEMA.md     ← standing orders / limits (harness memory)
  index.md      ← map of the territory
  log.md        ← what happened
  raw/          ← immutable sources
  entities/ concepts/ comparisons/ queries/
```

Habits: ingest → query → **lint** ([[../what-is-lint]]).
Karpathy pattern: [[../../research/karpathy-llm-wiki-and-openclaw]] · gist in [[../references]].

### Obsidian's job

- Human IDE for the filesystem (graph, mobile, clipper)
- Sync to phone = harness reaches the street (Session 05)
- The agent does **not** need Obsidian open to edit files; Obsidian is the viewer and editor for you

How-to: [[../howto-obsidian-setup-and-sync]]

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

From the old Session 03 ([[archive-13-session-plan/03-models-prompting-install]]). Ten minutes, honest access notes:

- **Proprietary cloud** (OpenAI, Anthropic, Google): strongest models, paid, your data leaves. Choose by strengths: [[../prompting-and-model-choice]].
- **Open weights** (Llama, Qwen, DeepSeek, Mistral, Nemotron): weights published; can run locally if small enough, or through a hosted provider. Closed versus open as power: student input in Session 03.
- **Local**: preview only. Hardware paths and memory math: Session [[03-hardware-open-models-prompting|03]].
- **European hosting** and **Austrian academic AI**: usually no agent API key; HPC / AI Factory is not a daily Hermes backend: [[../academic-ai-austria]]. Say explicitly what students can and cannot use.
- Cloud or local, where the notes go: the flowchart in [[../lectures/01-welcome-landscape-deep-dives/default-setup]] §3. Privacy and AI Act pointer: [[../eu-ai-act-and-datenschutz]].

### The free model for today

*technical suggestion* (checked 10 Nov 2026): **NVIDIA Nemotron 3 Ultra through OpenRouter's free tier**, model ID `nvidia/nemotron-3-ultra-550b-a55b:free`.

- Open: weights under the permissive OpenMDW 1.1 licence. $0 per token. Tool calling and up to 1 million tokens of context (Hermes needs at least 64,000 and tool calling).
- Limits: 20 requests per minute and 50 per day on a free account. Enough for a smoke test and light daily use, not for long agent runs.
- Privacy: it is open, but in this setup it runs in the cloud. Free providers may log prompts. No private notes through it until the data policy is checked.
- Fallback: the free plan of Nous Portal (`hermes setup --portal`, free models only), or students' own subscriptions or keys.
- Details and sources: [[../lectures/01-welcome-landscape-deep-dives/default-setup]] §4.

## Practical: install Hermes (≥45 min)

1. Install Hermes on student machines: [[../howto-hermes-setup]] (Windows, macOS, Linux).
2. Create a free OpenRouter account and key. Put it in `~/.hermes/.env` as `OPENROUTER_API_KEY`, never in the vault.
3. `hermes model` → OpenRouter → `nvidia/nemotron-3-ultra-550b-a55b:free` (or the student's own access).
4. Point Hermes at the Obsidian vault path (`WIKI_PATH` / `OBSIDIAN_VAULT_PATH`).
5. Smoke test: the agent creates one note, then lists the vault. Check the note in Obsidian.
6. Optional: create a `SCHEMA.md` stub with three lines: may edit / must ask / never touch.

If the install fails, label Model versus Harness on a product the student already uses (ChatGPT versus Cursor versus a local GGUF in a random UI) and sketch the future vault folders on paper. Finish the install as homework.

## Homework

- Finish the Hermes install and smoke test if class time ran out: [[../howto-hermes-setup]]
- One-page diagram: Model / Harness / Wiki folders (phone photo OK)
- Skim the Karpathy gist **or** the LangChain harness article (pick one)
- Next week: hardware paths, open models, prompting, chat versus reasoning ([[03-hardware-open-models-prompting]])

## Materials / References

| What | Link |
|---|---|
| Course: what is a harness | [[../what-is-harness]] |
| Structure versus model quality (research) | [[../../research/structure-vs-model-quality]] |
| LangChain: Anatomy of an agent harness | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness |
| LLM Wiki standard files | [[../llm-wiki-standard-files]] |
| What is lint | [[../what-is-lint]] |
| Karpathy research note | [[../../research/karpathy-llm-wiki-and-openclaw]] |
| Hermes install | [[../howto-hermes-setup]] · https://hermes-agent.nousresearch.com/docs/getting-started/installation |
| Hermes providers | https://hermes-agent.nousresearch.com/docs/integrations/providers |
| Free model (OpenRouter) | https://openrouter.ai/nvidia/nemotron-3-ultra-550b-a55b:free |
| Model choice, academic access | [[../prompting-and-model-choice]] · [[../academic-ai-austria]] |
| Flattening deep dive (student input) | [[../lectures/01-welcome-landscape-deep-dives/flattening-and-the-norm]] |
| Session 01 lecture (model versus product versus agent) | [[../lectures/01-welcome-landscape-lecture]] |
| Presentation style | [[../presentation-style]] |
