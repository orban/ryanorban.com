---
title: Approaching (Almost) Any Machine Learning Problem
date: 2016-07-23
categories:
  - machine-learning
  - data-science
  - workflow
  - kaggle
  - practical
description: Abhishek Thakur's systematic framework for tackling any supervised ML problem — from data cleaning and feature engineering through model selection and stacking. One of the most-shared practical ML workflow guides from the Kaggle blog era.
params:
  source: pinboard
  sourceUrl: http://blog.kaggle.com/2016/07/21/approaching-almost-any-machine-learning-problem-abhishek-thakur/
---

![Approaching (Almost) Any Machine Learning Problem](/images/notes/approaching-any-ml-problem.png)

## Summary

Abhishek Thakur — one of the first Kaggle Grandmasters — wrote this practical framework for the Kaggle blog in 2016. The post distills a systematic workflow for supervised machine learning problems that can be applied across domains. It was widely shared because it made explicit the implicit knowledge that experienced practitioners had developed through dozens of competition iterations.

The framework moves through a pipeline: data exploration (understanding distributions, missing values, outliers), feature engineering (creating and selecting predictive features), cross-validation strategy (choosing the right validation scheme for the data structure), model selection (starting with baselines, moving to gradient boosting and neural networks), and finally ensemble methods (stacking and blending multiple models for final predictions). Thakur gives concrete recommendations at each step — which libraries to use, which transforms to try first, when to use stratified vs. time-series cross-validation.

The article reflects the Kaggle competition culture of 2016: XGBoost was the dominant model for tabular data, scikit-learn was the standard library, and ensemble stacking (using one model's predictions as features for another) was a near-universal competition winning technique. For practitioners outside competitions, the framework translates well to real-world problems, though some advice (like heavy ensemble stacking) is more competition-relevant than production-practical. Thakur later expanded this into the book "Approaching (Almost) Any Machine Learning Problem" (2020).

## Key points

- Systematic pipeline: EDA → feature engineering → cross-validation → model selection → ensemble methods.
- Kaggle Grandmaster perspective: reflects competition-winning patterns, particularly the dominance of XGBoost and model stacking in 2016.
- Concrete library recommendations: scikit-learn, XGBoost, pandas — the standard 2016 practitioner stack.
- Cross-validation strategy is given more attention than most guides: how to choose fold strategy matters as much as the model.
- Later expanded into a full book (2020) with deep learning added and updated for the PyTorch era.

[Original](http://blog.kaggle.com/2016/07/21/approaching-almost-any-machine-learning-problem-abhishek-thakur/)
