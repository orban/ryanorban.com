---
title: Reproducible Machine Learning Results By Default
date: 2014-01-08
categories:
  - machine-learning
  - reproducibility
  - best-practices
  - random-seed
description: Jason Brownlee's Machine Learning Mastery post on setting random seeds and other practices to make ML experiments reproducible by default. A basic hygiene checklist that surprisingly many practitioners skip.
params:
  source: pinboard
  sourceUrl: http://machinelearningmastery.com/reproducible-machine-learning-results-by-default/
---

## Summary

Jason Brownlee's [Machine Learning Mastery](/notes/machine-learning-mastery/) post argues for making reproducibility the default posture in machine learning experiments, not an afterthought. The core practice: always set a random seed before any stochastic operation — data splitting, weight initialization, dropout — so results can be regenerated exactly. Beyond seeds, the post covers saving model configurations, logging hyperparameters, and pinning library versions.

The argument is practical: stochastic results are hard to debug, hard to compare, and create the awkward situation where a published accuracy can't be matched because nobody recorded what seed was used. Reproducibility by default costs almost nothing at experiment time but pays off heavily during debugging, peer review, and production deployment.

## Key points

- Always set `numpy.random.seed()` and framework-specific seeds (e.g., `tf.random.set_seed()`) before any stochastic operation
- Save all hyperparameters alongside model weights — a model file without its configuration is only half the information
- Log train/validation splits explicitly so you know exactly which rows were in each fold
- Pin library versions (`pip freeze > requirements.txt`) — the same code can produce different results across scikit-learn versions
- The discipline is especially important in deep learning where weight initialization has a large effect on which local minimum you reach

[Original](http://machinelearningmastery.com/reproducible-machine-learning-results-by-default/)
