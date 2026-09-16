---
title: MIT Can Predict How Many Retweets You'll Get
date: 2013-06-01
categories:
  - twitter
  - machine-learning
  - social-networks
  - prediction
  - mit
description: Wired's coverage of MIT research predicting retweet counts from tweet content and network features. An early demonstration that social network propagation could be modeled predictively, with implications for understanding how information spreads.
params:
  source: pinboard
  sourceUrl: http://www.wired.com/wiredenterprise/2013/05/twitter_predictor/
---

## Summary

Wired covered MIT research that built a predictive model for retweet counts — given a tweet and its author's network properties, the model could estimate how widely the tweet would spread before it was posted. The work combined natural language processing features (sentiment, hashtag use, URL inclusion, length) with social network features (follower count, historical retweet rate, network centrality).

The research was part of a broader wave of computational social science in the early 2010s: using Twitter's API to study information propagation at scale. The key findings: network position matters more than content quality in predicting spread. A mediocre tweet from a highly connected account outperforms an insightful tweet from a low-follower account. This validated the Matthew effect in social media — existing influence amplifies future reach regardless of content merit.

The practical implication — that you could A/B test tweet phrasing to maximize spread before posting — pointed toward the later explosion of social media optimization tools. It also raised questions about the distinction between genuine information value and engineered virality, a tension that only intensified as platforms refined their recommendation algorithms.

## Key points

- Retweet prediction features: follower count, prior RT rate, hashtag presence, URL, sentiment, posting time
- Network position (centrality, follower count) dominated content features in predictive power
- Cascade models for information diffusion: who retweets depends on who they follow and network position
- Matthew effect in social media: high-follower accounts generate exponentially more reach per tweet
- Research from MIT Media Lab or similar; used Twitter's Streaming API for training data
- Pre-cursor to the influencer marketing industry and social media optimization tools

[Original](http://www.wired.com/wiredenterprise/2013/05/twitter_predictor/)
