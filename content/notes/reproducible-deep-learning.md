---
title: Reproducible Deep Learning PhD Course
date: 2021-05-21
categories:
  - deep-learning
  - reproducibility
  - mlops
  - research
  - education
description: Simone Scardapane's PhD course on Reproducible Deep Learning — covering Git, Docker, DVC, experiment tracking, and CI/CD for ML research. Addresses the reproducibility crisis in deep learning with practical tooling.
params:
  source: pinboard
  sourceUrl: https://github.com/sscardapane/reprodl2021
---

## Summary

The [Reproducible Deep Learning](/notes/reproducible-deep-learning/) course by Simone Scardapane at Sapienza University of Rome was designed to address a structural problem in ML research: most papers are not reproducible. Results depend on random seeds, undocumented preprocessing steps, environment-specific library versions, and hyperparameter choices that didn't make it into the appendix. This course teaches the tooling and practices that make research reproducible by default.

The curriculum covers Git and GitHub for version-controlled experiments, Docker for reproducible environments, DVC (Data Version Control) for versioning datasets and models alongside code, Weights & Biases or MLflow for experiment tracking, Hydra for configuration management, and GitHub Actions for CI/CD pipelines that automatically run training jobs on push. Each tool addresses a specific reproducibility gap.

The framing is academic but the tools are the same ones used in production ML engineering — the course bridges the gap between runs on my machine research code and code that others can use. The reproducibility crisis in deep learning is real: surveys have found that the majority of ML papers cannot be reproduced from their published descriptions. Treating reproducibility as an engineering discipline rather than an afterthought is the core message.

## Key points

- Addresses the reproducibility crisis in deep learning with concrete tooling.
- Tools covered: Git, Docker, DVC, MLflow/Weights & Biases, Hydra, GitHub Actions.
- DVC versions datasets and model checkpoints alongside code — makes the full experiment reproducible.
- Hydra configuration management eliminates hardcoded hyperparameters in research scripts.
- By Simone Scardapane — PhD-level course, materials freely available on GitHub.

[Original](https://github.com/sscardapane/reprodl2021)
