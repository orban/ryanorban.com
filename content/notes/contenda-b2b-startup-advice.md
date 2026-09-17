---
title: Why You Don't Need to Be Enterprise-Ready Yet
date: 2022-06-01
categories:
  - startups
  - b2b
  - saas
  - product
  - yagni
description: Contenda founder Lilly Chen argues that early B2B SaaS founders shouldn't over-engineer for enterprise readiness or scalability — premature optimization for future requirements is a trap that distracts from solving the present problem. Practical framing for when to add infrastructure vs. when to ship.
params:
  source: pinboard
  sourceUrl: https://www.gorelay.co/t/why-you-don-t-need-to-be-enterprise-ready-or-scalable-as-yet-and-other-notes-on-crafting-b2b-software-with-contenda-s-founder-lilly-chen/743
---

## Summary

Lilly Chen, founder of Contenda, pushes back against a pattern she sees in early-stage B2B software: founders spending enormous time building enterprise features (SSO, SOC 2, audit logs, role-based permissions, multi-tenancy) before they've validated that anyone actually wants their product. The essay frames premature enterprise readiness as "lugging product freight from the future" — investing in capabilities that might never be needed at the expense of learning whether the core product works.

The argument is that most enterprise requirements are pull-based: a specific customer with a specific deal size will tell you what they need. Until you're talking to that customer, building to an imagined enterprise spec is speculation. Contenda's approach was to solve the current problem set aggressively — build what the first five customers actually need, not what the fifteenth hypothetical customer might want. This is a restatement of YAGNI (You Aren't Gonna Need It) applied to B2B product roadmaps.

The piece also addresses the scalability version of this trap: early-stage founders rewriting systems for scale before having any users. Contenda explicitly chose to delay infrastructure work until there was evidence it was needed. The practical implication is prioritization: every hour spent on Kubernetes orchestration or multi-region failover is an hour not spent talking to customers and shipping features. The constraint isn't technical at the early stage — it's product-market fit.

## Key points

- Enterprise readiness is pull-based: let specific deals pull specific requirements, don't build to a phantom spec
- YAGNI applied to B2B product roadmaps: premature scaling and compliance work is a form of technical debt acquisition without matching revenue
- Contenda's Lilly Chen: solve the current problem-set first, doggedly — future-proofing is speculation at the early stage
- Scaling prematurely: the bottleneck at seed stage is almost never infrastructure; it's almost always product-market fit
- Practical heuristic: if no customer has asked for it in the last 3 conversations, it's not a priority
- Related: Paul Graham on doing things that don't scale; DHH on Majestic Monolith philosophy

[Original](https://www.gorelay.co/t/why-you-don-t-need-to-be-enterprise-ready-or-scalable-as-yet-and-other-notes-on-crafting-b2b-software-with-contenda-s-founder-lilly-chen/743)
