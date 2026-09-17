---
title: "BLOOM Training Corpus: 2D Embedding Visualization"
date: 2022-07-12
categories:
  - bloom
  - embeddings
  - visualization
  - bigscience
  - nlp
description: A 2D UMAP visualization of 10 million text chunks from the BLOOM training corpus, encoded with all-distilroberta-v1. A rare window into the geometry of a frontier model's pretraining data.
params:
  source: pinboard
  sourceUrl: https://twitter.com/clured/status/1546913720340815873/photo/1
---

## Summary

This tweet by @clured visualizes a sample of the BLOOM model's pretraining corpus — 10 million text chunks from the English-language subset of the training data, approximately 1.25% of the total. The chunks were encoded using all-distilroberta-v1 (a sentence-transformers model) and projected to 2D with UMAP.

The visualization reveals the cluster structure of the BigScience training data: topic clusters emerge naturally from the embedding space, showing which domains and genres are well-represented in BLOOM's training distribution. These kinds of visualizations help diagnose training data composition — overrepresented domains (likely English web text) appear as dense clusters, while underrepresented topics are sparse.

This is the kind of exploratory data analysis that was rare to see publicly for frontier models at the time. OpenAI and Anthropic did not release training data details for GPT-3 or Claude respectively, making BLOOM's open training corpus a research opportunity. Understanding what's in the training data helps explain model behavior, bias, and capabilities — and this UMAP projection gives a visual entry point into that understanding.

## Key points

- 10M chunk sample ≈ 1.25% of the full BLOOM English training corpus
- Encoded with all-distilroberta-v1, a fast, general-purpose sentence embedding model from the sentence-transformers library
- UMAP projects the high-dimensional embedding space to 2D while preserving local cluster structure
- Cluster analysis of training data is standard practice for diagnosing data distribution and potential model bias
- Part of the broader BigScience transparency effort — BLOOM's training data was more documented than any contemporaneous frontier model

[Original](https://twitter.com/clured/status/1546913720340815873/photo/1)
