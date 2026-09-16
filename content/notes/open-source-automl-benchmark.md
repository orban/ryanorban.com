---
title: An Open Source AutoML Benchmark
date: 2022-04-09
categories:
  - automl
  - benchmark
  - machine-learning
  - meta-learning
  - evaluation
  - openml
description: This paper presents an open-source, extensible benchmark for comparing AutoML systems across 39 classification datasets, finding that no single system consistently dominates a tuned random forest baseline. It establishes best practices for fair AutoML evaluation and provides a living framework that accepts community contributions.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1907.00909.pdf
---

## Summary

This paper from Eindhoven University, H2O.ai, and LMU Munich introduces a rigorous, reproducible benchmark for comparing automated machine learning (AutoML) systems. Prior comparisons were plagued by dataset bias, incorrect tool configurations, and insufficient compute resources. The authors address these problems by open-sourcing the entire framework, running on standardized AWS infrastructure, using 39 datasets from OpenML, and publishing results continuously on a website.

The benchmark evaluates four major AutoML systems — auto-sklearn, Auto-WEKA, H2O AutoML, and TPOT — against strong baselines including a tuned Random Forest. Results are normalized so that a constant class-prior predictor scores 0 and the tuned Random Forest scores 1. The headline finding is sobering: no AutoML system consistently outperforms the tuned Random Forest baseline across all datasets. On some tasks — particularly high-cardinality multi-class problems like dionis and helena — all AutoML frameworks perform worse than the baseline. Auto-WEKA shows concerning overfitting behavior when given more time.

The framework matters beyond its specific results because it treats AutoML benchmarking as an ongoing infrastructure problem rather than a one-shot study. Adding a new AutoML framework requires fewer than 100 lines of wrapper code; adding an OpenML dataset takes 3 lines. The open-source approach invites the community to keep results current as tools evolve, addressing a core failure mode of academic benchmarking where comparisons age out of date immediately.

## Key points

- auto-sklearn uses Bayesian optimization + meta-learning warm-start + ensemble selection; it's the most complex of the four evaluated systems
- TPOT uses genetic programming to evolve scikit-learn pipelines; shows the most improvement with extended time budgets
- Datasets vary in size by orders of magnitude; ~15x larger on average than prior AutoML benchmark datasets
- Meta-learning introduces a fairness issue: systems trained on benchmark datasets gain an unfair advantage, left as open problem
- All experiments on AWS m5.2xlarge (8 vCPUs, 32GB RAM); explicit hardware standardization is a key contribution

[Original](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/1907.00909.pdf)
