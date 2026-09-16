---
title: Is Your Infrastructure Ready for Learning to Rank?
date: 2020-07-25
categories:
  - learn-to-rank
  - information-retrieval
  - search
  - infrastructure
  - machine-learning
description: OpenSource Connections' guide to the infrastructure required before you can deploy learning-to-rank — covering the judgment lists, feature logging pipelines, training data management, and model versioning that most LTR tutorials skip. The operational reality of LTR in production.
params:
  source: pinboard
  sourceUrl: https://opensourceconnections.com/blog/2017/07/05/infrastructure_for_ltr/
---

## Summary

This OpenSource Connections post addresses the gap most learning-to-rank tutorials skip: what infrastructure you need before training the first model. Getting LTR working in a lab with a toy dataset is straightforward; getting it working in production requires solving a set of operational problems that are rarely discussed.

The key infrastructure pieces for production LTR are: (1) **Judgment list management** — human relevance judgments for query-document pairs are the training signal. You need a workflow for collecting, maintaining, and versioning these labels. Editorial teams, crowd-sourced judgment, or click-based implicit labels all require different tooling. (2) **Feature logging pipeline** — you need to log the LTR features (BM25 score, custom signals) for the documents served at query time, not just at training time. This requires integration with your search engine's query pipeline. (3) **Training data management** — judgment lists plus logged features need to be assembled into training data in the format expected by RankLib, XGBoost, or your chosen training library. (4) **Model versioning and A/B testing** — ranking models need to be tested via controlled experiments, and you need rollback capability when a new model regresses.

The framing is specifically about Elasticsearch and Apache Solr deployments with the respective LTR plugins, but the infrastructure concerns are universal across LTR systems.

## Key points

- LTR infrastructure needs: judgment collection workflow, feature logging pipeline, training data assembly, model versioning.
- Judgment lists are the bottleneck: human labels are expensive; click-based implicit labels are noisy; either requires careful data management.
- Feature logging must be in the search engine's query path — features logged offline don't represent what the model sees at serving time.
- A/B testing for ranking: you need interleaving or randomized bucket experiments to measure ranking quality changes safely.
- Applies to both Elasticsearch and Apache Solr LTR plugin deployments.
- See also: Elasticsearch LTR tutorial, [LTR 101 Linear Models](/notes/ltr-101-linear-models/), Solr LTR.

[Original](https://opensourceconnections.com/blog/2017/07/05/infrastructure_for_ltr/)
