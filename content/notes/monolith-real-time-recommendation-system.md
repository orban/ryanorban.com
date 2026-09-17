---
title: "Monolith: Real Time Recommendation System With Collisionless Embedding Table"
date: 2022-10-30
categories:
  - machine-learning
  - recommendation-systems
  - distributed-systems
  - online-learning
  - infrastructure
description: Monolith is ByteDance's production recommendation system purpose-built for online training with dynamic sparse features, featuring a collisionless embedding table with expirable embeddings and frequency filtering. It demonstrates that general-purpose ML frameworks like TensorFlow are ill-suited for industrial recommendation with non-stationary data distributions.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2209.07663.pdf
---

## Summary

Zhuoran Liu, Leqi Zou, Xuan Zou, and colleagues at ByteDance present Monolith, a production recommendation system purpose-built for online training with dynamic sparse features. The core problem: general-purpose deep learning frameworks like TensorFlow and PyTorch were designed for dense, static parameters and batch training, making them fundamentally ill-suited for recommendation scenarios where features are sparse, categorical, and continuously evolving with non-stationary user behavior distributions (concept drift).

The central contribution is a collisionless embedding table that avoids the hash collision problem inherent in frameworks using fixed-size parameter tables for sparse ID features. Monolith's embedding table supports expirable embeddings (automatically removing low-frequency or stale feature representations) and frequency filtering (only promoting features above a threshold into the table), dramatically reducing memory footprint while maintaining model quality. This enables the system to handle the long-tail of user features that characterize real recommendation workloads.

The architecture provides production-ready online training with high fault-tolerance, allowing the model to learn from user interactions in real time rather than in nightly batch retraining cycles. The paper demonstrates that trading some system reliability for real-time learning improves recommendation quality on short-video ranking tasks — user behavior signal from minutes ago is more predictive than signal from yesterday. Monolith has shipped in BytePlus Recommend.

## Key Points

- Collisionless embedding table with expirable embeddings and frequency filtering solves memory explosion from sparse categorical features
- Online training with real-time user feedback vastly outperforms batch retraining for short-video and ads recommendation systems
- General-purpose frameworks (TensorFlow, PyTorch) are poor fits for recommendation: designed for dense/static parameters and separate train/serve stages
- Concept drift in user behavior makes yesterday's training signal stale — Monolith's online learning addresses this directly
- Architectural trade-off: accept some fault tolerance risk to gain real-time learning capability, shipping in ByteDance's production ranking systems

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2209.07663.pdf)
