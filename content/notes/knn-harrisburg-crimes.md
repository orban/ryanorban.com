---
title: k-Nearest Neighbor Classification for Harrisburg Crimes
date: 2014-01-09
categories:
  - machine-learning
  - knn
  - spatial-analysis
  - crime-prediction
  - applied-ml
description: k-Nearest Neighbor classification applied to predicting crime type in Harrisburg, PA from location and time features. A typical early applied ML blog post that makes the algorithm concrete with a public dataset.
params:
  source: pinboard
  sourceUrl: http://increasinglyfunctional.com/2014/01/08/knn-classification-for-harrisburg-crimes/
---

## Summary

This tutorial applies k-nearest neighbor (KNN) classification to publicly available Harrisburg, PA crime data. The task: given the location (latitude/longitude) and time of a crime report, predict the crime type (theft, assault, vandalism, etc.). It's a deliberately simple problem — KNN is among the most intuitive algorithms, and geographic crime data is easy to visualize — which makes it an effective teaching vehicle.

The post is representative of a genre of early data science blog content that made ML algorithms tangible by applying them to local public data. Rather than abstracting over benchmark datasets, working with a specific city's crime records made the feature choices and predictions feel real.

## Key points

- KNN classifies by majority vote among the k nearest neighbors in feature space — no training phase, just memorization of labeled examples
- Geographic distance as the primary feature captures spatial clustering of crime types — similar neighborhoods have similar crime patterns
- Choice of k significantly affects the bias-variance tradeoff: small k is sensitive to local noise, large k smooths over meaningful local variation
- Evaluation via cross-validation shows classification accuracy and, importantly, where the classifier fails (crime types that look alike geographically)
- A worked example of the full applied ML workflow: data loading → feature engineering → model fitting → evaluation → interpretation

[Original](http://increasinglyfunctional.com/2014/01/08/knn-classification-for-harrisburg-crimes/)
