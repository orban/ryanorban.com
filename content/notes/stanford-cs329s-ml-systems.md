---
title: Stanford CS 329S — Machine Learning Systems Design
date: 2021-12-18
categories:
  - machine-learning
  - mlops
  - education
  - stanford
  - systems
description: Stanford CS 329S Machine Learning Systems Design — Chip Huyen's course on building production ML systems. Covers the full lifecycle from problem framing through data, training, deployment, and monitoring with real-world case studies.
params:
  source: pinboard
  sourceUrl: https://stanford-cs329s.github.io/2021/syllabus.html
---

![Stanford CS 329S — Machine Learning Systems Design](/images/notes/stanford-cs329s-ml-systems.png)

## Summary

CS 329S is Chip Huyen's Stanford course on machine learning systems design — the engineering and systems thinking required to build ML in production, not just in notebooks. The 2021 syllabus covers the full lifecycle: problem framing, dataset creation, feature engineering, model selection, deployment, monitoring, and the business context that shapes ML decisions.

The course distinguishes itself from standard ML courses by treating ML as a systems engineering problem. A model is just one component of a system that includes data pipelines, serving infrastructure, monitoring, feedback loops, and organizational processes. Chip Huyen argues that most ML failures in production are systems failures, not model failures — bad data pipelines, distribution shift, infrastructure reliability, and misaligned metrics cause more problems than model accuracy.

The course inspired Chip Huyen's book Designing Machine Learning Systems (O'Reilly, 2022), which expanded the syllabus into comprehensive reference material. Key topics from the syllabus: data engineering and labeling at scale, feature store design, model training infrastructure, A/B testing and canary deployments, ML monitoring (data drift, model performance, infrastructure), and ML team structure.

For anyone building production ML systems, the CS 329S perspective is a significant upgrade over academic ML courses that treat deployment as an afterthought.

## Key points

- CS 329S by Chip Huyen (Stanford): ML as a systems problem, not just a modeling problem
- Full lifecycle: problem framing → data → training → deployment → monitoring → business impact
- Inspired Designing Machine Learning Systems (2022) — the course material became an O'Reilly book
- Key framing: most production ML failures are systems failures (data quality, distribution shift, infra) not model failures
- ML monitoring as a core topic: detecting data drift, model degradation, and pipeline failures in production

[Original](https://stanford-cs329s.github.io/2021/syllabus.html) → GitHub
