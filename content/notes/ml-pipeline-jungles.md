---
title: "The Perilous World of ML: Pipeline Jungles and Hidden Feedback Loops"
date: 2015-01-06
categories:
  - machine-learning
  - mlops
  - software-engineering
  - technical-debt
  - feedback-loops
description: John Foreman on the hidden technical debt in ML systems — pipeline jungles and feedback loops that make production ML fragile in ways that pure model metrics never reveal. Anticipates the 'Hidden Technical Debt in Machine Learning Systems' Google paper by months.
params:
  source: pinboard
  sourceUrl: http://www.john-foreman.com/blog/the-perilous-world-of-machine-learning-for-fun-and-profit-pipeline-jungles-and-hidden-feedback-loops
---

## Summary

John Foreman's post identifies two structural failure modes in production machine learning systems that pure model evaluation never surfaces: **pipeline jungles** and **hidden feedback loops**. Both are forms of technical debt specific to ML systems, and both became better understood after the famous Google paper "Hidden Technical Debt in Machine Learning Systems" (Sculley et al., 2015) — which this post anticipates by months.

A **pipeline jungle** emerges when the data pipeline feeding an ML model grows organically over time — each feature requiring its own data source, preprocessing step, and join. Over months, what started as a clean pipeline becomes an unmaintainable tangle: no single person understands the full data lineage, tests are absent or incomplete, and changing any step risks silent breakage downstream. The model might still work, but you can no longer reason about why or debug when it doesn't.

**Hidden feedback loops** are more insidious. When a model's predictions influence the system that generates its training data, the model is implicitly training on itself. Recommendation systems are the canonical example: the system recommends content that gets shown to users, users engage with what's shown, engagement becomes training signal, and the model drifts toward recommending what it already thinks is popular. The feedback loop can amplify biases, collapse diversity, and make it impossible to measure counterfactual performance.

## Key points

- Pipeline jungles: organic growth of data pipelines creates unmaintainable, untestable data engineering debt.
- Hidden feedback loops: model outputs influence training data → model trains on its own predictions → drift and bias amplification.
- Both are invisible to standard ML evaluation metrics — model accuracy can be fine while the system degrades.
- Anticipates the Google "Technical Debt in ML Systems" paper (Sculley et al., 2015) published shortly after.
- Prevention requires data lineage tracking, integration tests on pipelines, and explicit loop detection in system design.
- MLOps tooling (dbt, MLflow, Feast) addresses parts of this — but the feedback loop problem is architectural, not tooling.

[Original](http://www.john-foreman.com/blog/the-perilous-world-of-machine-learning-for-fun-and-profit-pipeline-jungles-and-hidden-feedback-loops)
