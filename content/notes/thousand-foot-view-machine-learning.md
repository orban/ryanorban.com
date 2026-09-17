---
title: A Thousand-Foot View of Machine Learning
date: 2013-06-18
categories:
  - machine-learning
  - overview
  - data-science
  - algorithms
  - fundamentals
description: A high-level orientation to machine learning from 2009 — the major paradigms (supervised, unsupervised, reinforcement), the core families of algorithms, and when to apply each. A useful framing piece for someone entering the field.
params:
  source: pinboard
  sourceUrl: http://awwthor.wordpress.com/2009/12/31/a-thousand-foot-view-of-machine-learning/
---

![A Thousand-Foot View of Machine Learning](/images/notes/thousand-foot-view-machine-learning.png)

## Summary

This 2009 Awwthor post provides a bird's-eye orientation to machine learning — the kind of overview useful for someone who understands the individual algorithms but wants a mental map of how the field is organized. Written before the deep learning era transformed ML's landscape, it captures the classical ML taxonomy at its clearest.

The core division: supervised learning (you have labeled examples and train a model to predict labels on new inputs), unsupervised learning (you have unlabeled data and want to discover structure — clusters, dimensions, associations), and reinforcement learning (an agent takes actions in an environment and learns from reward signals). These three paradigms organize the field's major algorithm families.

Within supervised learning: classification (discrete outputs — spam/not spam, disease/no disease) vs regression (continuous outputs — price prediction, demand forecasting). Each has its own family of algorithms with different inductive biases, computational costs, and assumptions. The 2009 view was clean: naive Bayes, SVM, decision trees, logistic regression for classification; linear regression, ridge regression, SVR for regression. The proliferation of ensemble methods and neural networks came after.

## Key points

- Three paradigms structure the entire field: supervised learning (labeled data), unsupervised learning (unlabeled), reinforcement learning (reward signals).
- Inductive bias is the key conceptual tool: every algorithm embeds assumptions about the relationship between inputs and outputs — choosing an algorithm means choosing which assumptions match your problem.
- The bias-variance tradeoff: complex models fit training data better but generalize worse; simple models do the reverse — every practitioner's central tuning tension.
- Feature engineering was the dominant SKILL in 2009's classical ML era: getting the representation right mattered more than which algorithm you used.
- This taxonomy held until ~2012-2013 when deep learning started automating feature extraction and collapsing the classification/regression boundary.

[Original](http://awwthor.wordpress.com/2009/12/31/a-thousand-foot-view-of-machine-learning/)
 → AI agent
