---
title: "Not Just for a Rainy Day: The True Meaning of Converged"
date: 2012-07-01
categories:
  - infrastructure
  - storage
  - cloud
  - nutanix
  - hyperconvergence
description: Nutanix's 2012 blog post making the case for converged infrastructure — combining compute, storage, and networking in a single appliance rather than maintaining separate silos. Written during their early go-to-market phase, when hyperconvergence was still a novel concept rather than an industry standard.
params:
  source: pinboard
  sourceUrl: http://www.nutanix.com/blog/2012/06/29/not-just-for-a-rainy-day/
---

## Summary

This 2012 Nutanix blog post makes the case for converged infrastructure — or more specifically, hyperconvergence (a term that would solidify around 2013). The traditional enterprise data center model separated compute (servers), storage (SAN/NAS), and networking into distinct hardware silos, each with its own management stack, procurement cycle, and specialist team. Nutanix was built on the proposition that this separation was operationally expensive and architecturally unnecessary — that all three could be combined in software running on commodity x86 hardware, managed through a single interface.

The not just for a rainy day framing rejects the idea that converged infrastructure is only appropriate for disaster recovery or secondary workloads. Nutanix's argument was that the simplified operational model and scale-out architecture made it appropriate for primary production workloads — that the reliability concern traditionally used to justify separate SAN arrays was addressed by their software-defined storage layer, which replicated data across nodes and could tolerate node failures without downtime. This was a significant claim in 2012, when enterprise storage was dominated by EMC, NetApp, and HP with expensive, proprietary hardware.

Nutanix was founded in 2009 by engineers from Google and Facebook who had seen first-hand how web-scale infrastructure operated differently from enterprise IT. The insight they brought: Google and Facebook ran enormous amounts of storage on commodity hardware with sophisticated software for redundancy and management — and it was dramatically cheaper and more operationally tractable than enterprise SAN arrays. The Nutanix product packaged this model into an enterprise-friendly appliance with proper support and management tooling. The hyperconverged infrastructure (HCI) category they pioneered became a significant market segment, eventually challenging traditional SAN vendors substantially.

## Key points

- Converged infrastructure / hyperconvergence: combines compute, storage, and networking on commodity x86 hardware managed by a single software layer.
- Nutanix position in 2012: appropriate for primary production workloads, not just DR — their replication layer addresses the reliability objection to removing SAN.
- Founded by ex-Google/Facebook engineers applying web-scale infrastructure principles to the enterprise data center.
- Disrupting EMC, NetApp, HP: traditional SAN is expensive, complex to manage, requires separate specialist teams.
- The HCI category Nutanix pioneered became a substantial market by 2016-2020; competitors include VMware vSAN, SimpliVity, Scale Computing.
- The blog's audience: enterprise IT buyers evaluating whether to trust a startup appliance with primary workloads — the argument is as much about risk framing as technology.

[Original](http://www.nutanix.com/blog/2012/06/29/not-just-for-a-rainy-day/)
