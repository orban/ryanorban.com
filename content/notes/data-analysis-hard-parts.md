---
title: "Data Analysis: The Hard Parts"
date: 2014-02-17
categories:
  - data-science
  - data-analysis
  - engineering
  - debugging
  - best-practices
description: Mikio Braun on the unglamorous hard parts of data analysis — bugs that look like insights, evaluation that requires ground truth you don't have, and reproducibility failures. A practitioner's counterweight to the hype around data science tools.
params:
  source: pinboard
  sourceUrl: http://blog.mikiobraun.de/2014/02/data-analysis-hard-parts.html
---

## Summary

Mikio Braun (JMLR editor, creator of the Scalala/Breeze linear algebra libraries for Scala) wrote this as a reality check on the difficulties that don't show up in tutorials or conference talks. The anecdote from the tweet is illustrative: "Hurrah, my classifier is brilliant! Oh no, it was just a bug." That experience is nearly universal — a bug that improves the metric is harder to find than a bug that breaks the code.

The hard parts Braun identifies include: **debugging data pipelines** (bugs in preprocessing silently corrupt results in ways that might actually look like improvements), **evaluation without ground truth** (you can't know if a model is good if you don't have labeled data for the domain), **overfitting to evaluation metrics** (models that optimize the metric you care about drift from the thing you actually care about), and **reproducibility** (running the same analysis twice and getting different results is common in data science in ways that don't happen in traditional software engineering).

These problems haven't gone away — they're the same issues that appear in modern MLOps discussions under names like data drift, model monitoring, feature stores, and evaluation harnesses. The 2014 version of this problem was felt more acutely because the tooling for addressing it barely existed: no MLflow, no Weights & Biases, no systematic versioning of datasets or experiments.

## Key points

- Bugs that improve the metric: the hardest kind to find in machine learning — they reward rather than punish the mistake.
- Evaluation without ground truth: if you don't have labeled data, you're flying blind — unsupervised learning and recommendation systems suffer from this the most.
- Overfitting to evaluation metrics: Goodhart's Law applied to ML — when a metric becomes a target, it ceases to be a good metric.
- Reproducibility in data analysis: non-deterministic operations (random seeds, parallel execution order) mean same analysis ≠ same result by default.
- The 2014 state of tooling: these problems were recognized but the systematic tooling (MLflow, DVC, Weights & Biases) that addresses them came years later.

[Original](http://blog.mikiobraun.de/2014/02/data-analysis-hard-parts.html)
