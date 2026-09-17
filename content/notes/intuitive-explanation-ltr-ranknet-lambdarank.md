---
title: "Intuitive Explanation of Learning to Rank: RankNet, LambdaRank, and LambdaMART"
date: 2020-07-25
categories:
  - machine-learning
  - learn-to-rank
  - information-retrieval
  - search
  - ranking
description: Nikhil Dandekar's intuitive explainer on the evolution from pointwise to pairwise to listwise learning-to-rank, covering RankNet, LambdaRank, and LambdaMART. One of the best conceptual introductions to how modern search ranking algorithms actually work.
params:
  source: pinboard
  sourceUrl: https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418
---

## Summary

This article by Nikhil Dandekar walks through the evolution of learning-to-rank (LTR) from first principles. The three generations of LTR algorithms correspond to three ways of framing the ranking problem. **Pointwise** methods treat ranking as regression or classification on individual documents — predict a relevance score per document, rank by score. The problem: they don't optimize the actual ranking objective, just a surrogate. **Pairwise** methods (RankNet) model the problem as: given two documents, which should rank higher? Optimize the cross-entropy loss on all pairs. This is much closer to what ranking actually means, but still indirect — pairwise loss doesn't directly optimize metrics like NDCG. **Listwise** methods optimize a ranking metric directly.

RankNet (Burges et al., Microsoft Research, 2005) is the pairwise foundation: a neural network trained on pairwise preferences. Given documents A and B, the model learns a score function such that the probability it assigns to "A should rank above B" matches the human preference labels. The gradient update is efficient because you can factor out the computation. LambdaRank improves on RankNet by weighting the pairwise gradients by the change in NDCG a swap would produce — you still compute pairwise comparisons, but you upweight the pairs that matter most to your actual metric. LambdaMART replaces the neural network in LambdaRank with gradient boosted trees (MART — Multiple Additive Regression Trees), which in practice outperforms the neural version on most tabular ranking problems due to gradient boosting's efficiency on structured features.

The result is LambdaMART — the algorithm underlying almost every major production search ranking system for most of the 2010s and still widely used today. It appears in LETOR benchmark comparisons, powers ranking at Bing, and is implemented in libraries like XGBoost, LightGBM, and the dedicated RankLib toolkit.

## Key points

- Three LTR paradigms: pointwise (score documents), pairwise (RankNet), listwise (optimize metric directly).
- RankNet: neural network trained on pairwise document preferences with cross-entropy loss.
- LambdaRank: extends RankNet by weighting pairwise gradients by NDCG improvement — more efficient use of training signal.
- LambdaMART: combines Lambda gradients with gradient boosted trees (MART) — most practically effective combination.
- Directly related to LambdaMART in Depth coverage in vault; see also Metarank and hybrid search with Metarank.
- NDCG (Normalized Discounted Cumulative Gain) is the canonical ranking metric these algorithms optimize.

[Original](https://medium.com/@nikhilbd/intuitive-explanation-of-learning-to-rank-and-ranknet-lambdarank-and-lambdamart-fe1e17fac418)
