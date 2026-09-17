---
title: "cleanlab 2.0: Automatically Find Errors in ML Datasets"
date: 2022-04-21
categories:
  - machine-learning
  - data-quality
  - label-noise
  - open-source
  - mlops
description: cleanlab 2.0 is an open-source Python framework for automatically finding and fixing errors in ML datasets — mislabeled examples, out-of-distribution samples, near-duplicates. Built on the 'confident learning' statistical framework for label noise estimation.
params:
  source: pinboard
  sourceUrl: https://cleanlab.ai/blog/cleanlab-2/
---

## Summary

cleanlab 2.0 is an open-source Python framework for finding and fixing errors in machine learning datasets. The core problem it addresses is label noise — training data that is mislabeled, ambiguous, or corrupted — which degrades model performance in ways that are hard to diagnose because the error is hidden in the data rather than the model. Cleanlab uses a statistical approach called confident learning to identify these errors automatically, without requiring manual inspection of every sample.

Confident learning works by comparing what a trained model predicts for each sample against the given label. When a model assigns high probability to a *different* class than the label, that's evidence the label might be wrong. The method formalizes this with thresholds per class — accounting for the fact that some classes are harder to learn than others — and produces ranked lists of likely mislabeled samples. Cleanlab 2.0 extended this to multiple data modalities (text, images, tabular data), added detection of out-of-distribution samples, near-duplicate detection, and non-IID data issues.

The practical motivation is significant: studies consistently find 3-8% error rates even in carefully curated benchmark datasets like ImageNet, CIFAR-10, and Amazon Reviews. This matters because models can be fundamentally limited by their training data ceiling, and cleaning 2-3% of labels can improve accuracy more than architectural improvements. Cleanlab makes this accessible by wrapping the analysis in a simple API: fit a model, run cleanlab, get a priority list of samples to review.

## Key points

- Confident learning: compares model predictions to training labels to statistically identify likely mislabels — works for any classifier.
- Cleanlab 2.0 handles text, images, and tabular data — not just image classification as in earlier versions.
- Detects label noise, out-of-distribution samples, near-duplicates, and non-IID train/test contamination.
- Open-source Python library — integrates with scikit-learn, PyTorch, TensorFlow via `cleanlab.filter` API.
- Even benchmark datasets like ImageNet contain 3-8% errors that limit model performance ceilings.
- Founded by Curtis Northcutt based on his MIT PhD work; became a company (Cleanlab) around the 2.0 release.

[Original](https://cleanlab.ai/blog/cleanlab-2/)
