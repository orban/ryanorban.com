---
title: "LTR with Bees: Learning to Rank in Apache Solr"
date: 2020-07-25
categories:
  - learn-to-rank
  - apache-solr
  - information-retrieval
  - search
  - tutorial
description: Christine Poerschke's tutorial using a bee-related dataset to demonstrate learning-to-rank in Apache Solr — end-to-end example from feature extraction through model training to serving. Concrete and dataset-grounded, unlike most abstract LTR tutorials.
params:
  source: pinboard
  sourceUrl: https://github.com/cpoerschke/ltr-with-bees
---

## Summary

Christine Poerschke (an Apache Lucene/Solr committer) built this tutorial repository around a fun concept: use bee-related data as a search corpus to make the dry mechanics of learning-to-rank concrete. The repo walks through the complete LTR pipeline with a real dataset rather than abstract examples — define features, log them for sample queries, train a model, deploy it in Apache Solr, and compare results with and without LTR reranking.

Having a concrete dataset makes the tutorial unusually useful for learning LTR mechanics. You can actually run the code, see the feature values in the logs, inspect the trained model's feature weights, and compare pre- and post-LTR rankings side by side. Abstract tutorials that describe the process without running code leave too many implementation details ambiguous — this repo closes that gap.

The technical stack: Apache Solr 7.x+, the built-in LTR plugin for feature extraction and model serving, and Python for the training data preparation and model training (using RankLib via a Python wrapper). The training data assembly step — joining feature logs with relevance judgments — is demonstrated explicitly, which is one of the most confusing parts of any LTR implementation.

## Key points

- Concrete dataset (bees!) makes LTR mechanics tangible compared to abstract walkthroughs.
- Full pipeline: corpus indexing → feature definition → query logging → training data → model training → Apache Solr deployment.
- By Christine Poerschke, an Apache Lucene/Solr committer — authoritative implementation.
- Feature logging in Solr: use the `efi` (external feature information) mechanism to log named feature values per document per query.
- Complements Solr-LTR reference implementation and LTR 101 conceptual introduction.
- Part of the learning-to-rank cluster in the vault; see Elasticsearch LTR, Infrastructure for LTR.

[Original](https://github.com/cpoerschke/ltr-with-bees) → GitHub
