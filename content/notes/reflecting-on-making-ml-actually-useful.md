---
title: Reflecting on a Year of Making Machine Learning Actually Useful
date: 2020-07-18
categories:
  - machine-learning
  - production-ml
  - data-science
  - career
  - reflection
description: Shreya Shankar's honest reflection on a year trying to make machine learning actually useful in industry — covering the gap between academic ML and production, the underappreciated role of data work, and why most ML projects fail before the model stage. One of the most cited personal essays in the MLOps space.
params:
  source: pinboard
  sourceUrl: https://www.shreya-shankar.com/making-ml-work/
---

![Reflecting on a Year of Making Machine Learning Actually Useful](/images/notes/reflecting-on-making-ml-actually-useful.png)

## Summary

Shreya Shankar wrote this essay in mid-2020 after her year of industry ML work following a research background. It became widely shared in the MLOps and production ML communities because it named, honestly, what practitioners know but rarely document: that most ML effort goes into things other than model training, and that the research-to-production gap is about data and infrastructure, not algorithms.

The central observations: (1) Data work dominates — most of her time went to understanding, cleaning, and validating training data, not to model selection or hyperparameter tuning. Data quality problems caused more model failures than algorithmic choices. (2) The feedback loop matters — in research you know quickly if an experiment worked; in production, model failures surface in production metrics after deployment delays, making iteration slow. (3) The stakeholder interface — explaining ML uncertainty to non-ML stakeholders, managing expectations about what models can and can't do, is a SKILL research doesn't develop. (4) ML systems degrade — data drift and model drift mean a model that works today silently stops working as the world changes around it.

This essay, alongside Applied ML by Eugene Yan and Rules of ML by Google, forms the canon of honest production ML writing that the industry needed in 2020. Shankar later went on to do PhD research at Berkeley specifically on data management for ML and model monitoring — the essay can be read as the problem statement for her research agenda.

## Key points

- Data work, not model training, dominates production ML time — data quality is the primary failure mode.
- Slow feedback loops in production: model failures surface in production metrics, not experiment logs.
- Data drift and model drift mean deployed models silently degrade — monitoring is non-optional.
- Stakeholder management is a real ML job skill — communicating uncertainty and limitations to non-ML partners.
- Research optimizes for benchmark improvements; production optimizes for reliability under data distribution shift.
- Influential essay in the MLOps community; Shankar went on to research ML monitoring and data management for ML at Berkeley.

[Original](https://www.shreya-shankar.com/making-ml-work/)
