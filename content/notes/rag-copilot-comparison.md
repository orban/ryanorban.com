---
title: "Comparing RAG Copilots: OpenAI, Anthropic, Perplexity, and More"
date: 2023-12-12
categories:
  - rag
  - llm
  - evaluation
  - copilot
  - comparison
description: Graphlit's comparison of RAG-powered copilots from OpenAI, Anthropic, Perplexity, and others against unstructured data retrieval tasks. Useful late-2023 benchmark of the RAG quality landscape across providers before the tooling matured.
params:
  source: pinboard
  sourceUrl: https://www.graphlit.com/blog/rag-copilot-comparison
---

![Comparing RAG Copilots: OpenAI, Anthropic, Perplexity, and More](/images/notes/rag-copilot-comparison.png)

## Summary

Graphlit is an API-first platform for building AI-powered applications over unstructured data, making them well-positioned to compare RAG implementations across providers. This blog post benchmarks copilot experiences — OpenAI Assistants, Anthropic Claude with RAG, Perplexity, and others — against domain-specific knowledge retrieval tasks involving unstructured documents.

The comparison is notable for its December 2023 timing: this was before OpenAI Assistants had matured, before Claude 3 arrived, and before the RAG tooling ecosystem consolidated. The results represent a snapshot of the quality landscape at a moment when there was significant variance across providers in how well they handled document retrieval, context injection, and coherent synthesis from retrieved content.

Graphlit's motivation for the comparison is commercial: they offer an alternative to building your own RAG pipeline, so benchmarking the field positions them. The comparison methodology covers tasks across legal, healthcare, sales, and engineering document domains — the vertical markets Graphlit targets. This domain-specificity matters: RAG quality varies significantly by document type, and a provider that performs well on news articles may struggle with dense technical specifications.

## Key points

- Compares OpenAI Assistants, Anthropic Claude RAG, Perplexity, and others on document retrieval tasks.
- December 2023 snapshot — significant quality variance across providers before the ecosystem matured.
- Domain-specific benchmarks: legal, healthcare, sales, engineering docs — RAG quality is domain-dependent.
- By Graphlit — API platform for AI on unstructured data, so comparison is commercially motivated.
- Late 2023 context: OpenAI Assistants pre-maturity, Claude 3 not yet released, tooling still consolidating.

[Original](https://www.graphlit.com/blog/rag-copilot-comparison)
