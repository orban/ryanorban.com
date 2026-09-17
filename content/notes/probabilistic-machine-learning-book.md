---
title: Probabilistic Machine Learning (Kevin Murphy)
date: 2022-03-02
categories:
  - machine-learning
  - books
  - probability
  - bayesian
  - education
description: Kevin Murphy's Probabilistic Machine Learning book series — a comprehensive treatment of ML through a probabilistic/Bayesian lens, freely available online. The 2012 original (MLPP) and its 2022 follow-ups are standard graduate-level references.
params:
  source: pinboard
  sourceUrl: https://probml.github.io/pml-book/
---

## Summary

Kevin Murphy's *Probabilistic Machine Learning* book series is a comprehensive, graduate-level treatment of machine learning framed through probability theory and Bayesian statistics. The original book, *Machine Learning: A Probabilistic Perspective* (2012), became a standard graduate reference. Murphy followed it with two updated volumes in 2022: *PML: An Introduction* (covering classical ML through a probabilistic lens) and *PML: Advanced Topics* (covering deep learning, generative models, inference algorithms).

The probabilistic framing distinguishes this series from other ML textbooks. Rather than presenting algorithms as procedures, Murphy grounds everything in probability: classification is posterior inference, regression is likelihood maximization, neural networks are flexible function approximators with probabilistic outputs, and uncertainty quantification is a first-class concern. This approach naturally leads to Bayesian deep learning, variational inference, and uncertainty estimation — topics that are either afterthoughts or absent in architecturally-focused texts.

The series is freely available online at `probml.github.io`, with companion Python notebooks using JAX for examples. The 2022 volumes reflect the state of the field post-deep learning revolution, incorporating variational autoencoders, normalizing flows, diffusion models, and transformers while maintaining the probabilistic perspective throughout.

This is the go-to reference for researchers who want theoretical rigor alongside practical relevance. It pairs well with [Understanding Deep Learning](/notes/understanding-deep-learning/) (Prince) for architectural intuition and Pattern Recognition and Machine Learning (Bishop) for classical Bayesian ML.

## Key points

- Three-volume series: original MLPP (2012), then *PML: Introduction* and *PML: Advanced Topics* (both 2022).
- All books freely available online — unusual for a graduate-level reference of this scope.
- Probabilistic framing throughout: every algorithm grounded in probability theory, uncertainty as first-class concern.
- Covers Bayesian inference, variational inference, deep generative models, diffusion models, transformers.
- JAX notebooks for all examples in the 2022 volumes.
- Complements [Understanding Deep Learning](/notes/understanding-deep-learning/) (architectural focus) and Bishop PRML (classical Bayesian ML).

[Original](https://probml.github.io/pml-book/) → GitHub
