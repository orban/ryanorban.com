---
title: Google Research Deep Learning Tuning Playbook
date: 2023-01-20
categories:
  - deep-learning
  - hyperparameters
  - training
  - machine-learning
  - google
description: Google Research's Deep Learning Tuning Playbook — a systematic guide to maximizing model performance through hyperparameter optimization. Written by Braxton Osting and team, it covers the science and art of tuning learning rates, batch sizes, regularization, and the full training configuration.
params:
  source: pinboard
  sourceUrl: https://github.com/google-research/tuning_playbook
---

![Google Research Deep Learning Tuning Playbook](/images/notes/google-deep-learning-tuning-playbook.png)

## Summary

Google Research's Deep Learning Tuning Playbook is a comprehensive guide to systematically maximizing deep learning model performance through thoughtful hyperparameter tuning. It's written from the perspective of Google's internal ML practice — reflecting hard-won experience tuning models at scale — and covers both the methodology (how to approach tuning systematically) and the specifics (what learning rate schedules work, how batch size affects optimization, when to use regularization).

The core philosophy is scientific rather than superstitious: treat hyperparameter tuning as an empirical science where you form hypotheses, design experiments to test them, and draw conclusions. The playbook explicitly criticizes the common approach of random tuning or blindly following rules of thumb, advocating instead for quasi-random hyperparameter sweeps that give good coverage of the search space, with systematic analysis of results.

Key topics include learning rate schedule design (warmup, cosine decay), batch size scaling (larger batch sizes require adjusted learning rates — the linear scaling rule and its limits), the priority ordering of hyperparameters (some matter much more than others), and the role of weight decay and dropout as complementary regularization tools. The guide also covers early stopping, gradient clipping, and the interaction effects between hyperparameters.

## Key points

- Treat hyperparameter tuning as empirical science: hypothesize → experiment → conclude
- Quasi-random sweeps over hyperparameter search space outperform sequential manual tuning
- Priority order: learning rate and schedule → batch size → regularization → architecture
- Batch size scaling: linear learning rate scaling rule holds until ~large batch regime, then breaks
- Weight decay and dropout are complementary — use both, tune separately
- From Google Research — reflects industrial ML practice, not academic toy problems

[Original](https://github.com/google-research/tuning_playbook)
 → GitHub
