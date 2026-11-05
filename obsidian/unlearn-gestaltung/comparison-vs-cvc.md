---
title: un/learn Gestaltung vs Critical Vibe Coding
date: 2026-11-04
tags:
  - research
  - kitegg
  - course
  - comparison
---

# Comparison — un/learn / KITeGG vs Critical Vibe Coding

**CVC anchors:** `course/lectures/01-welcome-landscape-lecture.md`, `course/sessions/01-welcome-and-landscape.md`, `course/course-outline.md`, `course/howto-local-llm-hardware.md`  
**KITeGG anchors:** three *un/learn ai* PDFs + https://unlearn.gestaltung.ai/ + articles `xeci6a49`, `2gtmc7uq` (this folder)

## Shared ground (not “different”)

- Critical stance toward vendor AI myths; ecology and labour appear on both agendas.
- Preference for **competence / appropriation** over pure cloud consumption (KITeGG bare-metal doctrine; CVC local/open options + political choice slide).
- “When not to use AI” as an explicit question (Vol. 3 Editor’s Note; CVC Session 11).
- Design/art students as primary public; hybrid DE/EN materials OK.

---

## Differences from our course

Striking contrasts only — bullets for lecture/prep use.

### Scale & institutional form
- **KITeGG:** ~4-year BMBF Verbund, **five Gestaltung schools**, shared MA pathway emerging, Summer/Winter schools, print trilogy.
- **CVC:** one Interface Cultures seminar (~13× 120 min), **personal** midpoint/final setup as deliverable — not a multi-campus research programme.

### Default technical object
- **KITeGG:** shared **Kubernetes GPU cluster** (5×8 A100 class) + **site AI/robotics labs** + Jupyter/LLP services; students often meet AI through **lab + course service**, not a personal agent.
- **CVC:** default stack **Hermes agent + Obsidian / LLM Wiki (+ MCP)**; agent = model + harness; authorship located in skills/tools/wiki.

### Compute scale (the main Task B contrast)
| | KITeGG (described) | CVC (planned) |
|---|---|---|
| Concurrent design | ~40 users/site, ~200 cluster-wide capacity planning | one student ↔ one agent session |
| Hardware | institutional HGX A100 fleet (+ optional ~€3k DIY nodes) | optional laptop / 7–8B local / single GPU / rare Studio–Spark; **no purchase required** |
| Ops | ≥1 FTE platform engineer + partner lab staff | student self-ops + teacher how-tos |
| Cloud stance | strong **public bare-metal** preference for funded infra | cloud API allowed; local taught as option |

### Pedagogy & “unlearn”
- **KITeGG** brands **un/learning** and aesthetic practice (Physical AI, type, robotics, Critical AI Studies, student showcases as publication).
- **CVC** twin tracks: political-economic landscape (bubble, visions/fears/regulation) **and** agent literacy; outdoor “group therapy” check-in; humanities pair inputs from Session 2.

### Publishing / knowledge form
- **KITeGG:** PubPub + semantic chunk network + print books as research output.
- **CVC:** course GitHub + personal LLM Wiki habit; knowledge store is **student infrastructure**, not a designed trilogy.

### Session 01 specifically
- CVC Block 2 teaches **model / chat product / agent** layers, tokens, hallucination, harness preview — vocabulary almost absent from *un/learn* front matter (their “agent” moment is more chatbot/multimodal in the Navigating phase, not Hermes-style tool loops).
- CVC Block 4–5 (bubble / ecology seed) overlaps Koch’s cloud-capital and datacenter critique, but Koch embeds it inside **platform-engineering justification**; CVC embeds it in seminar discourse without building a cluster.

---

## Systems-scale contrast (one paragraph)

KITeGG’s “systems” are a **federation**: one mid-scale interactive GPU cloud-on-prem, a custom teaching platform, and six thematically split labs that make AI tactile (objects, robots, sustainability materials, automation tools, art algorithms, design intuition). Critical Vibe Coding plans the opposite end of the same sovereignty spectrum: each student owns a **small agentic interface** to models and tools, with optional tiny local inference. Same distrust of locked cloud dependency; **different unit of infrastructure** (campus cluster + ateliers vs personal harness + wiki).

## Session 01 mapping (where KITeGG echoes CVC blocks)

| CVC Block (lecture.md) | KITeGG / unlearn echo | Do not collapse |
|---|---|---|
| 2 Model / product / agent | Weak in unlearn front matter — their “agent” moment is chatbot/multimodal (Vol. 2), not Hermes tool loops | Teach CVC vocabulary; cite unlearn only as contrast |
| 3 Visions / fears / regulation | Koch cloud-capital / anti-greenwash; Critical AI Studies in Vol. 3 | CVC script is `course/visions-fears-regulation` + Stewart/Coxon/Ismail clips |
| 4 Bubble / circular finance | Infrastructure-as-STS; public money → public capacity | CVC numbers from BIS / Tooze / Acemoglu research notes |
| 5 Ecology seed | Koch ecology argument; lab sustainability themes; DC energy visibility | Deep dive = Session 11 + `research/data-centers-energy-ecology-economy` |
| 7 Refusal / when not | Vol. 3 Editor’s Note “when not to use” | CVC Session 11 dedicated |
| 8 Personal Hermes + Obsidian | Opposite unit: campus Jupyter/LLP + cluster | Same sovereignty spectrum, different scale |

## Vault clippings that sharpen the contrast

- `Clippings/Adam Tooze on the AI Arms Race…` / `…AI Regulation Ep. 260` — political economy / regulation register CVC uses; KITeGG stays design-education + STS infrastructure.
- `Clippings/The Real Cost of AI Will Shock You` — popular ecology framing for Session 11; pair with Koch’s anti-greenwash paragraphs rather than treating either as sole authority.
- `Clippings/A new look at the economics of AI` (Acemoglu) — modest productivity; KITeGG rarely does macro GDP debate.
- `course/eu-ai-act-and-datenschutz` — EU/AT law orientation; unlearn volumes are not a law handbook.

## Related notes

- [[00-index]] · [[systems-labs-overview]] · [[article-kitegg-cluster]] · [[article-how-to-kitegg]] · [[vol3-integrating]]
