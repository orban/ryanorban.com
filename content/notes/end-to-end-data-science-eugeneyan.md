---
title: Unpopular Opinion — Data Scientists Should Be More End-to-End
date: 2020-09-03
categories:
  - data-science
  - career
  - machine-learning
  - engineering
  - full-stack
description: Eugene Yan argues that data scientists deliver more value when they own the full problem lifecycle — from identifying the problem through production deployment. Fewer handoffs, better context, faster iteration, and stronger ownership.
params:
  source: pinboard
  sourceUrl: https://eugeneyan.com/writing/end-to-end-data-science/
---

![Unpopular Opinion — Data Scientists Should Be More End-to-End](/images/notes/end-to-end-data-science-eugeneyan.png)

## Summary

Eugene Yan argues that end-to-end data scientists — those who own the full lifecycle from problem identification through production deployment — deliver significantly more value than specialists who handle only modeling. The argument is partly about communication overhead, partly about epistemic completeness, and partly about ownership dynamics.

On communication: when multiple specialized roles handle a project (data engineer → data scientist → ML engineer → DevOps), coordination costs grow superlinearly. As Yan notes, 21 people generate nearly 2,000 communication links — each handoff is an opportunity for context loss, misalignment, and delay. End-to-end practitioners eliminate most of these interfaces.

On context: a performance decline might stem from data quality issues, product changes, or model drift — not an algorithm problem. A specialist who only sees the modeling layer misses the upstream cause. Owning the full stack means owning the full diagnostic surface. This connects to the broader idea of T-shaped skills — depth in one area, breadth across the pipeline.

On ownership: the throw over the wall anti-pattern — where each role completes their piece and hands off — diffuses accountability. When one person owns the full problem, responsibility is clear and incentives align.

## Key points

- Essential skills for end-to-end data scientists: product thinking, communication, data engineering, analysis, ML, software engineering, DevOps basics — not all needed for every project.
- Specialization still has its place: deep ML research, hyper-specialized systems (algorithmic trading), or individuals who genuinely prefer narrow focus.
- Faster iteration is the biggest concrete benefit: fewer handoffs → tighter experimental loops → more hypotheses tested per unit time.
- Eugene Yan practiced this at Lazada and Amazon — the argument is grounded in experience, not just theory.
- Related to T-shaped skills, full-stack data science, and the data scientist role evolution debate in the ML community.

[Original](https://eugeneyan.com/writing/end-to-end-data-science/)
