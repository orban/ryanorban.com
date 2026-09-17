---
title: "PRML: Pattern Recognition and Machine Learning Algorithms in Python"
date: 2020-03-01
categories:
  - machine-learning
  - python
  - statistics
  - open-source
  - education
description: Python implementations of algorithms from Bishop's 'Pattern Recognition and Machine Learning' — the canonical probabilistic ML textbook. Bridges the gap between the math in the book and working code.
params:
  source: pinboard
  sourceUrl: https://github.com/ctgk/PRML
---

![PRML: Pattern Recognition and Machine Learning Algorithms in Python](/images/notes/prml-algorithms-python.png)

## Summary

Christopher Bishop's Pattern Recognition and Machine Learning (PRML) is the canonical textbook for probabilistic machine learning — covering Bayesian inference, Gaussian processes, graphical models, variational inference, mixture models, neural networks, and more, with mathematical rigor. The book is theory-heavy; this GitHub repository by ctgk provides Python implementations of the algorithms to make the math executable.

The implementation approach: each chapter of PRML gets a corresponding Python module implementing the algorithms from that chapter. This lets readers go from the mathematical derivation in the book to a running implementation, which substantially accelerates understanding. Probabilistic ML involves enough linear algebra and calculus that even careful readers benefit from seeing the operations as NumPy code — the indexing and broadcasting operations make abstract matrix equations concrete.

Topics implemented: Bayesian linear regression, Gaussian mixture models with EM algorithm, principal component analysis (PCA), hidden Markov models (HMM), support vector machines (SVM), neural networks (pre-deep learning style), Gaussian processes, variational autoencoders, mixture of experts, and kernel methods. This covers essentially all of classical probabilistic ML.

## Key points

- Python implementations of algorithms from Bishop's PRML — bridges the math-to-code gap.
- Covers: Bayesian inference, EM algorithm, Gaussian mixture models, PCA, HMM, SVM, Gaussian processes, neural networks.
- NumPy-based implementations: algebra operations are directly visible, not hidden by framework abstractions.
- Learning use: implement alongside reading to verify understanding before moving to the next chapter.
- PRML itself is among the books recommended in [Top ML Books 2020](/notes/top-ml-books-2020/) vault note.

[Original](https://github.com/ctgk/PRML)
