---
title: Locality-Sensitive Hashing
date: 2013-03-30
categories:
  - algorithms
  - hashing
  - similarity-search
  - machine-learning
  - big-data
description: Locality-sensitive hashing (LSH) is a family of algorithms for approximate nearest-neighbor search — hashing high-dimensional vectors so that similar items hash to the same bucket with high probability. The practical solution to similarity search at scale when exact methods are too slow.
params:
  source: pinboard
  sourceUrl: https://en.wikipedia.org/wiki/Locality_sensitive_hashing
---

## Summary

[Locality-sensitive hashing](/notes/locality-sensitive-hashing/) (LSH) is a class of algorithms designed to solve the approximate nearest-neighbor search problem: given a query item and a large dataset, find items that are approximately similar to the query without computing all pairwise distances. The key insight: design hash functions where similar items are more likely to collide (hash to the same bucket) than dissimilar items — the opposite of what cryptographic hash functions are designed to do.

The problem LSH solves: naive nearest-neighbor search over N items requires O(N) distance computations per query. For N = 1 billion and high-dimensional embeddings (common in recommendation systems, document similarity, and image search), this is computationally infeasible. LSH reduces this to O(N^ρ) for some ρ < 1 by using multiple hash tables with different hash functions — items that collide in many tables are likely similar; items that never collide are likely distant.

Different distance metrics require different LSH families: MinHash for Jaccard similarity (good for set overlap, used in near-duplicate document detection), SimHash for cosine similarity (good for text vectors), random projections for Euclidean distance. The bookmark note — "LSH to bucket data points, coalesce into blocks on HDDs for sequential reads. SSDs for metadata lookup" — reflects a storage optimization context: using LSH to physically co-locate similar data points on disk so that similarity queries produce sequential I/O rather than random reads.

## Key points

- Approximate nearest-neighbor search: LSH trades exact answers for dramatic speedup — finds probably close neighbors rather than guaranteed exact nearest neighbors.
- MinHash for Jaccard similarity: hash sets of items so that collision probability = Jaccard similarity — widely used for near-duplicate web page detection.
- SimHash for cosine similarity: Google used SimHash for near-duplicate detection at web scale (2007 paper).
- Storage optimization: using LSH to co-locate similar items on disk turns random I/O similarity queries into sequential I/O — a systems-level trick.
- Modern successors: FAISS (Facebook AI), HNSW (Hierarchical Navigable Small World), and Annoy (Spotify) implement approximate nearest-neighbor at production scale.

[Original](https://en.wikipedia.org/wiki/Locality_sensitive_hashing)
