---
title: EU AI Act and Datenschutz (Austria)
date: 2026-10-21
tags:
  - course
  - regulation
  - privacy
  - austria
  - eu
---

# EU AI Act and Datenschutz (Austria)

English course note. **Primary official pages are often German** — links below stay in the original language. This is orientation for artists/students, not legal advice.

Use with: session 1 (regulation discourse) · session [[sessions/09-authorship-labour-platforms]] · session [[sessions/10-local-ecology-when-not]] · [[academic-ai-austria]].

Labels: *verified fact* | *claim* | *technical suggestion*.

---

## Twin tracks (do not collapse them)

| Law / regime | What it mainly does | Austrian entry point |
|---|---|---|
| **GDPR / DSGVO** (+ Austrian DSG) | Rules when **personal data** are processed | [Datenschutzbehörde (DSB)](https://dsb.gv.at/) |
| **EU AI Act (KI-VO)** | Risk-based rules for placing / using **AI systems** on the EU market | [RTR KI-Servicestelle](https://www.rtr.at/rtr/service/ki-servicestelle/ki-servicestelle.de.html) |

*verified fact (DSB position):* The AI Act does **not** replace the GDPR. If personal data are processed, GDPR duties stay in parallel (AI Act Art. 2(7) as cited by the DSB).

---

## Official links (German — use these)

### Datenschutzbehörde — AI & data protection

| Page | URL |
|---|---|
| **KI & Datenschutz hub** | https://dsb.gv.at/kuenstlichebrintelligenz/kuenstliche-intelligenz-datenschutz |
| FAQs — KI und Datenschutz | https://dsb.gv.at/faqs/faqs-zum-thema-ki-und-Datenschutz |
| DSGVO ↔ KI-VO (private sector controllers) | https://dsb.gv.at/aktuelles/informationen-der-datenschutzbehoerde-zum-verhaeltnis-zwischen-der-dsgvo-und-der-verordnung-eu-ueber-kuenstliche-intelligenz-ki-vo-fuer-verantwortliche-des-privaten-bereichs |
| DSGVO ↔ KI-VO (public sector) | https://dsb.gv.at/aktuelles/informationen-der-datenschutzbehoerde-zum-verhaeltnis-zwischen-der-dsgvo-und-der-verordnung-eu-ueber-kuenstliche-intelligenz-ki-vo-fuer-verantwortliche-des-oeffentlichen-bereichs |

Note: the hub path really contains `kuenstlichebrintelligenz` (no hyphen) — that is the live DSB URL.

### RTR — KI-Servicestelle (AI Act information hub)

| Page | URL |
|---|---|
| **KI-Servicestelle home** | https://www.rtr.at/rtr/service/ki-servicestelle/ki-servicestelle.de.html |
| Contact | ki@rtr.at · +43 1 58058-0 |
| Legal basis (as stated by RTR) | § 20c KOG and § 194a TKG |

RTR positions itself as public information hub for the AI Act (actors, provider/operator duties, risk levels, transparency, prohibitions, sanctions) and related topics (cybersecurity, data economy, media). Materials often CC BY 4.0 unless noted.

---

## Classroom map of the AI Act (high level)

Do not turn session into a law seminar. Use this vocabulary:

1. **Prohibited practices** — certain uses banned (e.g. social scoring-style harms — check current RTR overviews).  
2. **High-risk systems** — stricter duties (documentation, risk management, human oversight). Most student art tools are **not** automatically “high-risk,” but **deployments that decide on people** can be.  
3. **Transparency** — when users must know they interact with AI / synthetic media (relevant for exhibitions and public agents).  
4. **GPAI / models** — separate layer of duties for general-purpose model providers (usually the vendor, not the student).  
5. **Timeline** — obligations phase in over years; RTR pages track the schedule.

*claim (course frame from session 1):* Calls for “regulation” can also function as **credibility marketing** (“we are so powerful we need laws”). Still take the rules seriously when personal data or public deployment is involved.

---

## Datenschutz for this seminar (practical)

Questions students should ask of **their** stack:

| Question | Why |
|---|---|
| Does the prompt / vault contain **personal data** (own or others’)? | Triggers GDPR thinking |
| Where does the API process data (US / EU region / local)? | Transfer + vendor ToS |
| Is training on user inputs opted out? | Provider settings |
| Phone sync / Discord bridge — who hosts the messages? | Extra processors |
| Public demo of an agent that talks about real people? | Transparency + dignity + DSGVO |

*technical suggestion:* Prefer local or EU-hosted models for sensitive material; keep secrets out of the synced vault ([[howto-obsidian-setup-and-sync]]). Academic HPC ([[academic-ai-austria]]) is not “privacy free” — read their terms.

---

## How this sits in the course

| Session | Angle |
|---|---|
| 01 | Regulation as politics + marketing; point here |
| 03 | Choosing vendors / academic / local with privacy in mind |
| 09 | Authorship + platform ToS; EU vs US copyright contrast already listed |
| 10 | Local infra as sovereignty / ecology *and* data-location choice |

---

## Disclaimer

This note orients students to **primary Austrian/EU sources**. It is not legal counsel for artworks, startups, or university administration.
