---
title: New to Machine Learning? Avoid These Three Mistakes
date: 2014-09-15
categories:
  - machine-learning
  - education
  - best-practices
  - data-science
  - beginners
description: A Medium post on the three common mistakes beginners make in machine learning — likely covering data leakage, premature model selection, and ignoring baselines. The kind of counterintuitive advice that every bootcamp graduate needs before their first real project.
params:
  source: pinboard
  sourceUrl: https://medium.com/@nomadic_mind/new-to-machine-learning-avoid-these-three-mistakes-73258b3848a4
---

## Summary

This 2014 Medium post addresses the gap between learning ML algorithms and applying them correctly — the common failure modes that catch beginners after the tutorials but before production experience. In 2014, with bootcamps proliferating and Kaggle growing, there was a generation of people who knew how to fit a random forest but hadn't yet encountered the sharp edges.

The three mistakes likely targeted are variants of the most common ML pitfalls: **data leakage** (letting future information or test set characteristics leak into training — produces models that look great on validation but fail in production), **ignoring baselines** (jumping to complex models before establishing what a simple heuristic achieves — a random forest that beats a coin flip but not a frequency-based rule isn't actually useful), and **overfitting** in its various forms (including overfitting to the validation set via too many model trials without holdout).

Each of these mistakes is counterintuitive because the training and validation pipelines appear to work — the model runs, metrics are computed, everything looks correct. The error is conceptual, not technical. This is what makes them common among practitioners who've learned the mechanics without the statistical reasoning.

## Key points

- Data leakage: training data contains information from the future or from the test set — produces inflated validation metrics that collapse in production.
- Baseline neglect: complex model beating a coin flip doesn't mean it's useful — always compare against the simplest possible approach.
- Overfitting to validation: running many experiments and selecting the best validation result without a holdout set is itself a form of data leakage.
- Temporal leakage: especially common with time-series data — shuffling before splitting means future data trains on past.
- Feature leakage: including features that are consequences of the target, not predictors.
- In 2014 context: bootcamp graduates were the target audience — the curriculum had taught algorithms but not the statistical discipline around evaluation.

[Original](https://medium.com/@nomadic_mind/new-to-machine-learning-avoid-these-three-mistakes-73258b3848a4)
