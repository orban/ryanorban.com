---
title: "LlamaIndex: Composable Indices and Query Decomposition"
date: 2023-03-13
categories:
  - llm
  - rag
  - llamaindex
  - composable-indices
  - query-decomposition
description: A LlamaIndex notebook demonstrating composable indices with query decomposition on city data — showing how to break complex queries into sub-queries across multiple document indices and synthesize the results. An early tutorial on the multi-hop retrieval patterns LlamaIndex specialized in.
params:
  source: pinboard
  sourceUrl: https://github.com/jerryjliu/llama_index/blob/main/examples/composable_indices/city_analysis/City_Analysis-Decompose.ipynb
---

![LlamaIndex: Composable Indices and Query Decomposition](/images/notes/llamaindex-composable-indices-city-analysis.png)

## Summary

This Jupyter notebook from Jerry Liu (creator of LlamaIndex, then called GPT Index) demonstrates composable indices — building a hierarchy of document indices that can be queried together, with automatic query decomposition. The city analysis example creates separate indices for multiple cities, then a top-level list index over them, enabling queries that require information from multiple cities simultaneously.

The core pattern: instead of a flat RAG index over all documents, LlamaIndex allows you to build tree structures, list indices, and graph indices that compose. A query like "compare the economies of New York and Los Angeles" gets decomposed into sub-queries for each city index, results retrieved from each, then synthesized into a combined answer. This multi-hop retrieval is more accurate than naively embedding everything together for cross-document reasoning.

LlamaIndex's composable indices were its key differentiator from LangChain in early 2023. LangChain was more tool/agent focused; LlamaIndex was more retrieval/query focused. The decomposition approach anticipated later agentic RAG patterns — where an LLM orchestrates multiple retrieval steps rather than doing one-shot semantic search. The notebook format made these concepts accessible to practitioners learning the library.

## Key points

- Composable indices: tree, list, and graph index hierarchies that enable multi-hop retrieval.
- Query decomposition: complex queries automatically broken into sub-queries across child indices.
- Demonstrates cross-document reasoning that flat vector search struggles with.
- LlamaIndex early differentiator vs. LangChain: retrieval-first vs. tool/agent-first.
- Anticipates agentic RAG patterns — multi-step LLM-orchestrated retrieval.

[Original](https://github.com/jerryjliu/llama_index/blob/main/examples/composable_indices/city_analysis/City_Analysis-Decompose.ipynb) → AI agent, GitHub
