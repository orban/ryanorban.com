---
title: "Sentence Transformers: Pretrained Models"
date: 2021-08-10
categories:
  - nlp
  - machine-learning
  - sentence-transformers
  - embeddings
  - semantic-search
description: The Sentence-BERT pretrained models documentation — a reference for choosing the right sentence embedding model for semantic similarity, semantic search, or paraphrase detection tasks. The go-to resource when you need to pick a model before training your own.
params:
  source: pinboard
  sourceUrl: https://sbert.net/docs/pretrained_models.html
---

## Summary

Sentence Transformers (SBERT) is a Python library from Nils Reimers and Iryna Gurevych that fine-tunes BERT-style models on natural language inference and semantic textual similarity tasks to produce high-quality sentence embeddings. The pretrained models page is a reference for choosing the right model for a task.

The key differentiation among pretrained models is the tradeoff between quality and speed. The all-mpnet-base-v2 model is the benchmark reference — highest quality on standard STS benchmarks but requires more compute. Models like all-MiniLM-L6-v2 trade a few quality points for 5x faster inference — useful when you're embedding millions of documents or doing real-time user query embedding. The paraphrase-multilingual series handles 50+ languages in a single model for cross-lingual applications.

Sentence Transformers solved a real problem with early BERT embeddings: the `[CLS]` token embedding from BERT's base pretraining is a poor sentence representation — it wasn't trained to encode overall sentence meaning. SBERT fine-tunes on sentence pair classification to make the embedding space semantically meaningful. The result: you can compute meaningful cosine similarity between two sentence embeddings to measure semantic relatedness, which is the foundation for semantic search, duplicate detection, and clustering.

## Key points

- Sentence Transformers fine-tunes BERT on NLI/STS to produce embeddings where cosine similarity = semantic similarity.
- Key model choice: `all-mpnet-base-v2` (best quality) vs. `all-MiniLM-L6-v2` (5x faster, slightly lower quality).
- Multilingual models: single model for 50+ languages — important for cross-lingual search applications.
- BERT `[CLS]` token is a poor sentence embedding; SBERT's fine-tuning is what makes the representations useful.
- Foundation for semantic search, duplicate detection, document clustering, and paraphrase identification.

[Original](https://sbert.net/docs/pretrained_models.html)
