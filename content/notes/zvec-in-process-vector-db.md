---
title: "Zvec: in-process vector database from Alibaba"
date: 2026-02-15
categories:
  - vector-database
  - machine-learning
  - infrastructure
  - open-source
description: Zvec is Alibaba's in-process vector database built on Proxima, their production search engine. No server to run — embed it directly in your app for billion-vector similarity search in milliseconds.
params:
  source: pinboard
  sourceUrl: https://github.com/alibaba/zvec
---

![Zvec: in-process vector database from Alibaba](/images/notes/zvec-in-process-vector-db.png)

## Summary

Zvec is an open-source, in-process vector database built by Alibaba on top of Proxima, their internal battle-tested vector search engine that powers large-scale production workloads. The \in-process\ part is the key design decision: instead of running as a separate service (like Qdrant, Weaviate, or Chroma), Zvec embeds directly into your application. No servers, no external connections, no config — just `pip install zvec` or `npm install @zvec/zvec` and you have similarity search available wherever your code runs.

The feature set covers what you need for modern RAG and similarity search applications: dense vectors, sparse vectors, hybrid search (semantic similarity combined with structured filters), and multi-vector queries in a single call. Searches across billions of vectors in milliseconds. The Python and Node.js SDKs expose the same interface. Runs on Linux (x86_64, ARM64) and macOS (ARM64).

The closest in-process vector database comparison is Chroma's embedded mode or LanceDB, which also runs in-process. The difference is the production-grade backing: Proxima has been running Alibaba's search infrastructure at scale for years. Zvec is essentially packaging that same engine with a developer-friendly SDK.

## Key points

- In-process vector database — runs inside your app, no server required.
- Built on Proxima, Alibaba's internal vector search engine used at production scale.
- Dense + sparse vectors with native hybrid search (semantic + structured filters).
- Python and Node.js SDKs; runs on Linux and macOS ARM64.
- Billion-vector scale in milliseconds of search latency.
- Apache 2.0 license.

[Original](https://github.com/alibaba/zvec)
