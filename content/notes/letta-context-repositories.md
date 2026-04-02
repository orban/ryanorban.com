---
title: "Letta Context Repositories: git-versioned memory for coding agents"
date: 2026-02-13
categories:
  - memory
  - ai-agents
  - git
  - letta
  - context-management
description: Letta introduces Context Repositories — git-versioned memory for coding agents that treats context as source code with branches, commits, and diffs. A substantive rethink of how stateful coding agents should manage long-lived context.
params:
  source: pinboard
  sourceUrl: https://www.letta.com/blog/context-repositories
---

![Letta Context Repositories: git-versioned memory for coding agents](/images/notes/letta-context-repositories.png)

## Summary

Letta is rebuilding how memory works in Letta Code with Context Repositories — a system that treats agent context as code. Instead of an opaque memory store, you get git-based versioning: context has commits, branches, diffs, and history. The core insight is that context management for long-running agents has the same requirements as version control for code — you need to track changes, roll back mistakes, and see what changed between sessions.

Programmatic context management means the agent itself can read and write structured context, not just accumulate a flat log. The git versioning layer gives this context history and auditability. A coding agent that can inspect its own memory like a codebase — running `git log` or `git diff` on its own context — has fundamentally different debugging and recovery properties than one that works from a floating summary.

This is a more ambitious take on agent memory than simple RAG retrieval or the BM25-indexed session logs in tools like Context Mode. The closest conceptual neighbor is the persistent identity files in [Agent Swarm](/notes/agent-swarm/) (`SOUL.md`, `IDENTITY.md`), but with full git-backed versioning instead of mutable markdown files.

## Key points

- Context treated as source code: git-versioned with commits, branches, diffs, and full history.
- Programmatic access means agents can read and modify their own context in structured ways, not just append.
- Part of the broader Letta Code platform for stateful long-running AI agents.
- Addresses the core weakness of session-scoped agents: memory that resets between runs.
- Positions context versioning as the next step after basic RAG — structured, auditable, recoverable.

[Original](https://www.letta.com/blog/context-repositories)
