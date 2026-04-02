---
title: Searchable Agent Memory in a Single File
date: 2026-02-10
categories:
  - memory
  - ai-agents
  - mcp
  - bm25
  - claude-code
description: A single-file BM25 MCP server that gives a Claude Code agent searchable access to its own conversation history. Shows how much mileage you can extract from a minimal implementation.
params:
  source: pinboard
  sourceUrl: https://eric-tramel.github.io/blog/2026-02-07-searchable-agent-memory/
---

![Searchable Agent Memory in a Single File](/images/notes/searchable-agent-memory.png)

## Summary

Eric Tramel's post describes a minimal MCP server — a single file — that indexes Claude Code conversation history and makes it searchable via BM25. The idea is that an agent's conversation history is itself a form of memory, and if that history is searchable rather than just scrollable, the agent can pull relevant past context on demand rather than relying on whatever happens to be in the current context window.

BM25 is the classic sparse keyword retrieval algorithm — it's fast, runs locally, requires no embeddings or vector database, and performs well on structured text like conversation logs. Using it as the search backend for a session history index is pragmatic: you get meaningful recall without needing to run an embedding model or maintain a vector store. This is the same retrieval approach used by Context Mode for its session indexing layer.

The single-file design matters as a point of philosophy. This isn't a framework or platform — it's a focused tool that does one thing. You add it to your MCP server list and Claude Code can now search its own conversation history. No infrastructure, no dependencies. The simplicity is the point.

## Key points

- Single-file MCP server that indexes Claude Code conversation history for BM25 search.
- Enables agents to retrieve relevant past context rather than relying on context window proximity.
- BM25 requires no embedding model or vector database — fast, local, minimal.
- Same retrieval approach as Context Mode's session indexing, but as a standalone minimal tool.
- Demonstrates how much utility you can ship in a single focused MCP implementation.

[Original](https://eric-tramel.github.io/blog/2026-02-07-searchable-agent-memory/)
