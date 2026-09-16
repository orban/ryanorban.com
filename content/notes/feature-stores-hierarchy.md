---
title: Feature Stores — A Hierarchy of Needs
date: 2022-01-06
categories:
  - machine-learning
  - mlops
  - feature-store
  - data-engineering
  - infrastructure
description: Eugene Yan's survey of feature stores organized as a hierarchy of needs — from basic feature reuse to online serving to real-time streaming. Practical taxonomy for understanding when you need a feature store and what tier of sophistication your use case requires.
params:
  source: pinboard
  sourceUrl: https://eugeneyan.com/writing/feature-stores/
---

## Summary

Eugene Yan applies a Maslow-style hierarchy to feature store adoption: teams don't start needing all the capabilities of a feature store at once. The article walks through what a feature store is, why teams start wanting one, and how requirements escalate from basic feature sharing to online serving to real-time streaming features.

Level 1 (basic needs): team needs to share features between data scientists to avoid redundant computation and inconsistent feature definitions. A shared feature registry — even a git repository of feature transformation code — addresses this. Level 2: training and serving features must match (the feature skew problem). A proper offline store that logs historical features solves this. Level 3: online serving requires low-latency feature retrieval for production prediction endpoints — Redis or DynamoDB as an online store. Level 4: real-time streaming features require features computed on live event streams via Apache Kafka and Apache Flink or similar.

The hierarchy of needs framing is useful because it justifies when *not* to build a feature store. Teams at Level 1 don't need to immediately implement a full streaming infrastructure — they just need consistency and sharing. The article maps major feature store tools to these levels: Feast (primarily offline + online serving), Tecton (full stack including streaming), and homegrown solutions. By 2022 this was an active commercial space with Feast (open source), Tecton, and Hopsworks all competing.

## Key points

- Feature store hierarchy: sharing → training/serving consistency → online serving → real-time streaming features
- Feature skew: training on historical features computed differently than serving-time features — the core problem
- Feast: open-source feature store, strong offline→online push; Tecton: enterprise, streaming included
- Online store (Redis/DynamoDB) vs offline store (data warehouse): different latency/freshness tradeoffs
- Teams often over-engineer: implement streaming features before actually needing millisecond feature freshness

[Original](https://eugeneyan.com/writing/feature-stores/)
