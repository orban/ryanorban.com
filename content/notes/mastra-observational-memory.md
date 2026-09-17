---
title: Mastra Observational Memory
date: 2026-02-10
categories:
  - memory
  - ai-agents
  - mastra
  - context-window
  - long-term-memory
description: Mastra's Observational Memory keeps agent context windows small by summarizing and compressing observations rather than keeping raw conversation history. A practical approach to the long-term vs. working memory tradeoff in AI agents.
params:
  source: pinboard
  sourceUrl: https://mastra.ai/docs/memory/observational-memory
---

![Mastra Observational Memory](/images/notes/mastra-observational-memory.png)

## Summary

Mastra's Observational Memory is a memory strategy for AI agents designed around a specific constraint: context window size. The core problem is that as agents have more and more conversations, storing complete conversation history in the context window becomes impossible. Observational Memory addresses this by compressing raw observations into a more compact representation that preserves what matters across sessions while keeping active context small.

The approach differs from raw retrieval systems like RAG or BM25 search. Rather than storing transcripts and retrieving chunks, Observational Memory synthesizes what the agent has observed into structured long-term knowledge. It's closer in spirit to [Remind](/notes/remind/)'s generalized concept extraction — the idea that useful memory is extracted knowledge, not raw transcripts.

This is part of Mastra's broader agent framework, which offers memory as a built-in primitive rather than an add-on. The documentation covers how the system integrates with the Mastra agent lifecycle — memory is populated through conversations and retrieved to inform future responses, without the agent (or user) having to manage memory explicitly.

## Key points

- Compresses conversation observations into compact long-term memory, keeping context window small.
- Preserves knowledge across sessions without replaying full conversation history.
- Part of Mastra's built-in memory infrastructure for AI agents.
- Philosophically similar to [Remind](/notes/remind/)'s concept extraction — synthesized knowledge over raw retrieval.
- Contrasts with BM25 or vector database approaches that store and retrieve raw text.

[Original](https://mastra.ai/docs/memory/observational-memory)
