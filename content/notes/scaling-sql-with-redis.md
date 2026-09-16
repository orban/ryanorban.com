---
title: Scaling SQL with Redis
date: 2014-05-13
categories:
  - databases
  - redis
  - sql
  - performance
  - caching
  - scaling
description: David Cramer's post on using Redis to scale SQL databases — covering caching patterns, read replica offloading, and where Redis fits in a stack that can't abandon SQL entirely. Practical patterns from the Disqus/Sentry engineering blog at production scale.
params:
  source: pinboard
  sourceUrl: http://cramer.io/2014/05/12/scaling-sql-with-redis/
---

## Summary

David Cramer (co-founder of Sentry, previously at Disqus) wrote this post from real production experience with high-traffic Python / Django applications. The core argument: you usually can't replace SQL with Redis, but you can dramatically reduce SQL load by putting Redis in front of it for the right access patterns.

The practical patterns: use Redis as a read-through cache for expensive query results (key = query fingerprint, value = serialized result, TTL = acceptable staleness), use Redis for counters and aggregations that would require constant row updates (increment a Redis key instead of UPDATE ... SET count = count + 1), use Redis sorted sets for leaderboards and ranked lists that would require expensive ORDER BY queries, and use Redis pub/sub for real-time event distribution that SQL can't serve.

The Disqus scale context (hundreds of millions of comments, social activity feeds) makes these patterns credible — this isn't premature optimization advice, it's patterns validated under production load. By 2014, Redis had become the standard secondary data store alongside SQL in web application architectures, and posts like this codified why and how.

## Key points

- Read-through caching with Redis: serve hot query results from memory, invalidate on write — reduces database CPU for read-heavy workloads by 80-90%.
- Atomic Redis operations (INCR, ZADD) replace locked SQL updates for counters and rankings — much faster and no transaction contention.
- Redis sorted sets are purpose-built for leaderboards and time-series queries — O(log n) insertion and range queries replace expensive ORDER BY + LIMIT.
- Cache invalidation strategy matters: write-through (update cache on write) vs. TTL-based expiry vs. explicit invalidation — each has different consistency tradeoffs.
- The 2014 standard stack: PostgreSQL or MySQL as source of truth + Redis for caching and real-time features + Celery for async work.

[Original](http://cramer.io/2014/05/12/scaling-sql-with-redis/)
