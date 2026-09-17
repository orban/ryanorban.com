---
title: "scrapy-history-middleware: S3 Historical Cache for Scrapy"
date: 2021-01-20
categories:
  - web-scraping
  - scrapy
  - python
  - aws-s3
  - caching
description: A Scrapy middleware that stores every crawled response in S3, building a historical archive of web resources over time. Enables point-in-time replay of crawls and separates the concerns of fetching from processing.
params:
  source: pinboard
  sourceUrl: https://github.com/skillupco/scrapy-history-middleware
---

## Summary

[scrapy-history-middleware](/notes/scrapy-history-middleware/) is a Scrapy middleware that saves each crawled HTTP response to Amazon S3 as it's fetched, building a persistent historical archive of web resources. On subsequent crawls, it can serve responses from the S3 cache instead of making live requests — but unlike a standard HTTP cache, it preserves all historical snapshots with timestamps. This means you can replay any crawl from any past date.

The use case is data pipelines that need reproducibility: if your extraction logic changes (you realize you need a field you weren't extracting before), you can reprocess historical data without re-crawling. This is valuable when the target site rate-limits aggressively or when the original content may have changed or disappeared. It's the web scraping equivalent of keeping raw event logs separate from derived tables.

The pattern also separates two concerns that are usually coupled: fetching and processing. Fetching is IO-bound, rate-limited, and fragile; processing is CPU-bound and deterministic. With the history middleware, you fetch once and process many times. This is architecturally similar to how Kafka allows replay of event streams for reprocessing.

## Key points

- Stores all Scrapy responses to Amazon S3 with timestamps, enabling point-in-time replay of any past crawl.
- Separates fetching (fragile, rate-limited) from processing (deterministic, repeatable) — replay old crawls with new extraction logic.
- Useful for any scraping pipeline where source data may disappear or change, or where extraction requirements evolve.
- Analogous to raw event log storage in data engineering: keep the source of truth, process it multiple times.
- Integrates via standard Scrapy middleware — no changes to spiders needed.

[Original](https://github.com/skillupco/scrapy-history-middleware) → GitHub
