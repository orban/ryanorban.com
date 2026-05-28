---
title: "Llama Hub: LlamaIndex Data Connector Marketplace"
date: 2023-02-17
categories:
  - llamaindex
  - rag
  - data-connectors
  - open-source
  - llm
description: Llama Hub is the LlamaIndex community marketplace for data loaders — connectors that pull data from Notion, Slack, GitHub, databases, APIs, and more into LlamaIndex for RAG pipelines. The npm registry equivalent for LLM data connectors.
params:
  source: pinboard
  sourceUrl: https://llamahub.ai/
---

![Llama Hub: LlamaIndex Data Connector Marketplace](/images/notes/llama-hub-data-connectors.png)

## Summary

Llama Hub is the community-maintained library of data loaders for LlamaIndex (then called GPT Index) — a curated collection of connectors that pull data from external sources into LlamaIndex for use in RAG pipelines. Connectors exist for Notion, Slack, GitHub, Google Drive, databases (SQL, MongoDB), websites, PDFs, and dozens of other sources.

The design mirrors a package registry pattern: contributors write a data loader for a specific source (a Python class with a `load_data()` method), submit it to Llama Hub, and others can install and use it with a simple API call. This lets the RAG ecosystem grow through community contribution without requiring LlamaIndex to maintain connectors for every possible data source themselves.

Llama Hub addressed a real friction point in RAG development: getting data out of the source system and into the format LlamaIndex needs (a list of `Document` objects with text and metadata). Each source has different authentication, API conventions, and data structures. A community-built library of solved connectors eliminates that work for common sources. By early 2023, Llama Hub had dozens of connectors — enough to cover most enterprise data integration scenarios without custom code.

## Key points

- Community marketplace of data loaders for LlamaIndex — connectors to 50+ data sources.
- Sources include Notion, Slack, GitHub, Google Drive, databases, websites, PDFs, APIs.
- Standard interface: each loader implements `load_data()` → returns `List[Document]`.
- npm-registry pattern: community-contributed connectors, installed with a simple API call.
- Solves the data ingestion problem in RAG pipelines without custom source-specific code.

[Original](https://llamahub.ai/)
