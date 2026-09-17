---
title: The Vector Database Index
date: 2022-09-20
categories:
  - vector-database
  - machine-learning
  - infrastructure
  - market-landscape
  - embeddings
description: Gradient Flow's landscape map of vector databases — published in 2022 when the category was forming, covering Pinecone, Weaviate, Qdrant, Chroma, Milvus, and others. A useful historical snapshot of the vector DB market at the moment it became strategically important.
params:
  source: pinboard
  sourceUrl: https://gradientflow.com/the-vector-database-index/
---

## Summary

Gradient Flow's vector database index is a landscape map of the emerging vector database category, published in late 2022 when the space was coalescing from a niche ML infrastructure concern into a mainstream developer tool. The timing coincided with the LLM explosion driving demand for embedding storage and similarity search — Pinecone, Weaviate, Qdrant, Chroma, Milvus, and Redis with vector search all launched or accelerated in this window.

Vector databases store high-dimensional embedding vectors and support approximate nearest neighbor (ANN) search, which is the core primitive needed for RAG (retrieval-augmented generation), semantic search, and recommendation systems. The category was relatively niche before LLMs — mainly used by teams running large-scale recommendation engines — and exploded in 2022-2023 as every LLM application needed a place to store embeddings.

The landscape mapped a few distinct approaches: purpose-built vector databases (Pinecone, Weaviate, Qdrant), general databases adding vector search (PostgreSQL + pgvector, Redis Stack), and in-process libraries (FAISS, Chroma). The choice matters for production use: purpose-built databases have better performance and filtering, while vector-augmented general databases reduce infrastructure complexity.

## Key points

- Landscape map of the vector database category at its formative moment (2022).
- Covers Pinecone, Weaviate, Qdrant, Chroma, Milvus, FAISS, pgvector.
- Category exploded with LLM adoption: every RAG system needs embedding storage.
- Three approaches: purpose-built vector DBs, general DBs + vector search, in-process libraries.
- ANN (approximate nearest neighbor) search is the core primitive.
- Published by Gradient Flow (Ben Lorica and Roger Chen).

[Original](https://gradientflow.com/the-vector-database-index/)
