---
title: "Faiss: The Missing Manual"
date: 2021-11-20
categories:
  - vector-search
  - machine-learning
  - faiss
  - embeddings
  - similarity-search
description: Pinecone's comprehensive tutorial on FAISS (Facebook AI Similarity Search) — the foundational open-source library for approximate nearest neighbor search over dense vectors. Essential reading before choosing or building any vector search system.
params:
  source: pinboard
  sourceUrl: https://www.pinecone.io/learn/faiss-tutorial/
---

## Summary

FAISS (Facebook AI Similarity Search) is Meta AI Research's open-source library for efficient similarity search and clustering of dense vector embeddings. Released in 2017, it became the foundational tool for approximate nearest neighbor (ANN) search before the managed vector database category existed. This Pinecone tutorial fills the gap between FAISS's academic documentation and practical deployment.

The core FAISS abstraction is the index — a data structure that stores vectors and supports similarity queries. Different index types trade off search accuracy, memory usage, and query speed. The tutorial covers the main options: `IndexFlatL2` (exact brute-force, useful as a baseline), `IndexIVFFlat` (inverted file index, clusters vectors into Voronoi cells, only searches nearby cells), and `IndexIVFPQ` (adds product quantization to compress stored vectors, trading some accuracy for a large memory reduction).

FAISS is the underlying library that Pinecone, Weaviate, and many other vector database services wrap. Understanding FAISS indexes directly is valuable for debugging retrieval quality, choosing the right index type, and understanding the accuracy-speed tradeoff inherent in ANN search. The `nprobe` parameter (how many Voronoi cells to search) is particularly important: setting it too low misses relevant vectors, too high negates the speed advantage.

## Key points

- FAISS is the foundation of most vector search systems — learning it gives you the mental model for the whole category.
- Index types matter: `Flat` for exact search, `IVF` for speed at scale, `IVFPQfor` memory efficiency at very large scale.
- Product quantization compresses vectors to ~1/8 their size with manageable accuracy loss — essential for billion-scale indexes.
- `nprobe` is the main search quality lever: higher values = better recall, slower queries.
- GPU acceleration is available for batch indexing and querying — important for training large indexes quickly.

[Original](https://www.pinecone.io/learn/faiss-tutorial/)
