---
title: "Not Just for Search: Using ElasticSearch with Machine Learning Algorithms"
date: 2014-03-10
categories:
  - elasticsearch
  - machine-learning
  - search
  - vector-search
  - infrastructure
description: An early (2013) case for using Elasticsearch beyond full-text search — specifically as a substrate for machine learning applications like nearest-neighbor lookup and feature indexing. Pre-dates the vector search era but anticipates the same pattern.
params:
  source: pinboard
  sourceUrl: http://euphonious-intuition.com/2013/04/not-just-for-search-using-elasticsearch-with-machine-learning-algorithms/
---

## Summary

This 2013 post explores Elasticsearch as infrastructure for machine learning applications beyond its primary use case of full-text search. The insight: Elasticsearch is essentially a distributed, indexed document store with fast query capabilities — and many ML workflows need exactly that, whether for storing feature vectors, running approximate nearest-neighbor lookups, or building recommendation systems.

The pattern the post describes predates vector databases by several years. In 2013-2014, practitioners were using Elasticsearch's inverted index and scoring functions as a proxy for similarity search. The approach was approximate and not designed for high-dimensional dense vectors, but it worked for sparse, keyword-rich feature representations common in NLP and collaborative filtering.

Elasticsearch was compelling in this context because it solved operational problems that pure ML infrastructure didn't: horizontal scaling, near-real-time indexing, a REST API for queries, and good tooling for monitoring. Using it as both the search layer and the ML serving layer reduced operational complexity compared to running separate systems. This dual-use pattern became more sophisticated later with Elasticsearch's addition of native vector field types and approximate nearest-neighbor search (HNSW).

## Key points

- Elasticsearch as ML infrastructure: leverage its distributed indexing and query execution for feature lookups and approximate similarity search.
- In 2013, sparse feature representations (term vectors, categorical features) mapped well to inverted indexes — dense embeddings came later.
- Common ML use cases: collaborative filtering (find users with similar item histories), content-based recommendation (find similar documents by feature overlap).
- The REST API made Elasticsearch easy to integrate into Python ML pipelines without a dedicated ML serving layer.
- Anticipates modern vector databases (Pinecone, Weaviate, Qdrant) which are purpose-built for what Elasticsearch handled as a workaround.

[Original](http://euphonious-intuition.com/2013/04/not-just-for-search-using-elasticsearch-with-machine-learning-algorithms/)
