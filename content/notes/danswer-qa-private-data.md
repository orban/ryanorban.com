---
title: "Danswer: Natural Language Q&A Over Private Sources"
date: 2023-12-10
categories:
  - rag
  - llm
  - enterprise
  - search
  - open-source
description: Danswer (now Onyx) is an open-source enterprise Q&A system that connects to Slack, GitHub, Confluence, and other internal tools to answer natural language questions over private knowledge. Self-hosted with strong access-control enforcement — a production-ready alternative to building RAG from scratch.
params:
  source: pinboard
  sourceUrl: https://github.com/danswer-ai/danswer
---

![Danswer: Natural Language Q&A Over Private Sources](/images/notes/danswer-qa-private-data.png)

## Summary

Danswer (rebranded as [Onyx](/notes/onyx/)) is an open-source enterprise search and Q&A system built on RAG. It connects to internal knowledge sources — Slack, GitHub, Confluence, Notion, Google Drive, Jira, and more — and answers natural language questions using LLMs grounded in retrieved documents. The architecture is roughly: connectors pull documents from sources → documents are chunked and embedded → queries retrieve relevant chunks → LLM generates a grounded answer with citations.

What distinguishes Danswer from building RAG from scratch is the connector ecosystem and access control handling. The connectors are pre-built — you configure credentials and it handles crawling, incremental updates, and metadata extraction. The access control layer is the harder problem: if a user asks a question, the answer should only use documents that user has permission to read. Danswer carries access control metadata through the pipeline so retrieved documents respect the same permissions as the source system.

This is the "enterprise RAG" problem that makes production deployments hard: it's not just retrieval quality, it's that the retrieval must respect the permission model of the source systems. A question asked by an engineer should not surface documents from HR folders they can't read in Confluence.

## Key points

- Connectors for Slack, GitHub, Confluence, Notion, Google Drive, Jira, Linear, and more.
- Access control propagation: retrieved documents respect source system permissions per-user.
- Self-hosted: documents and queries stay in your infrastructure — key for enterprise data residency requirements.
- LLM choice is configurable: OpenAI, Azure OpenAI, local models via Ollama.
- Includes a chat interface, Slack bot integration, and REST API for embedding into other tools.
- Rebranded to [Onyx](/notes/onyx/) — actively maintained with enterprise support tier.

[Original](https://github.com/danswer-ai/danswer)
