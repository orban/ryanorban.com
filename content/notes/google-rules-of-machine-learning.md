---
title: "Rules of Machine Learning: Best Practices for ML Engineering"
date: 2020-10-04
categories:
  - machine-learning
  - engineering
  - best-practices
  - google
description: Martin Zinkevich's 43-rule guide from Google on practical ML engineering, organized around the principle that most gains come from good features and solid infrastructure rather than clever algorithms. A pragmatic counterweight to academic ML papers — the kind of advice that separates production systems from demos.
params:
  source: papers
  sourceUrl: https://developers.google.com/machine-learning/guides/rules-of-ml
---

## Summary

Martin Zinkevich at Google distills lessons from years of building production machine learning systems into 43 practical rules, organized across four phases: before you build anything, the first ML pipeline, feature engineering, and optimization when gains plateau. The document's central maxim is "do machine learning like the great engineer you are, not like the great machine learning expert you aren't" — the point being that most ML failures come from bad engineering, not wrong algorithms.

The early rules are deliberately conservative: start with heuristics, measure everything before building a model, test infrastructure independently, and keep the first model simple. Rule #4 is "keep the first model simple and get the infrastructure right" — a principle that maps onto the broader lesson that getting training-serving skew under control and building reliable feature pipelines yields more value than any model improvement. The guide explicitly says to convert existing heuristics into features as a first step rather than replacing them.

The later rules address a subtler failure mode: optimization traps where the ML objective diverges from the actual product goal. Rules 38-43 deal with what happens when you've been iterating for a long time and gains have stopped — Zinkevich's advice is to seek qualitatively new data sources rather than squeeze more out of existing features, and to revisit whether the loss function actually captures what users want. The whole document reads as an empirical field guide rather than a textbook, written by someone who has debugged countless deployed ML systems.

## Key points

- Rule #1: Don't use ML until you've tried heuristics — most products should launch without ML first
- Training-serving skew is the most dangerous and common silent failure in production ML systems
- Convert existing heuristics to features before discarding them — heuristics encode real signal
- Keep metrics simple and observable; complex metrics that correlate with goals are often worse than direct proxies
- When gains plateau, seek new data sources rather than architectural changes — the bottleneck is usually data, not models

[Original](https://developers.google.com/machine-learning/guides/rules-of-ml)
