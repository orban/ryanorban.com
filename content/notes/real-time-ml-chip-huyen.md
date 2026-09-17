---
title: "Real-Time Machine Learning: Challenges and Solutions"
date: 2022-01-06
categories:
  - machine-learning
  - mlops
  - real-time
  - streaming
  - infrastructure
description: Chip Huyen's definitive survey of real-time ML challenges — the engineering gap between batch ML pipelines and systems that must make predictions on live data with low latency. Covers online prediction, continual learning, and the infrastructure needed to bridge training and serving.
params:
  source: pinboard
  sourceUrl: https://huyenchip.com/2022/01/02/real-time-machine-learning-challenges-and-solutions.html
---

## Summary

Chip Huyen published this article in January 2022 as a companion to her book Designing Machine Learning Systems. It's one of the clearest surveys of what separates batch ML from real-time ML and what the engineering challenges look like in practice. The article distinguishes between online prediction (making predictions on new data as it arrives) and continual learning (updating the model itself on incoming data), and maps out the infrastructure required for each.

The core challenge: most ML education and most ML tooling is built around the batch paradigm — you collect data, train offline, deploy a static model, and batch-score periodically. Real-time systems break this in multiple ways. Features must be computed on live data in milliseconds, not hours. The training-serving feature skew problem (features computed differently at training time vs serving time) becomes critical when staleness is measured in seconds rather than days. Data pipelines must be streaming (Kafka, Flink) not batch (Spark jobs, SQL queries).

Chip Huyen frames the solutions around two axes: prediction-serving latency (precomputed vs online) and feature freshness (batch features vs streaming features). This gives a 2x2 that covers most practical configurations. The feature store is the key infrastructure piece — it maintains computed features in low-latency storage (Redis, DynamoDB) so that online prediction doesn't have to recompute expensive features from scratch on every request.

## Key points

- Distinguishes online prediction (serve models in real time) from continual learning (update models in real time)
- Feature skew: features computed differently at training vs serving time — the #1 production ML reliability issue
- Feature store = low-latency store for precomputed features; separates feature computation from model serving
- Streaming infrastructure (Apache Kafka, Apache Flink) required for truly fresh features
- Latency budget allocation: total latency = feature retrieval + model inference + post-processing — each step must be optimized

[Original](https://huyenchip.com/2022/01/02/real-time-machine-learning-challenges-and-solutions.html)
