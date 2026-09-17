---
title: Introduction to Recommendations with Map-Reduce and mrjob
date: 2013-12-10
categories:
  - mapreduce
  - collaborative-filtering
  - recommendations
  - hadoop
  - python
description: Tutorial on building item-based collaborative filtering recommendation systems using MapReduce and Yelp's mrjob Python library. Shows why distributed computation is necessary for large-scale similarity calculations.
params:
  source: pinboard
  sourceUrl: http://aimotion.blogspot.com/2012/08/introduction-to-recommendations-with.html
---

## Summary

This tutorial builds movie and book recommendation systems using MapReduce and mrjob — Yelp's Python wrapper for Hadoop Streaming. The algorithm is item-based collaborative filtering via correlation: for each pair of items, find all users who rated both, build their rating vectors, and compute the correlation. At scale, this pairwise computation across millions of items and users makes distributed processing essential.

The mrjob implementation follows the canonical MapReduce pattern: the mapper emits user ratings grouped by item, and the reducer accumulates the aggregate statistics (sums, counts, squared sums) needed to compute Pearson correlation coefficients. The Star Trek/Star Wars example shows that franchise similarities cluster correctly, while cross-genre similarities are weaker.

The article also covers alternative similarity metrics: cosine similarity, regularized correlation, and Jaccard similarity. Regularized correlation is worth noting — it shrinks correlations toward zero for item pairs with few co-ratings, preventing the algorithm from confidently recommending based on just two shared ratings.

## Key points

- Item-based collaborative filtering via Pearson correlation between rating vectors — the classic Amazon-style approach.
- mrjob (Yelp's library) makes Hadoop Streaming accessible from Python without Java boilerplate.
- Mapper: emit ratings grouped by item. Reducer: accumulate sum, count, sum-of-squares for each item pair.
- Alternative metrics discussed: cosine similarity, Jaccard similarity, regularized correlation.
- Regularized correlation penalizes item pairs with few co-ratings — avoids overconfident recommendations from sparse data.
- The pairwise nature of collaborative filtering is why MapReduce matters: O(items²) comparisons benefit enormously from parallelism.

[Original](http://aimotion.blogspot.com/2012/08/introduction-to-recommendations-with.html)
