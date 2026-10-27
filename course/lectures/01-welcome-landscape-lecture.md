---
title: Session 01 — Classroom lecture draft (welcome + landscape)
date: 2026-10-20
session: 1
status: first-draft
tags:
  - course
  - lecture
  - political-economy
---

# Session 01 — Classroom input lecture (first draft)

Speaker notes for Part B of [[../sessions/01-welcome-and-landscape]]. Outdoor check-in stays in that file.

Style: [[../presentation-style]] (agent skill: `schaufler-presentation-style`) — one strong image per beat, argument in notes, label *claim* vs *verified fact*.

**Research base for this draft**

| Source | Role |
|---|---|
| [[../../research/ai-bubble-productivity-datacenter]] | Bubble / circular finance / productive bubble frame |
| [[../../research/data-centers-energy-ecology-economy]] | Ecology seed only in block 5; full teach in Session 11 |
| Vault clippings (teacher only — not in student kit) | Tooze Ep. 250/260, Acemoglu MIT Sloan, Verdegem, Be Smart transcript… under `KnowledgeBaseObsidian/Clippings/` |
| [[../course-outline]] | Twin tracks, deliverables |

---

## Timing (*technical suggestion*)

~45–55 min + Q&A after each block. Do not race all blocks equally — **#2 (technical), #3 (visions), #4 (bubble)** get the most airtime.

| Block | Min | Priority |
|---|---|---|
| 1 Scope | 4 | medium |
| 2 What LLMs / agents are | 12 | **high** |
| 3 Drivers / visions / fears / regulation | 10–15 | **high** — script [[../visions-fears-regulation]] |
| 4 Bubble / economy | 10–12 | **high** |
| 5 Ecology / labour (seed) | 5 | medium — deep dive Session 11 |
| 6 Regulation | — | folded into #3; law note [[../eu-ai-act-and-datenschutz]] |
| 7 Media-art workflows | 5 | medium |
| 8 Default setup | 5 | practical |

---

## Block 1 — Scope of the class

### Say

This seminar has **two tracks every week**:

1. **Technical** — you leave with a working personal agent setup (default: Hermes + Obsidian / LLM Wiki).
2. **Critical / shared space** — we name fears, hopes, authorship, labour, ecology — without pretending the tech is neutral.

A third thread: the **agent as interface**. The setup (skills, tools, knowledge) is artistic material, not only the pretty output.

Midpoint (session 9): demo the setup + short proposal. Final (session 13): architecture + one use + short reflection — not a polished exhibition by default.

### Image suggestions

| Slide | Image idea | Why / where |
|---|---|---|
| Title | Outdoor check-in photo (your park / campus) or blank title with course name only | Ground the “group therapy” half |
| Twin tracks | Simple two-column diagram (hand-drawn OK): *agent stack* \| *critical questions* | Avoid dashboard clutter — one composition |
| Agent as interface | Quadrature-style **tech flow diagram** energy (see `Fantasie#1@Quadrature_ Diagram.pdf` in Schaufler talks folder) — boxes: You → Agent → Tools / Wiki → World | Matches your existing diagram language |

### Speaker cue

Ask: “Who came mostly for the install, who mostly for the politics?” — both are valid; neither track is optional.

---

## Block 2 — What LLMs and agent systems are (technical)

This is the dense block. Keep vocabulary stable all semester.

### 2a — Three layers (draw this)

| Layer | What it is | Example |
|---|---|---|
| **Model** | A trained network that maps tokens → tokens (weights on disk / in a GPU) | Llama, Qwen, Claude’s underlying model, GPT… |
| **Product / chat** | UI + safety + memory + billing wrapped around a model | ChatGPT website, Claude.ai, Gemini app |
| **Agent** | A loop that can **call tools**, read/write files, follow skills, and keep going until a goal | Hermes, Cursor Agent, Claude Code, OpenClaw-style bots |

One-liner: *Chat answers; an agent acts (with your permission and tools).*

### 2b — How an LLM “knows” anything (without magic)

*verified fact / teaching model (simplified):*

1. **Training** — next-token prediction on huge text (and often code, images…). Parameters store statistical regularities, not a database of facts.
2. **Inference** — your prompt is tokenized; the model samples a continuation. Temperature / sampling change how wild that is.
3. **Context window** — the working memory of *this* call (prompt + retrieved notes + tool results). When it overflows, older stuff drops or must be summarized.
4. **Hallucination** — fluent continuation ≠ truth. Agents make this worse if they write files without verify steps.

What LLMs are **good at**: drafting, translating between formalisms, summarizing, proposing structure, generating boilerplate you will edit.  
What they are **bad at alone**: ground truth, long-horizon accountability, fabrication safety, “knowing” your unstated artistic intent.

### 2c — Tokens, context, cost (intuition, not exam)

- Rough intuition: English ≈ 0.75 words/token; code denser.
- Longer context = more compute per turn = more € and watts.
- **Why agents need files:** a 200-page vault does not fit in every call. Pattern: small schema + index + pull only relevant pages (LLM Wiki habit — Karpathy gist).

### 2d — Tools, skills, MCP, harness (preview — architecture = session 2)

| Piece | Role |
|---|---|
| **Filesystem tools** | Read/write a folder (Obsidian vault). Enough for a wiki. |
| **Skills** | Written procedures the agent should follow (`SCHEMA.md`, lint, ingest…). |
| **MCP** | Protocol so an agent can call *other apps* (browser, calendar, Blender, Fusion…) as tool kitchens — [[../what-is-mcp]], session [[../sessions/06-mcp-and-tools]] |
| **Harness** | Everything that isn’t the model (tools, files, schema, loops) — [[../what-is-harness]], session [[../sessions/02-agent-harness-and-wiki-architecture]] |

Metaphor you already use: **waiter (host) / kitchen (MCP server) / dish (tool result)**.

### 2e — Local vs cloud (one slide)

| | Cloud API | Local weights |
|---|---|---|
| Pros | Strong models, little hardware | Privacy, offline, cost control at scale, political choice |
| Cons | Lock-in, logging, price, jurisdiction | Hardware €, weaker models unless you invest, ops burden |

Deep dive later: [[../../research/local-gpu-hardware-for-llms]] · sessions 3 + 10.

### Image suggestions (block 2)

| Slide | Image idea | Source / note |
|---|---|---|
| Layers | Three stacked boxes or Russian-doll: Model ⊂ Product ⊂ Agent | Simple diagram — you draw |
| Training → inference | Classic “data lake → GPU cluster → chat bubble” but **use a real photo of a data hall or GPU rack**, not a stock “AI brain” | Search: hyperscale data center aisle (with credit); or IEA / news photos |
| Context window | Overflowing desk / sticky notes falling off — or a literal scrolling terminal with a cut-off prompt | Humour OK |
| Agent loop | Flowchart: Think → Act (tool) → Observe → Think… | Keep black/white |
| MCP | Waiter / kitchen sketch | From [[../what-is-mcp]] |

### Q&A prompts

- “Where in this stack is *authorship* located if the agent writes half the patch?”
- “Has anyone already used an agent that edits files, not only chat?”

---

## Block 3 — Drivers, visions, fears, regulation (10–15 min)

**Primary talk script:** [[../visions-fears-regulation]] — use that handout’s four beats; do not improvise a second structure.

### Spine (mirror the handout)

1. **Drivers** — growth treadmill after PC/internet/mobile; data + compute ready; monetise the archive; race incentives (Coxon). Technical scaling in parallel.  
2. **Two industry stories** — abundance / UBI–UHI rhetoric (Musk, Altman — *is* a real discourse, not delivered policy) **and** x-risk / misuse (same scene). Stewart: pick a lane; capitalism→“socialism” gag.  
3. **Amplifier vs power** — Ismail’s amplifier is useful; social science: not neutral, amplifies hierarchy, who owns the knob (Zajko / Crawford).  
4. **Regulation** — uses, data, liability yes; global off-switch no; credibility marketing. Point to [[../eu-ai-act-and-datenschutz]] — do not teach the Act here.

Teacher clips (vault): Coxon Daily Show; Stewart monologue; Ismail response — paths in the handout.

### Image suggestions

| Slide | Image idea |
|---|---|
| Growth treadmill | Three icons: PC → phone → GPU rack (no stock “brain”) |
| Double message | Split slide: “Star Trek” / “% extinction” — typographic only |
| Amplifier | Fire / gain knob — then “who owns it?” |
| Regulation | One sentence: “Uses & data — not maths” |

---

## Block 4 — Economic background / potential AI bubble

**Primary research note for this block:** [[../../research/ai-bubble-productivity-datacenter]]

### Core thesis (teach this sentence)

> Speculative finance, circular investment, and **real** infrastructure can coexist. “Bubble” does not automatically mean “useless technology.”

Three boxes:

1. **Financial bubble** — investors overpay / lose money  
2. **Productive investment boom** — overbuild still leaves usable infra later (Perez / DeLong / Takshashila)  
3. **Technological dead end** — infra itself ages into scrap  

Unresolved question: *Will independent end-user demand and productivity justify the build-out once circular loops are stripped out?*

### Circularity (*verified fact* — BIS Bulletin 137, 1 Oct 2026)

Quote the three bullets (numbers on a slide, source in footnote):

- 28.7% of AI firms’ investment deal value (2021–25) targeted other AI firms  
- 55.2% of incoming AI-firm investment came from other AI firms  
- Of AI-to-AI deals, 16.1% by count / 46.4% by value also had supplier–customer links  

**Interpretation (from research note):** the diagram proves **interdependence**, not that all demand is fake. Vendor financing and strategic supply locks are old industrial patterns.

Tooze (Chartbook + Ones and Tooze Ep. 250 clipping): strengthens the **skeptical political-economy** reading — concentrated capex, codependent hyperscalers, systemic risk — not a techno-optimist rebuttal.

### Productivity counterweight

Acemoglu (MIT Sloan clipping *A new look at the economics of AI*): macro GDP effect of gen-AI over ~10 years may be **nontrivial but modest** (~1% GDP order of magnitude in his framing), vs bank/consultancy headlines of 7%+.

Use as: *serious economists disagree on magnitude and timing* — not as “AI does nothing.”

### US vs Chinese / open weights (one slide)

| Ecosystem | Pattern to name |
|---|---|
| US hyperscalers | Capex race, closed APIs, CUDA stack, private credit into data centres (Van Nieuwerburgh financing talk — see research note) |
| Chinese open-ish weights | Fast release cycles, exportable weights, different domestic regulation story |
| EU / academic | Hosting jurisdiction, access rules (Austrian academic AI: say clearly if students **cannot** use it) |

### Image suggestions (block 4)

| Slide | Image idea | Note |
|---|---|---|
| Opening | Bloomberg-style **circular investment diagram** (Nvidia ↔ OpenAI ↔ Microsoft ↔ cloud) | Redraw simplified; cite genre, not leak proprietary art |
| Three boxes | Hand diagram: Financial / Productive / Dead end | Blackboard energy |
| BIS numbers | Typographic slide — three big % | No decoration |
| Tooze | Still from *Boom Bubble Burst* talk or Chartbook header | Clip: vault `Clippings/Adam Tooze…` |
| Capex | Photo of data-centre construction / transformers / substation | Ecology bridge to block 5 |
| Productive bubble | Historical: railway map or dark fibre cartoon (Perez installation phase) | Avoid steampunk kitsch |

### Q&A

- “If investors lose money but the GPUs remain, who actually benefited?”
- “Where does *your* ChatGPT subscription sit in that circular diagram?”

---

## Block 5 — Ecological and social implications

**Deep handout (Session 10, not this lecture):** [[../../research/data-centers-energy-ecology-economy]] · CapEx twin: [[../../research/ai-bubble-productivity-datacenter]]

### Ecology

- Training vs **inference**: students’ daily use is mostly inference; still scales with tokens and video/image models (Luccioni et al.; IEA *Energy and AI* — session 11).
- One slide seed: data centres are **local** (grid, water, neighbours) even when national electricity shares look “small”; US holds ~45% of global DC electricity (IEA 2024). Optional later: Be Smart *The Real Cost of AI Will Shock You*.
- Water, land, grid connections, who lives next to the campus — name the question; do not teach scopes 1–3 here.
- Space data centres: mention only as hype contrast — bubble research note §11–13 (UMD skeptical / TUM-ESPI optimistic); not the centre of this lecture.

### Labour / jobs

- Separate **macro claims** (IMF/McKinsey headlines) from **observed** shifts in creative freelance rates, student anxiety, studio expectations.
- Ghost work: annotation, moderation, eval farms (session 10 deep dive).
- Acemoglu: inequality and welfare can move differently from GDP.

### Image suggestions

| Slide | Image idea |
|---|---|
| Energy | Cooling towers / river intake for a known data campus (with location caption) |
| Labour | Historical labour image from your Mass of Money set (Koehler *Der Streik* or Pellizza *Der vierte Stand*) **reframed**: “who trains / who clicks / who owns the model” |
| Student anxiety | No stock “sad freelancer” — empty slide with question only |

---

## Block 6 — Regulation discourse

**Folded into Block 3.** Full beat: [[../visions-fears-regulation]] § Beat 4. Law orientation: [[../eu-ai-act-and-datenschutz]]. Tooze Ep. 260 (AI regulation) optional teacher prep only.

---

## Block 7 — What this might mean for media-art workflows

### Teacher view (editable)

| Pressure | Artistic stake |
|---|---|
| Speed | More iterations; less sitting with a bad idea |
| Taste flattening | Same Midjourney look; same “helpful” prose voice |
| Authorship | Who signed the work if the agent wrote the patch? |
| New interfaces | Agent + wiki + MCP as the piece (session 5) |
| Refusal | Knowing when **not** to use AI is a skill (Session 11) |

Link outdoor themes back: fears/hopes from Part A.

### Image suggestions

| Slide | Image idea |
|---|---|
| Flattening | Grid of near-identical AI images (compose yourself once) |
| Interface as work | Installation photo from your practice (CREDO / Fantasie / Mass of Money LED) — **own work preferred** |
| Refusal | Red “kill switch” sticky on a laptop |

---

## Block 8 — Suggested default setup

### Stack

1. **Obsidian** vault in a syncable folder (phone sync required) — [[../howto-obsidian-setup-and-sync]]  
2. **Hermes Agent** pointed at that vault — [[../howto-hermes-setup]] (Win / Mac / Linux)  
3. **Harness + LLM Wiki** habits — next class [[../sessions/02-agent-harness-and-wiki-architecture]] · [[../what-is-harness]] · [[../llm-wiki-standard-files]]  
4. Models: whatever they already pay for / can access; local hardware optional later — [[../../research/local-gpu-hardware-for-llms]]

Student-facing materials live in a **small share pack**, not the whole vault — [[../student-share-structure]].

### Image suggestions

| Slide | Image idea |
|---|---|
| | Three icons only: Obsidian / Hermes / phone — paths underneath |
| Homework | Checklist slide |

### Homework (repeat aloud)

- Install Obsidian; vault in syncable place  
- Note existing LLM access  
- Optional: Karpathy gist or beginner video — [[../references]]

---

## Slide order checklist (build deck from this)

1. Title  
2. Twin tracks  
3. Layers: model / product / agent  
4. Training vs inference + hallucination  
5. Context + why files  
6. Tools / skills / MCP preview  
7. Local vs cloud  
8. Why now — CLAIM slide  
9. Bubble thesis — three boxes  
10. BIS circularity numbers  
11. Acemoglu modest productivity  
12. US / CN / open weights  
13. Ecology photo  
14. Labour question  
15. Regulation as marketing  
16. Media-art stakes  
17. Default stack + homework  

---

## Teacher prep still open

- [ ] Pull 8–12 image files into `course/lectures/assets/01/` (credits in a `CREDITS.md`)  
- [ ] Re-clip Tooze *Boom Bubble Burst* if needed (`L4--A3hhOws`)  
- [ ] Update Austrian academic AI access sentence before class — after [[../academic-ai-austria]] / AI:AT contacts  
- [ ] Decide which outdoor themes to quote back in block 7  
