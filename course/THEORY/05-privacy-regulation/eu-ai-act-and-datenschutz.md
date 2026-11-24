---
title: EU AI Act and Datenschutz (Austria)
date: 2026-10-21
tags:
  - course
  - regulation
  - privacy
  - austria
  - eu
status: current
canonical: true
---

# EU AI Act and Datenschutz (Austria)

English course note. **Primary official pages are often German** — links below stay in the original language. This is orientation for artists/students, not legal advice.

Use with: Session 01 talk [visions fears regulation](../06-danger-and-risk/visions-fears-regulation.md) (what regulation can and cannot do, 10 to 15 min spine) · student input on privacy, session [07 coding and creative stacks](../../SESSIONS/07-coding-and-creative-stacks.md) · archived sessions [10 authorship labour platforms](../02-labour-authorship/labour.md#retired-session-10-prompts-readings-and-practical) and [11 local ecology when not](../03-ecology-infrastructure/ecology.md#retired-session-11-prompts-readings-and-practical) · [academic ai austria](../../PRACTICE/03-models-and-providers/academic-ai-austria.md).

This note is the **how the EU/AT rules look** layer. The visions handout is the **political frame** (utopia/x-risk rhetoric, amplifier debate, credibility marketing). Do not duplicate both in one sitting.

Source types: [references](../../REFERENCES/bibliography.md#source-types). A label names the source kind. It is not independent verification. Labels: *claim* | *technical suggestion*.

---

## Twin tracks (do not collapse them)

| Law / regime | What it mainly does | Austrian entry point |
|---|---|---|
| **GDPR / DSGVO** (+ Austrian DSG) | Rules when **personal data** are processed | [Datenschutzbehörde (DSB)](https://dsb.gv.at/) |
| **EU AI Act (KI-VO)** | Risk-based rules for placing / using **AI systems** on the EU market | [RTR KI-Servicestelle](https://www.rtr.at/rtr/service/ki-servicestelle/ki-servicestelle.de.html) |

*institutional summary (DSB position):* The AI Act does **not** replace the GDPR. If personal data are processed, GDPR duties stay in parallel (AI Act Art. 2(7) as cited by the DSB).

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
2. **High-risk systems** — stricter duties (documentation, risk management, human oversight). Most student art tools are **not** automatically “high-risk,” but **deployments that decide on people** can be. *orientation.* Not a ruling on your project.  
3. **Transparency** — when users must know they interact with AI / synthetic media (relevant for exhibitions and public agents).  
4. **GPAI / models** — separate layer of duties for general-purpose model providers (usually the vendor, not the student).  
5. **Timeline** — obligations phase in over years; RTR pages track the schedule.

## Decision questions

*orientation, not legal advice.* Answer these for your own project. A "yes" does not name a law. It tells you which separate topic to open.

1. Are you processing personal data?
2. Are you publishing synthetic content?
3. Are you making decisions about identifiable people?
4. Are you using biometric, health, educational, employment, or public-service data?
5. Are you deploying an interactive public system?
6. Are you acting as a provider, deployer, researcher, or private user?
7. Is the university the controller, or are you acting independently?

Provider, deployer, researcher, and private user are role names. This note does not assign your role.
Controller means who decides why and how personal data are used. This note does not decide that.

## Separate topics

These are not one privacy framework. The EU AI Act is not the GDPR.

| Topic | What the question is about |
|---|---|
| GDPR obligations | Personal data. Separate from the AI Act. |
| University policy | What the university requires of your project. |
| Platform terms | The contract of the service you use. |
| Copyright | Rights in material and in outputs. |
| Personality rights | A real person's image, voice, or name. |
| Exhibition disclosure | What a visitor is told. |
| Data retention | How long data are kept, and by whom. |
| Contractual confidentiality | What you agreed not to share. |

*claim (course frame from session 1):* Calls for “regulation” can also function as **credibility marketing** (“we are so powerful we need laws”). Still take the rules seriously when personal data or public deployment is involved.

---

## Datenschutz for this seminar (practical)

*orientation.* The rows below are separate questions. A vendor's terms are not the GDPR. A public demo is not the AI Act. See [Decision questions](#decision-questions).

Questions students should ask of **their** stack:

| Question | Why |
|---|---|
| Does the prompt / vault contain **personal data** (own or others’)? | Triggers GDPR thinking |
| Where does the API process data (US / EU region / local)? | Transfer + vendor ToS |
| Is training on user inputs opted out? | Provider settings |
| Phone sync / Discord bridge — who hosts the messages? | Extra processors |
| Public demo of an agent that talks about real people? | Exhibition disclosure. If the demo uses personal data, that is a GDPR question. Separate topics. |

*technical suggestion:* Prefer local or EU-hosted models for sensitive material; keep secrets out of the synced vault ([howto obsidian setup and sync](../../PRACTICE/02-knowledge-bases/howto-obsidian-setup-and-sync.md)). Academic HPC ([academic ai austria](../../PRACTICE/03-models-and-providers/academic-ai-austria.md)) is not “privacy free” — read their terms.

---

## How this sits in the course

| Session | Angle |
|---|---|
| 01 | Regulation as politics + marketing; point here |
| 03 | Choosing vendors / academic / local with privacy in mind |
| 04 | Authorship and platform terms. Provenance sits in this session. |
| 06 | Ecology, and where the data sits |
| 07 | Privacy and personal data, in the student input |

---

## Disclaimer

This note orients students to **primary Austrian/EU sources**. It is not legal counsel for artworks, startups, or university administration.
