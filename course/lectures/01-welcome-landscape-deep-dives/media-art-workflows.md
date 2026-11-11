---
title: "Deep dive: Media-art workflows"
date: 2026-11-09
session: 1
block: 7
status: teaching-ready
tags:
  - course
  - lecture
  - deep-dive
  - media-art
  - authorship
---

# Deep dive: Media-art workflows

Block 7 of [[../01-welcome-landscape-lecture]]. What agents change in artistic work, and the practices this course uses to keep the work your own. Later sessions: [[../../sessions/04-project-presentations-and-plans|04]] (semester plans, provenance note), [[../../sessions/06-agent-as-interface|06]] (agent as interface, material, canvas), [[../../sessions/07-coding-and-creative-stacks|07]] (coding and creative stacks). Flattening in depth: [[flattening-and-the-norm]] (student input, Session 02).

Labels: *verified fact* | *claim* | *course position* (a teaching decision of this course).

**Base material**

| Source | Role |
|---|---|
| [[../../ai-tools-creative-processes]] | Survey of creative tools, node canvases, MCP bridges. |
| Sessions 05 to 11 | Practices: provenance, interface score, refusal, hybrid wiki. |
| [[../../references]] | Artist and course examples with links. |
| Quadrature, *Cosmology of Capital* in the exhibition *The Mass of Money* (Schaufler Lab, TU Dresden, 2026) | Own work: a system as the artwork. |

---

## 1. Pressures

The slide (Sebastian's edit, 11 Nov 2026) names five: speed, democratization, flattening, authorship, refusal. Interface is no longer on the slide; it stays in section 2 below.

| Pressure | What changes | What is at stake |
|---|---|---|
| **Speed** | More iterations, less time with engineering, more time for thinking, and also more at the same time. | The value of specialization and of hesitation degrades. Less time spent with a bad idea, which is often where the good one comes from. |
| **Democratization** | More becomes possible for more people: code, images, sound without the training. | Possible for whom? More people can make, so there is more competition for the same attention and commissions. |
| **Flattening** | The same generated look, the same generated concepts. And beyond style: the model reproduces what is shown most online, not what exists. | That average becomes the norm. Thesis: AI kills the underground and it kills diversity. See [[flattening-and-the-norm]]. |
| **Authorship** | An agent writes half the patch, script or text. How to credit? How to value? | Who decided, who signed, who is responsible, and what is the work worth? |
| **Refusal** | Using AI becomes the default. | Knowing when not to use it is a skill, and it takes a lot of self discipline. |

*verified fact (OpenAI post-mortem, 29 Apr 2025):* OpenAI rolled back a GPT-4o update because it had become "overly flattering or agreeable". The helpful voice is a product decision, not a neutral one.

*claim (Richard Campbell, NDC keynote 2026):* The name "Copilot" means "you're the pilot. It's still your fault." Avoid treating the software as a person.

---

## 2. The setup as the work

*course position:* In this course the agent setup is artistic material, not only a means to produce outputs. An agent's interface is what you can ask, what it can touch, what it must refuse, and how it remembers. The schema file is the one place where the character of the agent is written down (Session [[../../sessions/06-agent-as-interface|06]]).

- Choosing which tools to connect and which to leave out is designing the agent's interface (Session [[../../sessions/05-knowledge-base-phone-discord|05]]).
- *verified fact (course survey, 2026-10):* Node canvases such as Figma Weave and FLORA turn AI workflows into graphs. The open question is who owns the graph.
- *claim (course survey):* vvvv, TouchDesigner and Max have no first-class MCP yet; they connect through file export, OSC or script bridges. Translating a prompt into a patch is itself the teaching point.
- *verified fact (blender.org Lab):* Blender's experimental MCP server (Blender 5.1+) runs model-generated code without guards. Use a throwaway file or a virtual machine.

**Own example.** Quadrature's *Cosmology of Capital* (LED wall, exhibition *The Mass of Money*, Dresden 2026) is an N-body simulation in which the fortunes of about 3,400 billionaires act as gravitational sinks for about 200,000 particles. The software pipeline (data loading, mass quotas, GPU simulation) is the work, not a tool that made it.

---

## 3. Examples from other schools and artists

- *verified fact:* HM Munich, *Our Br00d*: moving a project from cloud to local and open infrastructure as an artistic decision.
- *verified fact:* NYU IMA, *Chatbots for Art's Sake*: the chatbot as artistic material.
- *verified fact:* SFPC, *Handmade Datasets*: a small, cared-for dataset, with consent and scale as part of the work.
- *verified fact:* Kate Crawford and Vladan Joler, *Anatomy of an AI System* (2018) and *Calculating Empires* (2023): mapping AI as labour, data and material extraction. Research presented as artwork.
- *verified fact:* Holly Herndon and Mat Dryhurst, *Holly+* (2021): a voice model of the artist offered for others to use under rules she sets.
- *verified fact:* University of Chicago, *Glaze* and *Nightshade* (2023): tools that let artists protect their images against style copying and poison training data. Refusal as software.

---

## 4. Practices for this semester

| Practice | What you do | Session |
|---|---|---|
| **Provenance note** | A short `provenance.md` per project, written by you: which model, which tools, who decided (how), who was paid, where it ran (local, cloud...). | [[../../sessions/04-project-presentations-and-plans\|04]], final in [[../../sessions/08-final-presentations\|08]] |
| **Interface score** | One page: the agent's roles, tools, memory and taboos. Compare it with the real schema and tool list. | [[../../sessions/06-agent-as-interface\|06]] |
| **Human-only pages** | Your artistic voice lives in pages the agent may read but not write. Set this in the schema. | [[../../sessions/05-knowledge-base-phone-discord\|05]] |
| **Cloud versus local** | Run the same task on a cloud model and a local one. Log tokens, time, quality, and where the cloud call probably ran. | [[../../sessions/03-hardware-open-models-prompting\|03]] |
| **Refusal week** (optional, off the slide) | Give up one convenient cloud feature for a week. Write down what it cost you and what you gained. | archived: [[../../sessions/archive-13-session-plan/11-local-ecology-when-not\|old 11]] |
| **Kill switch** | A rule in the schema that stops the agent, and a checklist of when AI is unnecessary. | [[../../sessions/06-agent-as-interface\|06]] |

*course position:* "The agent proposes; the student owns the cut and the print." (Session 07)

---

## 5. Quotes usable in class

1. "Who signed the work if the agent wrote the patch?"
2. "When is refusal a better artistic move than a better model?" (Course rhythm)
3. "Our job was never to write code. It was to solve people's problems." Richard Campbell.

---

## 6. Questions for the room

- Which part of your practice would you never hand to an agent?
- Where in your last project did a tool decide something you did not notice?
- Could the setup itself be your midpoint piece?

---

## Sources

- [[../../ai-tools-creative-processes]] · [[../../references]]
- OpenAI, *Sycophancy in GPT-4o*: https://openai.com/index/sycophancy-in-gpt-4o/
- Blender Lab MCP server: https://www.blender.org/lab/mcp-server/
- Crawford and Joler, *Anatomy of an AI System*: https://anatomyof.ai/ · *Calculating Empires*: https://calculatingempires.net/
- Holly Herndon, *Holly+*: https://holly.plus/
- Glaze: https://glaze.cs.uchicago.edu/ · Nightshade: https://nightshade.cs.uchicago.edu/
- Richard Campbell, *After the AI Hype*: https://www.youtube.com/watch?v=uWnUnMphmPM
