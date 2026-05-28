---
title: Data Engineering Design Patterns (DEDP)
date: 2023-12-07
categories:
  - data-engineering
  - architecture
  - reference
  - book
  - pipelines
description: Data Engineering Design Patterns (DEDP) is a free online book covering canonical patterns for building data pipelines — ingestion, transformation, storage, and orchestration. Structured as a pattern catalog rather than a tutorial, useful as a reference for recurring architectural decisions.
params:
  source: pinboard
  sourceUrl: https://www.dedp.online/
---

![Data Engineering Design Patterns (DEDP)](/images/notes/data-engineering-design-patterns.png)

## Summary

[Data Engineering Design Patterns](/notes/data-engineering-design-patterns/) is a free online book organized as a catalog of reusable patterns for data pipeline architecture — similar in spirit to the Gang of Four patterns for software design, but applied to data systems. Each pattern addresses a recurring architectural problem: how to ingest from multiple sources, how to handle schema evolution, how to checkpoint long-running pipelines, how to ensure idempotency.

The pattern approach is more useful than tutorial books for data engineering because the problems are compositional. A real data pipeline combines ingestion patterns, transformation patterns, storage patterns, and orchestration patterns. Knowing the canonical solutions and their tradeoffs lets engineers assemble systems more deliberately rather than reinventing each piece.

Relevant patterns covered typically include: Lambda architecture and Kappa architecture for stream/batch tradeoffs, ELT vs ETL, Change Data Capture (CDC) for database synchronization, dead letter queues for error handling, data lake medallion architecture (Bronze/Silver/Gold tiers), and backfill patterns for reprocessing historical data.

## Key points

- Free online book at dedp.online — pattern catalog format, not step-by-step tutorial.
- Covers ingestion, transformation, storage, and orchestration as separate pattern domains.
- Lambda architecture: separate batch and streaming paths for latency vs. throughput tradeoffs.
- CDC (Change Data Capture): capture database changes as an event stream for downstream consumers.
- Medallion architecture: Bronze (raw) → Silver (cleaned) → Gold (aggregated) data lake tiers.
- Idempotency patterns: designing pipeline steps that can be safely rerun without producing duplicate results.

[Original](https://www.dedp.online/)
