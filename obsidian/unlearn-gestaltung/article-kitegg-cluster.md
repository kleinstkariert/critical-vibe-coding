---
title: Der KITeGG Cluster — condensed note
date: 2026-11-04
slug: xeci6a49
tags:
  - research
  - kitegg
  - infrastructure
---

# Der KITeGG Cluster – eine Infrastruktur für KI in der Gestaltungslehre

**Author:** Anton Koch  
**URL:** https://unlearn.gestaltung.ai/de/article/xeci6a49?chunks=xeci6a49  
**Also:** DOI [10.25358/openscience-11844](http://doi.org/10.25358/openscience-11844)  
**Language:** German

> Note: This is the article behind the Task A short-ID — a **cluster/infrastructure essay**, not the series colophon.

## Main points

1. **KITeGG since 2021** shares one teaching platform + own hard/software across five Gestaltung schools (Mainz, Offenbach, Schwäbisch Gmünd, KISD, Trier); BMBF + Land RLP.
2. **Infrastructure as STS concept** (Star/Ruhleder): relational, not a neutral underlay; AI itself as “technology + institutions + ideology” (McQuillan). The cluster is a political/pedagogical positioning, not only racks.
3. **Cloud vs bare-metal decision → own metal.** Reasons: long (~5y) project amortizes purchase (~halfway); public money should build public capacity; housing already available; avoid switching costs / cloud-capital dependency (Varoufakis); make energy/material costs *local and visible* rather than outsourced.
4. **Ecology argument is anti-greenwash.** PUE/offsets insufficient; hyperscale growth vs efficiency gains; water/energy burdens; universities shouldn’t only legitimize vendor narratives.
5. **Theoretical + technological dual infrastructure.** Critique of “best practices”; teach that Digitalität/KI are historically contingent; still ship a working platform for courses.
6. **Hardware anatomy (order of magnitude).** Five HGX servers × **8× NVIDIA A100 80 GB** each; dual 64-core CPUs / **2 TB RAM** / large NVMe per node; dual HDD storage servers; dual management/control planes; Ubuntu + **Kubernetes**; MIG slicing for multi-user interactive sessions (not classic batch HPC queues).
7. **Software stack.** JupyterHub first (weeks after start); later custom **Lehr-Lernplattform (LLP)** (Vue/Quasar + Directus API) for courses, GPU calendar/reservations, Docker “Services” students can clone; GitLab (RLP/JGU) + CI/CD + Harbor-style container workflow; Keycloak SSO.
8. **Ops realities.** Full-time platform person; MIG changes need reboots; security via isolation/DMZ + trust circle (not full hardening); ephemeral student data; warranty for project life; NVIDIA lock-in acknowledged with possible future AMD/SYCL path.
9. **Endgame.** Document + reproduce as case study; consolidate for lower-maintenance post-funding run; political stance: competence to *appropriate*, not only *apply*, vendor AI.

## Differences from our course

- **Shared 40-GPU-class institutional cluster** vs CVC **personal** Hermes + optional laptop/Ollama/single-GPU DIY.
- Explicit **anti-cloud public-money** doctrine as core pedagogy; CVC teaches cloud vs local as a choice table (Session 01/04) without requiring institutional bare-metal.
- Teaching UX is **JupyterLab + custom LLP services**, not agent loop + Obsidian wiki + MCP.
- Article’s STS/infrastructure theory is denser than Session 01’s political-economy blocks (bubble, regulation, ecology seed) — complementary, different register.

## Crosswalk to CVC landscape (Session 01)

| Koch claim (this article) | CVC place to teach / complicate |
|---|---|
| Cloud capital / switching costs (Varoufakis) | Block 2 local vs cloud table; Block 4 hyperscaler lock-in |
| Ecology: PUE/offsets insufficient; make energy *local and visible* | Block 5 seed — GW Ranch / DC photos; Session 11 handout |
| Infrastructure as STS (Star/Ruhleder); AI as tech + institutions + ideology | Block 3 amplifier / who owns the knob (`visions-fears-regulation`) |
| Public money should build public capacity | Contrast with student personal-stack homework (Block 8) |
| NVIDIA lock-in acknowledged | Local hardware research note; Session 04 |

Teacher clips that sit next to this essay (vault `Clippings/`): Tooze AI arms race; “Real Cost of AI”; Acemoglu economics — political-economy counterpoint, not a KITeGG summary.

## Related

- [[article-how-to-kitegg]] · [[diy-compute]] · [[systems-labs-overview]] · [[comparison-vs-cvc]] · [[00-index]]
