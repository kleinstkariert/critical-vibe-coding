---
title: Vibe-coding tools and agent environments, late 2026
date: 2026-11-20
updated: 2026-11-23
tags:
  - research
  - tools
  - course
status: current
canonical: true
---

# Vibe-coding tools and agent environments, late 2026

This is the one course page that compares tools. Other pages link here. They do not copy it.

Original check: **2026-11-20**. Second check, on **2026-11-23**, covered these items only: GitHub stars, licences and activity for every repository named below; Cursor, Claude, GitHub Copilot and Zed prices and plan pages; the Zed AI pages; and the AgentCraft repository. Every other row is as read on 2026-11-20. It was not read again.

This page is a map for students who are new to these tools. Prices, model names and quotas change. Open the linked page before you pay. Dated claims about install guides and models are on [dated models, prices, limits and hardware](../../course/REFERENCES/dated-models-prices-limits-and-hardware.md).

Labels: *verified fact* | *claim* | *uncertainty* | *technical suggestion*. A label names the source kind. It is not independent verification. See [bibliography](../../course/REFERENCES/bibliography.md#source-types).

Web pages and README files were read as untrusted data. A statement on a vendor page is a *claim* unless this page says it was checked in another way.

This page does not replace the course how-tos:

- Job split (harness, coding agent, always-on assistant): [hermes vs coding agents](../../course/PRACTICE/01-harness-and-agents/hermes-vs-coding-agents.md)
- What a harness is: [what is harness](../../course/PRACTICE/01-harness-and-agents/what-is-harness.md)
- What MCP is: [what is mcp](../../course/PRACTICE/06-mcp-and-tools/what-is-mcp.md)
- Hermes install: [howto hermes setup](../../course/PRACTICE/01-harness-and-agents/howto-hermes-setup.md)
- OpenCode install: [howto opencode setup](../../course/PRACTICE/01-harness-and-agents/howto-opencode-setup.md)
- Pair Hermes with OpenCode: [howto hermes opencode pairing](../../course/PRACTICE/01-harness-and-agents/howto-hermes-opencode-pairing.md)
- Prompting: [Prompting Guide for Critical Vibe Coding](../../course/PRACTICE/03-models-and-providers/prompting-guide-for-critical-vibe-coding.md)

---

## Words used on this page

Many products fit more than one word. Use the job name first, then the product name.

| Word | Meaning here | Examples |
|---|---|---|
| Model | The trained weights. A lab, a gateway or your own computer serves them. | Claude, GPT, Gemini, Qwen, Nemotron |
| Model provider | The lab, gateway or host that serves a model and bills for it. | Anthropic, OpenAI, Google, OpenRouter, a local server |
| Agent | A model that works in a loop: it reads, calls tools, checks the result, and repeats. | Any tool below |
| Agent harness | The program around the model: loop, tools, permissions, memory and context handling. **Agent = model + harness.** | Hermes, Claude Code, OpenCode, Zed Agent |
| Assistant agent | A harness built for long-lived personal work: notes, chat channels, schedules, tools. | Hermes |
| Coding agent | A harness built for a code repository: it reads files, edits them, runs commands and shows a diff. | Claude Code, OpenCode, Codex CLI, Aider, Cline |
| Environment | Where the harness runs and where you meet it: an editor panel, a terminal, a sandbox, a cloud machine, a chat app, a game world. | VS Code, Zed, a terminal, Minecraft (AgentCraft) |
| Editor | The app where you read and edit files. Some editors have their own agent. Some host agents from other makers. | Cursor, VS Code, Zed |
| Orchestrator | A program that runs several agents and gives you one place to steer them. | AgentCraft |
| Protocol | A shared message format. **MCP** connects an agent to tools and data. **ACP** (Agent Client Protocol) connects an editor to an agent. They do different jobs. | MCP, ACP |
| Model access | How you reach the model: a lab subscription, your own API key, a gateway, a hosted plan from the tool maker, or local open weights. | See the money section |

Short form of the course position: [what is harness](../../course/PRACTICE/01-harness-and-agents/what-is-harness.md) defines the harness. [hermes vs coding agents](../../course/PRACTICE/01-harness-and-agents/hermes-vs-coding-agents.md) compares the job of an assistant with the job of a coding agent. This page adds the product facts.

---

## Four jobs

| Job | What you do there | Course examples |
|---|---|---|
| Editor coding | Files, tabs and an agent panel in one window | Cursor, VS Code, Continue, Cline, Devin Desktop (formerly Windsurf), Zed |
| Terminal repo work | An agent in a project folder. It edits files and runs commands | Claude Code, OpenCode, Codex CLI, Aider, Gemini CLI |
| Assistant and messaging | Notes, chat apps, tools, and work that can stay up | Hermes |
| Multi-agent front end | One place that plans, assigns and reviews work by several agents | AgentCraft |

*technical suggestion:* Hermes is the course default for the assistant job. Add a coding agent when a repository needs a deep edit. The pairing note above is the short version.

Zed is an editor. Hermes is not an editor. Claude Code is not an editor. AgentCraft is not an editor and not a harness of its own: it drives Claude and Codex engines.

---

## How money and popularity are counted

Four ways a student pays:

1. **Quota.** You pay $0 until a cap. The company that serves the model pays the compute. That compute cost is **not published**.
2. **Subscription.** You pay the tool company a monthly fee. The fee buys a cap. It does not buy unlimited compute. If the company is also the model lab, you pay the lab. If not, the tool company pays the lab. The lab's wholesale price is **not published**.
3. **Pass-through.** You pay token prices. Your own API key means the model lab bills you. Some tools add a fee on top of list price.
4. **Local.** You run open weights on your machine. You pay electricity and the computer. There is no token bill.

**Open source** means the program source is public under a named licence. The model is a separate product. An open tool can still send your code to a closed model.

**Reach** uses two sources only.

- *verified fact:* Stack Overflow Developer Survey 2026, question "AI coding agents". "Have you used any of the following coding agents or assistants in the past year?" Fielded 23 June 2026 to 5 August 2026. Published 6 October 2026. n = 12,255 people who answered. People could pick more than one tool, so the shares add up to more than 100%. https://survey.stackoverflow.co/2026/ai/data/ai-code-agent (read 2026-11-20, not read again)
- *verified fact:* GitHub stars below were read from the GitHub API on 2026-11-23. Stars are not users. This page does not give download counts.

If the survey question did not name the tool, the cell says **not in this question**. If no public source repository was found, stars say **not published**.

The survey is a Stack Overflow sample. It is not a sample of this class.

---

## Editors

| Tool | Licence | Open weights on your machine | Own API key | Reach | What you pay |
|---|---|---|---|---|---|
| Cursor | Proprietary. Source not public. | Localhost is not a supported path. | Yes, from Premium up. Plus and Free: no. | Survey 25.5% (3,127). Stars: not published. | Free limited. Plus $8, Premium $30, Super $100, Ultra $200 per month. |
| VS Code + Copilot | Editor source: MIT. Copilot: proprietary. | Yes, in chat (Ollama and others). | Yes, for chat. Completions stay on Copilot. | Copilot survey 58.7% (7,196). VS Code repo stars: 195,754. | Copilot Free $0. Student $0. Pro $10. Pro+ $39. Max $100 per month. |
| Continue | Apache-2.0 | Yes, if you configure it. | Yes | Survey 3.8% (466). Stars: 36,543. | The extension is free. You pay the provider you configure. |
| Cline | Apache-2.0 | Yes. Ollama and LM Studio are documented. | Yes | Survey 4.5% (551). Stars: 71,846. | Extension free. Optional Cline bill, or ClinePass $9.99 per month, or your own key. |
| Windsurf, now Devin Desktop | Proprietary | Not the built-in default. | Not confirmed on a current official page. | Survey still lists Windsurf 6.5% (796) and Devin 2.9% (360) as two rows. Stars: not published. | March 2026 list: Free $0, Pro $20, Max $200 per month. See the note. |
| Zed | Editor source is open. Mixed licence. See below. | Yes. Ollama and LM Studio are named on the pricing page. | Yes, on the free plan. | Survey: not in this question. Stars: 95,565. | Editor $0. Pro $10 per month, with $5 of hosted tokens. Business $30 per seat per month. |

### Cursor

*verified fact:* Cursor is sold as part of The X Subscription. The current individual prices, read on https://cursor.com/docs/models-and-pricing on 2026-11-20 and again on 2026-11-23, are Free $0, Plus $8, Premium $30, Super $100 and Ultra $200 per month, tax excluded. Older Pro, Pro+ and Ultra plans still exist as legacy plans.

Plus includes Cursor's models named Grok and Composer on that page. Plus does not include your own API key, and it does not include Claude, GPT or Gemini.

From Premium up, you can add your own key for OpenAI, Anthropic, Google, Azure or AWS Bedrock. The provider bills that key. Cursor's help page says the request still goes through Cursor's servers, and that tab completion stays on Cursor's models. https://cursor.com/help/models-and-usage/api-keys

*verified fact (Cursor staff on the forum):* an own-key model must be reachable from Cursor's servers. A model that only listens on localhost is not a supported path. https://forum.cursor.com/t/using-local-model-with-cursor/149366

Included Grok and Composer use a weekly pool. You pay Cursor. What Cursor pays to run those models is not published. Third-party models on individual Premium and above are billed at API list price from prepaid credit. You pay that list price to Cursor. What Cursor pays the model lab is not published. On Teams and Enterprise, eligible third-party requests also add a Cursor Token Rate of $0.25 per million tokens, including requests that use your own key. Individual plans do not pay that rate.

### VS Code with GitHub Copilot

*verified fact:* The source repository `microsoft/vscode` is MIT (195,754 stars on 2026-11-23). The Visual Studio Code application you download from Microsoft is under Microsoft's product terms. Copilot is a separate proprietary service.

Copilot plan prices, read on https://docs.github.com/en/copilot/get-started/plans on 2026-11-23 (the same as on 2026-11-20):

- Copilot Free: $0, an allowance of GitHub AI Credits, auto model selection only, 2,000 code completions per month.
- Copilot Student: $0 for a verified student, auto model selection only, and an allowance of AI Credits. The overview table does not print one credit total for Student. That number is not copied here.
- Copilot Pro $10, Pro+ $39, Max $100 per month. The plans page lists base credits of 1,000, 3,900 and 10,000, and total monthly credits of 1,500, 7,000 and 20,000.

On a Copilot plan, you pay GitHub (or $0). GitHub pays the model labs for included use. That wholesale cost is not published.

*verified fact:* VS Code chat can use your own key, or a local runtime such as Ollama, without a Copilot plan. The provider bills a cloud key. A local model has no token bill. Inline completions, semantic search and embeddings still need Copilot. https://code.visualstudio.com/blogs/2026/06/18/byok-vscode · https://code.visualstudio.com/docs/agent-customization/language-models (read 2026-11-20)

*uncertainty:* that language-models page marks a separate "local harness" as deprecated, with removal set for February 2027. Bring-your-own-key chat is a different switch. Read the page again if you set this up later.

### Continue

*verified fact:* `continuedev/continue` is Apache-2.0 (36,543 stars on 2026-11-23). The README says the repository is no longer actively maintained and is read-only, after a final 2.0.0 release. https://github.com/continuedev/continue

*uncertainty:* the repository showed a push on 2026-11-23 although the README says it is read-only. This check did not find out what the push contains.

The extension can point at your own key or at an OpenAI-compatible local server, including Ollama. You pay that provider. Continue does not sell the seats in the README. https://docs.continue.dev/customize/model-providers/top-level/openai (read 2026-11-20)

*technical suggestion:* keep an existing Continue setup if it already works. Do not start there if you need a project that still ships fixes. Cline is the maintained open extension in this table.

### Cline

*verified fact:* `cline/cline` is Apache-2.0 (71,846 stars on 2026-11-23). Docs read 2026-11-20: https://docs.cline.bot/getting-started/authorizing-with-cline

Three pay paths:

- Cline usage-billing. You pay Cline. Cline pays the model side. Any markup is not published on the page read here.
- ClinePass, $9.99 per month, optional, for a quota on selected open coding models. https://docs.cline.bot/getting-started/clinepass
- Your own key, or Ollama / LM Studio with no key. A cloud provider bills you. A local model has no token bill. https://docs.cline.bot/running-models-locally/overview

Job: editor agent, with a CLI as well. You approve steps.

### Windsurf, now Devin Desktop

*verified fact:* Cognition's FAQ says Windsurf became Devin Desktop on 2 June 2026. The FAQ says the IDE remains, and that plan prices did not change on that day. https://docs.devin.ai/desktop/devin-desktop-faq (read 2026-11-20)

*verified fact:* Cognition's pricing post of 18 March 2026 lists Free $0, Pro $20 per month, Teams $40 per seat per month and Max $200 per month. Included use is a quota. Extra use is billed at API price. https://devin.ai/blog/windsurf-pricing-plans

*uncertainty:* the 2026-11-20 check did not find a newer public price table dated after June 2026. Read the current Devin page before you pay.

The product is proprietary. A general "paste any API key" page was not in the rename FAQ. *uncertainty:* treat bring-your-own-key as not confirmed for the current Devin Desktop. The FAQ does say you can use the desktop with local-only agents, without Devin Cloud.

You pay Cognition for a paid plan. Cognition pays the model labs for included quota. That wholesale cost is not published. On extra use, the March post says you pay API price.

### Zed

Zed is a code editor from Zed Industries, written in Rust. It is an editor with its own agent (Zed Agent), and it also hosts agents from other makers. It is not a Hermes-style assistant. Sources read on 2026-11-23: https://zed.dev/ai · https://zed.dev/pricing · https://zed.dev/docs/ai/overview · https://zed.dev/docs/ai/external-agents · https://zed.dev/docs/ai/llm-providers · https://zed.dev/docs/account/plans-and-pricing · https://zed.dev/software-overview

**What the AI pages say (read on 2026-11-23)**

- *claim:* https://zed.dev/ai describes four agent features: agentic editing, real-time following of the agent through your codebase, review in an editable unified diff with accept or reject, and "any agent, any tool". The page says you can bring agents like Claude Agent, Codex or OpenCode through ACP, and connect MCP servers.
- *verified fact:* the docs overview names three agent paths. **Zed Agent** is Zed's own agent. It uses built-in tools, profiles, skills, instructions and MCP servers, and it can use Zed-hosted models, provider API keys, supported subscriptions, gateways and local models. **External Agents** run through their own process over ACP. **Terminal Threads** run a CLI or TUI agent inside a terminal-backed thread. The Threads Sidebar lets you run several agent threads at once, in different projects.
- *verified fact:* the External Agents page lists Claude, Codex, OpenCode, Copilot, Cursor and Pi Coding Agent as common agents. The same page has setup text for Gemini CLI and Poolside. It says the list is curated, not complete, and that you install agents from the ACP Registry.
- *verified fact:* the same page says an External Agent usually owns its model, provider settings, login, API keys and subscription. A key you set for Zed Agent does not configure Claude Agent or Codex. Zed does not charge for External Agents. Billing, terms, retention and data handling are between you and the agent maker. Zed MCP servers may be forwarded to the agent over ACP, and the agent may also read its own MCP settings.
- *claim:* the AI page says Zeta, Zed's edit prediction model, is open-weight and open-data, and that Zed, Zeta and ACP are open source. This check did not read the Zeta licence or the model files.
- *claim:* the AI page says Zed offers fine-grain tool permissions for what the agent may use. This check did not test them.
- *claim:* the AI page says Zed is written in Rust and renders at 120 fps. These are Zed's own figures.

**Model access (read on 2026-11-23)**

- *verified fact:* the pricing page says you can use your own API keys. It names Amazon Bedrock, Anthropic, GitHub Copilot, Deepseek, Google AI, LM Studio, Mistral, Ollama, OpenAI, OpenRouter and Vercel "and more". The docs list five model access paths: Zed-hosted models, API access, an existing subscription, a gateway, and a local model.
- *verified fact:* the AI page names Ollama for local models. The text on the page reads "Nothing leaves your machine". *uncertainty:* that statement covers Zed's own model path. An External Agent has its own network behaviour, and a hosted model leaves your machine by design.
- *verified fact:* the AI page names Claude Opus and GPT 5.4 as examples of Zed-hosted models. The pricing page names GPT-6 Luna for the trial, and the plans page names Claude Fable, Claude Opus, GPT-6 Astra, GPT-5.5 pro and GPT-5.4 pro as excluded from the Student plan. Model names on these three pages do not match. Treat every model name here as a snapshot.

**What you pay (read on 2026-11-23)**

- *verified fact:* Personal (the plans page calls it Free) is $0. It has no Zed-hosted models and no Zed edit predictions. You can use your own keys and External Agents. You do not need an account to edit code, and you can turn AI off.
- *verified fact:* Pro is $10 per month. It includes $5 of hosted tokens and unlimited edit predictions. Hosted use beyond $5 is billed at API list price plus 10%. You pay Zed the list price and the 10%. The default spend limit for Pro is $10 of extra tokens. A 14-day trial includes $5 of GPT-6 Luna and needs no credit card.
- *verified fact:* Business is $30 per seat per month. It adds org-wide AI policies, data controls, spend visibility and role-based access. SSO, SAML and SCIM are "planned but not currently available" on the pricing page.
- *verified fact:* the Student plan is free for one year for a verified university student. It has unlimited edit predictions and $10 per month of token credit. Student users cannot set a spend limit. The cap is the $10.
- Zed does not add its 10% on keys you bring yourself. The provider bills that key.

**Licence and maturity**

- *verified fact:* the source is public: https://github.com/zed-industries/zed (95,565 stars, 11,819 forks, last push 2026-11-23, 3,088 open issues). GitHub's licence field is `NOASSERTION` because the tree uses more than one licence.
- *verified fact:* most of the source is GPL-3.0-or-later. Components meant for reuse, such as `gpui`, are Apache-2.0. The app that Zed distributes, and Zed's hosted services, are also under Zed's Terms of Service. The open source licences cover the source. They do not cover the hosted model service by themselves. https://zed.dev/software-overview
- *verified fact:* the repository was created on 2021-02-20.

**Correction of the claim "free, fully open source, and lighter than Cursor or Claude Code"** (from the 2026-11-20 check, not read again)

- **Free:** true for the editor. False for hosted models and for Zed's edit predictions. Those are paid, with the student exception above.
- **Open source:** true for the editor source, under the mixed licence above. GPL-3.0 is copyleft. It is not a permissive licence.
- **Fully open source, under permissive licences:** Zed's compare page says that. The page was marked updated 1 May 2026: https://zed.dev/compare/vscode . The software overview does not say that. It names GPL-3.0-or-later for most of the source, and Terms of Service for Zed's services. The word "permissive" on the compare page is the claim this course does not repeat.
- **Lighter:** the same compare page is about VS Code, not about Cursor, and not about Claude Code. Zed's page states native Rust, startup under 1 second, about 600 MB of RAM, and memory use often 3 to 4 times lower than VS Code. Those figures are Zed's own claims. This page does not copy third-party RAM tables. Those tables do not agree with each other.
- A checked memory number for Zed versus Cursor is **not published** in a source used here. Cursor is a VS Code-family editor. Zed is a native Rust editor. This page does not turn that difference into a RAM figure.
- A checked memory number for Zed versus Claude Code is **not published**. Claude Code is a terminal agent. Zed can run it beside the editor. "Lighter than Claude Code" compares two different kinds of program.

*technical suggestion:* Zed is a fair choice for a student who wants an editor, and who wants to try several agents in one window without a Cursor plan. Choose the agent first. Then check who bills it.

---

## Terminal coding agents

| Tool | Licence | Open weights | Own API key | Reach | What you pay |
|---|---|---|---|---|---|
| Claude Code | Proprietary. All rights reserved. | Not an Anthropic feature. See the note. | Yes. A set API key replaces the subscription for billing. | Survey 65.5% (8,030). | Paid Claude plans. Pro $20 per month, or $17 per month billed yearly. Max $100. Ultra $200. Or API rates. |
| OpenCode | MIT | Yes. The product page says you can connect local models. | Yes | Survey row "Open Code" 13.6% (1,662). Stars: 228,765. | The tool is free. Other providers can cost money. |
| Codex CLI | Apache-2.0 for the client | Yes. `codex --oss` with Ollama or LM Studio. | Yes. API-key use is a separate bill. | Survey "OpenAI Codex" 29.5% (3,620). Stars: 136,234. | Included in ChatGPT plans, limits vary. Or API rates. |
| Aider | Apache-2.0 | Yes. Ollama is documented. | Yes | Survey 2.1% (256). Stars: 50,228. | The CLI has no priced plan in this check. You pay the provider, or $0 for a local model. |
| Gemini CLI | Apache-2.0 | Not the product. | Yes, a paid Gemini API key or Vertex. | Survey: not in this question under this name. Stars: 109,023. | Individual free login ended 18 June 2026. See Antigravity. |

### Claude Code

*verified fact:* Claude Code is Anthropic's terminal coding agent. The public repository https://github.com/anthropics/claude-code (156,796 stars on 2026-11-23) is not an open-source release of the agent. `LICENSE.md` says all rights reserved and points at Anthropic's commercial terms (read 2026-11-20). GitHub shows no licence for the repository on 2026-11-23.

Prices read on https://claude.com/pricing on 2026-11-23: Pro is $20 per month, or $17 per month if you pay $200 up front for a year. Max is $100 per month. Ultra is $200 per month. Claude Code is included in the paid plans and shares the plan's use caps (Free has no Claude Code on that page). Max now lists $100 per month of API credits, and Ultra $200. Pro can use the top Fable model only with paid usage credits. https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-max-or-ultra-plan (read 2026-11-20)

You pay Anthropic. Anthropic is the model lab. Anthropic's own compute cost is not published. If `ANTHROPIC_API_KEY` is set, Claude Code bills the API, not the subscription. API rates are pass-through to Anthropic.

*uncertainty:* Ollama documents a local connection by pointing Claude Code at Ollama's Anthropic-compatible URL. https://docs.ollama.com/integrations/claude-code (read 2026-11-20). That page is Ollama's, not Anthropic's. This check did not confirm that Anthropic's terms allow that path. Do not treat it as an official open-weight mode.

Job: terminal repo work. It is the strongest "used in the past year" row in the survey above.

### OpenCode

*verified fact:* `anomalyco/opencode` is MIT (228,765 stars on 2026-11-23, default branch `dev`). The product page says the tool is free, that some models are free without an account, that you can connect local models, and that you can connect OpenAI, Anthropic, xAI and other providers. It also says ChatGPT Plus or Pro, and GitHub Copilot, can be used as logins. https://opencode.ai/product (read 2026-11-20)

On a free OpenCode model, OpenCode says it stores data. On your own provider, that provider bills you and OpenCode's product page says the tool itself is free. What a connected lab charges is that lab's price.

*uncertainty:* the survey row is spelled "Open Code". This page reads that row as this project. The survey page does not link the row to the GitHub repository.

*uncertainty:* a docs file on the Git branch `dev`, not on `main`, describes optional plans named Go ($10 per month), Go Plus ($40) and Go Teams ($20 per member). The product FAQ quoted above does not list those prices. Check https://opencode.ai before you subscribe to anything beyond the free tool.

Job: repo coding in the terminal, and also a desktop app. Course install: [howto opencode setup](../../course/PRACTICE/01-harness-and-agents/howto-opencode-setup.md).

### Codex CLI

*verified fact:* `openai/codex` is Apache-2.0 (136,234 stars on 2026-11-23). You can sign in with a ChatGPT plan, or use an API key. API-key sessions use API prices and do not draw the ChatGPT allowance. https://chatgpt.com/codex/pricing/ says Codex is included in ChatGPT Free, Go, Plus, Pro, Business and Enterprise. The help page https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan says the same inclusion, including Free and Go, with limits that depend on the plan. (read 2026-11-20)

*verified fact:* `codex --oss` uses a local provider. The CLI docs name Ollama and LM Studio. https://learn.chatgpt.com/docs/cli/reference.md · https://learn.chatgpt.com/docs/config-file/config-advanced

*verified fact (pricing page read via search extract 2026-11-20):* https://learn.chatgpt.com/docs/pricing lists Pro at $100, $200 or $500 per month. This note does not copy every other plan's dollar price. Open the page.

On a ChatGPT plan, you pay OpenAI the plan fee (or $0 on Free, inside the cap). OpenAI is the model lab. On an API key, you pay OpenAI's API rates. On `--oss`, you pay the local machine.

*uncertainty:* the survey row "OpenAI Codex" includes more than the CLI. Do not read 29.5% as "CLI only".

### Aider

*verified fact:* `Aider-AI/aider` is Apache-2.0 (50,228 stars on 2026-11-23). The default branch last showed a push on 2026-05-22, the same as on 2026-11-20. That is slower public activity than the other CLIs in this list. It is still a real project.

Ollama setup: https://aider.chat/docs/llms/ollama.html

This check did not find a priced Aider subscription. You pay the model provider for a cloud key. A local model has no token bill. Survey reach is 2.1%.

Job: terminal pair programming on a git repo.

### Gemini CLI

*verified fact:* `google-gemini/gemini-cli` is Apache-2.0 (109,023 stars on 2026-11-23). From 18 June 2026, individual free accounts and Google AI Pro / Ultra no longer get answers from this CLI. Google tells those people to use Antigravity CLI. Enterprise Gemini Code Assist, and paid Gemini API or Vertex keys, stay on Gemini CLI. https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ · the README in the repository. (read 2026-11-20)

A paid API key is pass-through: you pay Google. Open weights are not the Gemini CLI product.

The survey has a row "Gemini Code Assist" at 14.6% (1,789). That row is not this CLI. This CLI's survey cell is **not in this question**.

---

## One more tool students meet: Google Antigravity

Antigravity is Google's agent product (app, CLI and IDE extensions). It is the individual successor to Gemini CLI, so it belongs on this map. It is proprietary. No public source repository was found on 2026-11-20. Stars: **not published**. Survey: 16.0% (1,956).

*verified fact:* the plans page says there is no bring-your-own-key and no bring-your-own-endpoint for extra rate. Accounts that are not on Google AI Pro or Ultra get a weekly quota. Pro and Ultra get higher quotas. Dollar prices for Pro and Ultra are not on that page. https://antigravity.google/docs/plans/ (read 2026-11-20)

You pay $0 inside the free quota. Google pays the compute. That cost is not published. Pro and Ultra overage can use AI credits at "standard Gemini Enterprise consumption pricing". You pay Google for those credits.

*verified fact:* local models are documented for the Antigravity **SDK** (on-device LiteRT, or an OpenAI-compatible server such as Ollama). https://antigravity.google/docs/sdk/local-models/ That is a developer library. It is not the same switch as the signed-in CLI, which rejects bring-your-own-key on the plans page.

---

## Multi-agent front end: AgentCraft

AgentCraft is a different kind of tool. It does not edit code itself, and it is not an editor. It is a front end that lets you steer a team of coding agents inside a Minecraft world. Sources read on 2026-11-23: https://github.com/blendi-remade/agentcraft (repository metadata, `README.md`, `foreman/README.md`, `LICENSE`, commit list through the GitHub API).

**What it is**

- *claim (README):* "A team of Claude agents doing real work on your code, inside a Minecraft studio you can walk around in." You type a goal. A lead agent reads your repository, writes a plan and pins tasks to a wall. Workers code in their own git worktrees. You review a real diff and press **Merge**.
- *verified fact (foreman README):* the system has two parts. The **Foreman** is a Node 22 and TypeScript service. It runs the agents and owns all state: tasks, messages, shared memory, decisions and worktrees. The **mod** is a Fabric mod for Minecraft that draws what the Foreman knows. They talk over a WebSocket on `127.0.0.1`. The game is only a view, and the agents keep working when Minecraft is closed.
- Job in this page's words: an **orchestrator with a game interface**. The agents themselves run on two engines made by others: the Claude Agent SDK and a Codex app server. AgentCraft has its own team rules, task graph and merge policy around them.

**Model and provider support**

- *verified fact (README):* the Claude engine needs an `ANTHROPIC_API_KEY`, or Amazon Bedrock, Google Vertex AI or Microsoft Foundry through the Agent SDK. The README also offers a login with your own `claude` CLI. It says Anthropic does not allow third-party tools to offer a claude.ai login, so that option is off by default and meant for running the tool yourself.
- *verified fact (README):* a Codex engine runs agents through the Codex CLI or app, logged in with ChatGPT or an OpenAI API key. You can build an all-Codex team, an all-Claude team, or a mixed team, per agent.
- *verified fact (foreman README):* defaults are `opus` for the lead and `sonnet` for the workers. The tool accepts any model id or alias that the Claude CLI accepts. For Codex it passes model names to Codex.
- *uncertainty:* the two README files name no local, open-weight or other provider path. This check did not search the source code. Do not read this as proof that none exists.
- *claim (README):* the Claude backend bills per token to your Anthropic or cloud account. The author reports about $6 in total for three two-task goals on a sample repository, with a cheaper setting. This is one run by one person. Codex agents use your Codex plan or your OpenAI API key.

**Licence and maturity**

- *verified fact:* MIT licence. The licence text reads "Copyright (c) 2026 AgentCraft contributors". The README says the art is generated by scripts and is under the same licence. Minecraft is not included, and you need your own copy of Minecraft: Java Edition. The README says the project is not affiliated with Mojang, Microsoft or Anthropic.
- *verified fact (GitHub API, 2026-11-23):* repository created 2026-10-03. Last push 2026-10-08, so about 46 days without a push on the day of the check. 1,026 stars, 133 forks, 22 open issues. No published releases. More than 90 commits (GitHub lists four pages of 30), from at least seven author names. Some author names are agent names, such as "AgentCraft Juniper". The README says agents commit under that style of name.
- *uncertainty:* another read of the repository page showed 0 stars and 0 forks. This page uses the API values. Stars are not users.
- *verified fact (README, "Status"):* "AgentCraft is young and has been used by one person on one machine." It runs in singleplayer, one studio per world, on Minecraft 26.3, through the development client (`gradlew runClient`). A regular mod release for normal launchers is "planned". The README says macOS was tested on Apple Silicon only. The "Status" text names Windows and macOS launchers, while the quick start also shows Linux steps.
- *uncertainty:* the README test badge says 548 passing tests. The text of the same README says 482 tests. This check ran no tests.

**Safety claims**

- *claim (README and foreman README):* every task runs in its own git worktree. Nothing merges without your click. Agents never push, and the tool blocks git network access through git settings, not only a command filter. Risky commands become in-game permission prompts.
- *verified fact (foreman README):* the document itself says the git block "is not a sandbox", because code an agent runs could drop the variables on purpose. This check did not test any of these controls.
- *technical suggestion:* treat AgentCraft as a design example for the question "what does an interface for several agents look like". It fits [Session 06, agent as interface](../../course/SESSIONS/06-agent-as-interface.md). It is not a recommended install for this course. It needs Java 25, Node 22, Minecraft: Java Edition and paid model access.

---

## Hermes (course harness)

Hermes Agent is the course runtime. It is not an editor. It talks to tools, a vault and chat channels. It can edit code. The course does not use it as the deepest repo coder. Read [hermes vs coding agents](../../course/PRACTICE/01-harness-and-agents/hermes-vs-coding-agents.md) for that split.

| | |
|---|---|
| Licence | *verified fact:* MIT. `NousResearch/hermes-agent`. 265,610 stars on 2026-11-23. FAQ: https://hermes-agent.nousresearch.com/docs/reference/faq (read 2026-11-20) |
| Open weights | *verified fact:* yes. Custom endpoint (Ollama and others) and a managed Local Models path. https://hermes-agent.nousresearch.com/docs/user-guide/local-models |
| Own API key | *verified fact:* yes. OpenRouter, OpenAI, Anthropic, Google and other providers. |
| Job | Assistant, messaging, vault, and optional always-on hosting. Not an editor session. |
| Reach | Survey: **not in this question**. Stars: 265,610. |
| Price | The software is free. Your provider bills your key. A local model has no token bill. |

Optional Nous Portal, read on https://hermes-agent.nousresearch.com/ on 2026-11-20: Free is pay as you go on free models. Plus is $20 per month. Super is $100. Ultra is $200. Paid tiers add hosted tools and one cloud agent. You pay Nous. Nous pays the model labs for Portal use. That wholesale cost is not published. You can leave Portal and use your own key on the same install.

---

## Does the starter vault still fit these tools?

The install notes use a Wanderloots-style tree: `SCHEMA.md`, `index.md`, `log.md`, `raw/`, `wiki/` and `private/`. The written starter is [starter knowledge base](../../course/PRACTICE/02-knowledge-bases/starter-knowledge-base.md). The same three layers (sources, wiki pages, schema) are already in [karpathy llm wiki and openclaw](karpathy-llm-wiki-and-openclaw.md) and [llm wiki standard files](../../course/PRACTICE/02-knowledge-bases/llm-wiki-standard-files.md).

**Tool-agnostic, and still right for every tool in this list**

- The notes are files in a folder. Every editor and every terminal agent can read a folder.
- `raw/` holds sources you add. `wiki/` holds pages an agent may rewrite. That split is a writing rule. It does not depend on Hermes.
- `SCHEMA.md` is the contract: what the agent may read, what it may write, and what it must leave alone. The idea fits every tool. The file does nothing until that tool is told to read it.
- Secrets stay out of the vault. That includes `private/`. API keys live in the tool's own secret store or in an un-synced `.env`. A folder name is not a lock. This rule is for Cursor, Zed, Claude Code, AgentCraft and Hermes alike.

**Hermes-specific**

- `WIKI_PATH`, the bundled llm-wiki skill and the gateway.
- Hermes can be asked to keep `index.md` and `log.md` in step with the wiki. The other tools will not do that unless you ask in their own session.
- Chat channels and a cloud agent while the laptop is closed are Hermes jobs (or a hosted product such as Nous Portal). An editor does not become that assistant because it can see the same folder.

*technical suggestion:* keep this tree if you want one vault for the semester. Point Hermes at the vault. Point a coding agent at the code repository. Copy the access rules into the rules file that the coding tool actually reads (`AGENTS.md`, `CLAUDE.md`, Cursor rules or the Zed equivalent). Do not expect the folder names alone to stop a tool.

---

## Limits

- This is a snapshot. A vendor can change a price the next day. The rows are dated in the text.
- Survey shares are "used in the past year" among people who answered that question. They are not market share, and they are not this class.
- Stars are not users. No download counts are stated in this note.
- Wholesale compute cost, when it is not on the vendor page, is written as not published. Do not invent it.
- No install in these checks was run on a student laptop. No AgentCraft or Zed feature was run.

*technical suggestion:* for the semester, start with Hermes and the vault. Add OpenCode, Cline, Zed with an external agent, or another coding agent when the task is a repository. Pick with the job table, not with the star count.
