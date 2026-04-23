---
title: Why Deep Learning Works Unreasonably Well
date: 2025-08-20
categories:
  - machine-learning
  - deep-learning
  - theory
  - youtube
  - education
description: Part 3 of a 'How Models Learn' series on why deep learning works unreasonably well — addressing the apparent paradox that overparameterized models generalize when classical statistics says they shouldn't. Covers implicit regularization, loss landscape geometry, and the lottery ticket hypothesis.
params:
  source: pinboard
  sourceUrl: https://www.youtube.com/embed/qx7hirqgfuU
---

![Why Deep Learning Works Unreasonably Well](/images/notes/why-deep-learning-works.png)

## Summary

This YouTube video (Part 3 of a How Models Learn series) addresses one of the most important puzzles in modern machine learning: why do overparameterized deep learning models generalize to new data, when classical statistical learning theory says models with more parameters than training samples should overfit dramatically? The unreasonably well framing comes from the empirical observation that deep learning works far better than theory predicted.

Several explanations have emerged: implicit regularization via stochastic gradient descent (SGD finds flat minima that generalize better), loss landscape geometry (deep networks have many equivalent minima and SGD's noise helps navigate to generalizing ones), and the lottery ticket hypothesis (large networks contain sparse subnetworks that can learn effectively). The double descent phenomenon — where test error decreases again after rising during interpolation — challenged classical learning curves.

Understanding why deep learning works matters for knowing when it will fail and how to improve it. These mechanistic explanations — even incomplete ones — connect to mechanistic interpretability work and inform training choices like learning rate schedules and weight decay.

## Key points

- The paradox: overparameterized models shouldn't generalize but do — why?
- Implicit regularization: SGD finds flat minima that generalize better than sharp ones.
- Loss landscape geometry: many equivalent minima, noise helps navigate to good ones.
- Lottery ticket hypothesis: large networks contain trainable sparse subnetworks.
- Double descent: test error improves again after interpolation threshold — challenging classical curves.
- Part 3 of a series — builds on prior episodes on gradient descent and training dynamics.

[Original](https://www.youtube.com/embed/qx7hirqgfuU)
