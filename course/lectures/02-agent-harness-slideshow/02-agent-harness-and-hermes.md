---
title: Session 02. Agent harness and Hermes
session: 2
format: obsidian-slides
slot: 10:00 to 12:00
---

# Session 02
## Agent harness and Hermes

Critical Vibe Coding · 10:00 to 12:00

Obsidian Slides: Command Palette → **Start presentation**

---

# Today

1. Check-in
2. Student input: Flattening
3. Catch-up (one point from last class)
4. Hermes + harness (theory) → **5 min break** → more Hermes
5. Practical install start · homework = finish install

---

# Check-in

Listen only.

No fixing. No advice yet.

---

# Student input
## Flattening

Thesis to test: **AI kills the underground and it kills diversity.**

Include: AI and patriarchy · feminism and AI

Deep dive: `course/lectures/01-welcome-landscape-deep-dives/flattening-and-the-norm.md`

---

# Catch-up (Session 01, one beat)
## An alternative AI as a commons

Verdegem: AI as a commons · ecology · jobs · creative industry impact · practices for this semester

One frame for the rest of the course: structure and tools you control, not only bigger APIs.

---

# Core sentence

> The model contains the intelligence.
> The **harness** is the system that makes that intelligence useful.
>
> If you're not the model, you're the harness.

LangChain, *The Anatomy of an Agent Harness* (2026)

---

# Agent = Model + Harness

| Layer | What |
|---|---|
| Model | Weights: token in, token out |
| Thin harness | Chat UI + history |
| Thick harness | Files, tools, skills, sandbox, verify loops |

Hermes = thick harness. Cursor Agent and Claude Code sit in the same family.

Course note: `course/concepts/what-is-harness.md` (or `../what-is-harness`)

---

# Hermes in one slide

Open-source agent (Nous Research, MIT).

Providers · terminal · files · skills · memory · sandboxes · messaging gateway.

Not the same thing as **Hermes 4** chat models.

Install guide: [[../../setup/howto-hermes-setup]]
Overview: vault `course/setup/Local LLM Coding with Hermes.md`

---

# Skills

A skill = reusable instruction package (`SKILL.md`), loaded when needed.

Browse: `/skills` · Install: `hermes skills install …`
Guide: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills

**Review third-party skills before install.** Skills Guard exists for a reason.

---

# Security (defaults + laptop)

- Do not run as root · do not expose the gateway publicly
- Prefer Docker / sandbox for untrusted work
- Mount only needed folders · never the whole private vault
- Keys in Hermes env, never in synced notes
- Approvals + repair limits + human review of the Git diff

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/security  
Work machine: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine

---

# Break · 5 minutes

Then: models, local setup, chat links, install.

---

# What models exist (short)

| Path | Role today |
|---|---|
| Proprietary cloud | Strongest agents, paid, data leaves |
| Open weights (hosted) | Free/cheap smoke tests (e.g. Nemotron on OpenRouter) |
| Local | Privacy experiments; Session 03 goes deeper |
| Academic AU chat | Often **no** agent API key |

Honesty note: [[../../setup/academic-ai-austria]]

---

# Local models in Hermes

1. Hermes Desktop → Providers → **Local Models**, or
2. Ollama at `http://localhost:11434/v1`, or
3. llama.cpp / vLLM / LM Studio custom endpoint

Need: tool calling + enough context (≥64k for agent work).

Hardware cheat sheet: [[../../setup/howto-local-llm-hardware]]

---

# Subscription / API key

Fast path: `hermes setup --portal` (Nous Portal OAuth)

Or: `hermes model` → OpenRouter / Anthropic / OpenAI / Google / …

Class free smoke test: OpenRouter `nvidia/nemotron-3-ultra-550b-a55b:free`

Put keys in `%LOCALAPPDATA%\hermes\.env` (Windows) or `~/.hermes/.env`. Never put keys in the vault.

---

# Connect chat

| Platform | Hermes docs |
|---|---|
| Telegram | https://hermes-agent.nousresearch.com/docs/user-guide/messaging/telegram |
| Discord | …/messaging/discord |
| Matrix | …/messaging/matrix |
| **Signal** | …/messaging/signal (**yes**: via `signal-cli` HTTP daemon) |

Setup wizard: `hermes gateway setup`  
Always use allowlists / pairing on a personal laptop.

---

# Personal laptop: what to watch

1. Cloud provider = your code leaves the machine
2. Local backend = **no** isolation (Hermes docs)
3. Messaging gateway on always = attack surface
4. Battery, heat, disk (models), and sync fights (Obsidian + agent)
5. Separate agent-writable folders from private notes

Secure-on-laptop guide (link above).

---

# Practical now · Homework later

**In class (start):** install Hermes → model/key → point at vault → one smoke-test note.

**Homework:** finish install · one Model/Harness/Wiki diagram · skim Karpathy gist **or** LangChain harness article.

How-to: [[../../setup/howto-hermes-setup]]  
Coding efficiency (extra): [[../../setup/howto-hermes-efficient-coding]]

---

# References (sparse)

- Hermes docs: https://hermes-agent.nousresearch.com/docs/
- Providers: https://hermes-agent.nousresearch.com/docs/integrations/providers
- Skills: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills
- Karpathy LLM Wiki gist: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- LangChain harness anatomy: https://www.langchain.com/blog/the-anatomy-of-an-agent-harness
- Harness engineering README: https://github.com/q-qp-p/jrenaldi79-harness-engineering
- Session file: [[../../sessions/02-agent-harness-and-wiki-architecture]]
