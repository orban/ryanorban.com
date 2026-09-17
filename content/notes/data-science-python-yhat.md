---
title: Data Science in Python — Yhat Tutorial
date: 2014-01-14
categories:
  - python
  - data-science
  - tutorial
  - pandas
  - scikit-learn
description: Yhat's end-to-end data science tutorial in Python using pandas for data manipulation and scikit-learn for modeling. One of the cleaner introductory pipelines from 2014, before this kind of content became ubiquitous.
params:
  source: pinboard
  sourceUrl: http://blog.yhathq.com/posts/data-science-in-python-tutorial.html
---

## Summary

Yhat (a startup building model deployment infrastructure) published this tutorial as an end-to-end walkthrough of data science in Python: load data with pandas, explore and clean it, train a classifier with scikit-learn, and evaluate the results. The pipeline pattern it shows — load → explore → clean → model → evaluate — became the standard structure for most introductory data science courses and notebooks that followed.

Yhat's product was about deploying models to production, so their tutorials tended toward practical, applied work rather than theoretical depth. This one is notable for showing the full pipeline rather than just isolated code snippets, making it immediately actionable for beginners.

## Key points

- Shows the full analysis pipeline: data loading with pandas, EDA (exploratory data analysis), feature engineering, model training with scikit-learn, evaluation
- Uses pandas DataFrames as the central data structure — cleaning, filtering, and transformation all happen there before the data reaches the model
- scikit-learn's consistent `fit`/`predict` API makes it easy to swap classifiers — the tutorial exploits this to compare logistic regression and random forests
- Evaluation section covers accuracy, confusion matrix, and ROC curve — not just a single accuracy number
- Yhat later pivoted to focus on R model deployment and eventually shut down, but this tutorial series aged well as introductory material

[Original](http://blog.yhathq.com/posts/data-science-in-python-tutorial.html)
