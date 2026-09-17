---
title: Building the Next New York Times Recommendation Engine
date: 2015-08-11
categories:
  - recommendation-systems
  - nlp
  - collaborative-filtering
  - media-tech
  - nyt
description: The NYT engineering blog's post on building their new recommendation engine — combining collaborative filtering with content-based signals to recommend articles. A rare look at production recommendation systems at a major media company before the algorithmic feed era fully arrived.
params:
  source: pinboard
  sourceUrl: http://open.blogs.nytimes.com/2015/08/11/building-the-next-new-york-times-recommendation-engine/
---

## Summary

This New York Times engineering blog post describes the rebuild of their article recommendation system — moving from simple rule-based editorial recommendations toward a hybrid system combining collaborative filtering with content-based filtering. The context: the NYT needed to surface relevant articles to readers who mostly arrived via homepage or search, with the goal of increasing session depth.

The hybrid approach addresses the classic cold start problem: for new articles with no engagement history, content-based signals (topic similarity via TF-IDF or word embeddings) bootstrap recommendations until behavioral signals accumulate. For older articles with engagement history, collaborative filtering finds readers who read similar sets of articles and surfaces what that cohort read next. Blending the two prevents the popularity trap where collaborative systems just recommend viral content.

A key challenge in news recommendation is temporal decay — yesterday's article is usually irrelevant regardless of how similar it is to what you're reading. The NYT system weighted recency heavily, which is a domain-specific constraint that general recommendation systems (books, movies) don't face. This time-sensitivity makes news a harder recommendation problem than content with stable interest value.

## Key points

- Hybrid system: collaborative filtering + content-based filtering to handle cold start and popularity traps.
- Temporal decay is the defining constraint in news — recency must be weighted heavily.
- TF-IDF and word embeddings for content representation at the time of writing.
- Goal: increase session depth (articles per visit), not just immediate engagement.
- Reflects a broader trend: media companies building ML infrastructure to compete with algorithmic feeds.
- Saved via Ryan Orban's network ("reminds me of early convos with @ryanorban") — relevant to his Galvanize data science curriculum work.

[Original](http://open.blogs.nytimes.com/2015/08/11/building-the-next-new-york-times-recommendation-engine/)
