---
title: "EchoVault: local-first persistent memory for coding agents"
date: 2026-02-02
categories:
  - memory
  - ai-agents
  - local-first
  - mcp
  - fts5
  - developer-tools
description: EchoVault is local-first persistent memory for coding agents — decisions, bugs, and context stored as Markdown files indexed with FTS5, served via MCP. No cloud, no RAM overhead at idle, no external servers.
params:
  source: pinboard
  sourceUrl: https://github.com/mraza007/echovault
---

![EchoVault: local-first persistent memory for coding agents](/images/notes/echovault.png)

## Summary

[EchoVault](/notes/echovault/) gives AI coding agents persistent memory across sessions without any cloud dependency. Every decision, bug fix, and lesson is stored as Markdown in `~/.memory/vault/` and indexed with FTS5 for fast keyword search. An MCP server exposes `memory_save`, `memory_search`, and `memory_context` tools — agents call them directly without shell hooks or middleware.

The design choices are intentional responses to alternatives the author tried. Supermemory was ruled out because it stores data in the cloud, which is a problem for consultants working across multiple clients' codebases. Claude Mem caused context bloat that made running multiple sessions impractical. [EchoVault](/notes/echovault/) solves both: everything stays on disk, the server only runs when an agent starts it (zero idle overhead), and each session can be independent.

The hybrid search model is FTS5 keyword search by default, with optional Ollama or OpenAI embeddings for semantic search when needed. Memories are readable in Obsidian or any text editor. The combination of MCP interface, Markdown storage, and local FTS5 index makes this one of the more thoughtfully scoped entries in the agent memory space — it does exactly what it needs to and nothing else.

## Key points

- Local-first agent memory: Markdown files in `~/.memory/vault/`, no cloud, no remote API.
- MCP server exposes `memory_save`, `memory_search`, `memory_context` — direct agent integration.
- FTS5 keyword search by default; optional semantic search via Ollama or OpenAI embeddings.
- Zero idle overhead: the MCP server only runs when an agent starts it.
- Works with Claude Code, Cursor, Codex, and OpenCode.
- Memories stored as Markdown, readable in Obsidian or any text editor.

[Original](https://github.com/mraza007/echovault)
