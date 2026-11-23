---
title: DIY request draft, GPU teaching and project workstation
audience: student
status: current
canonical: true
date: 2026-10-29
updated: 2026-11-23
last_verified: 2026-10-29
price_status: dated 2026-10-29, not rechecked on 2026-11-23
tags:
  - research
  - hardware
  - procurement
  - dated-prices
---

# DIY request draft: GPU teaching and project workstation

Dated research. This page was first written as a letter to a budget office on 29 October 2026. It is an alternative request. It was **superseded as the primary recommendation** by the [Spark class system](spark-gb10-recommended-system.md). It remains as the higher-throughput alternative. Read the [hardware README](README.md) for the price date and the evidence labels.

## Request

The request is for a dual-GPU inference workstation in an open aluminium frame (2 × NVIDIA RTX 3090, 48 GB split VRAM). Estimated cost: **€4,990–6,750 including 10% contingency, with a ceiling of €7,000 including VAT.** Details: [Setup A](setup-a-dual-3090-open-frame.md).

Alternative if more capacity is preferred: three RTX 3090 (72 GB split VRAM), estimated **€7,050–9,280, with a ceiling of €9,500**. Details: [Setup C](setup-c-triple-3090-open-frame.md).

## Purpose

1. A system that students can inspect, measure and reconfigure: PCIe topology, power supply, cooling, GPU memory splitting and local inference software.
2. A dedicated local inference server for coding agents and student projects, without cloud costs or external data transfer.

## Relation to a DGX Spark

The systems serve different priorities. The comparison, with the speed figures and their limits, is in the [README efficiency section](README.md#efficiency-only-conclusion). The efficiency caveat of the draft is that a Spark class purchase is the stronger option if teaching value is left out and capacity, watts and maintenance are the main criteria. The DIY purchase is justified only if fast inference on models that fit, and hands-on system access, are required.

## Cost, risks and measures

The cost tables are in the setup pages. The risk measures are in the [README cautions](README.md#procurement-and-operation-cautions). GPU and RAM prices were checked against dealer and market data on 29 October 2026. The other components needed 2–3 quotations.

## Decision requested in the draft

Approval of **up to €7,000** for the dual-GPU variant, or **up to €9,500** for the three-GPU variant. The approval depends on current quotations and on the operating measures in the README.
