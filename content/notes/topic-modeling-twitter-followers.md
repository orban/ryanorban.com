---
title: Topic Modeling of Twitter Followers
date: 2015-11-04
categories:
  - nlp
  - topic-modeling
  - lda
  - twitter
  - data-science
description: A tutorial applying LDA topic modeling to Twitter follower descriptions to segment an audience by interest — one of the cleaner early examples of using unsupervised NLP to understand social media audiences programmatically.
params:
  source: pinboard
  sourceUrl: http://alexperrier.github.io/jekyll/update/2015/09/04/topic-modeling-of-twitter-followers.html
---

## Summary

This tutorial by Alex Perrier applies LDA (Latent Dirichlet Allocation) to Twitter follower profile descriptions to discover underlying audience segments. The approach: collect follower bios via the Twitter API, preprocess the text (tokenize, remove stopwords, stem), fit an LDA model to the corpus, and interpret the resulting topics as audience segments. The result is an unsupervised map of who follows this account — without needing manual labeling.

LDA is a generative probabilistic model that assumes each document (here: a Twitter bio) is a mixture of topics, and each topic is a distribution over words. By fitting the model to the corpus, you recover K latent topics — each described by its top words — and for each bio, a distribution over those topics. High-probability topic assignments reveal natural clusters in the follower base.

The approach is a good example of unsupervised learning for audience analysis before more powerful embeddings were widely available. Twitter bios are short and noisy, which makes LDA challenging — sparse text means many bios don't contain enough signal for reliable topic assignment. But at the corpus level, the method extracts interpretable segments that manual clustering would miss. It connects to broader social network analysis questions about community structure on platforms like Twitter.

## Key points

- LDA on Twitter bios: collect via API → preprocess → fit model → interpret topic clusters.
- Each follower bio is treated as a document; topics emerge from co-occurring vocabulary across the corpus.
- Short, noisy text is an LDA challenge — works better at the corpus level than for individual document assignment.
- Useful for audience segmentation without labeled data.
- Pre-dates word embeddings as the dominant NLP representation — LDA was the practical choice for topic discovery in 2015.
- Connects to social media analytics and community detection in social graphs.

[Original](http://alexperrier.github.io/jekyll/update/2015/09/04/topic-modeling-of-twitter-followers.html) → GitHub
