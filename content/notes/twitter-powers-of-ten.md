---
title: Twitter Powers of Ten
date: 2013-05-23
categories:
  - twitter
  - scale
  - distributed-systems
  - social-networks
  - data
description: Rob Weir's 2011 post using powers-of-ten framing to characterize Twitter's data and scale properties — from individual tweets to the full firehose. A snapshot of the social media scale conversation before big data tooling became mainstream.
params:
  source: pinboard
  sourceUrl: http://www.robweir.com/blog/2011/03/twitter-powers-of-ten.html
---

![Twitter Powers of Ten](/images/notes/twitter-powers-of-ten.png)

## Summary

Rob Weir used a powers of ten framing to characterize Twitter's scale properties — from a single tweet (140 characters, ~0.1KB) up through the full Twitter firehose (400 million tweets/day in 2011, ~40 GB/day of raw text). Each order of magnitude reveals different engineering and analytical concerns.

The post is a mental calibration exercise: what does Twitter's data actually look like at different scales, and what does that imply for storage, processing, and analysis? A single user's tweets fit in a text file. A day's worth of tweets fits on a laptop disk. A year of the firehose starts requiring distributed storage. Historical archives require something like HDFS or S3.

The powers-of-ten framing was popularized by the Eames Office short film (1977) that zoomed from human to cosmic to subatomic scale. Applied to data scale, it's a useful pedagogical device: each 10x jump changes what's tractable with which tools, from spreadsheet to pandas to Hadoop.

## Key points

- Single tweet: ~0.1-0.3KB including metadata — 400M tweets/day ≈ 40-120 GB/day raw text
- Per-user history: fits in a file, processable with any scripting language
- Per-day firehose: ~40GB compressed — a single large machine can process this
- Annual firehose: ~15TB uncompressed — starts requiring distributed storage
- Historical archive: hundreds of TB — Hadoop/S3 territory
- The Twitter firehose API was a commercial product; academic researchers used the 1% garden hose sample
- Powers-of-ten framing helps calibrate which tools are appropriate: `awk` → pandas → Spark based on data volume

[Original](http://www.robweir.com/blog/2011/03/twitter-powers-of-ten.html)
