---
title: Mining of Massive Datasets (Stanford)
date: 2013-06-24
categories:
  - algorithms
  - data-mining
  - machine-learning
  - stanford
  - textbook
description: The Stanford textbook by Rajaraman and Ullman on algorithms for mining massive datasets — locality-sensitive hashing, PageRank, collaborative filtering, stream algorithms, and more. Freely available online and a standard reference for large-scale data algorithms.
params:
  source: pinboard
  sourceUrl: http://infolab.stanford.edu/~ullman/mmds.html
---

## Summary

*[Mining of Massive Datasets](/notes/mining-of-massive-datasets/)* by Anand Rajaraman and Jeff Ullman (with Jure Leskovec added in later editions) is a Stanford textbook covering algorithms designed for data at scales that exceed single-machine memory. The book is freely available online from the Stanford InfoLab, which drove wide adoption — it became a standard reference for data engineers and scientists working on large-scale problems.

The book's coverage is broad but focused: locality-sensitive hashing (LSH) for approximate similarity search, the PageRank algorithm and its variants, collaborative filtering for recommender systems, stream processing algorithms (counting distinct items, heavy hitter detection), clustering at scale, and link analysis on web graphs. Each chapter addresses the same underlying challenge: how do you compute the thing you want when the data doesn't fit in memory and you need to minimize disk passes?

What makes this book distinctive is its treatment of approximation as a first-class concern. Many of its algorithms — locality-sensitive hashing, the count-min sketch, DGIM for sliding windows — trade exact answers for dramatically reduced memory and time requirements. The implicit argument: at web scale, an approximate answer available in milliseconds is more useful than an exact answer that takes hours.

## Key points

- Locality-sensitive hashing (LSH): find approximate nearest neighbors in high-dimensional spaces without scanning every pair — foundational for similarity search and deduplication at scale.
- PageRank formulation and computation: the random walk model, the dangling node problem, and efficient iterative computation on sparse graphs.
- Collaborative filtering for recommender systems: matrix factorization and neighborhood methods explained at a level that bridges theory and practical implementation.
- Stream algorithms: computing statistics on data streams in a single pass with sub-linear memory — Bloom filters, count-min sketch, HyperLogLog.
- Available free at Stanford: the open-access model made this the de facto starting point for learning large-scale data mining algorithms.

[Original](http://infolab.stanford.edu/~ullman/mmds.html)
