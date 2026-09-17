---
title: Probabilistic Data Structures for Web Analytics and Data Mining
date: 2013-03-17
categories:
  - probabilistic-data-structures
  - web-analytics
  - algorithms
  - big-data
  - data-mining
description: The Highly Scalable Blog's comprehensive survey of probabilistic data structures for web analytics — Bloom filters, HyperLogLog, Count-Min sketch, and MinHash explained with their trade-offs. The standard reference for understanding when to trade exactness for speed and memory.
params:
  source: pinboard
  sourceUrl: https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/
---

![Probabilistic Data Structures for Web Analytics and Data Mining](/images/notes/probabilistic-data-structures-web-analytics.png)

## Summary

This Highly Scalable Blog post is the canonical reference for understanding which probabilistic data structure to reach for when you're building web analytics pipelines. The central insight is that most analytics use cases don't need exact answers — they need fast answers at scale. Trading a small, bounded error rate for dramatic reductions in memory and computation is almost always the right engineering call when you're processing billions of events.

The post covers five core structures: Bloom filter for set membership testing (does this user ID appear in the blacklist?), HyperLogLog for cardinality estimation (how many unique visitors did we have today?), Count-Min sketch for frequency estimation (how many times did this URL appear in the last hour?), MinHash for Jaccard similarity (how similar are these two user session sets?), and LSH ([Locality-Sensitive Hashing](/notes/locality-sensitive-hashing/)) for approximate nearest-neighbor search in high-dimensional spaces. Each structure has a specific error guarantee and a specific operation it optimizes.

The web analytics context anchors the abstractions well. Counting unique visitors exactly requires storing every visitor ID — O(n) memory. HyperLogLog reduces this to O(log log n) memory with ~2% error, which is irrelevant for dashboarding. Checking if a URL has been crawled before using a hash set is expensive; a Bloom filter gives the answer in O(1) with a tunable false positive rate and no false negatives. Finding similar content or near-duplicate pages at web scale requires LSH rather than pairwise comparison. These aren't theoretical curiosities — they're how real web-scale systems work.

## Key points

- Bloom filter: O(1) set membership with no false negatives, tunable false positive rate — the right tool for crawl deduplication, spam detection, cache lookups
- HyperLogLog: ~2% error for cardinality estimation (unique visitors, distinct URLs) using kilobytes of state regardless of dataset size — invented by Philippe Flajolet
- Count-Min sketch: frequency estimation for stream data (click counts, query frequencies) — works like a compressed frequency table with error bounded by stream length × ε
- MinHash: estimates Jaccard similarity between sets — used by Google to detect near-duplicate web pages and by Spotify-style systems for collaborative filtering
- LSH ([Locality-Sensitive Hashing](/notes/locality-sensitive-hashing/)): approximate nearest-neighbor search in high-dimensional space by hashing similar items to the same buckets with high probability
- The underlying theme: most streaming / analytics problems reduce to one of these five patterns; pick the right probabilistic structure before reaching for an exact solution

[Original](https://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/)
