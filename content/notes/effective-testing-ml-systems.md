---
title: Effective Testing for Machine Learning Systems
date: 2020-08-31
categories:
  - machine-learning
  - testing
  - software-engineering
  - mlops
  - quality
description: Jeremy Jordan's framework for testing machine learning systems — pre-train checks, invariance tests, directional expectation tests, and minimum functionality tests. Organizes tests around model 'skills' rather than code structure.
params:
  source: pinboard
  sourceUrl: https://www.jeremyjordan.me/testing-ml/
---

![Effective Testing for Machine Learning Systems](/images/notes/effective-testing-ml-systems.png)

## Summary

Jeremy Jordan's post addresses a fundamental gap in ML engineering: while software testing is well-understood, machine learning systems require different testing strategies because the logic is learned, not written. Traditional unit tests verify explicit code paths; ML tests must verify the behavior that emerges from training — which is probabilistic, not deterministic.

The framework distinguishes between **pre-train tests** (catching errors before training begins) and **post-train tests** (evaluating learned behavior). Pre-train tests are cheap and should run before every training run: verify output shapes and ranges, confirm that gradient steps actually decrease loss (catching optimizer bugs), and check for data leakage between train/test splits. These catch implementation bugs, not model quality issues.

Post-train behavioral testing uses three strategies: **invariance tests** (the model's prediction shouldn't change when inputs are perturbed in ways that shouldn't matter — e.g., changing a person's name in a sentiment analysis input), **directional expectation tests** (when you change input X in direction D, the output should move in an expected direction — more bathrooms → higher predicted house price), and **minimum functionality tests** (the model should meet certain thresholds on specific critical subgroups or scenarios).

The key organizational insight: tests should be structured around the "skills" a model should have — robustness to noise, vocabulary understanding, invariance to protected attributes — not around the code structure. This parallels behavioral testing approaches in NLP (like CheckList from Microsoft Research).

## Key points

- Pre-train tests are high ROI: shape checks, gradient descent sanity checks, and data leakage detection catch bugs before expensive training runs.
- Invariance tests are critical for fairness: the model shouldn't change its output based on protected attributes (race, gender) when these shouldn't influence the prediction.
- Directional expectation tests encode domain knowledge as tests — a form of property-based testing applied to learned models.
- Organize by model skills, not code structure — this produces behavioral test suites rather than unit tests of internal components.
- Related tools: Great Expectations (data validation), Deepchecks, Evidently for model monitoring in production.

[Original](https://www.jeremyjordan.me/testing-ml/)
