---
title: "Deep dive: Ecology"
date: 2026-11-09
session: 1
block: 5
status: teaching-ready
tags:
  - course
  - lecture
  - deep-dive
  - ecology
  - data-centers
  - energy
---

# Deep dive: Ecology

Block 5 of [[../01-welcome-landscape-lecture]]. What AI costs in electricity, gas, water, land and neighbourhoods, and which part of that a student's daily use touches. The student input on the ecology of AI is in Session [[../../sessions/06-agent-as-interface|06]]; the earlier full unit with exercises is archived: [[../../sessions/archive-13-session-plan/11-local-ecology-when-not]]. This note is the Session 01 version with the facts students should hear on day one.

Labels: *verified fact* (IEA, US Congressional Research Service, EIA, peer-reviewed paper) | *claim* (video, interview, industry estimate) | *open question*.

**Base material**

| Source | Role |
|---|---|
| [[../../../research/data-centers-energy-ecology-economy]] | Course handout: IEA numbers, siting, scopes, built versus planned. |
| Be Smart / PBS, *The Real Cost of AI Will Shock You* (2026-10-22), vault clipping with transcript | Water, gas turbines, neighbours, tax breaks. Treat figures as *claim* unless traced to an agency. |
| Crawford and Joler, *Anatomy of an AI System* (2018) | The material chain beyond electricity: minerals, factories, labour, waste. Block 2 entry image. |
| [[bubble-economy]] | The money side of the same build-out. |

---

## 1. Small globally, large locally

- *verified fact (IEA, Energy and AI, 2025):* Data centres used about **415 TWh** in 2024, about **1.5% of world electricity**. The US accounts for about 45% of that, China about 25%, Europe about 15%.
- *verified fact (IEA base case):* Data-centre electricity roughly doubles to about 945 TWh by 2030, still under 3% of world use. The US and China make up about 80% of the growth.
- *verified fact (IEA):* In the US, data centres account for nearly **half of all electricity-demand growth to 2030**.
- *verified fact (IEA):* Nearly half of US data-centre capacity sits in **five regional clusters**, among them Northern Virginia, Texas and Phoenix.
- *claim (Be Smart):* US data centres used 4.7% of US electricity in 2024. Their use tripled between 2014 and 2024. One forecast puts them at 7 to 12% by 2028.
- *claim (Be Smart interviewee):* An AI server rack draws 5 to 30 times the power of a conventional rack. One fridge-sized GPU rack uses as much electricity as about 65 houses.

**Class line:** A national share of a few percent hides a local share that can decide whether a county needs a new power plant.

---

## 2. Gas behind the fence

- *verified fact (US CRS FAQ R49326):* Where data centres propose their own on-site generation, it is mostly **natural gas** turbines and engines, because gas is dispatchable and can be built in about one to three years.
- *verified fact (EIA, Annual Energy Outlook 2026):* US use of gas for power rises, largely because of data-centre expansion.
- *claim (Be Smart, citing IEA satellite analysis):* About a quarter of announced builds plan their own power plants. Only 2 to 3% of that capacity is running, but about a quarter of the planned plants have broken ground.
- *claim (Be Smart):* **GW Ranch**, West Texas (Amazon with Pacifico Energy): 35 gas turbines, more than 7 GW of peak power. It would be the largest power plant in the US and burn more than 1% of all US natural gas. Heise reported the plan in German; render in the slide deck.
- *claim (Be Smart):* An Abilene, Texas campus plans 50 turbines.
- *claim (energy researcher in Be Smart):* "I can build a solar battery plant in 18 months", against a wait of up to seven years for a new gas turbine. The race favours whatever is fastest to connect.

**Class line:** The fastest way to power AI today is to burn gas on site. The climate cost is global; the exhaust is local.

---

## 3. Water

- *verified fact (Ren et al. 2023, explained by co-author Shaolei Ren in Be Smart):* The "one bottle of water per prompt" figure comes from a 2023 GPT-3 study: about 500 ml for 30 medium-length queries, most of it indirect water used to generate the electricity. It should not be generalised to every prompt or model.
- *claim (Be Smart):* US data centres used about 17 billion gallons of water directly in 2023. Including power generation it was about 228 billion gallons, roughly two thirds of New York City's yearly drinking water.
- *claim (Be Smart):* Phoenix data centres use about 385 million gallons a year for cooling, possibly rising to 3.7 billion. Phoenix takes about half its water from the Colorado River, which has lost about a quarter of its flow.
- *claim (Be Smart):* One Abilene campus needed a one-time fill of 8 million gallons for its closed-loop cooling, about a third of the city's daily use.
- *claim (Shaolei Ren):* Cooling trades water against electricity. Evaporative cooling saves power but uses most water in summer, exactly when small local water systems are at their limit.

**Class line:** Water cannot be shipped in from elsewhere the way electricity can. "We cannot create a new water." (Shaolei Ren)

---

## 4. Neighbours

- *claim (Be Smart):* xAI's Colossus in Memphis, in a historically Black neighbourhood, ran up to 35 gas turbines while permitted for 15. Local reporting linked it to a 30 to 60% rise in smog.
- *claim (Be Smart, citing a 2024 analysis):* Data-centre air pollution could contribute to about 1,300 premature deaths in the US. The course handout treats this as an estimate, not settled epidemiology.
- *claim (Be Smart):* Projects arrive through shell companies and NDAs. Meta negotiated Texas tax breaks through firms named "Winner" and "Wurldwide"; officials in Pine Island, Minnesota knew about a project for two years before residents did.
- *claim (Be Smart):* 38 US states offer data-centre tax incentives. Loudoun County, Virginia reports about $1 billion a year in data-centre tax revenue.
- *claim (Kedrosky and Azhar, Ezra Klein Show):* A multi-billion-dollar data centre employs a handful of permanent staff. One New Mexico site cost about $4 million in subsidies per job.

**Class line:** The benefits are counted in tax revenue and shareholder value. The costs are counted in noise, air, water and electricity bills next door.

---

## 5. Emissions

- *claim (Be Smart):* US data centres emit about 0.5% of US greenhouse gas. AI-related emissions could reach 44 Mt CO2 by 2030, double 2025, comparable to about 10 million extra cars.
- Emissions are counted in three scopes: **Scope 1** on-site combustion (turbines, diesel backup), **Scope 2** grid electricity (depends on the local mix), **Scope 3** embodied carbon in concrete, steel and chips.
- *nuance:* Company totals are self-reported and often use renewable certificates bought elsewhere. Treat corporate "net zero" statements as *claim* unless there is audited, location-level data.

---

## 6. Materials and the full chain

- *verified fact (Crawford and Joler, Anatomy of an AI System, 2018):* One voice assistant (Amazon Echo) depends on mining, smelting, component factories, shipping, cloud infrastructure, data labelling and, at the end, e-waste dumps. The map traces each step and the labour inside it.
- *open question:* The course has no reliable per-model figures for chip minerals or e-waste yet. Say so rather than fill the gap with a guess.

---

## 7. What a student's use touches

- *verified fact (Luccioni, Jernite and Strubell, FAccT 2024, arXiv 2311.16863):* Training a model is rare and huge. **Inference**, the daily use, is small per request and adds up across millions of users. Generating images uses far more energy than classifying or summarising text; general-purpose models use more than small task-specific ones for the same job.
- *verified fact (Koomey, in Be Smart):* Computations per kWh doubled about every 1.6 years since the 1940s. Efficiency gains are real, and they also make more use affordable (Jevons paradox), so total consumption can still rise.
- Long agent runs, image and video generation multiply the number of tokens and requests. A two-hour agent session is not a single prompt.

**Three questions for any tool:**

1. Where is the rack?
2. What powers it?
3. Who lives next door?

---

## 8. From Linz

- *verified fact (IEA):* Europe hosts about 15% of data-centre electricity use. Most frontier training and inference runs in the US and China.
- Students in Austria mostly use models served from US clusters. The carbon is global; the water and smog stay in Texas, Virginia or Arizona.
- Local and open models move part of the load onto your own hardware and grid, where you can see it. Sessions [[../../sessions/03-hardware-open-models-prompting|03]] and [[../../sessions/06-agent-as-interface|06]].

---

## 9. Quotes usable in class

1. "Data centers to me are like the exhaust pipes of the AI industry." Interviewee, Be Smart.
2. "We cannot create a new water, and it's not like electricity." Shaolei Ren, Be Smart.
3. "Data center electricity use is a very local phenomenon." Interviewee, Be Smart.

---

## 10. Questions for the room

- Would you accept a data centre in your own district? On what conditions?
- Which of your weekly AI uses could run on a smaller or local model?
- When is not using AI the ecological choice for a project?

---

## Sources

- IEA, *Energy and AI* (2025), executive summary: https://www.iea.org/reports/energy-and-ai/executive-summary
- US Congressional Research Service, *Data Centers and the Electricity Grid* (R49326): https://www.congress.gov/crs-product/R49326
- Luccioni, Jernite, Strubell, *Power Hungry Processing* (arXiv 2311.16863): https://arxiv.org/abs/2311.16863
- Be Smart / PBS, *The Real Cost of AI Will Shock You*: https://www.youtube.com/watch?v=YgoiujmwLKI · sources page: https://sites.google.com/view/data-centers-impacts/home
- Pulitzer Center / Texas Tribune, *The next Texas gold rush*: https://pulitzercenter.org/projects/next-texas-gold-rush-data-centers-and-their-impacts
- heise online, Amazon gas plant for GW Ranch: https://www.heise.de/news/Amazon-plant-gigantisches-Gaskraftwerk-fuer-neues-KI-Rechenzentrum-11404032.html · project page: https://www.pacificoenergy.com/gw-ranch
- Crawford and Joler, *Anatomy of an AI System*: https://anatomyof.ai/
- Course handout: [[../../../research/data-centers-energy-ecology-economy]]

Update IEA and pipeline numbers before class; both move quickly.
