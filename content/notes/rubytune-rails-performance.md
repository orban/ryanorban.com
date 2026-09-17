---
title: "RubyTune: Rails Performance Cheat Sheet"
date: 2013-01-11
categories:
  - ruby
  - rails
  - performance
  - reference
  - cheatsheet
description: RubyTune's Rails performance cheat sheet — a condensed reference for profiling, benchmarking, and optimizing Rails applications. Saved when learning Rails performance optimization in early 2013.
params:
  source: pinboard
  sourceUrl: http://rubytune.com/cheat
---

![RubyTune: Rails Performance Cheat Sheet](/images/notes/rubytune-rails-performance.png)

## Summary

RubyTune was a consulting service offering Ruby on Rails performance tuning, emergency troubleshooting, and ops consulting. Their cheat sheet distilled common Rails performance patterns into a quick reference: what to profile, what tools to use, and what the common bottlenecks are.

Rails performance in 2013 followed predictable patterns. Database queries were almost always the primary bottleneck — the N+1 query problem (loading a collection and then querying for each element's associations) was the most common issue, solvable with `includes` or `eager_load`. Memory was the second concern: Ruby objects are expensive, GC pressure from too many short-lived objects degraded throughput. Caching was the standard mitigation — fragment caching, action caching, and page caching at different granularities. Rack middleware performance, asset pipeline configuration, and connection pooling rounded out the usual concerns.

The tools referenced: New Relic for production profiling, Rack::MiniProfiler for development, ActiveRecord::QueryCache, `EXPLAIN` in PostgreSQL for slow query diagnosis, and Bullet gem for N+1 detection. This was pre-RailsPanel, pre-Skylight; the profiling toolchain was less integrated than today.

## Key points

- N+1 query problem: the most common Rails performance issue — lazy-loading associations in a loop; solved with `includes` / `eager_load`
- Caching layers: Russian doll caching in views, action caching for full-page, fragment caching for partials — the standard performance mitigation
- Bullet gem: detects N+1 queries and unused eager loading in development; catches the most common database performance issues
- New Relic: the standard production APM in 2013 Rails apps — per-request profiling, slow query detection, error tracking
- Memory management: Ruby's garbage collector was a frequent pain point in 2013; since improved significantly in Ruby 2.x+

[Original](http://rubytune.com/cheat)
