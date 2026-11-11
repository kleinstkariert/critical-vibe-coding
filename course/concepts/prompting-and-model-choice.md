---
title: Prompting and model choice
date: 2026-10-26
updated: 2026-10-26
tags:
  - course
  - prompting
  - models
  - icao
  - reasoning
---

# Prompting and model choice

English handout for session [[sessions/03-hardware-open-models-prompting]] (prompting, chat versus reasoning, local hardware); model landscape in [[sessions/02-agent-harness-and-wiki-architecture]]. Complements harness thinking ([[what-is-harness]]): prompts are one harness surface; **structure** still matters more within a usable model tier ([[../../research/structure-vs-model-quality]]).

**ICAO habit (course + Hermes skill):** write prompts like clearances; Project chat uses radio words — vault skill `icao-prompting` · [[icao-project-comms]] (Hermes). Agents give short **prompt feedback** on user messages.

Labels: *technical suggestion* | *verified fact* | *nuance*. Links checked / papers cited 2026-10-26. Model names and API knobs move fast — re-check vendor docs before class.

---

## 1. What “good prompting” is

A prompt is a **brief for a junior collaborator with tools**, not a spell. Good prompts are:

1. **Clearance-shaped** — one intent, limits, report-back  
2. **Cheap enough** — tokens and energy cost real money and carbon  
3. **Matched to architecture** — chat ≠ agent ≠ multi-agent swarm  

Standing rules live in `SCHEMA.md` / skills — not only in one chat bubble.

---

## 2. Short tips (with *why* from research)

### Tip A — Write like ICAO (aviation phraseology)

**Do:** One goal sentence. Name role once. List constraints (paths, tools, refuse). Say what “done” and “Unable” look like. Optional: ask for a short plan before large edits.

**Why:** Aviation language exists to cut ambiguity under stress. Structured / standardized prompts raise decision accuracy and multi-agent clarity vs vague baseline prompts (*direction:* agent PE study in Hermes TEMP PDF; coordination tables). Clear **Unable + reason** prevents silent wrong action — same idea as radio discipline.

**Example clearance**

```text
Goal: Update course/prompting-and-model-choice.md with ICAO tip list.
Paths: course/ only. Do not edit emails/.
Done when: tips table has tip + why + source row.
If blocked: Unable + Request the missing path.
```

### Tip B — Mark the payload (tags / delimiters)

**Do:** Wrap code, data, and “incomplete” bits in clear markers (`<code>…</code>`, fenced blocks, “CONTEXT:” / “TASK:”).

**Why:** *verified fact (direction):* Rubei et al. (arXiv:2501.05899) — custom tags that separate prompt parts reduced **energy** for Llama-3 code completion without hurting accuracy vs untagged baselines. Models parse parts more reliably when boundaries are explicit.

### Tip C — Start cheap; escalate tokens only if needed

**Do:** Prefer plain instruction (Vanilla IO) or light “think step by step” before few-shot piles or self-consistency sampling.

**Why:** *verified fact:* Sypherd et al. (arXiv:2505.14880) — **Token Cost** (tokens per accuracy point) explodes as strategies go Vanilla → Fewshot CoT → CoT-SC. Marginal TC from Fewshot CoT to CoT-SC can be **orders of magnitude** worse. Big-O_tok: constant ≪ linear ≪ polynomial token growth.

### Tip D — Prefer router / single tool over default multi-agent

**Do:** For Q&A over a wiki or DB: select the right source, then answer. Spawn agents only when roles truly diverge.

**Why:** *verified fact (domain study):* UFRJ/COPPE dissertation (O&G RAG, 2025) — multi-agent once bought ~**28%** higher Q&A truthfulness but ~**3.7×** cost; a later cycle found a **non-agentic router** beat both single- and multi-agent on specialized data. Architecture choice *is* prompt strategy at system scale.

### Tip E — Reflect once under complexity; don’t narrate every step

**Do:** For hard multi-step work: “List plan (3 bullets), then execute.” Skip ritual CoT on trivial renames.

**Why:** Reflective / meta prompts raised accuracy and high-complexity completion in agent simulations (*nuance:* TEMP GRJNST paper — low-prestige venue; treat as illustration). Reflexion / self-critique literature supports critique loops for uncertain tasks — not as default token burn (see Tip C).

### Tip F — Short prompt + rich schema/wiki

**Do:** Put standing rules in `SCHEMA.md` / skills; keep the user message as a thin clearance.

**Why:** Same as Tip C + course harness lesson: structure ≫ stuffing the context window. Megaprompts raise Token Cost and hide constraints.

### Tip G — Verify / kill switches in the brief

**Do:** “Do not invent paths or citations; open the file. Refuse: …”

**Why:** Agents execute tool loops; without verify + refuse, they will “Wilco” a bad clearance. Course agent checklist (goal / paths / tools / verify / kill).

---

## 3. Chat vs agents

### Chat / role packs (starters)

OpenAI Academy — *ChatGPT for any role*:  
https://academy.openai.com/public/clubs/work-users-ynjqu/resources/chatgpt-for-any-role  

Steal: role + audience + output structure + paste context. Then ICAO-harden it (Tip A).

### Agent brief (Hermes, Cursor, …)

1. **Goal** — done means  
2. **Paths** — read/write scope  
3. **Tools** — allowed / ask first  
4. **Verify** — check files; no invented cites  
5. **Kill switches** — `SCHEMA.md`  

---

## 4. Chat LLMs vs reasoning models

### What is different?

| | **Chat / instruct LLM** | **Reasoning / “thinking” model** |
|---|---|---|
| Default behaviour | Next-token reply; may follow a short CoT if you ask | Often emits a long **internal monologue** (thinking / reasoning tokens) *before* the final answer |
| What you pay for | Mostly visible answer tokens | Answer **+** thinking tokens (often billed as output; may count toward `max_tokens`) |
| Latency | Usually lower | Higher — can be many seconds of silent “thinking” |
| Typical strength | Drafting, rewrite, chat, tool calls on clear briefs | Hard math, multi-step bugs, planning under uncertainty |
| Typical waste | Over-prompting (Tip C) | Thinking left **on** for “rename this file” / “say hello” |

*nuance:* “Reasoning model” is a product category, not a separate species of neural net. Many are instruct models **trained or templated** to produce a thinking block (DeepSeek-R1 style, Qwen3 thinking, Claude extended/adaptive thinking, OpenAI o-/GPT-reasoning effort, Gemini thinkingBudget). Chat models can still reason if you prompt CoT — but they do not *always* spend a fixed thinking budget.

*verified fact (research direction):* Long thinking is not always necessary. Ma et al., *Reasoning Models Can Be Effective Without Thinking* (arXiv:2504.09858) — bypassing the thinking block (**NoThinking**) can beat Thinking under **tight token budgets**; parallel short answers can rival long thinking at lower latency. Class takeaway: treat thinking as a **knob**, not a virtue signal.

### When it usually makes sense

| Use a **chat / instruct** (or thinking **off**) | Use a **reasoning** model (thinking **on** / higher effort) |
|---|---|
| Rewrite, tone, ICAO-style short clearances | Novel multi-step coding / math / formal proofs |
| Agent tool loop with a clear schema (wiki lint, one MCP call) | Debugging when the first answer is wrong and the task is hard |
| Batch tagging, summarising known notes | Planning an unfamiliar architecture |
| Local laptop, low VRAM, interactive studio | Cloud budget OK; accuracy > latency |
| You already have harness + tests doing the “thinking” | You need the model to explore alternatives before acting |

**Course line:** Default = **good chat/instruct + harness**. Escalate to reasoning / thinking-on for a **named hard task**, then turn it off again. Same spirit as Tip C (Token Cost).

---

## 5. Thinking on / off — save monologue tokens

Thinking tokens are often **invisible in the UI** but still cost money and time. Prefer models that allow a **switch** or **effort** level.

### Practical matrix (*technical suggestion* — verify before class)

| Family | Thinking off / low? | How (typical) |
|---|---|---|
| **Qwen3** (cloud / vLLM / many hosts) | Yes — often **on by default** | `chat_template_kwargs: { "enable_thinking": false }` · OpenRouter-style `reasoning` / provider docs |
| **DeepSeek** hybrid (e.g. V3.1-class) | Yes on hybrids | Switch **thinking vs non-thinking** via chat template / `thinking` param — R1-only distill may always think unless host supports `think: false` |
| **Ollama** (Qwen3, DeepSeek-R1, …) | Yes when model supports it | CLI: `ollama run MODEL --think=false` or `/set nothink` · API: `"think": false` — docs: https://docs.ollama.com/capabilities/thinking |
| **Gemini 2.5 Flash / Flash-Lite** | Yes | `thinkingConfig.thinkingBudget: 0` — **Pro** often cannot fully disable |
| **OpenAI reasoning / GPT-5.x effort** | Often **effort** not a hard off | `reasoning.effort`: `none` / `minimal` / `low` / … (model-dependent) |
| **Claude** (extended / adaptive thinking) | Model-dependent | Older: `thinking: { type: "disabled" }`. Newer adaptive-only lines may **reject** disable — use lowest **effort** instead. Check current Anthropic / OpenRouter model card |
| **OpenRouter (unified)** | Best student default for cloud | `"reasoning": { "effort": "none" }` or `"enabled": false` when allowed; `"exclude": true` hides reasoning in the response but may still bill depending on provider — https://openrouter.ai/docs/guides/best-practices/reasoning-tokens |

*nuance:* Some models are **mandatory-reasoning** (API returns 400 if you disable). Then pick a cheaper **non-reasoning** twin for daily work, not “effort: none” theatre.

### Setup sketches

**A. Hermes / OpenRouter (cloud multi-model)**  
1. Add OpenRouter (or vendor) key in Hermes provider settings.  
2. Pick a **flash / instruct** model as default.  
3. Add a second profile: reasoning model with `reasoning.effort` high (or thinking on).  
4. Route: daily wiki edits → default; hard debug → reasoning profile.  
(*Hermes budget posture in vault concepts may already prefer cheap Chinese / local — align with that.*)

**B. Ollama local**

```bash
ollama pull qwen3:8b
ollama run qwen3:8b --think=false "Summarise this note in 3 bullets: …"

# interactive
ollama run qwen3:8b
>>> /set nothink
```

API: `"think": false` on `/api/chat`. Discover levels: `POST /api/show` → `thinking.values`.  
Docs: https://docs.ollama.com/capabilities/thinking · blog: https://ollama.com/blog/thinking

**C. Cursor / IDE**  
Use model picker: “fast” vs “thinking/reasoning” SKUs when offered. Prefer fast for refactors; reasoning for unfamiliar bugs. Do not leave max-thinking as the only model.

---

## 6. Cheap & local lightweight options

Hardware memory rules: [[../../research/local-gpu-hardware-for-llms]].

| Class | Examples (*names age — pick current tags*) | Fits roughly | Role |
|---|---|---|---|
| Tiny / phone-laptop | Qwen3 0.6B–4B, Phi-class, Gemma small | 8–16 GB RAM / low VRAM | Offline draft, classification |
| Sweet laptop | **Qwen3 8B**, Llama 3.x 8B, DeepSeek-R1 **distill 8B** | 8–12 GB VRAM or 16–24 GB unified (Q4) | Daily local agent helper; toggle think |
| Mid local | 14–32B instruct / R1 distill | 16–24 GB+ | Stronger code; still optional think |
| Avoid as default | Full R1 / huge MoE with thinking **always on** | 40 GB+ | Studio server, not every chat |

**Stacks:** Ollama · LM Studio · llama.cpp · MLX (Apple).  
**Agent tip:** Point Hermes at a local OpenAI-compatible endpoint (Ollama `http://localhost:11434/v1`) for private runs — see [[howto-hermes-setup]].

**When local lightweight wins:** privacy, EU data location experiments, no API bill, class demos without accounts.  
**When it loses:** weak tool-calling, small context, slow on CPU-only — then cloud flash (thinking off) is often better than a struggling 70B offload.

---

## 7. Choosing models — strengths, not vibes (cheat-sheet)

| Need | Prefer |
|---|---|
| Agent + tools / MCP, clear brief | Chat/instruct mid-size, **thinking off** |
| Hard multi-step / novel bug | Reasoning model or thinking **on** / higher effort — then switch back |
| Private / offline | Local 7–8B Q4 ([[../../research/local-gpu-hardware-for-llms]]) |
| EU data location | EU-hosted endpoint or local; read ToS |
| Cheap ideation / rewrite | Flash / small instruct; **no** monologue |
| Hard multi-file code | Better model **and** harness — not model alone |
| Academic campus chat | [[academic-ai-austria]] — usually **not** the agent backend |

Azure Foundry models: https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?pivots=azure-openai  
Kaggle Game Arena (calibrate hype): https://www.kaggle.com/game-arena  
OpenRouter reasoning guide: https://openrouter.ai/docs/guides/best-practices/reasoning-tokens  
vLLM reasoning parsers: https://docs.vllm.ai/en/stable/features/reasoning_outputs/  
Campus chat ≠ agent backend: [[academic-ai-austria]]

---

## 8. Mini exercise (session 3)

1. Take one OpenAI Academy prompt → rewrite as **ICAO clearance** (Tip A) with paths + verify.  
2. Same micro-task: Vanilla vs Fewshot CoT — note quality **and** tokens/€ (Tip C).  
3. **Thinking A/B:** same hard question on one model with thinking **on** vs **off** (Ollama `--think=false` or OpenRouter `reasoning.effort: none`). Record latency, token bill if shown, answer quality.  
4. Log under `comparisons/` in the vault.  
5. Optional: tagged vs untagged code completion (Tip B).

---

## 9. Sources

| Resource | URL / path |
|---|---|
| Token usage / Big-O_tok / Token Cost | https://arxiv.org/html/2505.14880v1 |
| PETs + energy / custom tags | https://arxiv.org/html/2501.05899v1 |
| RAG architectures (router vs agents) | https://pesc.coppe.ufrj.br/uploadfile/publicacao/3242.pdf |
| NoThinking vs Thinking (reasoning without monologue) | https://arxiv.org/html/2504.09858 |
| OpenRouter reasoning tokens | https://openrouter.ai/docs/guides/best-practices/reasoning-tokens |
| Ollama thinking | https://docs.ollama.com/capabilities/thinking |
| Agent PE (TEMP; use cautiously) | Hermes `TEMP/Prompt_Engineering_for_Autonomous_AI_Agents_Enhanc.pdf` |
| ICAO skill (vault) | Hermes `skills/icao-prompting.md` · `skills/icao-project-comms.md` |
| Structure vs model | [[../../research/structure-vs-model-quality]] |
| Local hardware | [[../../research/local-gpu-hardware-for-llms]] |
