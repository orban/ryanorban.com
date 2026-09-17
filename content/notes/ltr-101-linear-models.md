---
title: "Learning to Rank 101: Linear Models"
date: 2020-07-25
categories:
  - learn-to-rank
  - information-retrieval
  - search
  - machine-learning
  - elasticsearch
description: OpenSource Connections' foundational explainer on linear models for learning-to-rank — the first step before gradient boosted trees. Covers feature engineering and the intuition for why linear LTR models are both a useful starting point and a useful baseline.
params:
  source: pinboard
  sourceUrl: https://opensourceconnections.com/blog/2017/04/01/learning-to-rank-linear-models/
---

## Summary

This OpenSource Connections post introduces learning-to-rank with linear models as the pedagogical starting point. Before reaching for LambdaMART or gradient boosted trees, understanding the linear baseline is important both conceptually and practically. A linear LTR model is simply a weighted sum of features: `score = w1*bm25 + w2*recency + w3*pagerank + ...`. The weights are learned from training data.

The value of linear models in search ranking goes beyond just being simple. First, they're interpretable — you can inspect the weights and understand what the model learned. A high weight on exact phrase match tells you something meaningful about your search problem. Second, they set a meaningful baseline. If your LambdaMART model doesn't substantially beat the linear baseline, you're either feature-limited or have a data quality problem. Third, for some search domains (especially with small training datasets), a regularized linear model can actually outperform tree models due to lower variance.

The feature engineering problem is the same regardless of model complexity: you need to define what signals matter for your ranking problem and log those signals for your query-document pairs. Common features: BM25 score (query-document term overlap), TF-IDF variants, phrase match score, query-title match, document recency, pagerank or authority signals, and personalization features. The elasticsearch-ltr plugin framework for logging these features applies whether you're training a linear model or a full LambdaMART model.

## Key points

- Linear LTR: weighted sum of hand-engineered features — simple, interpretable, strong baseline.
- Same feature logging infrastructure as complex models — linear is a good entry point before adding model complexity.
- Interpretable weights: high weight on "exact phrase match" → model learned phrase specificity matters for your domain.
- If LambdaMART doesn't beat the linear baseline, you have a feature or data quality problem, not a model complexity problem.
- MART (gradient boosted trees) learns feature interactions; linear models can't — but that may not matter for your use case.
- Series context: see also Elasticsearch LTR tutorial, LTR Infrastructure, Solr LTR.

[Original](https://opensourceconnections.com/blog/2017/04/01/learning-to-rank-linear-models/)
