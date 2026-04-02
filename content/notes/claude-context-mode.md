---
title: "Context Mode: MCP server for context window preservation"
date: 2026-02-25
categories:
  - claude-code
  - mcp
  - context-window
  - developer-tools
description: Context Mode is an MCP server that intercepts large tool outputs and keeps them out of the context window — 98% token reduction, with BM25-indexed session history for continuity after compression. Addresses the 40%-context-consumed-in-30-minutes problem.
params:
  source: pinboard
  sourceUrl: https://github.com/mksglu/claude-context-mode
---

![Context Mode: MCP server for context window preservation](/images/notes/claude-context-mode.png)

## Summary

Context Mode is an MCP server that addresses the most common way Claude Code sessions degrade: large tool outputs consuming context window tokens until the model loses track of what it was doing. A single Playwright snapshot is 56 KB. Twenty GitHub issues add up to 59 KB. After 30 minutes of work, roughly 40% of the context window is gone. When context window compression kicks in, the model forgets which files it was editing and what tasks remain.

Context Mode solves this in two ways. First, sandboxing: instead of returning raw tool output to the conversation, it intercepts large data and stores it externally, exposing only a reference. The documented reduction is 98% — 315 KB of output becoming 5.4 KB in the actual conversation. Second, session indexing: every file edit, git operation, task, error, and decision gets tracked in SQLite and indexed with BM25 search. When conversations compress, Context Mode doesn't redump history; it retrieves only the relevant events via search, letting the model pick up exactly where it left off.

Supports Claude Code, VS Code Copilot, Cursor, Gemini CLI, and others. Automatic routing enforcement through hooks where available — so the context-saving behavior is applied consistently, not just when you remember to use the right tool.

## Key points

- 98% context reduction: 315 KB of tool output → 5.4 KB in the conversation.
- Sandboxing intercepts large outputs before they hit the conversation — Playwright snapshots, file reads, GitHub issue dumps.
- SQLite + BM25 search index of all session events enables continuity after context compression.
- Supports Claude Code, Cursor, Gemini CLI, VS Code Copilot.
- Automatic routing enforcement via hooks — applies consistently without manual invocation.

[Original](https://github.com/mksglu/claude-context-mode)
