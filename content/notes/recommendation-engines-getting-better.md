---
title: Why Recommendation Engines Are About to Get Much Better
date: 2013-09-24
categories:
  - recommendation-systems
  - machine-learning
  - big-data
  - personalization
  - collaborative-filtering
description: Coverage of advances in recommendation engine technology in 2013 — driven by larger datasets, better collaborative filtering, and contextual signals. The moment when personalization was transitioning from a luxury to an expectation.
params:
  source: pinboard
  sourceUrl: http://preview.getprismatic.com/story/1379961281925?share=true
---

![Why Recommendation Engines Are About to Get Much Better](/images/notes/recommendation-engines-getting-better.png)

## Summary

In 2013, recommendation systems were a central application of machine learning at scale — Netflix, Amazon, Spotify, and Pandora had made algorithmic recommendation a standard consumer expectation. This piece from Big Data/Prismatic covered why they were getting better: larger datasets, more contextual signals (time, location, device), and advances in collaborative filtering and matrix factorization algorithms.

The Netflix Prize (2009) had established matrix factorization (specifically SVD-based methods) as the state of the art for collaborative filtering — decomposing the user-item rating matrix into latent factor representations and using those to predict unobserved ratings. By 2013, this was the standard approach, being combined with content features, temporal signals, and implicit feedback (what users watched without rating).

The about to get much better framing reflected genuine excitement about the intersection of larger datasets and better algorithms. The open challenge was context: a recommendation that's good on desktop at home might be wrong on mobile during a commute. Incorporating contextual signals into the recommendation model was an active research area.

## Key points

- Matrix factorization / collaborative filtering was the dominant approach in 2013, advanced by the Netflix Prize competition.
- Recommendation improvement drivers: scale (more data), context (time, location, device), implicit feedback (behavior without ratings).
- Collaborative filtering relies on user-item interaction patterns; content-based filtering uses item features — hybrid approaches usually outperform either alone.
- The personalization expectation was being set: once Netflix and Amazon established recommendation quality, users expected it everywhere.
- Connected to big data infrastructure: recommendation at scale required Hadoop or Spark to process interaction matrices over millions of users.

[Original](http://preview.getprismatic.com/story/1379961281925?share=true)
