---
title: "SuperDuperDB: Bring AI to Your Database"
date: 2023-12-05
categories:
  - llm
  - database
  - rag
  - vector-search
  - open-source
description: SuperDuperDB integrates AI models and APIs directly with existing databases — train, manage, and query models where your data already lives rather than moving data to a separate vector database. A database-native alternative to building a separate AI data pipeline.
params:
  source: pinboard
  sourceUrl: https://github.com/SuperDuperDB/superduperdb
---

![SuperDuperDB: Bring AI to Your Database](/images/notes/superduperdb-ai-database.png)

## Summary

SuperDuperDB (now rebranded as SuperDuper) is an open-source framework for integrating AI models directly with existing databases — MongoDB, PostgreSQL, MySQL, SQLite, Snowflake — rather than extracting data into a separate vector database for AI workloads. The premise: your data is already in a database; adding AI should be a layer on top of that, not a reason to duplicate it.

The standard architecture for RAG involves ETL: extract documents from a source database, chunk them, embed them, load into a vector database like Pinecone or Weaviate, and query the vector database at inference time. SuperDuperDB collapses this: you register a model with a database collection, and it handles embedding, storage, and retrieval within the same database. For MongoDB, vector indexes can live in Atlas Search; for PostgreSQL, it uses `pgvector`.

The advantage over a separate vector database is reduced data movement, simpler architecture, and keeping AI outputs co-located with the source data. The disadvantage is that embedded vector databases in general-purpose databases don't yet match dedicated vector databases on ANN (approximate nearest neighbor) search performance at scale. For most applications below millions of documents, this tradeoff favors SuperDuperDB.

## Key points

- Database-native AI: register models on collections/tables — no separate vector database needed.
- Supports MongoDB, PostgreSQL, MySQL, SQLite, Snowflake, DuckDB.
- Handles embedding, indexing, and vector search within the existing database.
- Model management: version models, track predictions, retrain on new data — all from the database layer.
- RAG in one place: source data + embeddings + retrieval in the same system.
- Trade-off: simpler architecture vs. dedicated vector database performance at large scale.

[Original](https://github.com/SuperDuperDB/superduperdb) → GitHub
