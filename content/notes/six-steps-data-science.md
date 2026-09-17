---
title: Six Steps in Data Science
date: 2013-09-04
categories:
  - data-science
  - methodology
  - workflow
  - machine-learning
  - process
description: A 2013 blog post laying out six practical steps in a data science workflow — from problem framing through data collection, exploration, modeling, evaluation, and deployment. A snapshot of how practitioners were thinking about the discipline before MLOps and production ML tooling matured.
params:
  source: pinboard
  sourceUrl: http://horicky.blogspot.ca/2013/08/six-steps-in-data-science.html
---

![Six Steps in Data Science](/images/notes/six-steps-data-science.png)

## Summary

This 2013 post on Pragmatic Programming Techniques outlined a six-step data science workflow aimed at practitioners who needed a structured way to approach analytical projects. The framing was deliberately practical — not academic — and the steps mapped closely to what would later be formalized as the CRISP-DM (Cross-Industry Standard Process for Data Mining) model: understand the problem, collect data, explore and clean, build models, evaluate, and deploy.

The 2013 version of this workflow had some distinct characteristics. Deployment was an afterthought in most companies — models were often delivered as static analysis rather than integrated into products. Feature engineering consumed the majority of practitioner time (the famous "80% of data science is data cleaning" heuristic). And the modeling step was typically scikit-learn on a single machine, maybe with Hadoop for the data prep, rather than the MLOps pipelines that would come later.

What makes these early methodology posts interesting in retrospect: they were attempts to define what doing data science actually meant when the role was new. The field was largely making up its own process as it went, borrowing from software engineering (iteration, versioning) and statistics (hypothesis testing, validation) without having synthesized them into a coherent practice.

## Key points

- Problem framing first: translating a business question into a concrete ML problem is harder than building the model — the most common source of project failure.
- Feature engineering as the core SKILL: the quality of your features dominates model performance; algorithm choice is secondary.
- Exploratory data analysis (EDA): mandatory before modeling — distributions, outliers, correlations, missing data patterns all inform what models will and won't work.
- Model evaluation: not just accuracy — precision/recall, AUC-ROC, calibration, and business metrics all matter depending on the use case.
- 2013 deployment reality: models were often Excel files, Python scripts, or reports rather than APIs with monitoring.
- Predates MLOps by years: version control for models, experiment tracking, and feature stores were not yet standard practice.

[Original](http://horicky.blogspot.ca/2013/08/six-steps-in-data-science.html)
