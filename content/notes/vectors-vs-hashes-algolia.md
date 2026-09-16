---
title: Vectors Are Over? Hashes as the Future of AI Search
date: 2022-10-08
categories:
  - search
  - vector-database
  - embeddings
  - algolia
  - machine-learning
description: Algolia's provocative post arguing that hash-based retrieval outperforms vector search for many real-world search use cases — a counterargument to the vector database hype of 2022. Grounds the comparison in production search quality metrics.
params:
  source: pinboard
  sourceUrl: https://www.algolia.com/blog/ai/vectors-vs-hashes/
---

## Summary

Algolia's post makes a contrarian argument against the 2022 consensus that vector search / semantic search would replace traditional keyword search. The claim: for most production search use cases, hash-based or inverted-index approaches (BM25, TF-IDF) still outperform vector embeddings on recall, latency, and predictability — especially for short queries and e-commerce search where exact matching matters more than semantic similarity.

The argument is partly self-serving (Algolia's core product is keyword search infrastructure), but the underlying points have merit. Vector search excels when the vocabulary gap between query and document is large — searching "happy" returns joyful documents. But most users don't have vocabulary gaps; they search for exact product names, error codes, or specific terms. For these cases, the noise introduced by semantic similarity hurts more than it helps.

The more nuanced view (which Algolia has since moved toward): hybrid approaches combining keyword and vector retrieval outperform either alone. The post's framing as vectors are over is clickbait, but the underlying critique of naive vector-only search holds — and was validated by the subsequent consensus around hybrid retrieval in RAG and enterprise search systems.

## Key points

- Contrarian 2022 argument: hash/inverted-index search often beats vector search in production.
- BM25 and exact match excel for short, specific queries (product names, error codes).
- Vector search's advantage — bridging vocabulary gaps — is less relevant than assumed for most search.
- Hybrid approaches (keyword + vector) now the consensus for production search quality.
- From Algolia, who has a stake in the debate but makes valid technical points.
- Anticipates the hybrid RAG retrieval pattern that became standard in 2023-2024.

[Original](https://www.algolia.com/blog/ai/vectors-vs-hashes/)
