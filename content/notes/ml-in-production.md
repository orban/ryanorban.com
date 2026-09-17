---
title: ML in Production — Best Practices for Real-World ML Systems
date: 2020-09-03
categories:
  - machine-learning
  - mlops
  - production-ml
  - engineering
  - data-science
description: ML in Production is a blog and newsletter focused on building and operating real-world ML systems — covering experimentation programs, deployment, monitoring, and the organizational practices that make ML succeed in production environments.
params:
  source: pinboard
  sourceUrl: https://mlinproduction.com/
---

## Summary

[ML in Production](/notes/ml-in-production/) is a publication focused on the operational side of machine learning — not model architecture or algorithms, but the practices, processes, and infrastructure that determine whether ML systems succeed in production. The target audience is data scientists, ML engineers, and AI product managers who need to ship and operate ML, not just develop it in notebooks.

The gap it addresses is real: most ML education focuses on model development (choosing algorithms, feature engineering, tuning), but production ML success depends heavily on things that aren't taught in courses — experiment tracking, model monitoring, data pipeline reliability, deployment infrastructure, organizational alignment, and the business processes around running experiments at scale. The research-to-production gap is a recognized problem in the industry, and publications like this one exist specifically to bridge it.

Topics covered include building effective experimentation programs (A/B testing at ML scale), stakeholder management, monitoring for model drift and data drift, deployment patterns (blue-green, canary, shadow modes), and the organizational structures that support sustained ML success.

## Key points

- The production ML SKILL set is distinct from the research ML skill set — bridging this gap is the core value proposition of resources like this.
- Experimentation programs aren't just about running A/B tests — they require organizational infrastructure: statistical rigor, stakeholder processes, decision rights, and feedback loops.
- Model monitoring is necessary because ML models degrade silently: data drift (input distribution changes) and concept drift (relationship between features and labels changes) are invisible without explicit monitoring.
- Related resources: Chip Huyen's ML Systems Design, [Made With ML](/notes/made-with-ml/) by Goku Mohandas, Full Stack Deep Learning.
- The MLOps discipline formalized much of this thinking into a framework after ~2020 — early publications like this contributed to that crystallization.

[Original](https://mlinproduction.com/)
