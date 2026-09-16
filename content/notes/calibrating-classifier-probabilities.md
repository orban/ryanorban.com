---
title: Calibrating Classifier Probabilities
date: 2014-10-15
categories:
  - machine-learning
  - classification
  - probability-calibration
  - statistics
description: Daniel Nee's post on calibrating classifier output probabilities — the underappreciated problem that a model's predicted probability of 0.8 doesn't always mean there's an 80% chance of the positive class. Essential reading before using model outputs for decision-making.
params:
  source: pinboard
  sourceUrl: http://danielnee.com/?p=90
---

## Summary

Most machine learning classifiers output a score that is then thresholded to produce a class label, but the score is often also used as a probability estimate. The problem: unless the model is explicitly calibrated, its raw output probabilities can be systematically wrong — a model that outputs 0.8 might only be right 60% of the time in practice. Probability calibration is the process of transforming raw model scores into accurate probability estimates.

The issue varies by classifier type. Logistic regression produces reasonably calibrated probabilities by design — its output is explicitly a probability under the assumed logistic model. SVM classifiers produce scores (signed distance to the decision boundary) that are not probabilities at all. Naive Bayes tends to produce extreme probabilities (close to 0 or 1) due to its conditional independence assumption. Random forests and gradient boosting produce probabilities that are often miscalibrated in different ways — they tend to be pushed toward the mean class prevalence.

The standard calibration techniques: Platt scaling (fit a logistic regression on the raw scores against true labels) and isotonic regression (a non-parametric monotone function that maps scores to probabilities). Both require held-out calibration data. The reliability diagram (also called calibration curve) visualizes the calibration quality: if a model is well-calibrated, its mean predicted probability for each bin should match the fraction of positive examples in that bin.

## Key points

- A classifier's raw output score ≠ probability unless the model is explicitly designed or calibrated for it.
- Logistic regression: well-calibrated by design. Random forests and SVMs: often poorly calibrated.
- Platt scaling: fit a logistic regression mapping raw scores to probabilities — parametric, fast.
- Isotonic regression: non-parametric monotone mapping — more flexible but needs more calibration data.
- Calibration curve / reliability diagram: visualize calibration quality by binning predictions and comparing to actual rates.
- Important when model outputs drive decisions with explicit probability interpretations (risk scores, medical diagnosis).

[Original](http://danielnee.com/?p=90)
