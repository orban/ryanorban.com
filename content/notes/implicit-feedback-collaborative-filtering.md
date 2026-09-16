---
title: Implicit Feedback and Collaborative Filtering
date: 2015-01-08
categories:
  - recommendation-systems
  - collaborative-filtering
  - machine-learning
  - matrix-factorization
  - implicit-feedback
description: A technical post on implicit feedback in collaborative filtering — when you have views, clicks, and dwell time instead of explicit ratings. Covers the ALS (alternating least squares) approach and linear algebra tricks for making matrix factorization tractable at scale.
params:
  source: pinboard
  sourceUrl: http://datamusing.info/blog/2015/01/07/implicit-feedback-and-collaborative-filtering/
---

## Summary

Most collaborative filtering tutorials teach the explicit feedback case: users rate items on a 1-5 scale, and you factorize the ratings matrix to predict missing ratings. But most real systems have only implicit feedback: clicks, views, purchases, dwell time — signals that indicate interest but not preference intensity, and where absence of signal doesn't clearly mean dislike.

The key challenge with implicit feedback is confidence weighting. A user who views an item once might be mildly interested; a user who views it 10 times is probably interested but might also be confused. A purchase is a strong signal; an impression that wasn't clicked could mean the item was irrelevant, or that the user just didn't see it. The Hu-Koren-Volinsky (2008) formulation handles this by treating each observation as having a confidence level proportional to the frequency of interaction.

The ALS (Alternating Least Squares) algorithm makes this tractable. Factorize the interaction matrix as a product of user and item latent factor matrices. Alternate between fixing the user factors and solving for items (a linear regression), then fixing items and solving for users. Each step is a standard least-squares problem that can be solved efficiently. The linalg tricks referenced in the bookmark likely refer to the observation that, with implicit feedback, the normal equations have a specific structure that allows solving them in O(k²f) instead of O(k²n) where n is the number of items.

## Key points

- Implicit feedback (views, clicks, purchases) is noisier and asymmetric compared to explicit ratings.
- Confidence weighting: observation frequency → confidence level (Hu-Koren-Volinsky formulation).
- ALS algorithm: alternate between solving for user factors (items fixed) and item factors (users fixed).
- Efficiency trick: the implicit feedback normal equations have structure exploitable for O(k²f) solve instead of O(k²n).
- Used by Netflix, Spotify, and most large-scale recommendation systems — explicit ratings are rare.
- Connects to matrix factorization as the dominant collaborative filtering approach before neural collaborative filtering.

[Original](http://datamusing.info/blog/2015/01/07/implicit-feedback-and-collaborative-filtering/)
