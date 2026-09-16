---
title: "High Performance at Massive Scale: Lessons Learned at Facebook"
date: 2013-07-12
categories:
  - distributed-systems
  - performance
  - facebook
  - infrastructure
  - scaling
description: Summary of a 2009 Facebook engineering talk on high-performance systems at massive scale — covering their memcached deployment, MySQL sharding, and the operational realities of running at hundreds of millions of users. An early public window into big-company distributed systems practice.
params:
  source: pinboard
  sourceUrl: http://idleprocess.wordpress.com/2009/11/24/presentation-summary-high-performance-at-massive-scale-lessons-learned-at-facebook/
---

![High Performance at Massive Scale: Lessons Learned at Facebook](/images/notes/high-performance-at-facebook-scale.png)

## Summary

This is a summary of a Facebook engineering presentation (circa 2009) that gave the broader engineering community a rare window into how Facebook operated at hundreds of millions of users. At the time, Facebook's scale was genuinely unprecedented for a consumer web application: they were running tens of thousands of servers, serving billions of page views per day, and making real-time personalization decisions on every request.

The core lessons covered the memcached deployment — Facebook was at that point the world's largest user of memcached, having scaled it to hundreds of servers and hundreds of billions of requests per day. The architecture used dedicated caching tiers, careful cache invalidation patterns, and regional distribution to keep latency acceptable. MySQL sharding handled the write path: a large fan-out of small, single-purpose databases rather than one large relational schema.

What made this talk influential in 2013 (even though it was from 2009) was that it remained a benchmark for how large-scale web infrastructure worked. Many engineers were just learning about distributed systems through blog posts and conference talks, and Facebook's transparency about their architecture — combined with the papers they were publishing on Haystack (photo storage) and Scribe (log collection) — provided a rare map of production-scale distributed systems.

## Key points

- Memcached at scale: Facebook ran the largest memcached deployment in the world — the operational patterns they developed (consistent hashing, pool segmentation) became industry standards.
- MySQL sharding over vertical scaling: splitting data across many small MySQL instances rather than scaling a single large database.
- Read/write asymmetry: most Facebook traffic was read-heavy, justifying massive cache investment to avoid database load.
- TAO and social graph challenges: serving the social graph efficiently required custom data structures beyond what a standard relational schema could handle.
- Facebook's willingness to publish engineering details — Hive, Cassandra, Scribe — seeded an ecosystem of tools that defined the big data era.

[Original](http://idleprocess.wordpress.com/2009/11/24/presentation-summary-high-performance-at-massive-scale-lessons-learned-at-facebook/)
