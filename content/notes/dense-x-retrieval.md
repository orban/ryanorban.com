---
title: "Dense-X-Retrieval: Proposition-Level RAG"
date: 2023-12-14
categories:
  - rag
  - retrieval
  - llamaindex
  - dense-retrieval
  - nlp
description: Dense-X-Retrieval is a LlamaIndex pack implementing proposition-level retrieval — splitting documents into atomic factual propositions rather than chunks, then retrieving at proposition granularity. Improves precision by matching query semantics at a finer level than paragraph chunks.
params:
  source: pinboard
  sourceUrl: https://llamahub.ai/l/llama_packs-dense_x_retrieval?from=llama_packs
---

![Dense-X-Retrieval: Proposition-Level RAG](/images/notes/dense-x-retrieval.png)

## Summary

[Dense-X-Retrieval](/notes/dense-x-retrieval/) is a LlamaIndex pack implementing the proposition-level retrieval technique from the paper "Dense X Retrieval: What Retrieval Granularity Should We Use?" The core idea: instead of chunking documents into paragraphs or fixed-size windows for embedding, first decompose the document into atomic factual *propositions* — single-sentence claims — then embed and retrieve at the proposition level. This gives finer-grained retrieval that better matches the semantic granularity of typical queries.

The problem with chunk-based RAG: a paragraph chunk might contain one highly relevant sentence surrounded by tangentially related content. When you retrieve that chunk and inject it as context, you include the noise along with the signal. Proposition-level retrieval retrieves only the specific factual claims relevant to the query. The tradeoff is that proposition decomposition requires an extra LLM call to split the document, which adds cost and latency at indexing time.

The implementation uses an LLM to decompose source documents into propositions, embeds each proposition independently, and retrieves propositions at query time. A retrieval passage (the original source chunk) can then be recovered from the proposition for context inclusion — you get the precision of proposition matching with the context richness of the original passage. This two-tier indexing approach is one of the advanced RAG patterns covered in resources like [RAG Techniques](/notes/rag-techniques/).

## Key points

- Proposition-level retrieval: decompose documents into atomic factual claims, embed and retrieve at that granularity.
- Addresses the noisy chunk problem — retrieve only the specific relevant claim, not surrounding text.
- Tradeoff: extra LLM call at index time to generate propositions; better retrieval precision at query time.
- Two-tier approach: retrieve proposition for precision, return original passage for context richness.
- Part of LlamaIndex packs ecosystem — connects to the broader advanced RAG pattern library.

[Original](https://llamahub.ai/l/llama_packs-dense_x_retrieval)
