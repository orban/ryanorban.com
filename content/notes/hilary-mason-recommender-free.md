---
title: How to Get Hilary Mason to Build Your Recommender for Free
date: 2013-05-08
categories:
  - recommendations
  - collaborative-filtering
  - data-science
  - machine-learning
  - mortar-data
description: Mortar Data's post on building a free recommender system using Hilary Mason's approach — a practical guide to collaborative filtering on Hadoop using Mahout. A snapshot of the state of accessible recommendation infrastructure in 2013.
params:
  source: pinboard
  sourceUrl: http://blog.mortardata.com/post/49934459499/recommender-systems-for-free
---

## Summary

Mortar Data (a Hadoop-as-a-service startup) published this post referencing Hilary Mason's approach to building recommender systems without a large ML team. The key insight was democratizing recommendation infrastructure that had previously required significant engineering resources: using Apache Mahout's collaborative filtering implementation on Hadoop to build item-based recommenders at scale.

Hilary Mason was Chief Scientist at bitly at this time and was a prominent voice in making data science accessible — her work at bitly on link click patterns and her public talks on practical machine learning were widely followed in the early data science community. The for free framing referred to using open-source tools (Mahout on commodity Hadoop clusters) rather than proprietary recommendation engines that charged per recommendation.

Item-based collaborative filtering (the dominant approach referenced here) works by computing item-item similarity matrices: users who bought X also bought Y. This scales better than user-based CF because the item catalog changes more slowly than the user base, so the similarity matrix can be precomputed on MapReduce and updated periodically rather than computed at query time. Amazon's recommendation engine (described in a 2003 paper) popularized this approach.

## Key points

- Item-based collaborative filtering via MapReduce: compute pairwise item similarities offline, serve recommendations from a lookup
- Apache Mahout provided Hadoop-native implementations of CF, making recommendation pipelines accessible without custom ML engineering
- Mortar Data's value proposition: managed Pig + Hadoop pipelines so data scientists could focus on the algorithm rather than cluster management
- Hilary Mason's influence: making practical ML accessible was central to her public work at bitly and in the broader data science community
- 2013 context: building a recommender still required significant infrastructure; the abstraction layers that make it easier today (cloud ML services, embeddings from pretrained models) didn't exist
- Matrix factorization methods (SVD, ALS) were beginning to displace pure CF approaches after the Netflix Prize demonstrated their superiority

[Original](http://blog.mortardata.com/post/49934459499/recommender-systems-for-free)
