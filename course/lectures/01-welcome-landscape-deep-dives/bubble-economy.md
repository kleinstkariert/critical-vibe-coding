---
title: "Deep dive: Economy and the AI bubble"
date: 2026-11-09
updated: 2026-11-11
session: 1
block: 4
status: teaching-ready
tags:
  - course
  - lecture
  - deep-dive
  - political-economy
  - ai-bubble
  - data-centers
---

# Deep dive: Economy and the AI bubble

Block 4 of [[../01-welcome-landscape-lecture]]. This note collects the facts behind the block: how much is being spent, what is being built, how far revenue lags, who carries the debt, how earlier build-outs ended, the arguments for and against a burst, who gets the income, and the commons as an alternative.

Labels: *verified fact* (company filing, agency, central bank, peer-reviewed paper) | *claim* (speaker in a talk, podcast or video; checkable but not checked here) | *open question*.

**Base material**

| Source | Role |
|---|---|
| [[../../../research/ai-bubble-productivity-datacenter]] | Vault copy of the original discussion summary (`ai_bubble_productivity_datacenter_summary.md` from Downloads, placed 2026-10-18). BIS 137, Tooze, Van Nieuwerburgh, space data centres. |
| [[../../../research/data-centers-energy-ecology-economy]] | Siting, energy, planned versus energized capacity. |
| Vault clippings (teacher vault `KnowledgeBaseObsidian/Clippings/`) | Ezra Klein debate (Kedrosky, Azhar), Tooze Ep. 250 and 260, Richard Campbell keynote, DW with Ed Zitron, Be Smart, MIT Sloan on Acemoglu, PÖDcast with Peter Schadt. |
| Company earnings, October 2026 | Capex guidance for Amazon, Alphabet, Microsoft, Meta. |

---

## 1. The spending

*verified fact (company guidance, October 2026 earnings calls):* Amazon, Alphabet, Microsoft and Meta plan **$720 to 740 billion** of capital spending (capex) in calendar 2026.

| Company | 2026 capex guidance | Note |
|---|---|---|
| Amazon | about $220 billion | Company-wide cash capex; "meaningfully more" planned for 2027 |
| Alphabet | $195 to 205 billion | "Significantly" higher in 2027 |
| Microsoft | about $170 billion | Trimmed from about $190 billion because third-party capacity arrived late |
| Meta | $135 to 145 billion | Against about $72 billion in 2025 |

- *verified fact:* The same four spent roughly $225 billion in 2024 and $375 to 415 billion in 2025, depending on how leases are counted. 2026 is about **three times 2024**.
- *verified fact:* In the third quarter of 2026 alone they spent about **$209 billion**, 84% more than a year earlier.
- *claim (Business Insider, Oct 2026):* Adding SpaceX, which now includes xAI, the 2026 total reaches $803 to 828 billion.
- *claim (Trimline Research brief, Oct 2026):* Combined free cash flow of the four turned negative in Q3 2026 for the first time in at least a decade.
- *claim (Adam Tooze, Ones and Tooze Ep. 260):* AI now drives about 36% of all US business investment.
- *claim (Azeem Azhar, Ezra Klein Show):* About 65% of the cost of an AI data centre is the chips.
- *claim (Ezra Klein):* Apple spends about $15 billion a year on capex and has outperformed the big spenders on the stock market.

Most of this money goes to AI data centres and chips. The totals also include non-AI assets, and no company publishes an audited AI-only figure.

### What the spending does to US growth

Richard Campbell shows three charts in a row (*After the AI Hype: What's Real, and What's Next*, NDC Copenhagen 2026, about 32:20 to 33:10). The deck redraws them as slides 20 to 22.

| Campbell's chart | What it shows | Deck |
|---|---|---|
| "Hyperscaler Capex By Year" (company reports; 2025 with company and analyst projections) | Microsoft, Alphabet, Meta and Amazon together: about $24 billion in 2015, $151 billion in 2022, $228 billion in 2024, $325 billion projected for 2025. The same series as our chart from the 10-K filings | `28-bigtech-capex-chart.png` |
| "US real GDP growth contribution from tech capex" (Bridgewater, Aug 2025, via J.P. Morgan Asset Management, *Eye on the Market*) | Growth split into tech investment and the rest of the economy, 1Q23 to 2Q25, two-quarter rolling average. Tech capex grows from almost nothing to about 0.9 points; the rest of the economy slows from about 3% to about 1%. J.P. Morgan: tech capex was **35 to 45% of US GDP growth** in the last three quarters | `35-us-gdp-tech-capex-chart.png` (values read from the chart, approximate) |
| S&P 500 donut (Voronoi / Visual Capitalist, 2 Jan 2025, "The Magnificent Seven Propel 55% of S&P 500's 2024 Gains") | Contribution to the 2024 gain in market value: Nvidia 20.4%, Apple 7.8%, Amazon 7.3%, Alphabet 5.7%, Meta 5.6%, Tesla 5.0%, Microsoft 3.3%; the other 493 companies about 45% | `36-mag7-sp500-gains-2024.png` |

- *claim (Campbell, 32:46):* "In 2024, more than half of the increase in value in the S&P 500 came from seven companies."
- *claim (Jason Furman, Harvard, Oct 2025):* Investment in information-processing equipment and software was about 4% of US GDP but about 92% of GDP growth in the first half of 2025. This is the source of the line "almost all of current growth is based on AI investments". Bridgewater and J.P. Morgan count differently and arrive at 35 to 45%.

**Class line:** Without the data-centre build, US growth in 2025 would have been about 1%. The economy leans on the same few companies that the stock market leans on.

**Class line:** In 2026 four companies spend more on buildings and chips than Austria's entire economy produces in a year (Austrian GDP is roughly $550 billion; check the current IMF figure before class).

---

## 2. The construction

### Stargate Abilene, Texas: what one campus looks like

*verified fact (Oracle earnings call 10 Sep 2026; Epoch AI satellite register, Nov 2026):*

- About 1,000 acres of scrubland north of Abilene. Eight buildings, about 4 million square feet.
- About **824 MW** of IT capacity on **1.2 GW** of total power capacity.
- Construction started in June 2024. Six of eight buildings (618 MW) were delivered to OpenAI by September 2026; Epoch AI estimates all eight operational by November 2026.
- Epoch AI estimates a capital cost of about **$31 billion** and compute equal to more than one million Nvidia H100 chips.
- About 9,000 construction workers were on site daily in March 2026.
- Chain of owners: Lancium owns the land and builds the grid connection, Crusoe builds and co-finances, Oracle leases the buildings and installs the chips, OpenAI is the customer, Blue Owl and Primary Digital Infrastructure supply equity.

*claim (MeasuredAI analysis, Oct 2026):* Oracle's four other Stargate campuses supplied no capacity in the June to August 2026 quarter. Abilene is the exception that worked on schedule, not the norm.

### The national pipeline

- *claim (Be Smart / PBS, Oct 2026):* The US has 68 hyperscale data centres built or under construction and **267 more approved or planned**. "Hyperscale" means more than 100 MW, enough for about 80,000 US homes.
- *claim (Be Smart):* GW Ranch in West Texas plans 35 gas turbines and more than 7 GW of peak power. It would be the largest power plant in the US. See [[ecology]].
- *verified fact (IEA, Energy and AI):* Without grid fixes, about 20% of planned data-centre projects could face delay.
- *nuance (CBRE / Bloomberg, early 2026, via [[../../../research/data-centers-energy-ecology-economy]]):* Capacity actually under construction can fall while announced pipelines grow. Planned gigawatts are not energized gigawatts.

### Overbooking

- *claim (Richard Campbell, NDC keynote 2026):* Developers over-order "like Taylor Swift tickets": they buy land through third parties, request grid power and order chips before a customer exists. Some sites have a single girder standing so the project can be reported as "underway".
- *claim (Campbell):* Memory makers refused to double RAM production in 2025. A new chip factory takes three to five years, and they doubted the buyers would still be there.
- *claim (Campbell):* Microsoft's 2019 annual report already warned that it struggled to find places allowed to build data centres.

**Class line:** The build-out is real concrete, steel and turbines. The announcements run far ahead of it, and the money is committed before the demand is visible.

---

## 3. Spending ahead of revenue

- *verified fact (Acemoglu, "The Simple Macroeconomics of AI", NBER w32487; MIT Sloan summary):* About 5% of tasks can be done profitably by AI within ten years. Estimated effect: productivity +0.7%, GDP about **+1.1% over ten years**. Goldman Sachs had forecast +7% of global GDP, McKinsey $17 to 26 trillion a year.
- *claim (Paul Kedrosky, Ezra Klein Show):* US productivity growth is still at trend. No AI effect is visible in the statistics yet.
- *claim (Ed Zitron to DW, Oct 2026, from financials he says he obtained):* OpenAI lost about $21 billion in 2025. Anthropic lost about $8 billion on $4.6 billion of revenue.
- *claim (Zitron):* Anthropic's headline "run rate" of $65 billion compares with about $11.5 billion of revenue in Q2 2026.
- *claim (Zitron):* About 80% of OpenAI's and Anthropic's revenue comes from AI start-ups that are themselves unprofitable.
- *claim (Azhar and Klein):* About 2.5% of Americans pay for an AI subscription.
- *claim (Kedrosky):* Performance-adjusted token prices fall about 13-fold a year, so each unit of use earns less.
- *claim (Peter Schadt, PÖDcast Ep. 20):* Roughly $3 trillion invested against roughly $50 billion of revenue. Order of magnitude only.

**Class line:** The spending is counted in hundreds of billions per year. The revenue is counted in tens of billions. The productivity gain economists can measure so far is small.

---

## 4. Debt, circular money, and who carries the risk

### From cash to debt

- *claim (Kedrosky):* AI spending is shifting from cash flow to borrowing. Tech is now the largest issuer of investment-grade bonds in the US, and ten-year hyperscaler bonds compete with US Treasuries.
- *claim (Kedrosky and Klein):* Meta keeps data-centre debt off its balance sheet in special purpose vehicles (SPVs). Oracle's credit rating sits just above junk.
- *claim (Kedrosky):* AI-related credit already runs to trillions of dollars and may reach $10 trillion, held by insurers, private-credit funds and sovereign wealth funds.
- *claim (Azhar):* External finance approaches 30% of hyperscaler spending by the end of 2026. He had named 30% as his own warning threshold.
- *verified fact (Van Nieuwerburgh, Princeton Bendheim / Columbia "Financing the AI Buildout"):* Data centres are financed through leases, project finance, private credit and SPVs. The research asks where the losses land if revenue does not arrive. Details: [[../../../research/ai-bubble-productivity-datacenter]] §10.

### Money that circulates inside the sector

- *verified fact (BIS Bulletin 137, 1 Oct 2026):* 55.2% of the investment AI firms received in 2021 to 2025 came from other AI firms. 28.7% of AI firms' outgoing investment went to other AI firms. Of AI-to-AI deals by value, 46.4% also had a supplier and customer link.
- *claim (Campbell):* Microsoft put $13 billion into OpenAI in three steps (2019, 2020, 2023). The first billion had to be spent on Microsoft's own Azure cloud.
- *claim (Campbell, Tooze):* Nvidia invests $100 to 500 million at a time in AI firms that then order Nvidia chips.
- *verified fact (Bloomberg, Emily Forgash and Agnee Ghosh, "OpenAI, Nvidia Fuel $1 Trillion AI Market With Web of Circular Deals", 7 Oct 2025):* Bloomberg's graphic *How Nvidia and OpenAI Fuel the AI Money Machine* maps the deals as arrows between circles sized by market value. Nvidia agrees to invest up to $100 billion in OpenAI, which fills its data centres with Nvidia chips. OpenAI signs a $300 billion cloud deal with Oracle, which spends tens of billions on Nvidia chips. AMD gives OpenAI an option on up to 160 million AMD shares while OpenAI deploys 6 GW of AMD GPUs. Nvidia also buys cloud capacity from CoreWeave, in which it holds shares. Sebastian added the graphic to the deck (slide 28, `33-bloomberg-circular-ai-deals.png`); Campbell shows it at about 33:45.
- What "circular" means in plain words: firm A invests in firm B, and B spends the money on A's products. A reports the purchase as revenue. Demand looks larger than the money that comes from outside the circle.

### Central banks

- *verified fact (Bank of England, reported by DW, Oct 2026):* Markets are increasingly exposed to AI; a reassessment could trigger a sharp fall in asset prices.
- *claim (Tooze, Ep. 250, citing the BIS Annual Economic Report 2026):* Data centres connect to the grid "a gigawatt at a time", and the BIS names AI investment as an inflationary pressure, for example on electricity in Virginia.

---

## 5. Concentration of value

- *claim (Kedrosky):* The ten largest companies make up about 40% of the S&P 500. About half of US household net worth is in stocks, a record. Households are more exposed than in the dot-com years.
- *claim (Campbell):* In 2024 more than half of the S&P 500's gain came from the "Magnificent Seven".
- *verified fact (Shiller CAPE data, Yale and multpl.com, 9 Nov 2026):* US stocks cost about **40 years of average profit**. The peak before the 1929 crash was about 33, the peak of the dot-com bubble in 2000 about 44. Kedrosky ("1929 levels") and Campbell ("second only to 2000") describe the same number. Chart: `29-shiller-cape-chart.png`.

### How to read the CAPE chart

CAPE stands for cyclically adjusted price-to-earnings ratio (Robert Shiller).

- **What is divided by what.** The y-axis is the price of the S&P 500 divided by the average yearly profit (earnings) of its companies over the **past ten years**. Both are adjusted for inflation.
- **What the ten years are.** Only the averaging window. A single boom year or recession year would make a one-year ratio jump; ten years smooth that out. The 10 is not a line on the chart and not a threshold.
- **What a value means.** 44 in 2000 means buyers paid 44 times the average yearly profit. Put differently: if profits stayed at that ten-year average, it would take 44 years of profit to add up to the price. Today about 40 means about 40 years.
- **What it does not mean.** It does not say whether firms are profitable. The ratio is positive whenever they make a profit, so "above 10" does not mean "profitable", and values around 10 to 20 for most of history do not mean the firms were losing money. It says how expensive the shares are compared with the profit behind them.
- **The scale.** Long-run average since 1881: about 18 (computed from the chart data). Cheap moments: about 5 in 1920 and about 7 in 1982. Expensive moments: about 33 in 1929, about 44 in 1999 and 2000, about 40 now.
- **The other way round.** 1 divided by CAPE is the earnings yield: at 40, each dollar invested buys 2.5 cents of yearly profit; at the long-run average, about 5.5 cents.
- **What it predicts.** Historically, a high CAPE was followed by low average returns over the next ten years. It does not tell you when a crash comes: the ratio stayed above 25 for most of the years since 1995.

Sebastian's question, answered: in 2000 it would not take 44 years to earn back what was *spent in 10 years*. It would take about 44 years of *average profit* to earn back the *share price*. The ten years are only how the average profit is measured.
- *claim (Kedrosky):* An IPO of OpenAI, Anthropic and SpaceX together would be larger than all post-war US IPOs combined.
- *verified fact (Verdegem 2022, AI & Society, from ycharts):* Between 2010 and 2021 the market value of Apple grew from about $238 billion to $2.2 trillion, Amazon from $63 billion to $1.7 trillion.

---

## 6. How earlier build-outs ended

- *claim (Kedrosky):* Western economic history has eight or nine big build-outs of general-purpose technology: canals, railways, electrification, highways, telecom fibre. Each ended in oversupply and crisis.
- *claim (Kedrosky):* About half of all US railroad track miles ever laid turned out useless, partly because competitors built parallel lines between the same cities.
- *claim (Campbell):* After 2000 most firms that built internet infrastructure went bankrupt. Their fibre was bought for about 10 cents on the dollar.
- *verified fact (company 10-K filings):* Hyperscalers depreciate servers over about five to six years. Amazon shortened part of its server life from six to five years in 2025. Rails and fibre lasted decades; chips last years.
- *claim (Azhar):* At current "surge" rental prices a GPU pays for itself in 18 to 24 months. About half of hyperscaler GPU rental revenue comes from OpenAI and Anthropic.
- *claim (Zitron):* AI data centres are good for one thing. Unlike dark fibre, they leave little for other uses if the demand does not come.
- *claim (Be Smart, Koomey):* Forecasts overshoot too: in 1999 critics claimed the internet would use half of US electricity. The real figure for the whole IT sector was about 3%.

### The US railroads: build-out, then receivership

The deck shows Samuel Augustus Mitchell Jr.'s *Railroad map of the United States* (1884, David Rumsey Map Collection, slide 27). It replaces the London Metropolitan Railway map of 1867, which showed one city line and could not carry a national overbuild.

- *verified fact (Interstate Commerce Commission, Seventh Annual Report on the Statistics of Railways, 1894):* On 30 June 1894, **192 railroads** with more than **42,000 miles** of line were in the hands of receivers: about a quarter of all US railway capital. Total US mileage was about 178,700.
- *verified fact (Stuart Daggett, Railroad Reorganization, 1908):* In 1893 alone courts took over more than 27,000 miles. Northern Pacific, Union Pacific and the Atchison, Topeka and Santa Fe all went into receivership in 1893.
- How it happened: in the 1870s and 1880s companies raised bonds to lay competing lines between the same cities and across the continent, each betting on the same traffic. The Panic of 1893 cut traffic and credit at once. Banks, J. P. Morgan's first among them, bought and merged the bankrupt lines cheaply ("Morganization").
- What stayed: the track. The investors lost; the network was used for another century. The AI difference: chips are written off in five to six years.

On the map: the dense web in the northeast and Midwest, and several transcontinental lines running side by side through the West.

### The hype cycle

Campbell frames the whole talk with the Gartner Hype Cycle (from 18:42, and again at 29:40). The deck shows it on slide 18, with its explanation on the same slide.

- **The model.** Gartner analyst Jackie Fenn drew the curve in 1995. It has five phases: *technology trigger*, *peak of inflated expectations*, *trough of disillusionment*, *slope of enlightenment*, *plateau of productivity*. It is a qualitative model, not measured data: the y-axis is "expectations", and nobody measures it. Gartner publishes new curves every year, and many technologies never reach the plateau.
- *claim (Campbell, 18:53 to 19:31):* A technological event "brings all the investors to the yard"; "stupid money makes stupid decisions". Firms have to make bigger and bigger promises to investors until the peak. When the promises cannot be met, the money flows back out and many companies fail.
- *claim (Campbell, 19:35 to 20:22):* The dot-com cycle ran from 1997 to 2001, triggered by the Netscape IPO, the first big pure-software listing. The web survived the crash.
- *claim (Campbell, 20:25 to 21:06):* "Doesn't happen every time." Mobile and the cloud were revolutions without a hype cycle. A hype cycle needs investors who do not understand what they are buying, so you can tell them stories and set "insane" expectations: "Every job will be replaced in the next 2 years". AI "fits that category brilliantly".
- *claim (Campbell, 29:41):* "I think we're headed down the trough of disillusionment just fine, far from bottomed out." Signs: price changes, less free use, more paid use.
- *claim (Campbell, 30:23 to 30:55):* In both booms, the hype paid for infrastructure. In the dot-com years: data centres and undersea cables; most of those firms went broke, and the cables were bought for 10 cents on the dollar. Now: AI data centres.

**Class line:** Every large infrastructure boom so far has overbuilt. This one builds faster, with shorter-lived hardware, and with more of it on credit.

---

## 7. Will it burst? Arguments for and against

Main sources: the Ezra Klein Show debate between Paul Kedrosky (bubble) and Azeem Azhar (more optimistic), 16 Oct 2026, and Richard Campbell's NDC keynote *After the AI Hype*, June 2026. Timestamps refer to the videos. Most points are *claims* by the speakers; filings or data that could check them are named.

Azhar's definition helps: a burst means investment falls by half and the relevant market by half or more. Low returns alone are not a burst (21:23).

### For a burst: a crash or a sharp correction

1. **History.** Every large build-out (canals, railways, electrification, fibre) ended in oversupply and crisis. About half of all US railroad track miles turned out useless. "There isn't a major economic CapEx episode in Western economic history that didn't end in a rolling series of crises." Kedrosky (2:24).
2. **A race guarantees overcapacity.** No firm can slow down alone, so all of them overbuild: "you're guaranteed overcapacity." Kedrosky (7:10). Zuckerberg accepts "misspending a couple hundred billion dollars" as the price (Klein, 5:23).
3. **Over-ordering.** Developers order land, power, concrete and chips "the same way you would buy Taylor Swift tickets"; a single girder lets a project count as underway. Campbell (35:10). The US has 68 hyperscale campuses built or under construction and 267 approved or planned (Be Smart).
4. **Revenue far behind spending.** Hundreds of billions a year in capex against tens of billions in revenue. "None of these companies are profitable, not even close." Campbell (28:36). Anthropic's $65 billion "run rate" compares with about $11.5 billion of revenue in Q2 2026 (Zitron to DW).
5. **Few customers, falling prices.** Perhaps eight customers make up 80% of a frontier lab's revenue, and coders make up about 80% of token use. Performance-adjusted token prices fall about 13-fold a year. "Never confuse your early customers for what the real market will look like." Kedrosky (14:52, 29:57).
6. **Circular money.** Nvidia invests in AI firms that then order Nvidia chips: "I just made $500 into $1 billion." Campbell (33:11). 55.2% of the money AI firms raised in 2021 to 2025 came from other AI firms (*verified fact:* BIS Bulletin 137).
7. **Debt and off-balance-sheet vehicles.** Spending shifts from cash flow to borrowing. "Tech is now the largest issuer of investment-grade bonds in the United States." Meta parks data-centre debt in special purpose vehicles; Oracle sits just above junk. Kedrosky (37:34).
8. **Ordinary savers carry the risk.** The ten largest stocks are about 40% of the S&P 500; about half of US household wealth is in stocks, a record. Shares cost about 40 years of average profit: more than in 1929 (33), less only than in 2000 (44) (*verified fact:* Shiller CAPE; reading explained in section 5). The OpenAI, Anthropic and SpaceX listings would be larger than all post-war US IPOs combined, and are "exit events" for insiders. Kedrosky (3:57, 22:09, 26:32).
9. **Short-lived assets.** Chips are written off in five to six years. Data centres are "useful for basically one thing", unlike dark fibre after 2000. Zitron (DW, 8:03).
10. **The hype is already turning.** In Q1 2026 big-tech profits dipped and pension funds began "backing out a little". Memory makers refused to double production because "we don't think you guys are going to be around". Campbell (34:52, 36:16).

### Against a burst

1. **Compute is scarce, not in surplus.** "There is vast vast undersupply of the compute." Azhar (8:32).
2. **The chips pay back fast.** At current "surge" rental prices a GPU pays for itself in 18 to 24 months. Azhar (11:34).
3. **Demand is broadening.** OpenAI and Anthropic's share of GPU rental revenue is falling as other companies pay: "a market that is maturing week after week." Anthropic's Q1 2026 revenue exceeded its whole 2025 revenue. Azhar (12:18, 30:12). Checkable in the Anthropic S-1 filing.
4. **The buildings get used anyway.** If customers switch to cheaper open models run by hyperscalers, the data centres still earn. Klein: "Anthropic might collapse, but Nvidia will be fine." (18:49)
5. **Debt is still limited.** External finance is just reaching Azhar's 30% warning threshold, a sign to watch, not a crash signal. The hyperscalers can absorb losses from their other businesses. Azhar (41:22); Klein (36:55).
6. **No stampede yet.** Institutional investors are trimming, "not running for the hills". Valuations are "not as out of whack as it was in 2000". Campbell (36:16, 36:58).

What would change each mind: Azhar turns bearish if enterprise AI spending growth halves two quarters in a row (1:02:19). Kedrosky points to the S-1 customer list: if a few customers dominate, his case holds (31:11).

**Class line:** The case for a burst rests on history, debt and the revenue gap. The case against rests on scarce compute and fast payback. Both sides agree the money is real and the build-out is enormous.

---

## 8. Charts for class

Generated by `01-welcome-landscape-slideshow/make_images.py`, white on black, source printed on each.

| Chart | Data | Label |
|---|---|---|
| `34-hype-cycle.png` | Gartner-style hype cycle (Fenn, 1995) with Campbell's placement of AI in 2026. Shown beside its explanation on one slide | *model*, placement *claim* |
| `28-bigtech-capex-chart.png` | Capex of Amazon, Alphabet, Microsoft, Meta, 2016 to 2025 from 10-K filings (cash purchases of property and equipment, fiscal years), 2026 guidance | *verified fact* |
| `35-us-gdp-tech-capex-chart.png` | US real GDP growth, tech investment against the rest, 1Q23 to 2Q25 (Bridgewater via J.P. Morgan, redrawn; values read from the chart) | *verified fact* (approximate reading) |
| `36-mag7-sp500-gains-2024.png` | Share of the S&P 500's 2024 market-value gain by company (Voronoi) | *verified fact* |
| `29-shiller-cape-chart.png` | Shiller CAPE ratio, monthly 1881 to Nov 2026 (Yale data, then multpl.com), with the long-run average and a reading line | *verified fact* |
| `30-bis-labour-share-scenario.png` | Bank for International Settlements (BIS) Annual Economic Report 2026, Graph C1.B, redrawn with plain labels. Values read from the chart | *verified fact* (scenario, not forecast) |

Capex series, $ billion: 2016: 31 · 2017: 40 · 2018: 64 · 2019: 69 · 2020: 93 · 2021: 125 · 2022: 150 · 2023: 140 · 2024: 217 · 2025: 358 · 2026 planned: 720 to 740. Filings do not separate AI from other spending. Finance leases are not included, so company headlines run higher.

---

## 9. Who gets the income: Tooze and the BIS

- *claim (Adam Tooze, Ones and Tooze Ep. 250, Foreign Policy, July 2026, from 32:33):* Tooze reads the AI boom as "a two-way bet on disaster either way". Either the investment is vindicated, and then "the labor market [is shaken] to its foundations", or it is not, and the companies are overvalued and losses land somewhere in the chain (3:51).
- *verified fact (BIS Annual Economic Report 2026, Box C, Graph C1.B):* The Bank for International Settlements, the central bank of central banks, models a "transformative AI" scenario in which the **labour share of income** falls from about **60%** today toward about **20%** by 2060. In a "demand bottleneck" scenario it falls to about 47%. The report says the labour share "falls towards zero" in the transformative case. This is a model scenario, not a forecast.
- *claim (Tooze, 33:30):* "That 20% share which is a third of the 60% average which is currently prevailing in advanced economies [...] will not necessarily mean that the wages of those employed goes down but it'll mean that the share in the total pie collapses and that's obviously a huge transformation in political power."
- In other words: today about 60% of income goes to wages and about 40% to owners of capital. In the scenario where the hype comes true, it is about 20% to wages and 80% to capital.

### The three lines of the BIS chart, in plain words

| Line | What the model assumes | Labour share |
|---|---|---|
| Business as usual | AI gives a bounded productivity boost, like earlier office software | stays at about 60% |
| Transformative AI | Machines take over most tasks; the money from automation is reinvested in more automation | falls toward about 20% by 2060, and toward zero in the long run |
| **Demand bottleneck** | Automation shifts income from wages to the owners of machines. But every worker who loses income is also a customer who buys less. When spending falls, it stops paying to automate the next task, so automation stalls | falls to about 47% and stays there; growth stays below the boom path |

- *verified fact (BIS Annual Economic Report 2026, Box C):* the report's own phrase is that every displaced worker is also a lost consumer. The bottleneck is not a policy; it is the market braking itself because demand is missing.
- *verified fact (BIS Working Paper 1381, Rungcharoenkitkul 2026):* depending on the scenario, the labour task share falls from 60% to between 15% and 50% within three decades.
- On the slide: "**Demand bottleneck:** replaced workers stop buying, so more automation stops paying. The fall stops near 47%."

The auto-transcript is rough; check the exact wording against the audio around 32:33 before quoting on a slide.

**Class line:** If AI delivers what its investors promise, income moves from wages to owners. The BIS draws the curve: from 60% to 20%.

---

## 10. An alternative: AI as a commons

- *claim (Pieter Verdegem, "Dismantling AI capitalism: the commons as an alternative to the power concentration of Big Tech", AI & Society, published online April 2022, open access):* AI is a general purpose technology, like electricity. A few firms hold the three things it needs: data, computing power and talent. Verdegem calls this AI capitalism.
- *verified fact (same, from CB Insights):* AI start-up acquisitions since 2010: Apple 29, Google 15, Microsoft 13, Facebook 12, Amazon 7.
- *claim (same):* The alternative is a commons, after Elinor Ostrom: data commons and data trusts, public computing capacity, public money that keeps AI research in universities, platform cooperatives, democratic governance. "Communities and workers should be involved in determining what sort of work should or should not be automated."
- Read: https://pmc.ncbi.nlm.nih.gov/articles/PMC8994059/

**Class line:** The question is not only whether the bubble bursts, but who owns what is left.

---

## 11. Quotes usable in class

1. "There isn't a major economic CapEx episode in Western economic history that didn't end in ... vast oversupply of capacity." Paul Kedrosky, Ezra Klein Show, Oct 2026.
2. "If we end up misspending a couple hundred billion dollars, that would be unfortunate." Mark Zuckerberg, as quoted by Ezra Klein.
3. "None of these companies are profitable, not even close." Richard Campbell, NDC keynote 2026.
4. "The cost of the power is immaterial to the investment." Interviewee, Be Smart, Oct 2026.
5. Amazon CEO Andy Jassy called the 2026 spending a "once in a lifetime opportunity" (Q3 2026 earnings call, via The Verge).
6. "There is vast vast undersupply of the compute." Azeem Azhar, Ezra Klein Show, Oct 2026.
7. "It's a kind of two-way bet on disaster either way." Adam Tooze, Ones and Tooze Ep. 250.

---

## 12. Questions for the room

- Your subscription costs about €20 a month. Who pays the rest of the cost of your prompt?
- If the revenue does not come, who holds the debt: the tech firms, pension funds, insurers, or the towns with new substations?
- What would an AI tool cost you if it were priced at what it costs to run?

---

## Sources

**Company and market data (October 2026)**
- The Motley Fool, *How much are AI companies spending on data centers?* https://www.fool.com/research/ai-companies-spending-on-data-centers/
- Yield Theory, AI capex dataset with primary filings per figure: https://www.yieldtheory.app/datasets/ai-capex
- Business Insider, hyperscaler capex up to $828B in 2026: https://www.businessinsider.com/amazon-alphabet-meta-microsoft-spacex-capex-ai-spending-total-2026-10
- The Verge, Q3 2026 earnings: https://www.theverge.com/ai-artificial-intelligence/1027344/amazon-microsoft-alphabet-google-meta-data-centers-earnings-q3
- Trimline Research, *The $800 Billion Bet*: https://trimlineresearch.com/the-800-billion-bet-research-brief/

**Stargate Abilene**
- fDi Intelligence: https://www.fdiintelligence.com/content/60563588-7373-45f7-9b1b-25bbcd1156aa
- Epoch AI register via Compute Terminal: https://compute-terminal.com/datacentres/site/openai-stargate-abilene
- Data Center Census: https://datacentercensus.com/dc/stargate-abilene-tx
- MeasuredAI, Oracle's 5 GW Stargate build-out: https://measuredai.substack.com/p/oracle-stargate-buildout

**Charts shown by Campbell, and the railroads**
- Bloomberg, *OpenAI, Nvidia Fuel $1 Trillion AI Market With Web of Circular Deals* (Forgash, Ghosh), 7 Oct 2025: https://www.bloomberg.com/news/features/2025-10-07/openai-s-nvidia-amd-deals-boost-1-trillion-ai-boom-with-circular-deals
- J.P. Morgan Asset Management, *Eye on the Market* (Bridgewater chart of tech capex in US GDP growth, Aug 2025): https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/eye-on-the-market/
- Voronoi (Visual Capitalist), *The Magnificent Seven Propel 55% of S&P 500's 2024 Gains*, 2 Jan 2025: https://www.voronoiapp.com/
- Gartner, Hype Cycle methodology: https://www.gartner.com/en/research/methodologies/gartner-hype-cycle
- Interstate Commerce Commission, *Seventh Annual Report on the Statistics of Railways in the United States* (year to 30 June 1894); Stuart Daggett, *Railroad Reorganization* (1908)
- Mitchell, *Railroad map of the United States* (1884), David Rumsey Map Collection: see `../01-welcome-landscape-slideshow/images/ATTRIBUTION.md`

**Institutions and papers**
- Bank for International Settlements (BIS) Annual Economic Report 2026, Box C, *Transformative AI, long-term growth and r-star*: https://www.bis.org/publications/aer-2026.pdf
- BIS Working Paper 1381 (Rungcharoenkitkul 2026): https://www.bis.org/publ/work1381.htm
- BIS Bulletin 137: https://www.bis.org/publications/bulletin-137-circular-relationships-among-ai-firms
- Robert Shiller, online data: http://www.econ.yale.edu/~shiller/data.htm · monthly continuation: https://www.multpl.com/shiller-pe/table/by-month
- Capex from SEC filings, compiled: https://500metrics.com/capex · https://chartedfacts.com/charts/big-tech-capital-expenditure
- Acemoglu, *The Simple Macroeconomics of AI*: https://www.nber.org/system/files/working_papers/w32487/w32487.pdf
- MIT Sloan, *A new look at the economics of AI*: https://mitsloan.mit.edu/ideas-made-to-matter/a-new-look-economics-ai
- Columbia, *Financing the AI Buildout*: https://business.columbia.edu/faculty/research/financing-ai-buildout
- Verdegem, *Dismantling AI capitalism*: https://pmc.ncbi.nlm.nih.gov/articles/PMC8994059/

**Talks and video (vault clippings)**
- Ezra Klein Show, *Is There an A.I. Bubble? A Debate* (Kedrosky, Azhar): https://www.youtube.com/watch?v=9GLdGc9OX-A
- Ones and Tooze Ep. 250, AI arms race: https://www.youtube.com/watch?v=QevC7OrdJP8
- Ones and Tooze Ep. 260, AI regulation: https://www.youtube.com/watch?v=EHU8vXCAsyo
- Richard Campbell, *After the AI Hype: What's Real, and What's Next*, NDC Copenhagen 2026: https://www.youtube.com/watch?v=uWnUnMphmPM (hype cycle 18:42 and 29:40; capex, GDP and S&P 500 charts 32:20 to 33:10; Bloomberg graphic 33:45)
- DW News, *What if the skeptics are right about AI* (Zitron): https://www.youtube.com/watch?v=JUY8NJ7gNAo
- Be Smart, *The Real Cost of AI Will Shock You*: https://www.youtube.com/watch?v=YgoiujmwLKI
- Adam Tooze, *Boom, Bubble, Burst?*: https://www.youtube.com/watch?v=L4--A3hhOws

Update the capex table before class; guidance changes every quarter.
