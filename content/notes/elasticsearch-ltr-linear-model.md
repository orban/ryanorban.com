---
title: Test Driving Elasticsearch Learning to Rank with a Linear Model
date: 2020-07-25
categories:
  - elasticsearch
  - learn-to-rank
  - information-retrieval
  - search
  - open-source
description: OpenSource Connections' hands-on tutorial for the Elasticsearch Learning to Rank plugin with a linear model — walks through feature logging, model training, and deployment. The entry point for adding ML-powered ranking to an existing Elasticsearch stack.
params:
  source: pinboard
  sourceUrl: https://opensourceconnections.com/blog/2017/04/03/test-drive-elasticsearch-learn-to-rank-linear-model/
---

## Summary

OpenSource Connections (Doug Turnbull's company, who also wrote LambdaMART In Depth) publishes a series on Elasticsearch learning-to-rank (LTR). This tutorial is the practical starting point: how to actually implement LTR in an Elasticsearch deployment using the elasticsearch-ltr plugin.

The workflow for LTR in Elasticsearch follows a three-phase pattern. First, **feature logging**: you define a set of features (BM25 score, phrase match score, query-title overlap, recency, etc.) and log those feature values for query-document pairs from your real traffic. Second, **model training**: you take the logged features plus relevance judgments (either human editorial labels or implicit feedback from clicks) and train a LambdaMART model using a tool like RankLib or XGBoost. Third, **deployment**: you upload the trained model to Elasticsearch's LTR plugin, which re-scores candidates at query time using the model.

The linear model in this tutorial is the simplest possible starting point — a linear combination of features — which is useful for understanding what signals matter before moving to the full gradient boosted trees approach. A linear model is interpretable: you can read off the feature weights to understand which signals the model learned to trust. The elasticsearch-ltr plugin supports both linear and tree-based models through a common interface.

## Key points

- Elasticsearch LTR plugin: enables ML-based re-ranking within Elasticsearch query execution.
- Three-phase workflow: feature logging → model training → model upload and deployment.
- Start with linear models for interpretability before moving to LambdaMART (gradient boosted trees).
- OpenSource Connections is the primary steward of LTR tooling in the Elasticsearch ecosystem.
- Feature logging happens at query time — Elasticsearch logs feature values for documents in the result set.
- Related: [LTR 101 Linear Models](/notes/ltr-101-linear-models/), Infrastructure for LTR, Solr LTR (same pattern, different engine).

[Original](https://opensourceconnections.com/blog/2017/04/03/test-drive-elasticsearch-learn-to-rank-linear-model/)
