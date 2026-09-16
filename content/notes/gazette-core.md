---
title: "Gazette Core: Unified SQL, Batch, and Stream Processing"
date: 2022-07-16
categories:
  - data-engineering
  - streaming
  - batch-processing
  - go
  - infrastructure
description: Gazette is an open-source platform for building data pipelines that mix SQL, batch, and stream processing in a unified model backed by journals (append-only logs). Designed for organizations that want Kafka-like durability with flexible processing paradigms without committing to a full streaming architecture.
params:
  source: pinboard
  sourceUrl: https://github.com/gazette/core
---

## Summary

Gazette is an open-source data platform built around the concept of journals — append-only, durable log primitives similar to Kafka partitions but with a different operational model. The core pitch is flexibility: you can run SQL queries, batch jobs, and stream processing against the same underlying data store without choosing a single paradigm upfront.

The architecture is Go-based and treats the journal as the fundamental storage primitive. Producers append records to journals; consumers read from them using different processing models depending on latency and throughput requirements. Gazette's consumer framework handles offset tracking, distributed coordination, and exactly-once semantics. This is the hard part of streaming systems that teams usually end up reimplementing.

By 2022, most teams were choosing between Apache Kafka + stream processing (high operational cost, high throughput) or batch-oriented dbt + warehouse patterns (lower cost, higher latency). Gazette occupies a middle ground for organizations that need sub-second processing on some data while also running heavy batch analytics — without running separate systems for each. The approach is architecturally elegant but requires buying into Gazette's specific journal abstraction.

## Key points

- Journals are append-only log segments stored durably (cloud object storage or local); both producers and consumers are decoupled
- Supports SQL queries via Estuary Flow integration, batch processing via offset-range reads, and stream processing via the consumer framework
- Go implementation with a focus on operational simplicity compared to Apache Kafka
- Exactly-once semantics via transactional log offsets — harder than at-least-once, required for stateful applications
- Predecessor to Estuary Flow, a managed version of the same ideas that gained more commercial traction

[Original](https://github.com/gazette/core) → GitHub
