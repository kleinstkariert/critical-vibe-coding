---
title: Session 02 — Agent harness and wiki architecture
session: 2
---

# Session 02 — Agent harness → LLM Wiki / Obsidian structure

Parent: [[../timeline]] · Outline: [[../course-outline]]

First **technical** session after the socio-political opener (session 1). Install comes next (session 3); phone/Discord practice in session 4.

## Goals

- Define **harness** in plain language: Agent = Model + Harness
- Map harness parts to what students will actually configure (not vendor mythology)
- Then specialise: **LLM Wiki + Obsidian** as the durable filesystem half of our harness
- Leave with a mental diagram they can redraw for midpoint / final

## Check-in

One sentence from last week’s outdoor/lecture themes. Who already has Obsidian installed?

## Teacher input — Part A: Harness (general)

Course note: [[../what-is-harness]]  
Read (teacher / optional students): [LangChain — *The Anatomy of an Agent Harness*](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) (2026-03-10).

### Core sentence

> The model contains the intelligence; the **harness** is the system that makes that intelligence useful.  
> If you’re not the model, you’re the harness.

### Layers (reuse vocabulary from session 1 lecture)

| Layer | What |
|---|---|
| **Model** | Weights — token in, token out |
| **Thin harness** | Chat UI + history loop (ChatGPT-style) |
| **Thick harness** | Files, tools, skills, MCP, sandboxes, verify loops (Hermes, Cursor Agent, Claude Code…) |

### Derive harness from desired behaviour (*teaching pattern from the article*)

| We want… | Harness provides… |
|---|---|
| Work that survives tomorrow | Filesystem / vault (not only chat scrollback) |
| Agent can act, not only talk | Tools, bash/code, MCP kitchens |
| Safe enough to try | Sandbox, allow-lists, human-only folders |
| Knowledge past the cutoff | Search, MCP, *your* notes |
| Long tasks without melting | Compaction, skills (progressive disclosure), plan files |
| “Did it actually work?” | Lint, tests, eyes-on for fab |

Emphasise: **harness engineering is design** — choosing tools, schemas, and kill-switches is already interface work (session 6 will aestheticise this).

### Why we invest in structure before model shopping

Research check: [[../../research/structure-vs-model-quality]] · short version in [[../what-is-harness#why-structure--harness-often-beats-just-a-better-model]].

Teach carefully:

1. **SE / coding-agent evidence** — same model, different harness → different scores and token costs; rankings can reverse (scaffold / model–harness papers, 2026). Repo context and retrieval often beat “just use a bigger model.”
2. **The ~70/30 rumour** — *nuance:* not a productivity study. Closest published split (~70% from provided context, ~30% from model weights in the answer) is Wadhwa et al. 2024. Useful as “the model leans on what you feed it,” not as a pie chart of student success.
3. **Within limits** — there is still a model floor; structure multiplies capability, it does not create it.

Classroom bet for CVC: spend the semester on **wiki + schema + tools** (structure), not on chasing the newest API name.

### Image / board suggestions

- One slide: `Agent = Model + Harness`  
- Sparse tech-flow (Quadrature style): You → Harness → Model → Tools/Files → World  
- Contrast slide: “Bigger model” vs “Better index / SCHEMA / tools” (two doors)  
- Avoid neon “AI brain” stock; avoid a fake 70/30 productivity pie unless you label it *misheard*

## Teacher input — Part B: LLM Wiki + Obsidian (our harness specialisation)

After the general frame, land in the course default.

### Why a folder wiki is harness, not “just notes”

- Context windows are scarce → durable state on disk  
- Humans + agents share the same files (collaboration surface)  
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

### Obsidian’s job

- Human IDE for the filesystem (graph, mobile, clipper)  
- Sync to phone = harness reaches the street  
- Agent does **not** need Obsidian open to edit files — Obsidian is the viewer/editor for you  

How-to (install still homework / session 3): [[../howto-obsidian-setup-and-sync]]

### Hermes’s job (preview)

- Runtime that runs the loop + skills + tools against `WIKI_PATH` / `OBSIDIAN_VAULT_PATH`  
- Full install next session: [[../howto-hermes-setup]]

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

## Practical (light — no full install required)

- On paper or whiteboard: label Model vs Harness on a product they already use (ChatGPT vs Cursor vs “just a local GGUF in a random UI”)
- Sketch their future vault folders (even empty names)
- Optional: open Obsidian if already installed and create `SCHEMA.md` stub with three lines: may edit / must ask / never touch

## Homework

- Install Obsidian; vault in syncable place (if not done) — [[../howto-obsidian-setup-and-sync]]
- One-page diagram: Model / Harness / Wiki folders (phone photo OK)
- Skim Karpathy gist **or** the LangChain harness article (pick one)
- Next week: model landscape + Hermes install ([[03-models-prompting-install]])

## Materials / References

| What | Link |
|---|---|
| Course — what is a harness | [[../what-is-harness]] |
| Structure vs model quality (research) | [[../../research/structure-vs-model-quality]] |
| LangChain — Anatomy of an agent harness | https://www.langchain.com/blog/the-anatomy-of-an-agent-harness |
| LLM Wiki standard files | [[../llm-wiki-standard-files]] |
| What is lint | [[../what-is-lint]] |
| Karpathy research note | [[../../research/karpathy-llm-wiki-and-openclaw]] |
| Session 1 lecture (model vs product vs agent) | [[../lectures/01-welcome-landscape-lecture]] |
| Presentation style | [[../presentation-style]] |
