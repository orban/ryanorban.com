---
title: Contextually Splitting Documents — Neum AI
date: 2023-09-21
categories:
  - rag
  - chunking
  - llm
  - embeddings
  - neum-ai
description: Neum AI introduces context-aware document splitting that improves RAG retrieval quality on structured documents like SEC filings and contracts — by splitting along semantic boundaries rather than fixed character counts. A practical improvement to the chunking step most RAG tutorials treat as an afterthought.
params:
  source: pinboard
  sourceUrl: https://www.neum.ai/post/contextually-splitting-documents
---

![Contextually Splitting Documents — Neum AI](/images/notes/neum-ai-contextual-splitting.png)

## Summary

Neum AI argues that the chunking step in RAG pipelines deserves more attention than it typically gets. Most RAG tutorials use fixed-size character or token chunks (e.g., 512 tokens with 50-token overlap), but this approach breaks semantic units arbitrarily — splitting a balance sheet entry across two chunks, or separating a contract clause from its heading. Context-aware splitting uses document structure to define chunk boundaries.

The core insight: different document types have natural splitting boundaries. SEC filings have labeled sections (Risk Factors, MD&A, Financial Statements). Templated contracts have clause hierarchies. Technical documentation has heading levels. A chunker that understands these structures produces chunks that are semantically coherent — a chunk contains a complete thought, not a random 512-token slice.

Neum AI built this as a feature in their RAG infrastructure platform (which they were also developing for distributed embedding synchronization, as covered in their scale post). The mechanism: document-type-specific parsers identify semantic boundaries, then the chunker splits at those boundaries rather than at fixed sizes. For unstructured documents, they fall back to structural cues like paragraph breaks and sentence boundaries.

## Key points

- Context-aware chunking splits at semantic boundaries (sections, clauses, headings) not fixed token counts.
- Fixed-size chunking breaks semantic units — degrades RAG retrieval quality on structured documents.
- SEC filings, contracts, and templated docs have exploitable structure for better chunking.
- Neum AI built this as a configurable strategy in their RAG pipeline infrastructure.
- Retrieval quality improvement: complete chunks → more relevant chunks → better LLM context.
- Connects to Vectara's RAG Done Right series on retrieval quality decisions.

[Original](https://www.neum.ai/post/contextually-splitting-documents) → Neum AI
