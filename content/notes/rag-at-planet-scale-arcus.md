---
title: RAG at Planet Scale
date: 2023-10-07
categories:
  - rag
  - distributed-systems
  - llm
  - retrieval
  - scaling
description: Arcus describes their multi-tiered RAG approach for handling massive external data corpora at planet scale — one of the largest RAG deployments of 2023. The key innovation is tiered retrieval that narrows the candidate pool progressively rather than searching the full index directly.
params:
  source: pinboard
  sourceUrl: https://www.arcus.co/blog/rag-at-planet-scale
---

## Summary

Arcus operates at what they claim is one of the largest scales of RAG in the world, processing massive corpora of external data sources and customer internal data to provide context for LLMs. This post describes the architectural innovations they developed when traditional RAG approaches hit scaling walls at planet scale.

The standard RAG pattern — embed a query, find the top-k similar chunks from a flat vector index, feed them to an LLM — breaks down when the corpus reaches billions of documents. At that scale, even a fast approximate nearest neighbor search has too much noise (too many irrelevant candidates in the top-k), and the latency of searching a single massive index becomes prohibitive.

Arcus developed a multi-tiered approach: a first-pass rough retrieval layer (fast, high recall, tolerant of irrelevant results) narrows billions of documents down to thousands; a second-pass semantic retrieval layer further narrows to hundreds of candidates; a final reranker pass selects the final context to pass to the LLM. Each tier trades precision for recall at its specific scale, and the architecture distributes the computational cost across tiers. They also built specialized indices for different data types (structured vs. unstructured) rather than a single uniform vector index.

## Key points

- Planet-scale RAG breaks the standard flat vector index approach — requires multi-tiered retrieval.
- Tiered architecture: rough filter (billions → thousands) → semantic search → reranker (final context).
- Each tier optimized for its scale: different precision/recall tradeoffs, different index structures.
- Specialized indices for structured vs. unstructured data — not one-size-fits-all vector database.
- Arcus works on financial and enterprise data analysis at large scale.
- Architectural pattern: funnel retrieval progressively rather than trying to do precision at full scale.

[Original](https://www.arcus.co/blog/rag-at-planet-scale) → Arcus
