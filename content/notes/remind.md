---
title: "Remind: generalized memory consolidation for AI agents"
date: 2026-03-23
categories:
  - memory
  - ai-agents
  - llm
  - knowledge-graph
  - open-source
description: "Remind consolidates raw AI experiences into generalized concepts stored in a knowledge graph, rather than dumping everything into a vector database. The distinction matters: instead of retrieving raw transcripts, it surfaces patterns like 'user prefers statically typed languages.'"
params:
  source: pinboard
  sourceUrl: https://sandst1.github.io/remind/
---

![Remind: generalized memory consolidation for AI agents](/images/notes/remind.png)

## Summary

[Remind](/notes/remind/) is an open-source memory layer for AI agents that consolidates raw experiences into generalized concepts rather than storing raw data in a vector database. The design reflects a real frustration with naive RAG approaches: if you store every conversation as an embedding and retrieve the closest match, you get raw transcripts back. What you actually want is extracted knowledge — patterns, preferences, exceptions — which is what [Remind](/notes/remind/) produces.

The system works in three phases: Remember (store raw experiences), Consolidate (an LLM extracts generalized concepts with confidence levels, conditions, and exceptions), and Recall (a spreading activation retrieval algorithm traverses the knowledge graph to find contextually relevant concepts). The spreading activation approach means a query can surface related concepts that don't match literally but are semantically connected through the graph.

It deploys either as project-scoped local databases or as centralized MCP servers, and it supports Anthropic, OpenAI, Azure, and Ollama backends. A built-in web dashboard shows concept graphs, entity exploration, and memory health. Released under Apache 2.0 and available on PyPI.

## Key points

- Generalizes episodes into concepts with confidence, conditions, and exceptions — not just vector-indexed transcripts.
- Spreading activation retrieval: queries propagate through the knowledge graph, surfacing related concepts beyond literal keyword matches.
- Dual deployment: project-scoped local database or centralized MCP server for shared memory across agents.
- Multi-provider: works with Anthropic, OpenAI, Azure, and Ollama.
- Built-in dashboard with concept graphs and memory health monitoring — rare for open-source memory tools.

[Original](https://sandst1.github.io/remind/)
