---
title: "claude-supermemory: real-time learning for Claude Code"
date: 2026-01-30
categories:
  - claude-code
  - memory
  - learning
  - developer-tools
  - mcp
description: claude-supermemory connects Claude Code to Supermemory so the agent learns in real-time — preferences, patterns, and project context accumulate across sessions. The memory grows alongside the developer's work.
params:
  source: pinboard
  sourceUrl: https://github.com/supermemoryai/claude-supermemory
---

![claude-supermemory: real-time learning for Claude Code](/images/notes/claude-supermemory.png)

## Summary

[claude-supermemory](/notes/claude-supermemory/) integrates Claude Code with Supermemory, an external memory platform, to give the agent persistent learning across sessions. As you work, preferences, patterns, and project context are captured and stored in Supermemory's cloud service. Future sessions draw on that accumulated knowledge — Claude Code arrives knowing what you care about, what patterns you prefer, and what's been established about the project.

The learns in real-time framing distinguishes this from static configuration approaches like CLAUDE.md files. Rather than a developer manually writing down what the agent should know, [claude-supermemory](/notes/claude-supermemory/) extracts knowledge automatically from the ongoing interaction. The tradeoff is that the memory lives in Supermemory's cloud, which [EchoVault](/notes/echovault/) was explicitly built to avoid for privacy reasons.

The MCP architecture is standard for this pattern: Supermemory runs as an MCP server that Claude Code can query and write to. This is one of several memory backends in this space — [EchoVault](/notes/echovault/) and [Episodic Memory](/notes/episodic-memory/) serve similar functions with different tradeoffs around storage location, search method, and infrastructure requirements.

## Key points

- Claude Code learns in real-time: preferences, patterns, and context stored in Supermemory cloud.
- Automatic extraction — no manual CLAUDE.md maintenance required.
- MCP interface: Supermemory server is queryable by Claude Code during sessions.
- Cloud-based storage (tradeoff: not local-first; compare with [EchoVault](/notes/echovault/) for local alternative).
- Part of a cluster: [EchoVault](/notes/echovault/), [Episodic Memory](/notes/episodic-memory/), and [claude-supermemory](/notes/claude-supermemory/) all solve agent memory with different architecture choices.

[Original](https://github.com/supermemoryai/claude-supermemory)
