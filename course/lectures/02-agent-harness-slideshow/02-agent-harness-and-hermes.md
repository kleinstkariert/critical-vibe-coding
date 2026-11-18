---
title: Session 02. Agent harness and Hermes
session: 2
format: obsidian-slides
slot: 10:00 to 12:00
css: cvc-slides
---

# Session 02
## Agent harness and Hermes

Critical Vibe Coding · 10:00 to 12:00

---

# Today

1. Check-in
2. Student input: Flattening
3. Catch-up (one point from last class)
4. Hermes + harness → **5 min break** → more Hermes
5. Practical install start · homework = finish install


---

# Core sentence

> The model contains the intelligence.
> The **harness** makes that intelligence useful.
>
> If you're not the model, you're the harness.

LangChain, *Anatomy of an Agent Harness* (2026)

---

# Agent = Model + Harness

| Layer | What |
|---|---|
| Model | Weights: token in, token out |
| Thin harness | Chat UI + history |
| Thick harness | Files, tools, skills, sandbox, verify loops |

Hermes = thick harness (same family as Cursor Agent, Claude Code).

Course note: [[what-is-harness]]

---

# Hermes in one slide

Open-source agent (Nous Research, MIT).

**Hermes Desktop** = native GUI for the same agent (closer to Cursor / Cowork than CLI alone).

Providers · terminal · files · skills · memory · sandboxes · messaging.

Not the same as **Hermes 4** chat models.

Install: [[howto-hermes-setup]] · Desktop: https://hermes-agent.nousresearch.com/desktop

---

# Skills

Reusable instruction package (`SKILL.md`), loaded when needed.

Browse: `/skills` · Install: `hermes skills install …`

Review third-party skills before install. Skills Guard exists for a reason.

Guide: hermes-agent.nousresearch.com/docs/guides/work-with-skills · [[howto-hermes-efficient-coding]]

---

# Security (defaults + laptop)

- Not root · gateway not public
- Docker / sandbox for untrusted work
- Mount only needed folders · not the private vault
- Keys in Hermes env, never in synced notes
- Approvals · repair limits · review the Git diff

Overview: [[Local LLM Coding with Hermes]] · Docs: hermes-agent.nousresearch.com/docs/user-guide/security

---

# Break · 5 minutes

Then: models, local setup, chat links, install.

---

# What models exist

| Path | Role today |
|---|---|
| Proprietary cloud | Strongest agents, paid, data leaves |
| Open weights (hosted) | Free/cheap smoke tests (Nemotron) |
| Local | Privacy experiments · Session 03 |
| Academic AU chat | Often **no** agent API key |

Honesty: [[academic-ai-austria]]

---

# Local models in Hermes

1. Hermes Desktop → **Local Models**, or
2. Ollama → `http://localhost:11434/v1`, or
3. llama.cpp / vLLM / LM Studio endpoint

Need: tool calling + context ≥64k.

Hardware: [[howto-local-llm-hardware]]

---

# Subscription / API key

Fast path: `hermes setup --portal`

Or: `hermes model` → OpenRouter / Anthropic / OpenAI / Google

Class free test: OpenRouter `nvidia/nemotron-3-ultra-550b-a55b:free`

Keys in Hermes `.env` only. Never in the vault.

---

# Connect chat

| Platform | Setup |
|---|---|
| Telegram | `hermes gateway setup` → Telegram |
| Discord | same wizard → Discord |
| Matrix | same wizard → Matrix |
| **Signal** | **yes** · via `signal-cli` HTTP daemon |

Always use allowlists / pairing on a personal laptop.

Docs: hermes-agent.nousresearch.com/docs/user-guide/messaging/

---

# Personal laptop

1. Cloud provider = code leaves the machine
2. Local backend = **no** isolation
3. Messaging gateway always on = attack surface
4. Battery, heat, disk, sync fights
5. Separate agent-writable folders from private notes

Guide: secure-hermes-on-a-work-machine (Hermes docs) · [[howto-obsidian-setup-and-sync]]

---

# Practical · Homework

**In class:** install Hermes Desktop or CLI → model/key → vault path → one smoke-test note.

**Homework:** finish install · Model/Harness/Wiki diagram · skim Karpathy gist **or** LangChain harness article.

[[howto-hermes-setup]] · [[howto-hermes-efficient-coding]] · [[agents-md-template]]

---

# References

- [[Local LLM Coding with Hermes]] · [[howto-hermes-setup]] · [[howto-hermes-efficient-coding]]
- Karpathy LLM Wiki gist · LangChain harness anatomy
- Session: [[02-agent-harness-and-wiki-architecture]]
- Comparison (optional): [[02-hermes-vs-coding-agents]] · [[hermes-vs-coding-agents]]
- CSS: `cvc-slides.css` (vault snippet)
