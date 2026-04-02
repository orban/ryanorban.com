---
title: "Episodic Memory: semantic search for Claude Code conversation history"
date: 2026-04-01
categories:
  - claude-code
  - memory
  - semantic-search
  - mcp
  - developer-tools
description: Semantic search over past Claude Code conversations via local embeddings and MCP. Preserves the trade-offs, alternatives, and preferences that live nowhere else.
params:
  source: pinboard
  sourceUrl: https://github.com/obra/episodic-memory
---

## Summary

[Episodic Memory](/notes/episodic-memory/) is a tool by obra (Jesse Vincent) that gives Claude Code searchable access to past conversations. It indexes your conversation transcripts locally using vector embeddings and SQLite, then exposes semantic search through both a CLI and an MCP server — so you can find previous discussions by meaning, not just keywords.

The core problem it addresses: when you're working with Claude Code across many sessions, valuable context gets lost. The trade-offs you discussed, the alternatives you considered, your stated preferences — none of that persists between conversations. [Episodic Memory](/notes/episodic-memory/) captures it by automatically copying conversations from Claude Code, generating embeddings for semantic similarity matching, and making everything searchable.

Exposing search via MCP is the key design choice. It means Claude Code itself can query past conversations during a session, effectively giving the agent long-term memory across sessions without requiring any changes to Claude's architecture.

## Key points

- Indexes Claude Code conversations locally using vector embeddings and SQLite for semantic search by meaning, not keywords.
- Exposes search through both CLI commands and an MCP server, so both humans and agents can query history.
- Preserves context that's otherwise ephemeral: trade-offs discussed, alternatives considered, user preferences expressed.
- Runs entirely locally — no data sent to external services, embeddings computed on your machine.
- The MCP integration lets Claude Code query its own past conversations during live sessions, creating a form of cross-session memory.

[Original](https://github.com/obra/episodic-memory)
