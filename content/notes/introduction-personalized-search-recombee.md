---
title: Introduction to Personalized Search
date: 2020-07-25
categories:
  - personalization
  - search
  - machine-learning
  - recommendations
  - learn-to-rank
description: Recombee's introduction to personalized search — connecting the recommendation systems world to search, covering how behavioral signals (clicks, purchases) can be used to personalize result ranking per user. Bridges the gap between generic LTR and user-specific personalization.
params:
  source: pinboard
  sourceUrl: https://medium.com/recombee-blog/introduction-to-personalized-search-2b70eb5fa5ae
---

## Summary

This article from Recombee (a recommendation-as-a-service company) bridges the gap between recommender systems and personalized search. Standard learning-to-rank optimizes for a global relevance function — the best ordering for a generic query-document pair. Personalized search goes further: the optimal ranking differs by user, because different users have different intents, backgrounds, and preferences even for the same query.

The practical implementation of personalization in search builds on the LTR framework by adding user-specific features. Where a standard LTR model uses only query and document features (BM25 score, document quality, freshness), a personalized model adds signals like: has this user interacted with similar content before? What categories does this user tend to prefer? What is the user's historical query pattern? These user-level signals substantially improve ranking for returning users — the cold-start case (new users with no history) still falls back to generic LTR.

Collaborative filtering techniques from recommendation systems port naturally to search personalization: the interest graph from user-item interaction matrices can provide signals that pure text matching misses. A user who consistently clicks on engineering tutorials when searching for Python should get results different from a data scientist who consistently clicks on pandas documentation. The article connects these ideas explicitly, making it a useful bridge for practitioners coming from either the search side or the recommendations side.

## Key points

- Personalized search extends learning-to-rank by adding user-specific features to the ranking model.
- User signals: interaction history, category preferences, query patterns, past clicks on similar content.
- Cold-start problem: new users with no history fall back to generic LTR — personalization accumulates over sessions.
- Collaborative filtering signals from recommendation systems can enrich search ranking features.
- Same concept as DoorDash search and recommendations case study — behavioral personalization in ranking.
- Part of the learning-to-rank cluster; see Yandex personalised search, Metarank, learning-to-rank overview.

[Original](https://medium.com/recombee-blog/introduction-to-personalized-search-2b70eb5fa5ae)
