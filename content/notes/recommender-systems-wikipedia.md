---
title: Recommender Systems
date: 2012-12-02
categories:
  - machine-learning
  - recommendation-systems
  - data-science
  - information-retrieval
description: Wikipedia's overview of recommender systems — collaborative filtering, content-based filtering, and hybrid approaches. Saved in 2012 when Netflix Prize aftermath and the rise of personalization made recommendation algorithms a hot research area.
params:
  source: pinboard
  sourceUrl: https://en.wikipedia.org/wiki/Recommender_system
---

![Recommender Systems](/images/notes/recommender-systems-wikipedia.png)

## Summary

A recommender system filters information to predict a user's preferences and surface relevant items from a large catalog. The Wikipedia article covers the two foundational approaches: collaborative filtering (predict preferences based on similar users' behavior) and content-based filtering (recommend items similar to those the user liked, based on item features).

Collaborative filtering itself splits into memory-based methods (nearest-neighbor algorithms over user-item matrices) and model-based methods (matrix factorization, SVD, latent factor models). The 2009 Netflix Prize had just established matrix factorization as the dominant approach, with Simon Funk's SVD variant and the winning BellKor's Pragmatic Chaos ensemble establishing benchmarks that shaped research for years.

The 2012 context matters: Netflix, Amazon, Spotify (launched 2008), and Last.fm were all deploying recommenders at scale. The gap between academic algorithms and production systems — handling cold start, scalability, real-time updates, and diversity — was becoming apparent. Hybrid recommender systems mixing collaborative and content signals, and context-aware models incorporating time, location, and sequence, were active research frontiers.

## Key points

- Collaborative filtering: user similarity (user-user) or item similarity (item-item) over rating matrices
- Content-based filtering: feature similarity between items based on item attributes
- Matrix factorization (SVD, ALS): the post-Netflix Prize standard for CF — decomposes user-item matrix into latent factors
- Cold start problem: new users/items have no interaction history — the key practical weakness of CF
- Hybrid recommender systems: mixing CF + content signals addresses cold start and improves coverage

[Original](https://en.wikipedia.org/wiki/Recommender_system)
