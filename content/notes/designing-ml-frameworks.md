---
title: Designing Machine Learning Frameworks
date: 2013-09-18
categories:
  - machine-learning
  - software-design
  - frameworks
  - api-design
  - architecture
description: Mikio Braun's reflection on the design principles behind ML frameworks — the tensions between flexibility and usability, scikit-learn's consistency, and what makes a good ML library API. Written by the author of jBLAS.
params:
  source: pinboard
  sourceUrl: http://blog.mikiobraun.de/2013/09/designing-machine-learning-frameworks.html
---

![Designing Machine Learning Frameworks](/images/notes/designing-ml-frameworks.png)

## Summary

Mikio Braun (author of jBLAS, a Java linear algebra library) reflected on the design challenges of building machine learning frameworks — a topic that was very live in 2013 as scikit-learn, Theano, Weka, and others were all making different design choices. The core tension: generality (supporting every algorithm and use case) vs. usability (a clean, consistent API that new users can learn quickly).

scikit-learn's design philosophy was influential and explicit: a consistent `fit/predict/transform` API across all estimators, explicit separation of model specification from fitting, and a pipeline abstraction that composed transformers and estimators. This consistency enabled powerful meta-learning tools (grid search, cross-validation, pipelines) that worked across all algorithms. The cost was inflexibility for novel algorithms that didn't fit the paradigm.

Braun's piece likely covered: how to abstract over different algorithm types, what an ideal data representation layer looks like, how to handle the exploration (interactive analysis) vs. production (deployed model) workflow split, and what the right level of abstraction is for a framework that will be used by both beginners and experts.

## Key points

- The core ML framework design tension: generality (every algorithm fits) vs. usability (consistent, learnable API).
- scikit-learn's `fit/predict/transform` API is the gold standard for consistent ML library design — enables composable pipelines and meta-learning.
- Mikio Braun brought a systems/JVM perspective (from jBLAS) to a space dominated by Python scientists.
- The exploration vs. production split: interactive notebooks for analysis, but ML frameworks also need to support deployment pipelines.
- Written in 2013 — before TensorFlow (2015) and PyTorch (2016) shifted ML framework design toward differentiable programming models.

[Original](http://blog.mikiobraun.de/2013/09/designing-machine-learning-frameworks.html)
