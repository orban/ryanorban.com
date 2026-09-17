---
title: Semantic Textual Similarity — Papers with Code Benchmark
date: 2021-08-10
categories:
  - nlp
  - machine-learning
  - benchmarks
  - sentence-embeddings
  - research
description: Papers with Code's benchmark page for Semantic Textual Similarity — a task measuring how similar two sentences are in meaning, scored against human judgments. The canonical reference for comparing embedding models on this fundamental NLP task.
params:
  source: pinboard
  sourceUrl: https://paperswithcode.com/task/semantic-textual-similarity
---

## Summary

Semantic Textual Similarity (STS) is an NLP task: given two sentences, predict a similarity score (usually 0–5) matching human judgments of how similar their meanings are. Papers with Code aggregates the leaderboard of models and datasets for this task, making it a one-stop reference for where the field stands.

The canonical STS benchmark datasets — STS-B (from SemEval competitions), SICK-R, and STS-12 through STS-16 — consist of sentence pairs annotated by humans with similarity ratings. A model that achieves high Spearman correlation against these human ratings is encoding semantic similarity well in its embedding space. This is the foundational evaluation for sentence embeddings and the main task that Sentence Transformers was developed to optimize.

High STS scores predict good downstream performance on semantic search (embed query and documents, retrieve by cosine similarity), duplicate detection (find near-paraphrase pairs), and clustering (group semantically similar documents). The STS benchmark is to sentence embeddings what ImageNet is to image recognition — the standard test before claiming a model is ready for production use.

## Key points

- STS measures cosine similarity between sentence embeddings against human-rated sentence pairs (0–5 scale).
- Spearman correlation is the standard metric: how well does your ranking of pairs match human judgments?
- Canonical datasets: STS-B, SICK-R, STS-12 through STS-16 — built from SemEval competitions.
- Strong STS performance → reliable downstream performance on semantic search, duplicate detection, clustering.
- The main benchmark that drove development of Sentence Transformers and subsequent sentence embedding research.

[Original](https://paperswithcode.com/task/semantic-textual-similarity)
