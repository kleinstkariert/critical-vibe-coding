---
title: Session 02. Agent harness and Hermes
session: 2
format: obsidian-slides
slot: 10:00 to 12:00
css: cvc-slides
---

# Session 02
## Agent harness and Hermes

Critical Vibe Coding · 10:00(15) to 12:00(15)

This deck teaches the setup path for today. You can follow it without other notes open. Links at the end point to full how-tos.

*demonstration. Optional extension. Not required for assessment.* Any one agent plus one folder meets [[minimum-path]].

---

# Today

|Time|Activity|
|---|---|
|10:00–10:20|Check-in|
|10:20–10:35|Student input: flattening|
|10:35–10:55|Harness and LLM Wiki|
|10:55–11:05|Break|
|11:05–11:15|Model landscape|
|11:15–12:00|Hermes installation and smoke test|

Today has two aims:

- Understand how a model becomes a useful agent.
- Start a safe Hermes setup.

Full guides: [[howto-hermes-setup]] · [[Local LLM Coding with Hermes]]

---
# Critical Vibe Coding

An AI system can read files, call tools, and change projects.

This creates useful possibilities.

It also creates risks.

Use this working method:

- Define the task.
- Limit access.
- Check the result & review the effect.
- Keep human control.
---


> The model contains the intelligence.
> The **harness** makes that intelligence useful.
>
> If you're not the model, you're the harness.

LangChain, *Anatomy of an Agent Harness* (2026)

In plain words: the model predicts text. The harness is everything around it that makes that text able to act in the world.

---

# What is a harness?

A **harness** is the software and rules around a model.

It gives the model useful context and controlled actions.

A harness can provide:

- Project files.
- Tools.
- Memory.
- Skills.
- Project rules.
- Sandboxes.
- Tests.
- Approval steps.
- Logs.

`Model + harness = agent system`

Course note: [[what-is-harness]]

---

# Thin harness vs thick harness

| Kind | What you get | Example |
|---|---|---|
| **Thin harness** | Chat window + message history | Simple ChatGPT-style UI |
| **Thick harness** | Files, tools, skills, sandbox, checks, memory | Hermes, Cursor Agent, Claude Code |

Hermes is a thick harness. Cursor Agent and Claude Code are also thick harnesses, built more for IDE coding.
They focus on different workflows.

---

# Harness design

1. Start with the required behaviour.
2. Then choose the required controls.

| Required behaviour      | Harness component             |
| ----------------------- | ----------------------------- |
| Store project knowledge | Files, memory, or wiki        |
| Read project files      | File tools and permissions    |
| Change project files    | Write access and scope limits |
| Run software            | Terminal or application tools |
| Use another application | MCP or another integration    |
| Limit damage            | Sandbox, docker and allowlist |
| Check results           | Tests, logs, and review       |
| Work across sessions    | Persistent files and memory   |
| Ask before danger       | Approval rules                |

A harness defines what the agent can do.

It also defines what the agent cannot do.

---
# Suggested harness flow

[User]  The user defines the task.
↓ 
[Hermes]  Agent interface
↓ 
[Rules and skills]  The harness manages access and actions.
↓ 
[Selected model]  The model produces responses and tool requests.
↓ 
[Files and tools]  MCPs
↓ 
[Verification]  Verification checks the result. (user in the loop?)
↓ 
[Creative or technical result] 


---

# Why structure matters

A stronger model can improve results.
A clear structure can also improve results.

The agent needs:

- Relevant context.
- Clear project rules.
- Correct files.
- Useful tools.
- Good feedback.
- Reliable checks.

A larger model cannot repair missing project information.
A smaller model cannot solve every difficult task.
Use model quality and harness quality together.

---

# LLM Wiki

An LLM Wiki is a structured collection of project information.
It gives the agent stable project knowledge.
It is not only a collection of chat messages.

It can contain:

- Project rules.
- Concepts.
- Sources.
- Decisions.
- Comparisons.
- Questions.
- Task records.
- Known errors.

Give the agent only the relevant information.
Do not give it the complete vault by default.

[[llm-wiki-standard-files]] · [[knowledge-store-options]]

---

# Wiki structure

```text
vault/
├── SCHEMA.md
├── index.md
├── log.md
├── raw/
├── entities/
├── concepts/
├── comparisons/
└── queries/
```

[[llm-wiki-standard-files]]

---

# File roles

**SCHEMA.md:** Rules for structure and use.
**index.md:** Map of important content.
**log.md:** Record of events and changes.
**raw/:** Original source material.
**entities/:** People, tools, groups, or places.
**concepts/:** Ideas and definitions.
**comparisons/:** Structured comparisons.
**queries/:** Research questions and tasks.

[[llm-wiki-standard-files]]

---

# Obsidian and the LLM Wiki

Obsidian displays and edits the files.
The agent does not need Obsidian to be open.
The agent can work with the files directly.

Use Obsidian for:

- Reading.
- Editing.
- Linking.
- Reviewing.
- Teaching.
- Human decisions.

Use the LLM Wiki for:

- Stable project knowledge.
- Agent context.
- Searchable records.
- Repeated procedures.

These tools organise information.
They do not replace operating-system permissions or sandboxing.

[[howto-obsidian-setup-and-sync]] · [[llm-wiki-standard-files]] · [[knowledge-store-options]]

---

# Hermes

**Hermes Agent** is an open-source agent from Nous Research (MIT licence).

It can:

- talk to many model providers (cloud or local)
- use the terminal and files
- load **skills**
- keep memory across sessions
- run commands in sandboxes
- connect to messaging apps
- multipurpose tool, depends highly on users settings

**Hermes Desktop** is a native app UI for the **same** agent. It feels closer to Cursor or Claude Cowork than a raw terminal.

Install: [[howto-hermes-setup]] · Desktop: https://hermes-agent.nousresearch.com/desktop

---

# Hermes and OpenCode

Hermes is a **multipurpose** tool. It is strong for **24/7 assist** and **MCP** work.

For **deep repo development**, a coding agent is better. **OpenCode** is the open-source coding agent that fills that gap.

Use them together: plan and stay connected in Hermes. Hand hard coding work to OpenCode. Bring results back.

- OpenCode setup: [[howto-opencode-setup]]
- Pairing: [[howto-hermes-opencode-pairing]]

---

# Suggested basic setup

Default stack:

1. **Obsidian** vault for notes (phone sync).
2. **Hermes** on the computer as the agent.
3. Optional **MCP** later for apps such as CAD / 3D / creative tools.
4. Optional **Code agents** (like Claude Code) when a large coding repo needs a stronger IDE loop.

Comparison: [[hermes-vs-coding-agents]]

---

# Skills

A **skill** is a reusable instruction package. Usually a folder with a `SKILL.md` file.

Hermes loads a skill when the task needs it. That saves tokens. The agent does not load every procedure into every chat.

Examples of skill topics: verified coding, wiki lint, research, deploy steps.

Browse skills: `/skills` or `hermes skills list`  
Install: `hermes skills install …`  
Guide: https://hermes-agent.nousresearch.com/docs/guides/work-with-skills · [[howto-hermes-efficient-coding]]

---

# Skills: safety before install

Skills can include scripts and commands. Treat a third-party skill as untrusted code.

**Check Skills Guards** and review the skill files before you install.

Better workflow for class:

1. Ask the agent to **read** the skill.
2. Ask for a short **summary** of what it does and what it can change.
3. Prefer a **personal skill** the agent writes for your case, if that is enough.
4. Only then install a third-party skill if you still need it.

**Do not install a skill you did not understand!**

---

# Project rules: AGENTS.md

`AGENTS.md` is a file at the root of a project. Hermes loads it as standing orders.

It tells the agent:

- which folders it may edit
- which commands to run after changes
- what it must never touch (secrets, private notes)

Course template: [[agents-md-template]]  
Course repo example: root `AGENTS.md`

For a wiki, you may also use `SCHEMA.md`. Same job: standing rules on disk.

---

# Security (defaults + laptop)

An agent with terminal access can delete files, leak keys, or install bad packages.

Minimum course rules:

1. Do not run the agent as administrator / root.
2. Do not expose the messaging gateway to the public internet.
3. Prefer Docker or another sandbox for untrusted work.
4. Mount only the folders the task needs.
5. **Keep API keys in Hermes `.env`, never in synced vault notes.**
6. Require approval for destructive commands.
7. Review the Git diff before you accept work.

Overview: [[Local LLM Coding with Hermes]]  
Docs: https://hermes-agent.nousresearch.com/docs/user-guide/security

---

# Security: local is not enough

**Local model** means the prompt can stay on your machine.

It does **not** mean the agent is safe.

Risks that remain on a local setup:

- the agent still runs commands as your user
- a bad skill can still read files
- a prompt in a web page can still try to steer the agent
- sync tools can still copy secrets if you put them in notes

Local inference mainly reduces the risk of sending code to a cloud model provider. You still need approvals and folder limits.

---

# Docker sandbox

Docker runs software inside a container.

A container is a restricted process environment. It can limit files, network, processes, CPU, memory, and user permissions.

Docker does not provide perfect security.

Use it with limited mounts, non-root users, and network controls.

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/docker  
[[howto-hermes-docker-sandbox]] · [[Local LLM Coding with Hermes]] · [[howto-hermes-setup]]

---

# Break · 5 minutes

Pause here.

After the break: where Hermes can run, which models exist, keys, chat apps, then install practice.

---

# Where Hermes can run

Hermes is software you install. It can run in more than one place.

Main options for this course:

1. **Your laptop** (class default for most students)
2. **A desktop or small server at home**
3. **A hosted server you rent** (VPS)
4. **Hermes Cloud / hosted agent** (Nous Portal paid options)

The next slides say what changes for security, data, and local models in each place.

Laptop guide: https://hermes-agent.nousresearch.com/docs/guides/secure-hermes-on-a-work-machine

---

# Run location: your laptop

**What it is:** Hermes Desktop or CLI on the machine you carry.

**Good for:** class install, daily notes, light agent work, learning the stack.

**Data:** notes stay in your Obsidian vault on disk (then sync to phone). Cloud models still receive prompts if you choose a cloud provider.

**Local models:** possible if the laptop has enough memory. Often slow on small machines.

**Security watch:** battery, heat, always-on gateway, sync fights, no isolation on the default local backend.

---

# Run location: home desktop or server

**What it is:** a PC that stays on at home, or a mini PC / NAS-style box.

**Good for:** heavier local models, longer jobs, keeping the laptop light.

**Data:** you can keep vault + models on that machine. Phone still syncs notes through Obsidian, not through Hermes.

**Local models:** usually better than a thin laptop if you have more RAM / GPU.

**Security watch:** home network exposure, backups, who can reach the gateway, physical access at home.

---

# Run location: hosted server (VPS)

**What it is:** a Linux server you rent in a data centre. You install Hermes there.

**Good for:** always-on messaging gateway, work that should continue when your laptop sleeps.

**Data:** files on the VPS are under that provider’s physical control. Encrypt and limit what you store.

**Local models:** only if the VPS has a suitable GPU / enough RAM. Many cheap VPS boxes are CPU-only and weak for big local models.

**Security watch:** public IP, firewall, SSH keys, gateway allowlists. Do not leave open ports you do not need.

---

# Run location: Hermes Cloud / hosted agent

**What it is:** Nous can host an always-on Hermes agent (paid Portal plans; check current docs).

**Good for:** 24/7 agent without your laptop on.

**Data:** prompts and files that the hosted agent sees go through that hosted environment. Read the current Portal / Cloud privacy terms before you send private work.

**Local models:** not the point of Cloud. Use Cloud when you accept hosted inference / hosted runtime.

**Security watch:** account access, which channels you connect, what folders you sync or mount.

Compare products: https://hermes-agent.nousresearch.com/compare

---

# Personal laptop

If your main machine is a laptop, treat these as standing checks:

1. If the provider is cloud, your code and notes in the prompt leave the machine.
2. The default **local** command backend has **no** isolation.
3. An always-on messaging gateway is an attack surface. Use allowlists.
4. Watch battery, heat, disk space for models, and Obsidian sync conflicts.
5. Keep private notes out of agent-writable folders.

Obsidian sync: [[howto-obsidian-setup-and-sync]]  
Secure machine guide: Hermes docs (link above)

---

# What models exist

A **model provider** is the service or program that runs the model.

| Path | What it means for you |
|---|---|
| **Proprietary cloud** | Strong agents, you pay, prompts leave your machine (OpenAI, Anthropic, Google, …) |
| **Open weights, hosted** | Weights are public, but a host still runs them (example: free Nemotron on OpenRouter) |
| **Local** | The model runs on your hardware. More privacy for the prompt. Needs enough memory. |
| **Academic AU chat** | Campus chat UIs often have **no** agent API key. Do not expect Hermes to “just use” them. |

Honesty note: [[academic-ai-austria]]

---

# What a model can do for agents

For Hermes agent work, prefer models that:

1. Support **tool calling** (the model can request tools in a structured way).
2. Have a large **context window** (Hermes docs often want about 64 000 tokens or more for agent work).
3. Follow instructions about project rules.

A clever chat model that cannot call tools well will feel broken inside Hermes.

Session 03 goes deeper into hardware and prompting but also into the universe of models.

---

# Local models in Hermes

**Local model** means inference runs on your machine (or your home server).

Ways to attach a local model to Hermes:

1. Hermes Desktop → Providers → **Local Models** (managed runtime).
2. **Ollama** as an OpenAI-compatible server at `http://localhost:11434/v1`.
3. **llama.cpp**, **vLLM**, or **LM Studio** with a local endpoint.

You still need tool calling and enough context. Small laptops may only handle small models.

Hardware cheat sheet: [[howto-local-llm-hardware]]  
Docs: https://hermes-agent.nousresearch.com/docs/user-guide/local-models

---

# Subscription / API key

Hermes Agent is free and open source. **Model use** is separate. You need a provider.

Fast path:

```text
hermes setup --portal
```

Or pick a provider in the UI / with `hermes model` (OpenRouter, Anthropic, OpenAI, Google, local, …).

**Class free smoke test:** OpenRouter model `nvidia/nemotron-3-ultra-550b-a55b:free`

Put keys only in Hermes `.env` (Windows: `%LOCALAPPDATA%\hermes\.env`). Never put keys in the vault.

---

# Free model limits

The free OpenRouter Nemotron path is for learning and a short smoke test.

Limits on a free account are low (rate and daily caps change; check OpenRouter). Free hosts may log prompts.

**Do not send private artwork notes or secrets through a free cloud path until you accept that risk.**

Fallback: Nous Portal free models via `hermes setup --portal`, or your own paid key, or a local model.

Details: [[howto-hermes-setup]]

---

# Connect chat

Hermes can talk on messaging apps through the **gateway**.

```text
hermes gateway setup
```

| Platform | Notes |
|---|---|
| Telegram | Common class path; bot token + allowlist |
| Discord | Bot in a server or DM; allowlist users |
| Matrix | Federated chat; good open option |
| **Signal** | **Yes**, via a local `signal-cli` HTTP daemon |

Always restrict who can message the agent. Pairing / allowlists are mandatory on a personal machine.

Docs: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/

---

# Chat apps: 

Messaging is optional for Session 02 install.

If you enable it later:

1. The gateway process must stay reachable.
2. Unknown senders must not get free access.
3. The agent on chat can still use tools on the host. Treat chat as remote control.
4. Signal needs extra local software (`signal-cli`). It is more work than Telegram.

Full phone + Discord practice sits in Session 05. Today: know that the path exists.

---

# Vault path vs AgentShare

Two different layers:

| Layer | Class default | Hardening |
|---|---|---|
| Hermes `.env` | Point `OBSIDIAN_VAULT_PATH` / `WIKI_PATH` at your vault or `wiki/` | Later narrow to agent-writable folders only |
| Docker mounts | Often unused on day one | Overview says mount only `AgentShare/`, never private folders |

Class smoke test uses the vault path in `.env`. Container mount rules are extra isolation for untrusted work.

[[howto-hermes-setup]] · [[Local LLM Coding with Hermes]]

---

# Install order

1. Install **Hermes Desktop** (or CLI if Desktop is not available).
2. Configure a **model** (Portal, OpenRouter free path, or your key).
3. Set **absolute** vault paths in Hermes `.env`.
4. Open Hermes + Obsidian. Ask Hermes to create one test note in an agreed folder.
5. Confirm the note appears in Obsidian.

If install runs long, finish as homework. Draw Model / Harness / Wiki on paper if the machine fails.

[[howto-hermes-setup]]

---

# Practical · Homework

**In class:** install Hermes Desktop or CLI → model/key → vault path → one smoke-test note.

**Homework:**

1. Finish the install if needed.
2. Draw one diagram: Model / Harness / Wiki folders.
3. Skim the Karpathy LLM Wiki gist **or** the LangChain harness article.
4. Optional: copy [[agents-md-template]] into a personal project as `AGENTS.md`.

[[howto-hermes-setup]] · [[howto-hermes-efficient-coding]] · [[agents-md-template]]

---

# References

- [[Local LLM Coding with Hermes]] · [[howto-hermes-setup]] · [[howto-hermes-efficient-coding]]
- [[what-is-harness]] · [[what-is-mcp]] · [[academic-ai-austria]] · [[howto-local-llm-hardware]]
- Karpathy LLM Wiki gist · LangChain harness anatomy
- Session: [[02-agent-harness-and-wiki-architecture]]
- Comparison: [[hermes-vs-coding-agents]] · OpenCode: [[howto-opencode-setup]] · [[howto-hermes-opencode-pairing]]
- Desktop: https://hermes-agent.nousresearch.com/desktop
- CSS: `cvc-slides.css` (vault snippet)
