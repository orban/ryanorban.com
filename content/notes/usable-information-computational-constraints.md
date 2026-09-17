---
title: A Theory of Usable Information Under Computational Constraints
date: 2025-03-25
categories:
  - information-theory
  - machine-learning
  - representation-learning
  - iclr-2020
description: ""
params:
  source: papers
  sourceUrl: https://arxiv.org/abs/2002.10689
---

## Summary

Yilun Xu, Shengjia Zhao, Jiaming Song, Russell Stewart, and Stefano Ermon (Stanford, ICLR 2020 oral) extend Shannon information theory to account for the fact that an observer's computational capacity shapes what information is actually useful to them. Their concept of V-information — predictive information relative to a hypothesis class V — differs from classical mutual information in a striking way: it can increase through computation, violating the data processing inequality.

The intuition is clean. Classical mutual information is a property of the joint distribution over variables — it can't be created by transforming data, only preserved or lost. But if you condition on what a specific model class can actually compute with that data, then a learned feature representation can make information more accessible than the raw input. This is exactly what happens when a deep network learns a hierarchy of representations: each layer doesn't add information in the Shannon sense, but it makes the relevant information more usable for the downstream task.

The paper formalizes this with PAC-style statistical guarantees for estimating V-information in high-dimensional settings, which makes it practically deployable rather than purely theoretical. Demonstrated applications include structure learning (identifying causal or statistical dependencies) and fair representation learning (constructing representations that are informative for a target task but uninformative about a protected attribute). The framework gives a principled way to talk about what a representation learning algorithm is actually doing — not maximizing information preservation, but maximizing usable information for a constrained observer.

## Key points

- Classical mutual information is fixed by the data distribution; V-information extends this to account for what a hypothesis class V can compute, allowing information to be created through representation learning
- Violates the data processing inequality by design — this is a feature, not a bug: it captures the information gain from learning good features
- Provides PAC-style estimation guarantees, making the framework applicable to real high-dimensional datasets
- Applications in structure learning and fair representation learning demonstrate practical utility beyond the theoretical contribution
- Stefano Ermon's group at Stanford positions this as a foundation for understanding why deep representation learning works from an information-theoretic perspective

[Original paper](https://arxiv.org/abs/2002.10689)
