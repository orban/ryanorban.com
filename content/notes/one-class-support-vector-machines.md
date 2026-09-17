---
title: Introduction to One-Class Support Vector Machines
date: 2013-07-13
categories:
  - machine-learning
  - svm
  - anomaly-detection
  - unsupervised-learning
description: A practical introduction to one-class SVMs — the variant of Support Vector Machines used for anomaly detection and novelty detection when you only have examples of normal behavior. Useful when collecting labeled anomaly examples is impractical or impossible.
params:
  source: pinboard
  sourceUrl: http://rvlasveld.github.io/blog/2013/07/12/introduction-to-one-class-support-vector-machines/
---

![Introduction to One-Class Support Vector Machines](/images/notes/one-class-support-vector-machines.png)

## Summary

Standard Support Vector Machine (SVM) classification draws a decision boundary between two labeled classes. One-class SVMs solve a different problem: you only have examples of one class (normal data), and you want to detect points that fall outside it. This is anomaly detection — or in Schölkopf's terminology, novelty detection.

The approach, introduced by Bernhard Schölkopf et al. in 1999, maps the training data into a high-dimensional feature space via the kernel trick and finds a hyperplane that separates the training data from the origin with maximum margin. At inference time, new points that fall on the same side as the training data are classified as "normal"; points on the origin side are flagged as anomalies. The decision function outputs +1 for inliers and -1 for outliers.

In practice, one-class SVMs are used when labeled anomaly examples are scarce or unavailable — which is the common case. Intrusion detection, equipment failure prediction, and fraud detection often have this structure: you have plenty of normal behavior data but few confirmed examples of what you're trying to catch. The tradeoff is tuning the `nu` parameter (the upper bound on the fraction of training points treated as outliers), which effectively controls the tightness of the decision boundary.

## Key points

- One-class SVM learns the boundary of a normal-data distribution using only positive examples — no anomaly labels required.
- The kernel trick (RBF kernel is common) maps data to a space where the sphere around normal data is well-defined.
- `nu` parameter: controls the fraction of the training set that can be on the wrong side — higher `nu` means a tighter, stricter boundary with more false positives.
- Compared to Isolation Forest and local outlier factor, one-class SVMs scale poorly to very high-dimensional data but perform well on lower-dimensional feature spaces.
- In 2013, this was the go-to anomaly detection method before Isolation Forest (2008, but less known) and deep autoencoders took over for high-dimensional use cases.

[Original](http://rvlasveld.github.io/blog/2013/07/12/introduction-to-one-class-support-vector-machines/)
 → GitHub
