---
title: "Deep dive: Flattening, the norm, and feminist critiques of AI"
date: 2026-11-10
session: 1
block: 7
status: teaching-ready
tags:
  - course
  - lecture
  - deep-dive
  - flattening
  - feminism
  - bias
---

# Deep dive: Flattening, the norm, and feminist critiques of AI

Linked from Block 7 of [[../01-welcome-landscape-lecture]] (the "flattening" pressure) and from the student input of Session [[../../sessions/02-agent-harness-and-wiki-architecture|02]].

Labels: *thesis* (the argument this note makes) | *verified fact* (peer-reviewed paper, agency study, documented analysis) | *claim* (book argument, journalism, talk) | *open question*.

**Base material.** The teacher vault has no clipping on feminism or patriarchy yet. This note draws on published research, listed under Sources. Related course notes: [[media-art-workflows]] (five pressures), [[labour]] (who trains the model), [[../../visions-fears-regulation]] (amplifier or power).

---

## 1. The thesis

*thesis:* **AI kills the underground, and it kills diversity.**

Flattening is not only a matter of taste: the same generated look, the same helpful voice. It goes deeper.

1. A language or image model is a statistical tool. It learns what appears most often in its training data and reproduces the most likely continuation.
2. Its training data is what is **most displayed online**: the most posted, most linked, most scraped. That is not the same as what exists, and not the same as reality.
3. So the model's output is an average of the visible. It turns what is most shown into a **norm**.
4. What is rare, small, offline, closed or deliberately marginal (the underground) is either missing from the data or so thin that the model treats it as noise.
5. As generated content floods the web and the next models train on it, the average of the average gets narrower.

**Class line:** A model does not show the world. It shows what the internet shows most, and it calls that normal.

---

## 2. How a statistical model makes a norm

- *verified fact (how the systems work):* A language model predicts the next piece of text by probability. Default settings favour high-probability continuations. Image models do the same with visual patterns.
- *verified fact (Shumailov et al., Nature 2024):* When models are trained on data produced by earlier models, "tails of the original content distribution disappear". The authors call this **model collapse**. Rare events, minority patterns and unusual styles go first.
- *verified fact (Doshi and Hauser, Science Advances 2024):* In an experiment, writers with AI story ideas wrote stories judged more creative and better written. The AI-assisted stories were also **more similar to each other**. Individually better, collectively narrower: the authors call it a social dilemma.
- *verified fact (OpenAI, April 2025):* OpenAI rolled back a GPT-4o update because it had become "overly flattering or agreeable". The tone of the helpful voice is a product decision, tuned on what most users rate highly.

**Class line:** Averaging is not a bug in these systems. It is how they work.

---

## 3. Most shown is not reality

Who writes the internet that models learn from?

- *verified fact (Bender, Gebru, McMillan-Major, Mitchell, FAccT 2021, "On the Dangers of Stochastic Parrots"):* Size does not guarantee diversity. GPT-2's training data came from links shared on Reddit, where 67% of US users were men and 64% aged 18 to 29 (Pew 2016). Only 8.8 to 15% of Wikipedia editors are women or girls.
- *verified fact (same):* Moderation and harassment push people out of mainstream platforms. Groups who build their own spaces, such as older adults writing blogs, are "less likely to be included in training data".
- *verified fact (same):* Data filters target words referencing sex, which "likely also" removes LGBTQ online spaces.
- *verified fact (same):* "The voices of people most likely to hew to a hegemonic viewpoint are also more likely to be retained." The paper names white supremacist, misogynistic and ageist views as over-represented relative to the population.

**Class line:** The training data overrepresents the loudest, best-linked and most-moderated-for spaces. The rest is underrepresented or filtered out.

---

## 4. The norm has a gender: AI and patriarchy

Feminist research on data and AI asks who is counted, who counts, and whose view becomes the default.

### What the models produce

- *verified fact (UNESCO and IRCAI, March 2024, "Bias Against Women and Girls in Large Language Models"):* GPT-2, GPT-3.5 and Llama 2 associated female names with "home", "family" and "children", and male names with "business", "executive", "salary" and "career". Llama 2 described women in domestic roles four times as often as men. In open-ended completions it produced sexist and misogynistic content in about 20% of cases.
- *verified fact (same):* Stories about men used words like "adventurous" and "decided". Stories about women used "garden", "love", "gentle", "husband". When asked for occupations across cultures, the models gave men varied, high-status jobs and gave women and Zulu people servant roles.
- *verified fact (Bloomberg analysis of more than 5,000 Stable Diffusion images, 2023):* For the prompt "judge", about 3% of generated images showed women. In the US about 34% of judges are women. Men with lighter skin dominated every high-paying job; women dominated only low-paid ones like housekeeper and cashier.
- *verified fact (Buolamwini and Gebru, "Gender Shades", 2018):* Commercial face-analysis systems misclassified darker-skinned women up to 34.7% of the time and lighter-skinned men at most 0.8%.

The pattern: the model does not only repeat today's inequality. It **exaggerates** it, because it pushes toward the most frequent case.

### What feminist theory adds

- *claim (Catherine D'Ignazio and Lauren Klein, *Data Feminism*, MIT Press 2020, open access):* Data is never neutral. It reflects who collects it, for what purpose and under which power relations. Their principles include "examine power", "challenge power" and "make labour visible".
- *claim (Safiya Umoja Noble, *Algorithms of Oppression*, 2018):* Search and ranking systems present commercial and majority views as neutral results, and reinforce sexist and racist representations.
- *claim (Caroline Criado Perez, *Invisible Women*, 2019):* The "default human" in data is male. Where women are not counted, the gap is filled with assumptions.
- *claim (Joy Buolamwini, *Unmasking AI*, 2023):* The "coded gaze": the priorities and blind spots of those who build systems become the system's view of the world.

**Class line:** The statistical average of the internet is not neutral. It carries the gender order of the people who wrote, linked and moderated that internet.

### Labour and the gender gap

- *verified fact (Acemoglu, via MIT Sloan, Jan 2025, vault clipping "A new look at the economics of AI"):* Acemoglu expects AI's negative effects on workers to fall "particularly [on] women with low levels of education".
- See [[labour]] for the hidden annotation workforce and the first jobs that disappear.

---

## 5. The underground disappears

What is the underground here? Small scenes, local languages, zines, closed chats, club nights, queer and feminist spaces, niche archives, experimental work, anything deliberately not mainstream. Much of it is offline, behind logins, or too small to weigh in a training set.

*thesis, with evidence:*

1. **Missing from the data.** Spaces outside the big platforms are less likely to be scraped (Bender et al.). Filters remove what is coded as sexual or offensive, which hits queer and feminist spaces first.
2. **Averaged away.** Where rare material is in the data, high-probability sampling still favours the common case. Model collapse removes the tails first (Shumailov et al.).
3. **Flooded over.** As generated text and images fill the web, the next crawl contains more average and less underground. Each round is narrower.
4. **Converging users.** When many people use the same few models for ideas, their outputs converge (Doshi and Hauser). A scene that writes with the same assistant starts to sound like everyone else.
5. **Extraction instead of survival.** When an underground style does reach the data, it can be reproduced on demand by name, detached from its scene and its makers. That is visibility without the community. See *Glaze* and *Nightshade* in [[media-art-workflows]].

**Class line:** Culture has always renewed itself from the edges. A system that learns from the centre and feeds back into the centre starves the edges.

---

## 6. Counterarguments to test

The student group should test the thesis, not only repeat it.

- *open question:* Models can be prompted, fine-tuned or trained on small, cared-for datasets. Could a scene use its own local model to strengthen itself? (Counter-practices: SFPC *Handmade Datasets*, Holly Herndon's *Holly+*, community-owned models.)
- *open question:* Did platforms and recommendation algorithms flatten culture before generative AI? Is AI a new force or an accelerator?
- *open question:* Vendors now tune models to show more diverse people in images. Does that fix the norm, or paint over it? (Google paused Gemini image generation of people in February 2024 after over-correcting.)
- *open question:* Is "underground" partly a privilege of those who can afford to stay offline?

---

## 7. Student input: questions to pick from

For the Session 02 pair or group (see [[../../course-rhythm]]):

- Whose internet is the "average" of? Bring numbers on who writes Wikipedia, Reddit or the web in your language.
- Run the same prompt ("a judge", "an artist", "a nurse", "a genius") through two image or text models. What norm appears?
- Pick one underground scene you know. Is it in the model? What does the model make of it?
- Is AI killing the underground, or only making it harder to find?

---

## Sources

- Bender, Gebru, McMillan-Major, Mitchell, *On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?*, FAccT 2021: https://dl.acm.org/doi/10.1145/3442188.3445922
- Shumailov et al., *AI models collapse when trained on recursively generated data*, Nature 631, 2024: https://www.nature.com/articles/s41586-024-07566-y
- Doshi and Hauser, *Generative AI enhances individual creativity but reduces the collective diversity of novel content*, Science Advances 2024: https://www.science.org/doi/10.1126/sciadv.adn5290
- UNESCO and IRCAI, *Challenging Systematic Prejudices: An Investigation into Bias Against Women and Girls in Large Language Models*, 2024: https://www.unesco.org/en/articles/generative-ai-unesco-study-reveals-alarming-evidence-regressive-gender-stereotypes
- Nicoletti and Bass, *Humans Are Biased. Generative AI Is Even Worse*, Bloomberg, 2023: https://www.bloomberg.com/graphics/2023-generative-ai-bias/
- Buolamwini and Gebru, *Gender Shades*, PMLR 81, 2018: https://proceedings.mlr.press/v81/buolamwini18a.html
- D'Ignazio and Klein, *Data Feminism*, MIT Press 2020 (open access): https://data-feminism.mitpress.mit.edu/
- Noble, *Algorithms of Oppression*, NYU Press 2018
- Criado Perez, *Invisible Women*, 2019
- Buolamwini, *Unmasking AI*, 2023
- OpenAI, *Sycophancy in GPT-4o*, 2025: https://openai.com/index/sycophancy-in-gpt-4o/
- MIT Sloan, *A new look at the economics of AI* (Acemoglu), 2025: https://mitsloan.mit.edu/ideas-made-to-matter/a-new-look-economics-ai
