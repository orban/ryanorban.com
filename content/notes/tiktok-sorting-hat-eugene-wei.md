---
title: TikTok and the Sorting Hat
date: 2020-08-06
categories:
  - social-media
  - recommendation-systems
  - tiktok
  - product-strategy
  - machine-learning
description: Eugene Wei's landmark essay arguing TikTok's algorithm is the product — not the content or creators — and that it functions as a 'sorting hat' that matches users to their taste tribes faster than any previous social network. Required reading for anyone thinking about content recommendation systems.
params:
  source: pinboard
  sourceUrl: https://www.eugenewei.com/blog/2020/8/3/tiktok-and-the-sorting-hat
---

## Summary

Eugene Wei's essay is one of the most influential pieces of product analysis written about TikTok. The central argument: TikTok's algorithm is the product. Where Instagram, Twitter, and YouTube built their distribution around social graphs (you follow people, people follow you), TikTok built around a interest graph that it infers entirely from behavior — what you watch, how long you watch, what you replay. The result is a recommendation system that can surface content you'll love from creators you've never heard of, in a language you don't even speak.

Wei frames TikTok's algorithm as a sorting hat — a reference to Harry Potter's sorting mechanism that instantly categorizes students. TikTok's version is the For You Page (FYP), which rapidly classifies users into interest clusters and routes content accordingly. Unlike the years it took earlier platforms to learn your preferences via explicit social signals, TikTok learns from implicit feedback (watch time, replays, shares) within hours of a new user opening the app. This explains TikTok's legendary speed at hook — many users report the FYP is accurate by the second or third session.

The essay also addresses the creator side. On graph-based platforms, creator success correlates with follower acquisition — you need distribution to grow, and growth is path-dependent. TikTok inverts this by distributing new posts to small test audiences and expanding based on engagement signals. An account with zero followers can go viral on day one. This changes the economics of content creation: the interest graph democratizes distribution in ways the social graph never could, because a strong social graph is slow to build while algorithmic interest matching is instant.

## Key points

- TikTok's core innovation is the interest graph over the social graph — it learns taste from behavior, not followership.
- The For You Page is the product: the feed, not the app shell, is what users return for.
- Implicit feedback (watch time, replays) is more accurate than explicit signals (likes) for predicting preference.
- Distribution is algorithm-controlled: any creator can go viral regardless of follower count, which disrupts creator economy dynamics.
- The approach explains TikTok's cold-start problem advantage: new users get a working feed in minutes, not weeks.
- ByteDance built the system in China for Douyin and transported the algorithmic infrastructure to global markets — the "sorting hat" works across cultures.

[Original](https://www.eugenewei.com/blog/2020/8/3/tiktok-and-the-sorting-hat)
