---
title: "BERTopic: BERT-Based Topic Modeling"
date: 2023-02-15
categories:
  - topic-modeling
  - nlp
  - bert
  - embeddings
  - python
description: BERTopic is the leading open-source topic modeling library using sentence embeddings and clustering rather than word co-occurrence statistics — produces coherent, human-readable topics that LDA-style models often can't. The changelog tracks its evolution as the library added new backends and features.
params:
  source: pinboard
  sourceUrl: https://maartengr.github.io/BERTopic/changelog.html
---

![BERTopic: BERT-Based Topic Modeling](/images/notes/bertopic-topic-modeling.png)

## Summary

BERTopic is the dominant open-source topic modeling library built around sentence embeddings rather than traditional word co-occurrence statistics. Created by Maarten Grootendorst, it replaces LDA (Latent Dirichlet Allocation) and NMF with a pipeline: embed documents with a sentence transformer, reduce dimensionality with UMAP, cluster with HDBSCAN, then extract representative keywords per cluster using TF-IDF variants. The result is topics that are semantically coherent rather than just co-occurrence patterns.

Traditional topic modeling (LDA) produces topics that often look like word salad because they're driven by word frequency patterns rather than meaning. BERTopic's embedding-based approach groups documents by semantic similarity first, then labels the groups — which produces topic representations that actually make sense to humans. This is a fundamental architecture difference, not an incremental improvement.

The changelog link suggests this was bookmarked to track BERTopic's evolution. The library grew rapidly in this period, adding support for multiple embedding backends (OpenAI, Cohere, spaCy), online/incremental learning for streaming data, and advanced topic representations including LLM-generated topic labels. By early 2023, BERTopic had become the go-to for production topic modeling in Python.

## Key points

- Sentence embeddings → UMAP → HDBSCAN → TF-IDF keyword extraction — replaces LDA's word co-occurrence approach.
- Produces semantically coherent topics vs LDA's often-noisy word associations.
- By Maarten Grootendorst — actively maintained with frequent new features.
- Supports multiple embedding backends: Sentence Transformers, OpenAI, Cohere, spaCy.
- Added LLM-generated topic labels, incremental learning, and fine-grained topic control over 2022-2023.

[Original](https://maartengr.github.io/BERTopic/changelog.html) → GitHub
