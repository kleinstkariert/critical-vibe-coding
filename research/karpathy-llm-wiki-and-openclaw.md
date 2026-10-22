# Karpathy LLM Wiki — still current? vs human wiki / OpenClaw

Research date: 2026-10-15. Labels: *requirement* | *verified fact* | *technical suggestion* | *anecdote*.

## Question

1. Does Andrej Karpathy’s LLM Wiki approach still stand, and is it still up to date?
2. A friend prefers a more **human-readable wiki** they use themselves, and uses **OpenClaw**, which feels more like a **distributor** than a single “self-learning personal agent” in the middle. How do these relate?

## Short answers

| Question | Answer |
|---|---|
| Does Karpathy’s idea still stand? | **Yes.** The April 2026 gist is still the reference; tools and plugins still implement it. The idea makes sense for the scale he describes. |
| Is it “the only” wiki approach? | **No.** A human-authored wiki (or a hybrid) is a different design choice, not a failed Karpathy setup. |
| OpenClaw vs Karpathy? | OpenClaw is primarily a **gateway / router** (channels → one or many agents). It *can* run a Memory Wiki that is related to Karpathy’s pattern, but with stronger machine-managed blocks *and* reserved space for human notes. The “distributor” feel matches OpenClaw’s multi-agent routing docs. |

## What Karpathy’s approach is

*verified fact:* Gist `llm-wiki.md`, dated **4 April 2026**: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Core idea (from the gist, paraphrased carefully):

- **Raw sources** stay immutable.
- An LLM **writes and maintains** a wiki of markdown files (summaries, entities, concepts).
- A **schema** file (`CLAUDE.md` / `AGENTS.md`) tells the agent how to ingest, query, lint.
- You mostly **source and ask**; the agent does filing and cross-linking.
- Obsidian (or any editor) is the **viewer / IDE**; the wiki is “just a git repo of markdown.”
- At moderate scale (~100 sources, hundreds of pages), an `index.md` can replace a vector/RAG store.

Famous line from the gist: *“Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.”*

## Does this still stand? (2026-10-15)

*verified fact:* Yes, in the sense of an active pattern, not a dead blog post.

Evidence checked this date:

- The gist remains the canonical “idea file” people paste into agents.
- **Hermes Agent** still ships a bundled `llm-wiki` skill based on that pattern (same layout: schema, index, log, raw/, entities/, …). See earlier course note [[obsidian-vs-joplin-hermes-llmwiki]].
- Guides still teach “Karpathy wiki in Obsidian” (e.g. Dexio, fetched 2026-10-15).
- Community implementations keep shipping, including an Obsidian plugin `karpathywiki` / `GD4AI/obsidian-llm-wiki` (releases into September 2026) and other CLI / skill reimplementations.

*technical suggestion:* “Still stands” means: **the design is still coherent and widely reused**. It does *not* mean: this is the only good knowledge setup, or that it scales forever without RAG. Karpathy himself frames it as an idea file for collaboration with an agent, not a finished product.

### Why it still makes sense (for this course)

- Transparent: everything is markdown + git; students can see what the agent wrote.
- Fits critical inquiry: authorship is visible (agent-written pages vs your raw sources).
- No mandatory vector DB for small/medium personal research.
- Sync and tooling debates (Obsidian vs Joplin, MCP vs files) sit *around* the same folder idea.

Limits (still true):

- Large corpora may outgrow “read the index every time.”
- Wiki quality depends on the schema and on lint discipline; garbage in → confident garbage out.
- Pure Karpathy assumes you **accept** that most pages are LLM prose, not your diary.

## Human-readable wiki (the friend’s preference)

*technical suggestion:* Two different centres of gravity:

| | Karpathy-leaning | Human-wiki-leaning |
|---|---|---|
| Who writes the pages? | Mostly the agent | Mostly the human |
| What the agent does | Maintains structure, summaries, links | Reads / searches / answers; edits carefully |
| Feel | “Self-learning personal knowledge compiler” | “My notes, agent as assistant” |
| Risk | You stop reading what was filed | Wiki stays small; agent under-informed |
| Strength | Compounding structure over time | Trust, voice, teaching material |

They are not enemies. Hybrids are common: human owns voice and judgments; agent owns grunt work (summaries, indexes, link repair).

*anecdote (friend, via this conversation):* Prefers a wiki they can read as themselves, and uses OpenClaw, which feels more like a **distributor** than one self-learning agent at the centre. That tracks with OpenClaw’s documented multi-agent routing (see below) — treat as their practice, not as OpenClaw marketing.

## What OpenClaw is (and why “distributor” fits)

*verified fact:* OpenClaw is a **self-hosted gateway** that connects messaging channels (WhatsApp, Slack, Telegram, Discord, Teams, …) to AI agents. Docs: https://docs.openclaw.ai/start/openclaw

*verified fact:* **Multi-agent routing:** one Gateway process can run several isolated agents (each with its own workspace, state, sessions). Incoming messages are **bound** to the right agent by channel/account. Docs: https://docs.openclaw.ai/concepts/multi-agent/

That architecture is literally a **router / distributor**: many inboxes → many brains — not necessarily one personal agent that owns one growing wiki as its sole centre.

*verified fact:* OpenClaw also has an optional **Memory Wiki** plugin (`memory-wiki`): markdown vault with sources, entities, concepts, syntheses; `ingest` / `compile` / `lint` / `search`; Obsidian-friendly mode. Docs: https://docs.openclaw.ai/cli/wiki and `docs/plugins/memory-wiki.md` in the OpenClaw repo.

Important difference from pure Karpathy:

- OpenClaw Memory Wiki uses **managed / generated blocks** plus reserved **human Notes** blocks that are preserved on re-ingest (explicit product goal; see e.g. PR preserving human notes on source re-ingest).
- Docs say: prefer `wiki apply` over hand-editing managed sections; do not overwrite human note blocks.
- Compile builds indexes and a **compiled digest** used for prompts (also stored in OpenClaw’s plugin SQLite state) — more “platform” than a naked folder + agent.

So: OpenClaw can *host* a wiki that looks related to Karpathy, but the product centre is the **gateway + routing**, with wiki as one memory plugin — and the design expects **human-editable regions**.

## Side-by-side

| | Karpathy LLM Wiki (gist / Hermes skill) | OpenClaw (+ Memory Wiki) | Friend’s human wiki |
|---|---|---|---|
| Centre | One agent maintaining a folder wiki | Gateway distributing work to agent(s); optional wiki plugin | Human as author |
| Authorship default | LLM writes almost all wiki pages | Machine blocks + human Notes | Human writes pages |
| Interface | Folder + Obsidian / editor | Channels (chat apps) + CLI + optional Obsidian | Whatever they already use |
| Multi-agent | Usually one researcher | First-class multi-agent bindings | Optional |
| Fits course exercise “agent-readable structure” | Direct match | Possible, but more moving parts | Possible if files are open to the agent |

## Course takeaway

*technical suggestion:*

1. Teach Karpathy’s pattern as a **clear, still-current** model of agent-maintained knowledge (files, schema, index, raw vs wiki).
2. Name the alternative honestly: a **human-centred wiki** where the agent is a reader/helper — often better for teaching materials and personal voice.
3. Treat OpenClaw as a **different architecture** (channel gateway + routing = “distributor”), which *may* attach a wiki, not as a replacement for the Karpathy folder idea.
4. For students: asking “who is allowed to write which pages?” is the real design question — more important than Obsidian vs Joplin branding.

## Open points

- Unverified: how the friend configured OpenClaw in practice (personal assistant vs multi-agent team).
- Unverified: whether every OpenClaw Memory Wiki deployment is Obsidian-synced; docs support Obsidian-friendly mode and official Obsidian CLI hooks, with limits under agent-scoped vaults.
- Unverified: long-term quality comparison of pure LLM-maintained wikis vs human-maintained ones beyond anecdotes.

## Sources

- Karpathy, `llm-wiki.md` gist (2026-04-04): https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Hermes LLM Wiki skill (via previous research): https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/research/research-llm-wiki
- Dexio guide (Obsidian setup): https://dexio.wiki/guides/llm-wiki-obsidian/
- Obsidian plugin marketplace entry: https://community.obsidian.md/plugins/karpathywiki
- OpenClaw personal assistant: https://docs.openclaw.ai/start/openclaw
- OpenClaw multi-agent: https://docs.openclaw.ai/concepts/multi-agent/
- OpenClaw wiki CLI: https://docs.openclaw.ai/cli/wiki
- OpenClaw Memory Wiki plugin docs: https://github.com/openclaw/openclaw/blob/main/docs/plugins/memory-wiki.md
