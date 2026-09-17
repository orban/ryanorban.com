---
title: Machine Learning Engineering for the Real World
date: 2021-10-12
categories:
  - machine-learning
  - software-engineering
  - mlops
  - production
  - engineering
description: A practical guide to ML engineering as a discipline — applying software engineering processes (agile, simplicity, iterative development) to ML projects from scoping through production. Makes the case that ML projects fail not from algorithmic complexity but from lack of engineering discipline around planning, experimentation, and deployment.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/ML-Engineering-Ebook-Final.pdf
---

## Summary

This ebook (based on Ben Wilson's Manning book "Machine Learning Engineering in Action") frames machine learning engineering as a distinct discipline that applies software engineering processes to ML projects. The core argument: ML projects fail not because the algorithms are too complex, but because practitioners don't apply the same planning, scoping, and process discipline that successful software projects demand. The seductive complexity of ML — thousands of algorithms, advanced statistics, impressive demos — distracts from the engineering fundamentals that determine whether a project ships and delivers value.

The guide covers the full ML project lifecycle: planning (translating business needs into ML objectives), scoping and research, experimentation (building MVPs with maintainable code), development (production-grade extensible code), and evaluation (measuring what matters). Each phase is treated as an engineering problem requiring explicit process, not just technical SKILL. A key theme is the foundation of simplicity: simpler models that ship are better than complex models that don't, and the goal of experimentation is the fastest path to a working MVP, not the technically most impressive solution.

The guide also addresses the organizational dimension: the diverse personas (data scientists, data engineers, ML engineers, product managers) involved in ML initiatives have different incentives and communication styles, and successful ML projects require deliberate coordination across these roles. Adapting agile principles to ML — embracing iteration, managing stakeholder expectations, building for change — is positioned as the difference between research-style and production-style ML work.

## Key Points

- ML projects fail most often from insufficient planning and process discipline, not from insufficient algorithmic sophistication
- MLOps lifecycle: planning → scoping → experimentation → development → deployment → evaluation, each requiring distinct process rigor
- Foundation of simplicity: build the simplest thing that works first; add complexity only when the simple thing fails
- Agile principles apply to ML: iteration, accepting change, cross-functional communication, and fast feedback loops
- The translation problem — converting business requirements into ML problem formulations — is the hardest and most neglected skill in applied ML engineering

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/ML-Engineering-Ebook-Final.pdf)
