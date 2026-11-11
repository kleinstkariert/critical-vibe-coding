---
title: "Session 01: Classroom lecture (welcome and landscape)"
date: 2026-11-09
updated: 2026-11-11
session: 1
status: third-draft
tags:
  - course
  - lecture
  - political-economy
---

# Session 01: Classroom lecture

Speaker notes for Part B of [[../sessions/01-welcome-and-landscape]]. The outdoor check-in (Part A) stays in that file.

Style: [[../presentation-style]]. Text slides are white on black; image slides are full-screen with one small credit line (who, where, photo or rendering). Images appear only where they carry the beat (Sebastian's edits of 9 and 11 Nov 2026). One exception: the hype-cycle slide in Block 4 shows the curve beside its explanation. Slide titles are the block titles below; bold labels on the slides are bold here too. Arguments and sources live in the deep-dive notes; the slides carry only what is said aloud.

Deck: [`01-welcome-landscape-slideshow/`](01-welcome-landscape-slideshow/README.md) · earlier versions: `01-welcome-landscape-slideshow/archive/`

---

## Blocks and timing

Part B runs about **11:00 to 11:55** inside the 10:00 to 12:00 slot. Short Q&A after each block.

| # | Block title (= slide title) | Min | Priority | Deep dive |
|---|---|---|---|---|
| 1 | Scope of the class | 3 | medium | this file |
| 2 | What LLMs and agents are | 8 | medium | this file · [[../what-is-harness]] · [[../what-is-mcp]] · [[01-welcome-landscape-deep-dives/default-setup]] §3 |
| 3 | Drivers, visions, fears, regulation | 8 | **high** | [[../visions-fears-regulation]] · law: [[../eu-ai-act-and-datenschutz]] |
| 4 | Economy and the AI bubble | 12 | **high** | [[01-welcome-landscape-deep-dives/bubble-economy]] |
| 5 | Ecology | 6 | **high** | [[01-welcome-landscape-deep-dives/ecology]] |
| 6 | Labour | 8 | **high** | [[01-welcome-landscape-deep-dives/labour]] |
| 7 | Media-art workflows | 4 | medium | [[01-welcome-landscape-deep-dives/media-art-workflows]] · [[01-welcome-landscape-deep-dives/flattening-and-the-norm]] |
| 8 | Default setup | 6 | practical | [[01-welcome-landscape-deep-dives/default-setup]] |

Regulation has no block of its own; it is the fourth beat of Block 3. The session ends with the choice of student-input topics (end of Block 8).

If time runs short, shorten Block 2 and Block 7 first. Blocks 3 to 6 carry the session.

---

## Block 1: Critical Vibe Coding - Scope of the class

### Say

Every week has two tracks.

1. **Technical:** you build a working personal agent setup: a notes folder, an agent that can read and write it, and rules you wrote yourself.
2. **Critical:** what this technology does to society, our planet, work, money, energy and art, without pretending it is neutral.

A third thread runs through both: **the agent as interface**. The setup itself is material and/or canvas, not only a machine for producing outputs.

The course has **eight sessions** ([[../course-outline]]). Midpoint in Session 4 (demo your setup and a short proposal), final in Session 8 (architecture, one real use, a short reflection). No polished exhibition is expected by default.

### Slides

| Slide | Content |
|---|---|
| Image | `13-meta-el-paso-contentstack.jpg`: rendering of Meta's planned campus, El Paso, Texas (opens the deck, before the title) |
| Text | Title: Critical Vibe Coding, Session 01 |
| Text | **Critical Vibe Coding** - Scope of the class: two tracks, the third thread, milestones |

### Q&A

Who came for the setup, and who for the politics? Both are welcome; neither track is optional.

---

## Block 2: What LLMs and agents are

Medium priority. Keep it plain; the architecture comes in Session 02.

### Entry: the system behind the chat window

A chat window is the visible tip of a large system. Kate Crawford and Vladan Joler's *Anatomy of an AI System* (2018) maps one voice assistant from the mine to the dump: minerals, smelters, factories, shipping, data centres, data labelling, and the people at each step. Today we focus on the visible part. The rest returns in every block.

### Basic vocabulary

| Word | Plain meaning |
|---|---|
| **Model** | A large file of numbers trained on text. Given some text, it continues it. It does not look anything up. |
| **Chat product** | The app built around a model: ChatGPT, Claude, Gemini. Interface, safety filters, memory, payment. |
| **Agent** | A program that runs a model in a loop and lets it act: read and write files, search, run code, until the task is done or you stop it. |
| **Context** | Everything the model can see at this moment: your message, the files it opened, the last results. What is not in the context does not exist for the model. This is why agents work with files and indexes. |
| **Harness** | Everything around the model that you set up: tools, files, skills, rules. In this course, the harness is your material. |
| **MCP** | **Model Context Protocol.** A standard plug between an agent and other apps and tools: calendar, browser, Blender, a database. Each app that offers an "MCP server" can be used by any agent that speaks the protocol. Open standard, introduced by Anthropic in 2024. Session 05: [[../what-is-mcp]]. |
| **Sandbox** | A closed-off space where the agent can run code and change files without touching the rest of your computer: a container, a virtual machine, a locked folder. If the agent makes a mistake, the damage stays inside. Case in Session 05: the Hugging Face incident, where agents escaped their sandbox. |
| **Lint** | An automatic check for mistakes. In code: errors and bad style (the name comes from a 1978 tool for C). In a wiki: broken links, contradictions, forgotten pages. In the LLM Wiki it is the third operation next to ingest and query: [[../what-is-lint]]. |

One sentence to remember: *a chat answers; an agent acts, with the tools you allow it.*

### The agent loop (image)

After the vocabulary, the black and white **agentic AI loop** Sebastian chose: **reason** (plan from what is in context), **act** (call a tool: write a file, search, run code), **observe** (read what came back), **evaluate** (compare with the goal, decide the next step), then round again until the task is done or a limit stops it. In this course the results land in your notes folder, and the next pass reads them from there. Source of the graphic still to confirm.

### How a model writes

1. It learned from huge amounts of text which words tend to follow which.
2. When you ask something, it writes the most plausible continuation, piece by piece.
3. Plausible is not the same as true. Confident mistakes are normal behaviour, not a malfunction.
4. Good at: drafts, summaries, translating between formats, proposing structure.
5. Weak at: facts it never saw, your unstated intentions, taking responsibility.

### Local or cloud

| | Cloud | Local |
|---|---|---|
| What you get | The strongest models, no hardware needed | Privacy, offline use, your own rules |
| What it costs | Your data leaves; prices and terms can change; the hardware sits in someone else's country | Expensive hardware, smaller models, your own maintenance |

→ The choice is technical, economic and political at once.

**The diagram (image): standard setup or course setup.** A dashed line separates your computer from company servers.

- **Standard setup:** ChatGPT, or Cursor with default settings. Only the window (and, in Cursor, your project files) is on your side. The agent loop and prompt building run on the company's servers; Cursor routes every request through its own backend even with your own model key and keeps a code index there. ChatGPT keeps chats and memory on OpenAI's servers, and for personal accounts "Improve the model for everyone" is on by default, so chats can train future models.
- **Course setup:** Hermes with its skills, rules and memory, and the notes folder (sources, wiki, schema), all on your computer. Only the model call leaves: the prompt plus the notes the agent selected. With a local model, nothing leaves.

**Why the course setup.** Your data stays with you (notes, memory, skills are files on your disk). You set the limits: which folders the agent may read, which it may write, which stay human-only. Easy to switch: skills, rules and memory are local, so you can change the agent or the model and keep them. No lock-in: plain markdown. You can check it: every page the agent wrote is a file you can open, compare and undo. Model by choice: paid, free tier, or local. Limits, said aloud: the model call still leaves unless the model is local; free tiers can log prompts; a local agent needs upkeep.

Full explanation: [[01-welcome-landscape-deep-dives/default-setup]] §3. Hardware: Session [[../sessions/03-hardware-open-models-prompting|03]] · [[../../research/local-gpu-hardware-for-llms]].

### Slides

| Slide | Content |
|---|---|
| Text | What LLMs and agents are: the chat window is the visible tip |
| Image | `15-anatomy-of-an-ai-system-joler.jpg`: Crawford and Joler, *Anatomy of an AI System* (2018) |
| Text | Basic vocabulary (Model, Chat product, Agent, Context, Harness, MCP, **Sandbox, Lint**) |
| Image | `32-agentic-ai-loop-bw.png`: agentic AI loop (reason, act, observe, evaluate), Sebastian's choice. Source: David Davies, Online Inference (Medium), Aug 2026 |
| Text | How a model writes |
| Text | Local or cloud |
| Image | `27-cloud-vs-local-flowchart.png`: cloud or local, where your notes go |
| Text | **Why the course setup** |
| Image | `27-standard-vs-course-setup.png`: standard setup or course setup, where your things live |

### Q&A

Has anyone used an agent that edits files, not only a chat? Where in this stack is authorship if the agent writes half the patch?

---

## Block 3: Drivers, visions, fears, regulation

High priority. **Script:** [[../visions-fears-regulation]]. Keep its four beats.

1. **What drives the build.** Tech firms needed a next growth platform after PC, internet, smartphone, social networks. They already held the data and the computing power. → LLMs is what they have; they have no other idea. It is a race: no single firm can pause alone.
2. **Two industry stories.** Abundance (universal basic or "high" income, Musk, Altman) and extinction risk, often from the same people. Both are real rhetoric; neither is delivered policy. Jon Stewart: pick a lane.
3. **Amplifier or power.** **Salim Ismail:** AI is an amplifier; fire heats the house or burns it down (the tool argument). **Social science:** it amplifies those who already hold power, plus a lot of other issues.
4. **What regulation can do.** Rules can limit uses, protect personal data, assign liability and shape markets. They cannot put the technology back into the box. Calls for regulation can also be marketing ("we are so powerful we need rules"), and regulation that slows the race benefits the current leaders (Anthropic, OpenAI). The EU AI Act and the GDPR set rules for uses and personal data, also in student projects: [[../eu-ai-act-and-datenschutz]] (student input on privacy, Session 07).

Teacher clips (vault): Coxon on The Daily Show, Stewart monologue, Ismail response. Links in the script.

### Slides

| Slide | Content |
|---|---|
| Text | Drivers, visions, fears, regulation: what drives the build |
| Image | `16-bruegel-tower-of-babel.jpg`: Bruegel, *The Tower of Babel* (1563): building higher than anyone needs |
| Text | Two industry stories |
| Text | Amplifier or power |
| Text | What regulation can do |

### Q&A

What would your rule for AI usage be?

---

## Block 4: Economy and the AI bubble

High priority. **Deep dive:** [[01-welcome-landscape-deep-dives/bubble-economy]]. Research base: [[../../research/ai-bubble-productivity-datacenter]].

Teach the facts of the build-out first, then the debate, then who gets the income. Sebastian opens the block with a short video (link on the opener slide).

0. **Where are we in the hype cycle?** Gartner's curve (Jackie Fenn, 1995; a model, not data): a technology trigger brings in money, promises grow to a *peak of inflated expectations*, results disappoint and money flows out (*trough of disillusionment*), then the useful parts remain (*slope of enlightenment*, *plateau of productivity*). **Richard Campbell:** AI is "headed down the trough of disillusionment", "far from bottomed out" *(claim, about 29:40)*. Mobile and cloud had no hype cycle; dot-com and AI did, and in both the hype paid for a huge infrastructure build-out. The curve and its explanation share one slide. Deep dive §6.
1. **The spending.** Amazon, Alphabet, Microsoft and Meta plan $720 to 740 billion of capex in 2026, about three times 2024. In Q3 2026 they spent about $209 billion in one quarter. *(verified fact: company guidance)* Then Campbell's three charts in a row: hyperscaler capex by year; tech investment as a share of US growth (Bridgewater via J.P. Morgan: 35 to 45% of US real GDP growth in the three quarters to mid-2025; without it, growth was about 1%); and seven companies making 55% of the S&P 500's 2024 gain (Voronoi). Deep dive §1.
2. **Building ahead of demand.** Stargate Abilene: eight buildings, 1.2 GW, about $31 billion, built in under two and a half years. 267 more US campuses approved or planned. Land, power and chips are ordered before customers exist. Planned gigawatts are not working gigawatts.
3. **Spending ahead of revenue.** OpenAI lost about $21 billion in 2025 *(claim)*. About 2.5% of Americans pay for an AI subscription *(claim)*. Acemoglu estimates about 1% more GDP over ten years *(verified fact: paper)*. A growing share is borrowed: bonds, private credit, off-balance-sheet vehicles. More than half of the money AI firms raise comes from other AI firms *(verified fact: Bank for International Settlements, Bulletin 137)*.
4. **Every build-out overbuilt.** Canals, railways, electrification, fibre: each ended in oversupply. About half of US railroad track miles turned out useless *(claim)*. Fibre sold for 10 cents on the dollar after 2000 *(claim)*. Rails lasted a century; chips are written off in five to six years. **The map:** the whole US rail network in 1884 (Mitchell), with competing parallel lines. After the Panic of 1893, by 30 June 1894, 192 railroads with more than 42,000 miles of line, about a quarter of all US railway capital, were in receivership *(verified fact: Interstate Commerce Commission)*. The track stayed; the investors lost. Then Bloomberg's graphic of the circular deals (Nvidia, OpenAI, Oracle, AMD), Sebastian's addition. Deep dive §4 and §6.
5. **Will it burst? Arguments for.** From the Ezra Klein debate (Paul Kedrosky) and Richard Campbell's keynote: every big build-out ended in oversupply, and a race makes everyone overbuild. Revenue is a fraction of spending; few customers, falling prices per token. More of it is debt, partly off the balance sheet, and AI firms fund each other (circle investment). Ordinary savers carry it: the ten largest stocks are about 40% of the S&P 500. Stocks cost about 40 times their earnings: above 1929, below only 2000 *(verified fact: Shiller CAPE; reading in the deep dive, section 5)*. Chinese models are much cheaper and almost as good. Almost all of current US growth comes from AI investment (Furman: about 92% in the first half of 2025, *claim*; Bridgewater and J.P. Morgan: 35 to 45%).
   **Reading the CAPE chart:** price of the S&P 500 divided by the average yearly profit of the past ten years, both adjusted for inflation. The ten years are only the averaging window, not a threshold. 44 in 2000 means the price equalled 44 years of average profit. The ratio says how expensive shares are, not whether firms make a profit. Long-run average about 18. Deep dive §5.
6. **Will it burst? Arguments against.** Azeem Azhar and Ezra Klein, with Campbell: compute is scarce and demand still exceeds supply. A GPU pays for itself in 18 to 24 months at today's rental prices. More customers pay every quarter; Anthropic's Q1 2026 beat its whole 2025. If the labs fail, the data centres still get used. Debt is still limited; big investors trim, they do not flee.
7. **Who gets the income.** **Adam Tooze:** "a two-way bet on disaster either way". If the investment fails, losses land somewhere in the chain. If it pays off, the labour market is shaken to its foundations. The Bank for International Settlements (BIS), the central bank of central banks, models a scenario in which labour's share of income falls from about 60% to 20%: today about 60% goes to wages; then 20% to wages and 80% to owners. **Demand bottleneck**, the middle line of the chart: replaced workers stop buying, so automating more stops paying; the fall stops near 47%. *(claim: Tooze; verified fact: BIS scenario, a model, not a forecast)* Deep dive §9.
8. **An alternative: AI as a commons.** A few firms own what AI needs: data, computing power, talent. **Pieter Verdegem:** dismantle AI capitalism and build commons instead: data trusts, public computing, cooperatives, democratic rules. Workers and communities decide what should be automated. Read: *Dismantling AI capitalism: the commons as an alternative to the power concentration of Big Tech*, AI & Society, 2022: https://pmc.ncbi.nlm.nih.gov/articles/PMC8994059/ · notes: [[01-welcome-landscape-deep-dives/bubble-economy]] §10.

Sources for beats 0 to 7: Ezra Klein Show, *Is There an A.I. Bubble? A Debate* (16 Oct 2026, https://www.youtube.com/watch?v=9GLdGc9OX-A) · Richard Campbell, *After the AI Hype: What's Real, and What's Next*, NDC Copenhagen (June 2026, https://www.youtube.com/watch?v=uWnUnMphmPM; hype cycle about 29:40, charts 32:20 to 33:10, Bloomberg graphic 33:45) · Ones and Tooze Ep. 250, *Adam Tooze on the AI Arms Race*, Foreign Policy (10 Jul 2026, https://www.youtube.com/watch?v=QevC7OrdJP8, from about 32:33) · Bank for International Settlements (BIS) Annual Economic Report 2026, Box C · Bloomberg, Forgash and Ghosh, 7 Oct 2025.

### Slides

| Slide | Content |
|---|---|
| Text | Economy and the AI bubble: opener with video link (Sebastian's) |
| Text + image | **Where are we in the hype cycle?** `34-hype-cycle.png` beside its explanation (the one exception to image-only slides) |
| Text | The spending |
| Image | `28-bigtech-capex-chart.png`: hyperscaler capex by year, 2016 to 2026 |
| Image | **`35-us-gdp-tech-capex-chart.png`**: US growth, tech investment against the rest |
| Image | **`36-mag7-sp500-gains-2024.png`**: who made the S&P 500's gain in 2024 |
| Text | Building ahead of demand |
| Text | Spending ahead of revenue |
| Image | `20-nyse-crowd-1929.jpg`: crowd outside the New York Stock Exchange, 1929 |
| Text | Every build-out overbuilt |
| Image | **`31-us-railroad-map-1884.jpg`**: US railroads 1884, with the 1893 to 1894 receiverships in the caption |
| Image | `33-bloomberg-circular-ai-deals.png`: Bloomberg, circular AI deals (Sebastian's) |
| Text | Will it burst? Arguments for |
| Image | `29-shiller-cape-chart.png`: Shiller CAPE, 1881 to 2026, with long-run average and reading line |
| Text | Will it burst? Arguments against |
| Text | Who gets the income (Tooze, Bank for International Settlements, demand bottleneck) |
| Image | `30-bis-labour-share-scenario.png`: workers' share of income in the BIS scenarios, with plain labels |
| Text | An alternative: AI as a commons (Verdegem) |

### Q&A

Your subscription costs about €20 a month. Who pays the rest? If the bubble bursts, who should own what is left?

---

## Block 5: Ecology

High priority. **Deep dive:** [[01-welcome-landscape-deep-dives/ecology]]. Student input on the ecology of AI: Session [[../sessions/06-agent-as-interface|06]]. Earlier full unit (archived): [[../sessions/archive-13-session-plan/11-local-ecology-when-not]]. Research base: [[../../research/data-centers-energy-ecology-economy]].

1. **Small globally, large locally.** About 1.5% of world electricity in 2024; the US uses 45% of that. Half of US capacity sits in five clusters. Data centres drive almost half of US electricity-demand growth to 2030. *(verified fact: IEA)*
2. **Gas, water, neighbours.** New campuses build gas turbines on site to skip the grid queue (sometimes illegally). GW Ranch in Texas plans 35 turbines and more than 7 GW *(claim)*. Memphis: xAI ran up to 35 turbines with a permit for 15 *(claim)*. Water is local: Phoenix cools servers with water from a shrinking Colorado River. A multi-billion campus employs only a handful of permanent staff. → Generally there is not enough data available to really know the actual ecological impact of AI.
3. **Your prompt, their campus.** Training is rare and huge; daily use adds up. Images, video and long agent runs cost far more than short text. Three questions for any tool: where is the rack, what powers it, who lives next door?

### Slides

| Slide | Content |
|---|---|
| Text | Ecology: small globally, large locally |
| Image | `11-gw-ranch-heise.jpg`: rendering of GW Ranch, Pecos County, West Texas (Pacifico Energy, via heise online) |
| Text | Gas, water, neighbours |
| Image | `06-datacenter-cooling-tower.jpg`: photo, cooling tower on a data centre, Mesa, Arizona |
| Text | Your prompt, their campus |
| Image | `25-ashburn-data-centers.jpg`: aerial photo, data centres among commercial buildings, Ashburn, Loudoun County, Virginia |

### Q&A

Would you accept a data centre in your own district? On what conditions?

---

## Block 6: Labour

High priority. **Deep dive:** [[01-welcome-landscape-deep-dives/labour]]. Earlier full unit (archived): [[../sessions/archive-13-session-plan/10-authorship-labour-platforms]]. Research base: [[../../research/ai-jobs-rising-tide-productivity]].

1. **The work inside the model.** Models are trained on human work, mostly unpaid. Then low-paid people clean them: Kenyan workers labelled toxic text for OpenAI for under $2 an hour *(verified fact: TIME 2023)*. Every answer you rate is more training work.
2. **Almost 40% of jobs.** **IMF:** almost 40% of jobs worldwide are exposed to AI, about 60% in rich countries. Half may gain; half may see lower demand, lower wages, fewer hires *(verified fact: Georgieva, IMF blog, Jan 2024)*. Exposed is not replaced. **Brian Merchant** (*A Luddite's Guide to the AI Economy*, Carnegie, July 2026): the question is what management does with it; "complemented" work can still be paid less, and the threat of AI alone disciplines workers *(claim)*. **Daron Acemoglu:** only about 5% of tasks can be automated profitably within ten years; GDP about +1.1% *(verified fact: paper)*. Gains go to capital first; the IMF itself expects more inequality.
3. **Creative work and first jobs.** Illustrators, translators and copywriters were hit first. Translators now check machine output, for lower rates. → **deskilling.** Workers aged 22 to 25 in AI-exposed jobs have about 19% lower employment than comparable peers, mostly through less hiring *(verified fact: Stanford)*. Juniors gain most from AI tools, and are hired least.
4. **What the Luddites wanted.** Skilled weavers who fought cheaper, worse goods and the loss of control over their work. Parliament refused a minimum wage; organising was illegal. In 2023 Hollywood writers won contract rules on AI after a 148-day strike. The question is how much say workers have over the technology.

### Slides

| Slide | Content |
|---|---|
| Text | Labour: the work inside the model |
| Image | `05-quarto-stato-pellizza.jpg`: Pellizza da Volpedo, *Il Quarto Stato* (1901) |
| Text | Almost 40% of jobs (IMF, Merchant, Acemoglu) |
| Text | Creative work and first jobs |
| Image | `21-koehler-der-streik.jpg`: Robert Koehler, *Der Streik* (1886) |
| Text | What the Luddites wanted |
| Image | `22-luddite-leader-1812.jpg`: *The Leader of the Luddites* (1812) |
| Image | `23-quadrature-cosmology-of-capital.jpg`: Quadrature, *Cosmology of Capital*, in *The Mass of Money*, Dresden 2026 (own work); bridge to Block 7 |

### Q&A

If your first job is the one being automated, how do you learn the craft?

---

## Block 7: Media-art workflows

Medium priority. **Deep dive:** [[01-welcome-landscape-deep-dives/media-art-workflows]]. Bring back themes from the outdoor check-in.

1. **Pressures** (Sebastian's wording on the slide). Speed: more iterations, less time with engineering, more time for thinking, also more at the same time (the value of specialization and hesitation degrades). Democratization of what is possible for whom → more competition. Flattening: the same generated look, the same generated concepts. Authorship: how to credit? How to value? Refusal: knowing when not to use AI is a skill and takes a lot of self discipline.
2. **Flattening is more than style.** A statistical model reproduces what is shown most online, not what exists. That average becomes a norm, skewed toward the most visible content: male, English, commercial, young. Thesis for the Session 02 student input: **AI kills the underground and it kills diversity.** Deep dive: [[01-welcome-landscape-deep-dives/flattening-and-the-norm]].

The practices for the semester moved to the end of the session (after the student inputs, Block 8).

### Slides

| Slide | Content |
|---|---|
| Text | Media-art workflows: pressures |

---

## Block 8: Default setup

Practical. **Deep dive with the diagram explained part by part:** [[01-welcome-landscape-deep-dives/default-setup]].

### Stack

1. **Knowledge store** with phone sync. Default Obsidian: [[../howto-obsidian-setup-and-sync]]. Alternatives: [[../knowledge-store-options]] · SilverBullet: [[../howto-silverbullet-setup-and-sync]].
2. **Hermes Agent** pointed at that folder: [[../howto-hermes-setup]] (Windows, macOS, Linux). Installed together in Session 02.
3. **LLM Wiki** structure (sources, wiki, schema): [[../llm-wiki-standard-files]] · [[../../research/karpathy-llm-wiki-and-openclaw]] · Obsidian versus Joplin: [[../../research/obsidian-vs-joplin-hermes-llmwiki]].
4. **Model**: whatever access you prefer: [[../prompting-and-model-choice]] · campus access: [[../academic-ai-austria]] · local later: [[../howto-local-llm-hardware]]. Free start: **Nemotron 3 Ultra through OpenRouter's free tier** ([[01-welcome-landscape-deep-dives/default-setup]] §4).
5. **Harness** (next session): [[../what-is-harness]] · [[../sessions/02-agent-harness-and-wiki-architecture]] · tools and MCP: [[../what-is-mcp]] · checking the wiki: [[../what-is-lint]].

### Homework (say aloud)

- Bookmark or clone the course GitHub: [[../START-HERE]].
- Install a knowledge store with phone sync (Obsidian by default; alternatives allowed).
- Write down which AI access you already have.
- Read Karpathy's LLM Wiki note ([[../references]]). → If you do not want to use AI: you can do research, investigative work on AI and input lectures.
- Next week: setup guide, Karpathy and the harness, after a student humanities input.

### Student inputs: choose a topic

Groups of four (or two pairs) pick one session by next week. Each input runs about 15 minutes at the start of the session, followed by discussion. Sessions 04 and 08 have no input (project presentations and finals). Rhythm and grading weight: [[../course-rhythm]].

| Session | Topic | Question for the group | Starting points |
|---|---|---|---|
| **02** | **Flattening** | AI kills the underground and it kills diversity? A statistical model reproduces the most shown, not reality, and makes it the norm. Include AI and patriarchy, feminism and AI. | [[01-welcome-landscape-deep-dives/flattening-and-the-norm]] |
| **03** | **Closed versus open weights as power** | Who holds the power when the weights are secret, and who when they are public? Is "open" open if only big labs can train? | [[../prompting-and-model-choice]] · [[../../research/local-gpu-hardware-for-llms]] |
| **05** | **How dangerous is AI really?** | From frontier risk to everyday harm. Case: the Hugging Face incident (July 2026), in which OpenAI evaluation agents escaped their sandbox and reached Hugging Face's production systems. | Hugging Face incident report: https://huggingface.co/blog/security-incident-july-2026 · OpenAI: https://openai.com/index/hugging-face-incident-and-the-road-ahead/ · [[../visions-fears-regulation]] |
| **06** | **The ecology of AI** | Energy, water, gas, land and neighbours. What can we know, and what is hidden? | [[01-welcome-landscape-deep-dives/ecology]] · [[../../research/data-centers-energy-ecology-economy]] |
| **07** | **Privacy: what happens with the data?** | Where do prompts, notes and files go? Who stores them, who trains on them? | [[../eu-ai-act-and-datenschutz]] · [[01-welcome-landscape-deep-dives/default-setup]] §3 |

### Practices for this semester (closing slide, no block title)

A provenance note per project: which model, which tools, who decided (how), where it ran (local, cloud...). Personal ethics: what the agent may touch, remember, and what to refuse; your own manifesto on AI. Practical and theoretical work: use this class to work on your projects with an agent, or use it for research.

Q&A: Which part of your practice would you never hand to an agent?

### Slides

| Slide | Content |
|---|---|
| Text | Default setup: notes, agent, structure, model |
| Image | `14-llm-wiki-annotated.png`: *LLM Wiki: Karpathy's knowledge compilation pattern* (via Medium), with a note next to each part and the row labels in white |
| Text | Homework |
| Text | Student inputs: choose a topic |
| Text | Practices for this semester |
| Image | `04-messy-desk.jpg`: every vault starts like this |

No credits slide: each image slide carries its credit line.
