---
title: Building a Recommender System Using Embeddings
date: 2020-07-18
categories:
  - recommender-systems
  - embeddings
  - machine-learning
  - product
  - similarity
description: Drop Engineering's walkthrough of building a brand recommender using learned embeddings — training entity embeddings from user-brand interaction data to capture brand similarity in continuous vector space. A practical case study in embedding-based recommendations.
params:
  source: pinboard
  sourceUrl: https://drop.engineering/building-a-recommender-system-using-embeddings-de5a30e655aa
---

![Building a Recommender System Using Embeddings](/images/notes/building-recommender-system-embeddings.png)

## Summary

Drop Engineering describes building a recommender system for their product platform using entity embeddings learned from user-brand interaction data. The core technique: treat brands like words in word2vec — if two brands frequently appear together in the same user's purchase history, they're contextually similar and should be close in embedding space. Training this embedding model on interaction co-occurrence produces a continuous vector space where brand similarity can be measured via cosine similarity.

The approach is a variant of collaborative filtering via embeddings: rather than building a user-item matrix and factorizing it (matrix factorization), you train a shallow neural network to predict brand co-occurrence (similar to Skip-gram in word2vec). The embeddings that result capture both explicit category similarity (running shoe brands cluster together) and subtler affinity signals (brands that share a customer demographic cluster even if categorically different).

The business use case: once you have brand embeddings, recommendations become nearest-neighbor search in embedding space. If a user has purchased from brand A, recommend brands close to A in the embedding space. Scaling this requires approximate nearest neighbor (ANN) search (e.g., FAISS, ScaNN, HNSW) because exact nearest-neighbor search over millions of items is too slow. The post also notes that brand embeddings can be combined with other features for downstream ML tasks — a common pattern where learned representations become features in larger models.

## Key points

- Entity embeddings via co-occurrence training: brands that appear together in user histories get similar embeddings.
- Technique: Skip-gram-style training on brand co-occurrence — same idea as word2vec, applied to user-brand interactions.
- Embeddings capture category similarity *and* demographic affinity — latent structure beyond explicit categories.
- Recommendations as nearest-neighbor search in embedding space: fast via approximate nearest neighbor indices.
- Brand embeddings as reusable features: can be input to other ML models (ranking, lifetime value prediction).
- Related to NVIDIA Merlin recommender system and DoorDash search and recommendations in the vault.

[Original](https://drop.engineering/building-a-recommender-system-using-embeddings-de5a30e655aa)
