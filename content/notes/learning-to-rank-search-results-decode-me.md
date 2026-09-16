---
title: Using Machine Learning to Rank Search Results (Part 2)
date: 2020-07-25
categories:
  - learn-to-rank
  - information-retrieval
  - search
  - machine-learning
description: A practical tutorial on applying machine learning to re-rank search results — part 2 of a series covering feature engineering, training data construction, and evaluation for LTR in production search. Hands-on complement to the more theoretical LTR literature.
params:
  source: pinboard
  sourceUrl: https://dec0de.me/2014/10/learning-to-rank-2
---

## Summary

This tutorial from dec0de.me is part of a practical series on learning-to-rank for production search. Part 2 picks up after the basic setup to focus on the real engineering challenges: feature engineering for search ranking, constructing training data from query logs, and evaluating ranking improvements in a disciplined way.

The key problem with applying standard supervised learning to ranking is that you don't have a natural loss function. You can't minimize MSE on relevance scores because what matters is the relative order of results, not the absolute scores. This motivates the pairwise and listwise approaches covered in RankNet, LambdaRank, and LambdaMART — but this tutorial focuses on the practical feature engineering side rather than the algorithmic side, showing what signals are actually useful in real search systems.

Common features covered: BM25 and its variants for query-document term matching, phrase proximity scores, document freshness signals, click-through rate from past queries, and field-specific match scores (query matches title vs. body vs. URL). The training data construction problem — aligning feature logs with relevance labels — is where most real implementations run into friction. Human editorial labels are expensive; click logs are noisy. The tutorial discusses how to handle both.

## Key points

- Practical focus: feature engineering and training data construction for search LTR, not algorithm derivation.
- BM25, phrase proximity, recency, historical CTR, and field-specific matches are common useful features.
- Training data challenge: aligning feature logs with labels (editorial judgments or click signals).
- Click logs as implicit labels: clicks are biased toward the top of the page (position bias) — must be corrected.
- Evaluation: offline metric (NDCG, MAP) first, then online A/B test to measure business impact.
- Part of the learning-to-rank cluster; see also LTR 101, Elasticsearch LTR tutorial, Yandex personalised search.

[Original](https://dec0de.me/2014/10/learning-to-rank-2)
