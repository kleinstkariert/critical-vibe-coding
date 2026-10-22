---
title: Prompting and model choice
date: 2026-10-21
tags:
  - course
  - prompting
  - models
---

# Prompting and model choice

English handout for session [[sessions/03-models-prompting-install]]. Complements harness thinking ([[what-is-harness]]): prompts are one harness surface; **structure** still matters more within a usable model tier ([[../research/structure-vs-model-quality]]).

Labels: *technical suggestion* | *verified fact* (links checked 2026-10-21).

---

## 1. Prompting — chat vs agents

### Chat / role packs (useful starters)

OpenAI Academy — *ChatGPT for any role* (For Work Prompt Pack):  
https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role  

Patterns to steal (then adapt for art/studio):

| Pattern | Example use |
|---|---|
| Role + audience + constraint | “Rewrite for peers / executives / public” |
| Structure the output | Agenda sections, decision criteria, risk list |
| Paste context explicitly | “Text: [paste]” — never assume the model remembers your vault |
| Actionables | Decisions / owners / deadlines |

*nuance:* These packs optimise **workplace chat**. For **agents** (Hermes, Cursor, …) add:

1. **Goal** — what “done” means  
2. **Paths** — which folders/files may be read or written  
3. **Tools** — what it may call; what needs asking first  
4. **Verify** — “do not invent citations / paths; check the file”  
5. **Kill switches** — tasks it must refuse ([[llm-wiki-standard-files]] / `SCHEMA.md`)

Agent prompting is closer to **writing a brief for a junior collaborator** than to a magic spell.

### Course defaults

- Keep standing rules in `SCHEMA.md`, not only in one chat message.  
- Prefer short task prompts + rich wiki over megaprompts.  
- After the agent acts: **lint / open the file / run the patch** — human eyes.

---

## 2. Choosing models — strengths, not vibes

### Vendor capability sheets (what they claim to sell)

Azure AI Foundry — models sold directly by Azure (Azure OpenAI pivot):  
https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai  

Use this (or the current Anthropic / Google / open-weights cards) to compare **context length, modalities, region, pricing tier, tool-calling support** — not as art criticism.

*technical suggestion for agents:* Prefer models with reliable **tool / function calling** over “highest creative writing score” alone.

### Live skill / reasoning arenas

**Kaggle Game Arena** — models ranked in dynamic games (planning, adaptation; harder to saturate than static quiz benchmarks):  
https://www.kaggle.com/game-arena  

*nuance:* Game Elo ≠ “best for my Blender MCP task.” Use arenas to **calibrate hype**, then test on *your* stack (one coding task, one wiki ingest, one creative rewrite).

Also useful elsewhere: LMSYS / Chatbot Arena-style blind chats; SWE-Bench / Terminal-Bench for coding agents (see structure-vs-model research).

### Decision cheat-sheet for students

| Need | Prefer |
|---|---|
| Agent + tools / MCP | Strong tool-calling model; mid-large is often enough |
| Private / offline | Local open weights ([[../research/local-gpu-hardware-for-llms]]) |
| EU data location | EU-hosted endpoint or local; read ToS |
| Cheap ideation | Small / flash tier; don’t burn frontier tokens on rename-refactors |
| Hard multi-file code | Better model *and* repo context / harness — not model alone |

Academic campus chat without API: [[academic-ai-austria]] — usually **not** the agent backend.

---

## 3. Mini exercise (session 3)

1. Take one OpenAI Academy prompt → rewrite it as an **agent** brief with paths + verify.  
2. Pick two models (e.g. from Azure catalog or Game Arena top/mid) → run the **same** wiki or code micro-task → note quality, latency, €.  
3. Log the comparison under `comparisons/` in the vault.

---

## Links (quick)

| Resource | URL |
|---|---|
| OpenAI Academy — ChatGPT for any role | https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role |
| Azure Foundry — models sold by Azure | https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai |
| Kaggle Game Arena | https://www.kaggle.com/game-arena |
| Structure vs model quality | [[../research/structure-vs-model-quality]] |
| Local hardware | [[../research/local-gpu-hardware-for-llms]] |
