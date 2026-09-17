---
title: "Benchmarking Postgres vector search: pgvector vs Lantern"
date: 2024-01-17
categories:
  - postgresql
  - vector-search
  - benchmark
  - embeddings
  - database
description: Tembo's benchmark comparing pgvector and Lantern for vector similarity search in PostgreSQL — tests query speed, indexing time, and recall across different dataset sizes. Practical data for choosing a Postgres vector extension.
params:
  source: pinboard
  sourceUrl: https://tembo.io/blog/postgres-vector-search-pgvector-and-lantern/
---

![Benchmarking Postgres vector search: pgvector vs Lantern](/images/notes/pgvector-lantern-benchmark.png)

## Summary

Tembo (the managed PostgreSQL cloud platform) benchmarked two competing PostgreSQL vector search extensions: pgvector (the dominant, widely-deployed choice) and Lantern (a newer alternative claiming better performance). The benchmark covers query latency, index build time, and recall — the three dimensions that matter for RAG and semantic search applications built on PostgreSQL.

pgvector uses HNSW (hierarchical navigable small world) and IVFFlat index types. Lantern uses a usearch index, a different approximate nearest neighbor algorithm that claims faster indexing and better query performance at scale. The Tembo benchmarks give concrete numbers to evaluate those claims — which is important because benchmarks from the vendor of a competing extension should always be checked by a neutral third party.

Vector search in PostgreSQL is a meaningful alternative to dedicated vector databases like Pinecone or Weaviate for applications that are already on Postgres. The tradeoffs are well understood: Postgres-native vector search simplifies the stack and enables ACID transactions across data and embeddings, while dedicated vector databases can offer better performance at large scale. Benchmarks like this help calibrate where the crossover point is. For most RAG applications, pgvector with proper HNSW indexing is sufficient.

## Key points

- Benchmarks pgvector vs Lantern for vector similarity search in PostgreSQL.
- Dimensions tested: query latency, index build time, and recall.
- pgvector uses HNSW / IVFFlat index types; Lantern uses usearch.
- Postgres-native vector search enables ACID transactions and removes a separate service from the stack.
- Related: VectorChord (successor to pgvecto.rs), pgai (Timescale).

[Original](https://tembo.io/blog/postgres-vector-search-pgvector-and-lantern/)
