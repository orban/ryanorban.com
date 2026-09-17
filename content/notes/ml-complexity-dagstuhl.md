---
title: Machine Learning and Complexity Theory
date: 2023-02-21
categories:
  - ml-theory
  - complexity-theory
  - research
  - academia
  - theory
description: A theoretical computer scientist's reflection on the relationship between machine learning and computational complexity theory after a Dagstuhl seminar — noting that the two fields remain largely disconnected despite studying adjacent phenomena. Raises questions about whether complexity theory has useful things to say about why ML works.
params:
  source: pinboard
  sourceUrl: https://blog.computationalcomplexity.org/2022/09/machine-learning-and-complexity.html
---

![Machine Learning and Complexity Theory](/images/notes/ml-complexity-dagstuhl.png)

## Summary

This blog post by Lance Fortnow (editor of the Computational Complexity blog) reflects on a Dagstuhl seminar that brought machine learning researchers and computational complexity theorists together. The observation: despite ML and complexity theory both being concerned with computation and learning, the two communities have developed largely in parallel with limited mutual influence.

The complexity theory perspective on ML is interesting and underexplored. PAC learning (probably approximately correct learning) is the formal bridge — complexity theory's framework for asking when efficient learning is possible in principle. But modern deep learning success doesn't fit cleanly into PAC learning — it works far beyond the regimes where the theory makes predictions. The empirical success of overparameterized models trained with gradient descent is not well-explained by existing complexity-theoretic frameworks.

The post raises the productive question: should we expect complexity theory to explain why ML works, or is ML operating in a regime where the theory's assumptions break down? The double descent phenomenon (where more model parameters improve generalization past the interpolation threshold) is a concrete example of ML behavior that defies classical learning theory. This tension between theory and empirical ML reality is one of the more intellectually honest conversations in ML research.

## Key points

- Machine learning and computational complexity developed in parallel — limited mutual influence despite adjacent concerns.
- PAC learning is the formal bridge, but modern deep learning success doesn't fit PAC learning's predictions.
- Overparameterized models + gradient descent work in ways that existing theory doesn't explain.
- Double descent is a concrete example: more parameters → worse then better generalization, beyond classical theory.
- Honest reflection on a productive disciplinary gap: neither field has absorbed the other's key results.

[Original](https://blog.computationalcomplexity.org/2022/09/machine-learning-and-complexity.html)
