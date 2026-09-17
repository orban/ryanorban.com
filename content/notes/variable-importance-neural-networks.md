---
title: Variable Importance in Neural Networks
date: 2013-08-13
categories:
  - neural-networks
  - interpretability
  - r
  - variable-importance
  - machine-learning
description: R-bloggers post on measuring variable importance in neural networks — techniques like the Garson algorithm and Olden's method for attributing prediction contributions to input features. An early attempt at neural network interpretability before SHAP, LIME, and modern explainability tools existed.
params:
  source: pinboard
  sourceUrl: http://www.r-bloggers.com/variable-importance-in-neural-networks/
---

![Variable Importance in Neural Networks](/images/notes/variable-importance-neural-networks.png)

## Summary

This R-bloggers post by Beck Marcus covered methods for computing variable importance in neural networks — techniques to attribute how much each input feature contributes to predictions. In 2013, neural networks in practice meant small feedforward networks trained with backpropagation, often with a single hidden layer, used for regression and classification tasks in R packages like `neuralnet` and `nnet`.

The challenge with neural network interpretability — compared to decision trees or linear regression — is that importance isn't directly readable from the model parameters. Weights are entangled across layers and can't be summed straightforwardly. Methods like the Garson algorithm (1991) decompose connection weights by tracing paths through the network and attributing proportional contributions; Olden's method uses the product of input-hidden and hidden-output weights to score feature contributions. Both are heuristic rather than theoretically rigorous, but practical for small networks.

This work predates modern explainability tools by several years: LIME appeared in 2016, SHAP in 2017. The demand for interpretable ML was real in 2013 but the tooling was primitive. The R ecosystem had these small-network-specific methods; practitioners using scikit-learn often fell back on permutation importance or just ran random forests where feature importance was built in and better understood.

## Key points

- Garson algorithm: decomposes neural network weights to estimate input variable importance — proportional contribution based on connection weights through all hidden nodes.
- Olden's method: uses the product of input-to-hidden and hidden-to-output weights summed across hidden nodes — captures the full connection path contribution.
- Limitation: both methods assume weight magnitudes reflect importance, which breaks down with regularization, weight sharing, or non-trivial activation patterns.
- Context: small feedforward networks in R were common for structured data; the methods were designed for this scale, not deep multi-layer networks.
- Precursor to SHAP and LIME: the interpretability demand was there in 2013, but the tools that would generalize to complex networks didn't exist yet.
- Why not just use random forests? Random forests' feature importance was better understood and more reliable — neural nets were often chosen for accuracy, then justified with post-hoc interpretation.

[Original](http://www.r-bloggers.com/variable-importance-in-neural-networks/)
