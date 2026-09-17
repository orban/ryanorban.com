---
title: The Bell Curve Scar — Handicapping Passengers on the Unsinkable Ship
date: 2014-02-20
categories:
  - statistics
  - data-analysis
  - data-visualization
  - titanic
  - survivorship-bias
description: A statistical analysis of Titanic passenger survival rates examining how aggregated bell curve thinking obscures survival disparities by class, gender, and ticket price. Uses Titanic as a historical dataset to illustrate how summary statistics can mislead.
params:
  source: pinboard
  sourceUrl: http://curtwehrley.com/post/75217383699/handicapping-passengers-on-the-unsinkable-ship
---

## Summary

Curt Wehrley's post uses Titanic survival data as a case study in the limitations of aggregate statistics. The bell curve scar in the title refers to how normally-distributed summary statistics — averages, standard deviations — can obscure the structural disparities in the underlying data. When you look at survival rates overall (roughly 32%), the distribution masks dramatically different outcomes across subpopulations.

The Titanic dataset is beloved by data scientists precisely because its ground truth is known and its patterns are stark: first-class passengers had survival rates around 62%, second-class 41%, third-class 25%. Women survived at 74%, men at 19%. The women and children first policy was real and measurable. Ticket price was a good proxy for survival odds — not because of any direct causal mechanism, but because of its correlation with class, cabin location (closer to lifeboats), and crew prioritization.

The analysis highlights Simpson's paradox-adjacent thinking: a statistic that looks one way in aggregate can look very different when properly segmented. The broader lesson is about exploratory data analysis: before building models, segment and visualize your data to find the structure that summary statistics obscure. The 2014 data science community often used Titanic as a beginner Kaggle competition dataset, making this kind of analysis particularly relevant.

## Key points

- Titanic data as a statistical teaching example: survival is a binary outcome with strong signals by class, gender, and age — good for demonstrating segmentation vs. aggregate statistics.
- Simpson's paradox awareness: aggregate survival rate (32%) is misleading without stratification — class and gender interactions dominate.
- The "bell curve scar": assuming a normal distribution when the underlying data has bimodal or stratified structure — a common mistake in quick summary statistics.
- Survivorship bias adjacent: the very act of being in the sample (being recorded as a passenger) is non-random.
- Titanic was a canonical early Kaggle competition dataset — an entry point where data science beginners learned to do feature engineering and classification.

[Original](http://curtwehrley.com/post/75217383699/handicapping-passengers-on-the-unsinkable-ship)
