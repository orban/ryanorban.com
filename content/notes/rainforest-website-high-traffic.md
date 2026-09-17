---
title: A Rough Guide to Keeping Your Website Up Through High Traffic
date: 2012-06-30
categories:
  - web-performance
  - devops
  - scaling
  - infrastructure
  - startup
description: Rainforest's 2012 guide to keeping a web application running through traffic spikes — covering CDN, caching, database connection pooling, and graceful degradation. Early practical devops writing from the era before managed auto-scaling became trivial.
params:
  source: pinboard
  sourceUrl: http://blog.rainforestapp.com/post/26217277790/a-rough-guide-to-keeping-your-website-up-through
---

## Summary

This 2012 post from Rainforest (later RainforestQA) documented practical strategies for keeping a web application available during sudden traffic spikes — the kind that might follow a Product Hunt or Hacker News front page appearance, a press mention, or a marketing campaign. Written at a time when AWS auto-scaling was available but not as mature or well-understood as it would become, the guide focused on defensive measures: things you could set up in advance to buy time and graceful degradation when load exceeded capacity.

The core recommendations centered on separating static from dynamic content: put everything that doesn't change behind a CDN (CloudFront, Fastly, CloudFlare) so that images, CSS, and JavaScript hit your application servers as little as possible. Caching at multiple layers — HTTP cache headers, Varnish or nginx as a caching reverse proxy, Memcached or Redis at the application level — means repeated requests don't hit the database. Database connection pooling (PgBouncer for PostgreSQL) prevents the naive pattern where each request opens a new database connection from becoming the bottleneck under load.

The graceful degradation philosophy runs through the advice: plan for the failure mode. If your service falls over, what should users see? A static maintenance page is better than an error storm. Feature flags that disable expensive functionality (real-time updates, complex queries, external API calls) under load can keep the core experience working when full functionality is unavailable. The 2012 context matters: this was practical devops advice for startups running on a handful of servers, not the Kubernetes-based auto-scaling world that followed. The fundamental patterns — CDN, caching layers, connection pooling, graceful degradation — remain valid even if the specific tools have changed.

## Key points

- CDN for static assets: images, CSS, JS should never hit application servers — CloudFront, Fastly, or CloudFlare absorb the majority of traffic.
- Multi-layer caching: HTTP headers (browser cache), reverse proxy cache (nginx, Varnish), application cache (Redis, Memcached) — each layer eliminates a class of redundant database queries.
- Database connection pooling (PgBouncer): prevents the too many connections failure mode when concurrent requests spike.
- Graceful degradation: design for failure — a static maintenance page and feature flags are better than an error storm.
- Read replicas and query optimization before scaling vertically — the database is almost always the bottleneck.
- 2012 context: pre-mature AWS auto-scaling, pre-Docker — manual capacity planning and defensive architecture were more important than they are now.

[Original](http://blog.rainforestapp.com/post/26217277790/a-rough-guide-to-keeping-your-website-up-through)
