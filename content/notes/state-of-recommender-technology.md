---
title: The State of Recommender Technology (2013)
date: 2013-07-02
categories:
  - recommender-systems
  - machine-learning
  - collaborative-filtering
  - data-science
description: A 2013 survey of recommender system technology covering collaborative filtering, content-based approaches, and the state of the field before deep learning took over. Published by Data Community DC alongside coverage of CoBrain, a startup working on recommendation infrastructure.
params:
  source: pinboard
  sourceUrl: http://datacommunitydc.org/blog/2013/07/recommender-technology-and-cobrain/
---

## Summary

This Data Community DC post surveyed recommender systems technology as of mid-2013 — the algorithms, architectures, and commercial landscape. The article was published alongside coverage of CoBrain, a startup building recommendation infrastructure as a service.

By 2013, recommender systems had been a serious research and production field for over a decade. Amazon's item-to-item collaborative filtering (2003 paper) had become the canonical industrial approach: compute similarities between items based on co-purchase patterns rather than user-to-user similarities, which scaled better to millions of items. The Netflix Prize (2006–2009) had pushed matrix factorization techniques — particularly SVD++ and ALS — to the forefront, demonstrating that decomposing the user-item rating matrix into latent factors produced better recommendations than neighborhood methods alone.

The 2013 state of the art was ensemble methods: combining multiple recommendation signals (collaborative filtering, content features, temporal patterns, social graph connections) and blending their outputs. Hybrid recommender systems that merged collaborative filtering with content-based filtering handled the cold-start problem more gracefully. The open challenge was real-time personalization at scale — serving updated recommendations to millions of users in milliseconds as new interactions arrived.

## Key points

- Collaborative filtering at scale: item-to-item similarity (Amazon's approach) outperformed user-to-user similarity computationally; worked better for sparse, high-dimensional matrices.
- Matrix factorization (SVD, ALS): the post-Netflix Prize approach — decompose the rating matrix into latent user and item factors, allowing predictions for unseen user-item pairs.
- Cold start problem: new users and items have no interaction history — content-based filtering using item metadata patches this gap.
- Implicit feedback vs explicit ratings: most interactions are implicit (views, clicks, time-on-page) rather than explicit ratings — different algorithms for each.
- 2013 open problem: real-time updates — refreshing recommendations as new interactions arrived, which batch ALS couldn't handle without periodic full retraining.

[Original](http://datacommunitydc.org/blog/2013/07/recommender-technology-and-cobrain/)
