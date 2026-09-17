---
title: "Solr-LTR: From Zero to Learning to Rank in Apache Solr"
date: 2020-07-25
categories:
  - learn-to-rank
  - apache-solr
  - information-retrieval
  - search
  - open-source
description: A practical guide and reference implementation for setting up learning-to-rank in Apache Solr from scratch — covers the Solr LTR plugin, feature extraction, model training, and deployment. Complement to the Elasticsearch LTR tutorials for Solr shops.
params:
  source: pinboard
  sourceUrl: https://github.com/airalcorn2/Solr-LTR
---

## Summary

This GitHub repository by airalcorn2 provides a complete walkthrough for implementing learning-to-rank (LTR) in Apache Solr from scratch. Apache Solr has had built-in LTR support since version 6.4 (2017) via the `ltr` query parser and feature store — this repo provides the practical glue to make it work end-to-end.

The workflow mirrors the Elasticsearch LTR approach: define features in Solr's feature store, log feature values for your query-document pairs, train a LambdaMART or linear model using RankLib or XGBoost, upload the model back to Solr, and run queries using the LTR reranker on top of standard Solr retrieval. The key difference from Elasticsearch is the API surface: Solr uses a feature store concept where features are defined as named queries, and model upload happens via Solr's REST API with a JSON model definition.

Apache Solr and Elasticsearch represent the two main open-source search engines, and both grew LTR plugins around the same time period (2016-2018) as the technique moved from research to industry standard. The choice between them for LTR purposes is largely determined by which search engine you're already running — the LTR workflow is substantively the same on both.

## Key points

- Apache Solr LTR plugin built-in since v6.4: feature store, feature logging, model upload, LTR reranking.
- Same three-phase workflow as Elasticsearch LTR: feature definition → training data → model upload.
- RankLib is the typical training library used with Solr LTR (Java ecosystem match).
- Solr feature store: features are defined as Solr queries — BM25 scores, query-field match signals, custom functions.
- Also see LTR with bees for a Solr LTR tutorial with a concrete dataset.
- Part of the learning-to-rank cluster in the vault; see Elasticsearch LTR, LTR 101, Infrastructure for LTR.

[Original](https://github.com/airalcorn2/Solr-LTR)
