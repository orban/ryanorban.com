---
title: RAG Is More Than Just Embedding Search
date: 2023-09-20
categories:
  - rag
  - llm
  - embeddings
  - retrieval
  - instructor
description: Jason Liu's influential post arguing that RAG systems need more than vector similarity search — covering query understanding, routing, reranking, and structured extraction as the layers that separate working RAG from production-grade RAG. Written for the Instructor library blog.
params:
  source: pinboard
  sourceUrl: https://jxnl.github.io/instructor/blog/2023/09/17/rag-is-more-than-just-embedding-search/
---

![RAG Is More Than Just Embedding Search](/images/notes/rag-more-than-embedding-search.png)

## Summary

Jason Liu (creator of Instructor, the structured output library for LLMs) wrote this post as a corrective to the oversimplified embed everything and search framing of RAG. The argument: naive RAG — embed your documents, embed the query, return the top-k nearest neighbors — works in demos but fails in production. Real RAG systems require additional layers that tutorials ignore.

The layers Jason Liu identifies: **query understanding** (parse and reformulate the user's query before searching — expand acronyms, decompose multi-part questions, classify query intent to route to the right index); **retrieval** (hybrid search combining dense vectors with sparse keyword matching, not pure ANN search); **reranking** (a second-pass cross-encoder model that re-scores the retrieved chunks with more context than the initial vector similarity); and **structured extraction** (using Instructor-style structured outputs to extract exactly the information the answer needs, not just return raw chunks).

This post helped shift the conversation from "how do I set up a vector database to how do I design a retrieval system." The query understanding layer in particular was underappreciated — many RAG failures are query formulation failures, not retrieval failures.

## Key points

- RAG requires: query understanding, routing, hybrid retrieval, reranking, structured extraction.
- Query reformulation before retrieval is frequently the highest-leverage improvement.
- Hybrid search (dense + sparse/BM25) consistently beats pure vector search.
- Reranking: a cross-encoder pass after initial retrieval improves precision significantly.
- Instructor framing: structure the output of retrieval, don't just dump raw chunks into the prompt.
- From Jason Liu — foundational post for practitioners building production RAG systems.

[Original](https://jxnl.github.io/instructor/blog/2023/09/17/rag-is-more-than-just-embedding-search/) → Instructor
