---
title: KITeGG systems & labs overview
date: 2026-11-04
tags:
  - research
  - kitegg
  - labs
---

# Systems overview — shared platform + site labs

**Frame sources:** Jenett *Vorwort Blick in die Labore* https://unlearn.gestaltung.ai/article/p60hmh5a · *Standorte & Team* https://unlearn.gestaltung.ai/article/ft3m75a5 · lab interviews (Vol. 1) · Koch cluster/how-to articles · site https://unlearn.gestaltung.ai/

Labs are **extra learning environments** for forschendes Lernen, equipment, expertise, and cross-school exchange — each thematically tuned (electronics/rapid prototyping → automation → sustainability).

## A. Shared systems (cross-site)

| System | Role | Scale cue |
|---|---|---|
| **KITeGG Cluster** | Bare-metal GPU Kubernetes at JGU Mainz housing | 5× HGX × 8× A100 80 GB; interactive multi-user |
| **JupyterHub / JupyterLab** | Browser coding + GPU + Linux for staff/students | First production surface |
| **Lehr-Lernplattform (LLP)** | Courses, materials, GPU calendar, Docker services, SSO | Custom Vue/Directus; not Moodle replacement |
| **GitLab + CI/CD + registry** | Collaborative service/model development | RLP/JGU GitLab |
| **Keycloak SSO** | Campus-linkable identity | Single login to hub/services |
| **DIY GPU node option** | ~€3k mining-rack PCIe nodes as cheaper complement | See [[diy-compute]] |

Deep notes: [[article-kitegg-cluster]] · [[article-how-to-kitegg]]

## B. Site labs (one note each, condensed)

### autoLab — HS Mainz
- **URL:** https://unlearn.gestaltung.ai/article/8nx63ze3 · Markus Mau  
- **Theme:** automation of design tools; generative Gestaltung  
- **Daily tool named:** the **shared compute cluster** (browser-reachable, campus-built)  
- **Form:** “dezentrales Labor” — knowledge walks into other disciplines; founded with KITeGG 2022 (Holzstraße)

### Living Objects Lab — KISD (TH Köln)
- **URL:** https://unlearn.gestaltung.ai/article/vap82tjw · Jakob Kilian, Laura Juliane Wagner  
- **Theme:** embed AI models in objects via microcontrollers / small computers; sensors+actuators  
- **Context:** next to prototyping / wood / metal labs; opened Spring 2022; gear lag until ~SS23  
- **Standort accent (team page):** societal effects of designing *with/of* AI; products, processes, interactions

### KINDLAB — HS Trier
- **URL:** https://unlearn.gestaltung.ai/article/11huwc4x · Peter Ehses-Reifer, Alexander Bauer (+ Prof. Simon Maris)  
- **Theme:** generative AI × **(social) sustainability**, fab (e.g. 3D print), unusual materials  
- **Form:** new lab Summer 2022; physical computing lineage; Fairtrade University campus framing  
- **Interest:** students from early adopters to skeptics; not everyone finds the lab yet

### Robotik Lab — HfG Offenbach
- **URL:** https://unlearn.gestaltung.ai/article/2p1mvu66 · Ivan Iovine  
- **Theme:** robotics + computer vision as artistic/creative expression; Arduino/RPi, cameras, actuators  
- **Users:** more art than design students in practice; interdisciplinary material + electronics  
- **Pre-KITeGG:** only rudimentary robotics inside physical-computing courses

### KI Labor — HfG Offenbach
- **URL:** https://unlearn.gestaltung.ai/article/giccoyet · Joscha Berg (2022–24)  
- **Theme:** algorithms as sources of beauty; deep learning, datasets, style transfer; procedural 3D later  
- **Pedagogy:** deep programming + math-of-nets as “craft tools” of the former Handwerkerschule ethos  
- **Projects:** mostly generative image potentials + simpler CV in installations

### AI+D Lab — HfG Schwäbisch Gmünd
- **URL:** https://unlearn.gestaltung.ai/article/k7zdxzqw · Felix Sewing  
- **Theme:** AI+Design intuition; theory+practice; modules for existing courses (e.g. type + generative fonts)  
- **Vernetzung:** hackathons/helpdesks with other campus labs; Strategic design + Creative Machine Learning accents on team page  
- **Pre-history:** ML workshops existed; dedicated AI+D lab with KITeGG (2022)

## C. How the pieces fit

```
Students / courses at 5 schools
        │
        ▼
   LLP + Jupyter + Docker services  ←── GitLab/CI (staff)
        │
        ▼
   Kubernetes cluster (A100 MIG slices, storage, SSO)
        │
        ├── autoLab (automation / tools)     Mainz
        ├── AI+D (design intuition / ML)     Gmünd
        ├── KINDLAB (sustainability / fab)   Trier
        ├── Living Objects (embodied AI)     Köln
        └── KI Labor + Robotik Lab           Offenbach
```

## vs Critical Vibe Coding (preview)

Full write-up: [[comparison-vs-cvc]]. Short: KITeGG systems are **shared institutional studios + mid-scale GPU platform**; CVC plans **personal agent stacks** with optional small local GPUs — same “own the means” spirit at a **different scale**.
