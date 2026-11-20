---
title: Vibe-coding tools and agent environments, late 2026
date: 2026-11-20
tags:
  - research
  - tools
  - course
---

# Vibe-coding tools and agent environments, late 2026

Checked **2026-11-20**. This page is a map for students who are new to these tools. Prices, model names, and quotas change. Open the linked page before you pay.

Labels: *verified fact* | *claim* | *uncertainty* | *technical suggestion*.

This page does not replace the course how-tos:

- Job split (harness, coding agent, always-on assistant): [[../course/concepts/hermes-vs-coding-agents]]
- What a harness is: [[../course/concepts/what-is-harness]]
- Hermes install: [[../course/setup/howto-hermes-setup]]
- OpenCode install: [[../course/setup/howto-opencode-setup]]
- Pair Hermes with OpenCode: [[../course/setup/howto-hermes-opencode-pairing]]
- Prompting: [[../course/setup/Prompting Guide for Critical Vibe Coding]]

---

## Three jobs

Use the job name, then the product name.

| Job | What you do there | Course examples |
|---|---|---|
| Editor coding | Files, tabs, and an agent panel in one window | Cursor, VS Code, Continue, Cline, Devin Desktop (formerly Windsurf), Zed |
| Terminal repo work | An agent in a project folder. It edits files and runs commands | Claude Code, OpenCode, Codex CLI, Aider, Gemini CLI |
| Assistant and messaging | Notes, chat apps, tools, and work that can stay up | Hermes |

*technical suggestion:* Hermes is the course default for the assistant job. Add a coding agent when a repository needs a deep edit. The pairing note above is the short version.

Zed is an editor. Hermes is not an editor. Claude Code is not an editor.

---

## How money and popularity are counted

Four ways a student pays:

1. **Quota.** You pay $0 until a cap. The company that serves the model pays the compute. That compute cost is **not published**.
2. **Subscription.** You pay the tool company a monthly fee. The fee buys a cap. It does not buy unlimited compute. If the company is also the model lab, you pay the lab. If not, the tool company pays the lab. The lab's wholesale price is **not published**.
3. **Pass-through.** You pay token prices. Your own API key means the model lab bills you. Some tools add a fee on top of list price.
4. **Local.** You run open weights on your machine. You pay electricity and the computer. There is no token bill.

**Open source** means the program source is public under a named licence. The model is a separate product. An open tool can still send your code to a closed model.

**Reach** uses two sources only.

- *verified fact:* Stack Overflow Developer Survey 2026, question "AI coding agents". "Have you used any of the following coding agents or assistants in the past year?" Fielded 23 June 2026 to 5 August 2026. Published 6 October 2026. n = 12,255 people who answered. People could pick more than one tool, so the shares add up to more than 100%. https://survey.stackoverflow.co/2026/ai/data/ai-code-agent
- *verified fact:* GitHub stars below were read from the GitHub API on 2026-11-20. Stars are not users. This page does not give download counts.

If the survey question did not name the tool, the cell says **not in this question**. If no public source repository was found, stars say **not published**.

The survey is a Stack Overflow sample. It is not a sample of this class.

---

## Editors

| Tool | Licence | Open weights on your machine | Own API key | Reach | What you pay |
|---|---|---|---|---|---|
| Cursor | Proprietary. Source not public. | Localhost is not a supported path. | Yes, from Premium up. Plus and Free: no. | Survey 25.5% (3,127). Stars: not published. | Free limited. Plus $8, Premium $30, Super $100, Ultra $200 per month. |
| VS Code + Copilot | Editor source: MIT. Copilot: proprietary. | Yes, in chat (Ollama and others). | Yes, for chat. Completions stay on Copilot. | Copilot survey 58.7% (7,196). VS Code repo stars: 195,702. | Copilot Free $0. Student $0. Pro $10. Pro+ $39. Max $100 per month. |
| Continue | Apache-2.0 | Yes, if you configure it. | Yes | Survey 3.8% (466). Stars: 36,529. | The extension is free. You pay the provider you configure. |
| Cline | Apache-2.0 | Yes. Ollama and LM Studio are documented. | Yes | Survey 4.5% (551). Stars: 71,791. | Extension free. Optional Cline bill, or ClinePass $9.99 per month, or your own key. |
| Windsurf, now Devin Desktop | Proprietary | Not the built-in default. | Not confirmed on a current official page. | Survey still lists Windsurf 6.5% (796) and Devin 2.9% (360) as two rows. Stars: not published. | March 2026 list: Free $0, Pro $20, Max $200 per month. See the note. |
| Zed | Editor source is open. Mixed licence. See below. | Yes. Ollama and LM Studio are on the free plan. | Yes, on the free plan. | Survey: not in this question. Stars: 95,418. | Editor $0. Pro $10 per month for hosted models. |

### Cursor

*verified fact:* Cursor is sold as part of The X Subscription. The current individual prices, read on https://cursor.com/docs/models-and-pricing on 2026-11-20, are Free $0, Plus $8, Premium $30, Super $100, and Ultra $200 per month, tax excluded. Older Pro, Pro+, and Ultra plans still exist as legacy plans.

Plus includes Cursor's models named Grok and Composer on that page. Plus does not include your own API key, and it does not include Claude, GPT, or Gemini.

From Premium up, you can add your own key for OpenAI, Anthropic, Google, Azure, or AWS Bedrock. The provider bills that key. Cursor's help page says the request still goes through Cursor's servers, and that tab completion stays on Cursor's models. https://cursor.com/help/models-and-usage/api-keys

*verified fact (Cursor staff on the forum):* an own-key model must be reachable from Cursor's servers. A model that only listens on localhost is not a supported path. https://forum.cursor.com/t/using-local-model-with-cursor/149366

Included Grok and Composer use a weekly pool. You pay Cursor. What Cursor pays to run those models is not published. Third-party models on individual Premium and above are billed at API list price from prepaid credit. You pay that list price to Cursor. What Cursor pays the model lab is not published. On Teams and Enterprise, eligible third-party requests also add a Cursor Token Rate of $0.25 per million tokens, including requests that use your own key. Individual plans do not pay that rate.

### VS Code with GitHub Copilot

*verified fact:* The source repository `microsoft/vscode` is MIT (195,702 stars on 2026-11-20). The Visual Studio Code application you download from Microsoft is under Microsoft's product terms. Copilot is a separate proprietary service.

Copilot plan prices, read on https://docs.github.com/en/copilot/get-started/plans and the individual billing page on 2026-11-20:

- Copilot Free: $0, an allowance of GitHub AI Credits, auto model selection only, 2,000 code completions per month.
- Copilot Student: $0 for a verified student, auto model selection only, unlimited code completions, and an allowance of AI Credits. The overview table does not print one credit total for Student. That number is not copied here.
- Copilot Pro $10, Pro+ $39, Max $100 per month. Paid plans include larger credit pools. See the plans page for the credit counts.

On a Copilot plan, you pay GitHub (or $0). GitHub pays the model labs for included use. That wholesale cost is not published.

*verified fact:* VS Code chat can use your own key, or a local runtime such as Ollama, without a Copilot plan. The provider bills a cloud key. A local model has no token bill. Inline completions, semantic search, and embeddings still need Copilot. https://code.visualstudio.com/blogs/2026/06/18/byok-vscode · https://code.visualstudio.com/docs/agent-customization/language-models

*uncertainty:* that language-models page marks a separate "local harness" as deprecated, with removal set for February 2027. Bring-your-own-key chat is a different switch. Read the page again if you set this up later.

### Continue

*verified fact:* `continuedev/continue` is Apache-2.0 (36,529 stars). The README says the repository is no longer actively maintained and is read-only, after a final 2.0.0 release. https://github.com/continuedev/continue

The extension can point at your own key or at an OpenAI-compatible local server, including Ollama. You pay that provider. Continue does not sell the seats in the README. https://docs.continue.dev/customize/model-providers/top-level/openai

*technical suggestion:* keep an existing Continue setup if it already works. Do not start there if you need a project that still ships fixes. Cline is the maintained open extension in this table.

### Cline

*verified fact:* `cline/cline` is Apache-2.0 (71,791 stars). Docs read 2026-11-20: https://docs.cline.bot/getting-started/authorizing-with-cline

Three pay paths:

- Cline usage-billing. You pay Cline. Cline pays the model side. Any markup is not published on the page read here.
- ClinePass, $9.99 per month, optional, for a quota on selected open coding models. https://docs.cline.bot/getting-started/clinepass
- Your own key, or Ollama / LM Studio with no key. A cloud provider bills you. A local model has no token bill. https://docs.cline.bot/running-models-locally/overview

Job: editor agent, with a CLI as well. You approve steps.

### Windsurf, now Devin Desktop

*verified fact:* Cognition's FAQ says Windsurf became Devin Desktop on 2 June 2026. The FAQ says the IDE remains, and that plan prices did not change on that day. https://docs.devin.ai/desktop/devin-desktop-faq

*verified fact:* Cognition's pricing post of 18 March 2026 lists Free $0, Pro $20 per month, Teams $40 per seat per month, and Max $200 per month. Included use is a quota. Extra use is billed at API price. https://devin.ai/blog/windsurf-pricing-plans

*uncertainty:* this check did not find a newer public price table dated after June 2026. Read the current Devin page before you pay.

The product is proprietary. A general "paste any API key" page was not in the rename FAQ. *uncertainty:* treat bring-your-own-key as not confirmed for the current Devin Desktop. The FAQ does say you can use the desktop with local-only agents, without Devin Cloud.

You pay Cognition for a paid plan. Cognition pays the model labs for included quota. That wholesale cost is not published. On extra use, the March post says you pay API price.

### Zed

Zed is a code editor from Zed Industries, written in Rust. It is not a Hermes-style harness. It can launch external agents, including Claude Code and Codex CLI. https://zed.dev/

**What is true**

- *verified fact:* The editor is free. You do not need an account to edit code. You can turn AI off. https://zed.dev/pricing · https://zed.dev/docs/account/plans-and-pricing
- *verified fact:* The source is public: https://github.com/zed-industries/zed (95,418 stars on 2026-11-20). GitHub's licence field is `NOASSERTION` because the tree uses more than one licence.
- *verified fact:* Most of the source is GPL-3.0-or-later. Components meant for reuse, such as `gpui`, are Apache-2.0. https://zed.dev/software-overview and the repository README.
- *verified fact:* The app Zed distributes, and Zed's hosted services, are also under Zed's Terms of Service. The open-source licences govern the source. They do not by themselves govern the hosted model service. Same software-overview page.
- *verified fact:* On the free plan you can use your own API keys and external agents. The pricing page names Ollama, LM Studio, OpenRouter, and the major labs. The provider bills your key. Zed does not add its 10% fee on that path.
- *verified fact:* Pro is $10 per month. It includes $5 of hosted tokens and unlimited edit predictions. Hosted use past $5 is billed at API list price + 10%. You pay Zed the list price and the extra 10%. The 10% is Zed's fee. The list price is the model bill. https://zed.dev/pricing
- *verified fact:* A student plan is free for one year for a verified university student. It includes unlimited edit predictions and $10 of hosted tokens per month. Some hosted models are excluded (the plans page names Claude Fable, Claude Opus, GPT-6 Astra, GPT-5.5 pro, and GPT-5.4 pro). Spend past $10 is not a setting on the student plan. The cap is the $10.

**Correction of the claim "free, fully open source, and lighter than Cursor or Claude Code"**

- **Free:** true for the editor. False for hosted models and for Zed's edit predictions. Those are paid, with the student exception above.
- **Open source:** true for the editor source, under the mixed licence above. GPL-3.0 is copyleft. It is not a permissive licence.
- **Fully open source, under permissive licences:** Zed's compare page says that. The page was marked updated 1 May 2026: https://zed.dev/compare/vscode . The software overview does not say that. It names GPL-3.0-or-later for most of the source, and Terms of Service for Zed's services. The word "permissive" on the compare page is the claim this course does not repeat.
- **Lighter:** the same compare page is about VS Code, not about Cursor, and not about Claude Code. Zed's page states native Rust, startup under 1 second, about 600 MB of RAM, and memory use often 3 to 4 times lower than VS Code. Those figures are Zed's own claims. This page does not copy third-party RAM tables. Those tables do not agree with each other.
- A checked memory number for Zed versus Cursor is **not published** in a source used here. Cursor is a VS Code-family editor. Zed is a native Rust editor. This page does not turn that difference into a RAM figure.
- A checked memory number for Zed versus Claude Code is **not published**. Claude Code is a terminal agent. Zed can run it beside the editor. "Lighter than Claude Code" compares two different kinds of program.

---

## Terminal coding agents

| Tool | Licence | Open weights | Own API key | Reach | What you pay |
|---|---|---|---|---|---|
| Claude Code | Proprietary. All rights reserved. | Not an Anthropic feature. See the note. | Yes. A set API key replaces the subscription for billing. | Survey 65.5% (8,030). | Paid Claude plans. Pro $20 per month, or $17 per month billed yearly. Max $100. Ultra $200. Or API rates. |
| OpenCode | MIT | Yes. The product page says you can connect local models. | Yes | Survey row "Open Code" 13.6% (1,662). Stars: 228,195. | The tool is free. Other providers can cost money. |
| Codex CLI | Apache-2.0 for the client | Yes. `codex --oss` with Ollama or LM Studio. | Yes. API-key use is a separate bill. | Survey "OpenAI Codex" 29.5% (3,620). Stars: 135,982. | Included in ChatGPT plans, limits vary. Or API rates. |
| Aider | Apache-2.0 | Yes. Ollama is documented. | Yes | Survey 2.1% (256). Stars: 50,199. | The CLI has no priced plan in this check. You pay the provider, or $0 for a local model. |
| Gemini CLI | Apache-2.0 | Not the product. | Yes, a paid Gemini API key or Vertex. | Survey: not in this question under this name. Stars: 108,953. | Individual free login ended 18 June 2026. See Antigravity. |

### Claude Code

*verified fact:* Claude Code is Anthropic's terminal coding agent. The public repository https://github.com/anthropics/claude-code (156,428 stars on 2026-11-20) is not an open-source release of the agent. `LICENSE.md` says all rights reserved and points at Anthropic's commercial terms. The repository has no `package.json`.

Prices read on https://claude.com/pricing on 2026-11-20: Pro is $20 per month, or $17 per month if you pay $200 up front for a year. Max is $100 per month. Ultra is $200 per month. Claude Code is included in paid plans and shares the plan's use caps. https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan

You pay Anthropic. Anthropic is the model lab. Anthropic's own compute cost is not published. If `ANTHROPIC_API_KEY` is set, Claude Code bills the API, not the subscription. API rates are pass-through to Anthropic.

*uncertainty:* Ollama documents a local connection by pointing Claude Code at Ollama's Anthropic-compatible URL. https://docs.ollama.com/integrations/claude-code (read 2026-11-20). That page is Ollama's, not Anthropic's. This check did not confirm that Anthropic's terms allow that path. Do not treat it as an official open-weight mode.

Job: terminal repo work. It is the strongest "used in the past year" row in the survey above.

### OpenCode

*verified fact:* `anomalyco/opencode` is MIT (228,195 stars). The product page says the tool is free, that some models are free without an account, that you can connect local models, and that you can connect OpenAI, Anthropic, xAI, and other providers. It also says ChatGPT Plus or Pro, and GitHub Copilot, can be used as logins. https://opencode.ai/product

On a free OpenCode model, OpenCode says it stores data. On your own provider, that provider bills you and OpenCode's product page says the tool itself is free. What a connected lab charges is that lab's price.

*uncertainty:* the survey row is spelled "Open Code". This page reads that row as this project. The survey page does not link the row to the GitHub repository.

*uncertainty:* a docs file on the Git branch `dev`, not on `main`, describes optional plans named Go ($10 per month), Go Plus ($40), and Go Teams ($20 per member). The product FAQ quoted above does not list those prices. Check https://opencode.ai before you subscribe to anything beyond the free tool.

Job: repo coding in the terminal, and also a desktop app. Course install: [[../course/setup/howto-opencode-setup]].

### Codex CLI

*verified fact:* `openai/codex` is Apache-2.0 (135,982 stars). You can sign in with a ChatGPT plan, or use an API key. API-key sessions use API prices and do not draw the ChatGPT allowance. https://chatgpt.com/codex/pricing/ says Codex is included in ChatGPT Free, Go, Plus, Pro, Business, and Enterprise. The help page https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan says the same inclusion, including Free and Go, with limits that depend on the plan.

*verified fact:* `codex --oss` uses a local provider. The CLI docs name Ollama and LM Studio. https://learn.chatgpt.com/docs/cli/reference.md · https://learn.chatgpt.com/docs/config-file/config-advanced

*verified fact (pricing page read via search extract 2026-11-20):* https://learn.chatgpt.com/docs/pricing lists Pro at $100, $200, or $500 per month. This note does not copy every other plan's dollar price. Open the page.

On a ChatGPT plan, you pay OpenAI the plan fee (or $0 on Free, inside the cap). OpenAI is the model lab. On an API key, you pay OpenAI's API rates. On `--oss`, you pay the local machine.

*uncertainty:* the survey row "OpenAI Codex" includes more than the CLI. Do not read 29.5% as "CLI only".

### Aider

*verified fact:* `Aider-AI/aider` is Apache-2.0 (50,199 stars). The default branch last showed a push on 2026-05-22. That is slower public activity than the other CLIs in this list. It is still a real project.

Ollama setup: https://aider.chat/docs/llms/ollama.html

This check did not find a priced Aider subscription. You pay the model provider for a cloud key. A local model has no token bill. Survey reach is 2.1%.

Job: terminal pair programming on a git repo.

### Gemini CLI

*verified fact:* `google-gemini/gemini-cli` is Apache-2.0 (108,953 stars). From 18 June 2026, individual free accounts and Google AI Pro / Ultra no longer get answers from this CLI. Google tells those people to use Antigravity CLI. Enterprise Gemini Code Assist, and paid Gemini API or Vertex keys, stay on Gemini CLI. https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ · the README in the repository.

A paid API key is pass-through: you pay Google. Open weights are not the Gemini CLI product.

The survey has a row "Gemini Code Assist" at 14.6% (1,789). That row is not this CLI. This CLI's survey cell is **not in this question**.

---

## One more tool students meet: Google Antigravity

Antigravity is Google's agent product (app, CLI, and IDE extensions). It is the individual successor to Gemini CLI, so it belongs on this map. It is proprietary. No public source repository was found on 2026-11-20. Stars: **not published**. Survey: 16.0% (1,956).

*verified fact:* the plans page says there is no bring-your-own-key and no bring-your-own-endpoint for extra rate. Accounts that are not on Google AI Pro or Ultra get a weekly quota. Pro and Ultra get higher quotas. Dollar prices for Pro and Ultra are not on that page. https://antigravity.google/docs/plans/

You pay $0 inside the free quota. Google pays the compute. That cost is not published. Pro and Ultra overage can use AI credits at "standard Gemini Enterprise consumption pricing". You pay Google for those credits.

*verified fact:* local models are documented for the Antigravity **SDK** (on-device LiteRT, or an OpenAI-compatible server such as Ollama). https://antigravity.google/docs/sdk/local-models/ That is a developer library. It is not the same switch as the signed-in CLI, which rejects bring-your-own-key on the plans page.

---

## Hermes (course harness)

Hermes Agent is the course runtime. It is not an editor. It talks to tools, a vault, and chat channels. It can edit code. The course does not use it as the deepest repo coder. Read [[../course/concepts/hermes-vs-coding-agents]] for that split.

| | |
|---|---|
| Licence | *verified fact:* MIT. `NousResearch/hermes-agent`. 264,928 stars on 2026-11-20. FAQ: https://hermes-agent.nousresearch.com/docs/reference/faq |
| Open weights | *verified fact:* yes. Custom endpoint (Ollama and others) and a managed Local Models path. https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Own API key | *verified fact:* yes. OpenRouter, OpenAI, Anthropic, Google, and other providers. |
| Job | Assistant, messaging, vault, and optional always-on hosting. Not an editor session. |
| Reach | Survey: **not in this question**. Stars: 264,928. |
| Price | The software is free. Your provider bills your key. A local model has no token bill. |

Optional Nous Portal, read on https://hermes-agent.nousresearch.com/ on 2026-11-20: Free is pay as you go on free models. Plus is $20 per month. Super is $100. Ultra is $200. Paid tiers add hosted tools and one cloud agent. You pay Nous. Nous pays the model labs for Portal use. That wholesale cost is not published. You can leave Portal and use your own key on the same install.

---

## Does the starter vault still fit these tools?

The install notes use a Wanderloots-style tree: `SCHEMA.md`, `index.md`, `log.md`, `raw/`, `wiki/`, and `private/`. The written starter is `course/setup/starter-knowledge-base.md`. That file is on the install-guides branch. It is **not on main** on 2026-11-20, so this page does not link it. The same three layers (sources, wiki pages, schema) are already in [[../research/karpathy-llm-wiki-and-openclaw]] and [[../course/setup/llm-wiki-standard-files]].

**Tool-agnostic, and still right for every tool in this list**

- The notes are files in a folder. Every editor and every terminal agent can read a folder.
- `raw/` holds sources you add. `wiki/` holds pages an agent may rewrite. That split is a writing rule. It does not depend on Hermes.
- `SCHEMA.md` is the contract: what the agent may read, what it may write, and what it must leave alone. The idea fits every tool. The file does nothing until that tool is told to read it.
- Secrets stay out of the vault. That includes `private/`. API keys live in the tool's own secret store or in an un-synced `.env`. A folder name is not a lock. This rule is for Cursor, Zed, Claude Code, and Hermes alike.

**Hermes-specific**

- `WIKI_PATH`, the bundled llm-wiki skill, and the gateway.
- Hermes can be asked to keep `index.md` and `log.md` in step with the wiki. The other tools will not do that unless you ask in their own session.
- Chat channels and a cloud agent while the laptop is closed are Hermes jobs (or a hosted product such as Nous Portal). An editor does not become that assistant because it can see the same folder.

*technical suggestion:* keep this tree if you want one vault for the semester. Point Hermes at the vault. Point a coding agent at the code repository. Copy the access rules into the rules file that the coding tool actually reads (`AGENTS.md`, `CLAUDE.md`, Cursor rules, or the Zed equivalent). Do not expect the folder names alone to stop a tool.

---

## Limits

- This is a snapshot from 2026-11-20. A vendor can change a price the next day.
- Survey shares are "used in the past year" among people who answered that question. They are not market share, and they are not this class.
- Stars are not users. No download counts are stated in this note.
- Wholesale compute cost, when it is not on the vendor page, is written as not published. Do not invent it.
- No install in this check was run on a student laptop.

*technical suggestion:* for the semester, start with Hermes and the vault. Add OpenCode, Cline, or another coding agent when the task is a repository. Pick with the job table, not with the star count.
