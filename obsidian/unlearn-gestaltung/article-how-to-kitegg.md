---
title: How to KITeGG — condensed note
date: 2026-11-04
slug: 2gtmc7uq
tags:
  - research
  - kitegg
  - infrastructure
---

# How to KITeGG: A Semi-impractical Introduction to Sourcing AI Infrastructure

**Author:** Anton Koch  
**URL:** https://unlearn.gestaltung.ai/de/article/2gtmc7uq?chunks=2gtmc7uq  
**Language:** English  
**Audience:** technical/SysOps staff at HEIs for **small–mid** AI/ML teaching infra (not commercial SLA / mission-critical)

## Main points

1. **Reproduction frame, not a copy-paste runbook.** Principles + capacity math + component choices; no frozen repo links (they rot); readers must research current packages themselves.
2. **Guiding principles.** Prefer mature open-source communities; exception: **NVIDIA HGX/CUDA** chosen for ecosystem access (AMD ROCm acknowledged as alternative if training/research > ready-made models). Plan for **EOL** and **5-year warranty**.
3. **Cost claim (*their figure*):** buy+house ≈ **3–4× cheaper** than Azure over project life *if* replacements don’t blow the budget.
4. **Capacity planning model.** Target ~**40 concurrent users / institution → 200 across five**; per-user floor ~4 CPU threads, 32 GB RAM, 200–300 GB disk; double for headroom; worker-node class ≈ 2×64-core CPUs, 2 TB RAM, large NVMe with replication.
5. **Topology.** Worker GPU nodes (one bought per partner budget logic) + Mainz-funded control/storage; dual control planes (prod vs experiment); dual storage nodes; 10 Gbit fabric; optional InfiniBand; climate-controlled cabinet.
6. **Bare-metal Kubernetes path.** ContainerD, Calico (after Flannel), Longhorn (faster start than Ceph/Rook for them), MinIO S3 on HDD nodes, NVIDIA GPU Operator + MIG, JupyterHub + Keycloak quickstart within ~2 weeks of hardware arrival.
7. **Interactive vs HPC.** Reserve resources for people/groups over time; not only job queues — matches Gestaltung studio pedagogy.
8. **Staffing punchline.** Needs **≥1 FTE** dedicated to tend + grow the platform in dialogue with users; Prometheus monitoring; major changes between semesters.

## Systems they describe (map)

| Layer | What |
|---|---|
| Metal | HGX A100 workers, control planes, HDD storage |
| OS / orch | Ubuntu, Kubernetes, ContainerD |
| Storage | ZFS/local (control), Longhorn (workers), MinIO (object) |
| GPU | NVIDIA drivers + GPU Operator + MIG slices |
| Auth | Keycloak / SSO |
| Teaching UX | JupyterHub/Lab → later LLP + Docker services |
| Dev | GitLab + CI workers + private registry |

Detail + labs: [[systems-labs-overview]] · politics/hardware argument: [[article-kitegg-cluster]] · cheap end: [[diy-compute]]

## Differences from our course (mainly scale)

- **Institutional mid-scale HPC-like teaching cluster** (hundreds of concurrent possible slices; five schools) vs CVC **per-student agent on personal cloud/API or small local model**.
- Audience is **platform engineers**; CVC audience is **artists/media students** building a personal harness.
- Closest CVC touchpoint is Session 04 + `howto-local-llm-hardware` / research note — still **orders of magnitude smaller** (single GPU / Mac / optional DIY), with explicit “no purchase required.”

## Related

- [[comparison-vs-cvc]] · [[00-index]]
