---
title: What Learning Algorithm Is In-Context Learning? Investigations with Linear Models
date: 2022-11-30
categories:
  - llm
  - in-context-learning
  - transformers
  - theory
  - linear-models
description: ICLR 2023 paper showing that transformers trained on in-context learning tasks implicitly implement gradient descent and ridge regression on linear problems, with layers encoding weight vectors and moment matrices. Foundational theoretical work explaining ICL as implicit algorithm execution rather than pure pattern matching.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2211.15661.pdf
---

## Summary

Ekin Akyürek, Dale Schuurmans, Jacob Andreas, Tengyu Ma, and Denny Zhou (ICLR 2023) tackle the mechanistic question behind in-context learning: when a transformer adapts to a new task from a few examples, *what computation is it actually performing*? The paper provides three types of evidence — theoretical constructions, empirical comparisons, and analysis of learned representations — showing that transformers implicitly implement standard learning algorithms: primarily gradient descent and ridge regression, at least on linear problems.

The theoretical contribution is constructive: the authors explicitly show that a transformer can implement one step of gradient descent for linear regression using its attention and feedforward components. This isn't just an observation — it's a proof that the architecture is expressive enough to encode these algorithms. The empirical validation shows that trained transformers on linear regression tasks produce predictions that match those of gradient descent and ridge regression at the corresponding number of examples, and diverge from simpler baselines.

The representation analysis reveals that transformer layers encode weight vectors and moment matrices in interpretable ways — the internal state carries information about the current estimate of the optimal weights, updated as more in-context examples are processed. This ground-level mechanistic account complements the later "implicit MLP weight modification" account from the 2507.16003 paper; together they paint a picture of ICL as a structured computation over the in-context examples rather than statistical pattern matching.

## Key points

- Theoretical proof that transformers can implement gradient descent on linear problems in their attention+feedforward structure
- Empirical: trained transformers match gradient descent and ridge regression predictions on linear regression benchmarks — not just correlations, the predictions align
- Transformer layers encode weight vectors and moment matrices in interpretable ways — the residual stream carries a running estimate of the optimal solution
- Uses linear regression as the prototypical problem: analytically tractable enough for exact comparisons, complex enough to be informative
- Related to Learning without training (2507.16003): that paper explains the mechanism via MLP implicit weight modification; this paper shows the full algorithm (gradient descent) emerges in practice
- ICLR 2023 — one of the early influential mechanistic studies of in-context learning, predates the ICL mechanistic interpretability wave

[Original paper](https://arxiv.org/abs/2211.15661)
