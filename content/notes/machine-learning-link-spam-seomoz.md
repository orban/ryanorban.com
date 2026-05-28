---
title: "Machine Learning and Link Spam: My Brush With Insanity"
date: 2013-04-25
categories:
  - machine-learning
  - spam-detection
  - seo
  - classification
  - practical-ml
description: A practitioner's account of applying machine learning to link spam detection at SEOMoz — the messy reality of building a classifier with noisy labels, adversarial inputs, and shifting distributions. An honest account of ML in production before MLOps was a field.
params:
  source: pinboard
  sourceUrl: http://www.seomoz.org/blog/machine-learning-and-link-spam-my-brush-with-insanity
---

## Summary

This SEOMoz post (the company later became Moz) is a practitioner's candid account of building a machine learning classifier for link spam detection. The author's description as brush with insanity is honest: spam detection is one of the hardest ML problems in practice because it combines **noisy training labels** (what counts as spam is subjective and contested), **adversarial inputs** (spammers adapt to your classifier), and **distribution shift** (the nature of spam changes over time, making models trained on historical data stale).

The post covers the feature engineering process for link spam: anchor text patterns (over-optimized exact-match anchor text was a strong signal in 2013), PageRank-adjacent link graph features, temporal velocity (links appearing in bulk bursts vs. natural accumulation), domain registration patterns, and TF-IDF anomalies in linking page content. Many of these features were discovered by analyzing cases where human reviewers disagreed — the disagreements revealed edge cases where the model's decision boundary needed work.

The adversarial dynamic is the genuinely hard part: once your classifier's decision boundary becomes known (either by reverse-engineering or by observing what gets penalized), spammers adjust their link patterns to cross the boundary. This requires retraining, which requires labeling, which is expensive. The only sustainable approach is either continuous labeling pipelines or unsupervised anomaly detection that catches patterns the spammers don't know you're looking for.

## Key points

- **Noisy labels**: is this spam? is a human judgment call with genuine disagreement — the classifier can only be as good as the label quality
- **Feature engineering** dominated the ML workflow in 2013: anchor text ratios, link velocity, TF-IDF of linking pages, domain age — all hand-crafted signals before deep learning automated representation learning
- **Adversarial ML**: classifiers in security contexts face an active adversary that optimizes against the known decision boundary — concept drift is not random but directed
- Precision vs. recall tradeoff: false positives (penalizing legitimate links) destroy trust with publishers; false negatives (missing spam) degrade search quality — the tradeoff is explicit and business-driven
- Google's Penguin algorithm (April 2012) had just punished link spam at scale, creating demand for tools to audit link profiles — this was the business context for SEOMoz's feature
- Pre-cursor to modern adversarial ML research (GANs, adversarial examples) — the same conceptual problems in a practical industry application

[Original](http://www.seomoz.org/blog/machine-learning-and-link-spam-my-brush-with-insanity)
