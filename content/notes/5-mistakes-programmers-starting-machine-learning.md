---
title: 5 Mistakes Programmers Make When Starting in Machine Learning
date: 2014-02-06
categories:
  - machine-learning
  - learning
  - career
  - best-practices
  - beginner
description: Jason Brownlee's list of five mistakes programmers make when transitioning into machine learning — over-focus on theory, skipping problem definition, ignoring data quality, neglecting model evaluation, and treating ML as a programming challenge. The practitioner's onramp.
params:
  source: pinboard
  sourceUrl: http://machinelearningmastery.com/5-mistakes-programmers-make-when-starting-in-machine-learning/
---

## Summary

Jason Brownlee at [Machine Learning Mastery](/notes/machine-learning-mastery/) identified five recurring mistakes he saw in programmers attempting to learn machine learning — patterns that make the transition harder than it needs to be. The framing programmers is deliberate: these mistakes differ from what statisticians or domain experts would make. Programmers tend to approach ML as a code problem when it's actually a data problem.

**Mistake 1: Too much time on theory.** Programmers who learned from textbooks want to understand the math before touching code. But ML intuition comes from running experiments and observing outcomes — the theory makes more sense after you've seen gradient descent converge. Start with implementations, develop intuition, then revisit theory. **Mistake 2: Not defining the problem first.** What does "good" look like? What metric matters? Without a clear problem definition and success criterion, you're just running algorithms. **Mistake 3: Ignoring data quality.** Missing values, outliers, data leakage, wrong encodings — these kill model performance far more often than algorithm choice. **Mistake 4: Poor evaluation.** Not using cross-validation, evaluating on training data, or using the wrong metric (accuracy on an imbalanced dataset). **Mistake 5: Too focused on the algorithm.** The algorithm is rarely the bottleneck — feature engineering and data representation typically matter more.

These five mistakes remain relevant in 2024. The errors are structural, not tooling-specific — they show up whether you're using scikit-learn, PyTorch, or any other framework.

## Key points

- ML is a data problem first, a code problem second — programmer instincts to reach for the most sophisticated algorithm usually miss the real leverage.
- Evaluation rigor: always use held-out data for evaluation, never train-set performance alone. Cross-validation is the minimum bar.
- Feature engineering > algorithm selection: time spent on features typically improves models more than trying more algorithms.
- Problem definition: without a clear metric and success criterion, experimentation has no direction.
- Start applied, revisit theory: intuition from running experiments makes the theory click — the reverse order is frustrating and slow.

[Original](http://machinelearningmastery.com/5-mistakes-programmers-make-when-starting-in-machine-learning/)
