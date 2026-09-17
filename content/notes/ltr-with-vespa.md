---
title: Learning to Rank with Vespa
date: 2020-07-25
categories:
  - learn-to-rank
  - vespa
  - information-retrieval
  - search
  - machine-learning
description: Thiago Martins' tutorial on learning-to-rank with Vespa for text search — covers how Vespa's native ML integration makes LTR simpler than Elasticsearch/Solr plugins, with models evaluated inside the search engine. Vespa's approach to embedding LTR natively.
params:
  source: pinboard
  sourceUrl: https://medium.com/vespa/learning-to-rank-with-vespa-9928bbda98bf
---

## Summary

Vespa is Yahoo's open-source search and recommendation engine, now independently operated. Unlike Elasticsearch and Apache Solr, which added LTR via plugins after the fact, Vespa was designed from the start with ML ranking as a first-class feature. This tutorial by Thiago G. Martins covers how to use Vespa's learning-to-rank capabilities for text search.

The key architectural difference: in Vespa, ML models are evaluated *inside* the search engine's ranking phase rather than as a separate reranking step. Vespa has a native rank profile system where you define ranking expressions that can include ML model evaluation alongside classical BM25 scores. This tight integration means feature computation and model evaluation happen in the same execution path, reducing latency compared to the external reranker pattern used in Elasticsearch LTR and Apache Solr LTR.

Vespa supports multiple ML model formats directly: ONNX models (covering PyTorch and TensorFlow exports), XGBoost/LightGBM models (for gradient boosted trees), and Vespa's own expression language for simple models. This makes it practical to train a LambdaMART model in Python and deploy it directly to Vespa without a translation layer.

## Key points

- Vespa has native first-class ML ranking support — models run inside the search execution path, not as external rerankers.
- Rank profiles let you combine classical retrieval (BM25) with ML scoring in a single expressive ranking function.
- Supports ONNX, XGBoost, LightGBM model formats — trained in Python, deployed to Vespa directly.
- Lower latency than external reranking patterns (Elasticsearch LTR, Solr LTR) because feature computation is co-located with model evaluation.
- Yahoo origin: Vespa powers Yahoo's search and recommendations at production scale — LTR support reflects real production requirements.
- Part of the learning-to-rank cluster; see also Metarank for the open-source LTR orchestration layer.

[Original](https://medium.com/vespa/learning-to-rank-with-vespa-9928bbda98bf)
