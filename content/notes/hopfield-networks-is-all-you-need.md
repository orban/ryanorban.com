---
title: Hopfield Networks is All You Need
date: 2022-05-29
categories:
  - hopfield-networks
  - transformers
  - attention
  - associative-memory
  - deep-learning
  - theory
description: Ramsauer et al. introduce a modern continuous-state Hopfield network with exponential storage capacity and prove that its update rule is mathematically equivalent to transformer self-attention. This is the foundational paper connecting classical associative memory to the attention mechanism, explaining why transformers work through an energy-function lens.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2008.02217.pdf
---

## Summary

Hubert Ramsauer, Bernhard Schäfl, Johannes Lehner, Philipp Seidl, Michael Widrich, and colleagues at Johannes Kepler University Linz (including Sepp Hochreiter) present a modern reformulation of Hopfield networks with continuous states that resolves a decades-old bottleneck in associative memory: storage capacity. Classical binary Hopfield networks could only store roughly 0.14N patterns for N neurons; the new continuous-state version stores exponentially many — scaling as the exponent of the dimension of the associative space. Patterns are retrieved in a single update step rather than through iterative relaxation.

The paper's central result is that this new Hopfield network update rule is mathematically identical to the self-attention mechanism used in transformer architectures. This equivalence isn't a curiosity — it provides a theoretical grounding for why attention works: each attention head is performing associative memory retrieval from a Hopfield network whose stored patterns are the value vectors. The softmax operation that appears in attention corresponds directly to the energy function's gradient in the Hopfield formulation. This connection has since been elaborated by Dmitry Krotov and others in the associative memory literature (see modern methods for associative memory and the ICML 2025 tutorial series).

The authors demonstrate practical applications: a Hopfield layer used as a pooling mechanism for multiple instance learning achieves state-of-the-art on drug activity prediction datasets. The layer learns to retrieve the most relevant instances from a bag, acting as a learned attention-based aggregator. This work bridges the theoretical foundations of recurrent neural networks and the empirical success of transformer architectures, providing a unified vocabulary for understanding memory, retrieval, and attention in deep learning systems.

## Key points

- Modern Hopfield networks with continuous states store exponentially many patterns — solving the classical capacity bottleneck
- Single update step retrieval (vs. iterative relaxation in classical networks) makes them practical as neural network layers
- The update rule is provably equivalent to self-attention in transformers — attention is Hopfield retrieval
- softmax in attention corresponds to the Lagrangian / energy gradient in the Hopfield formulation
- Applied to multiple instance learning for drug design: Hopfield pooling outperforms standard attention pooling
- Foundational paper for the connection between energy-based models, associative memory, and modern deep learning

[Original](https://arxiv.org/abs/2008.02217)
