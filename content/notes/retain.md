---
title: "Retain: unified AI conversation knowledge base for macOS"
date: 2026-01-23
categories:
  - memory
  - ai-agents
  - claude-code
  - mac-app
  - knowledge-base
description: Retain is a native macOS app that aggregates AI conversations from Claude Code, Cursor, ChatGPT, and others into a unified searchable knowledge base, then exports learnings to CLAUDE.md so Claude remembers your preferences.
params:
  source: pinboard
  sourceUrl: https://github.com/BayramAnnakov/retain
---

![Retain: unified AI conversation knowledge base for macOS](/images/notes/retain.png)

## Summary

[Retain](/notes/retain/) is a native macOS app that solves a specific problem: context is scattered across many AI coding tools, and each one starts fresh. You teach Claude Code something in one session; it's gone the next. You establish a preference in Cursor; Claude doesn't know about it. [Retain](/notes/retain/) aggregates conversations from all of them into one searchable database, then exports approved learnings to CLAUDE.md so Claude actually remembers.

The sync coverage is broad: Claude Code, Codex CLI, Cursor, Gemini CLI, OpenCode, GitHub Copilot CLI auto-sync; claude.ai and ChatGPT sync via browser cookie. Full-text search via FTS5 works across 10,000+ conversations. The learning extraction is the clever part — it detects patterns like no, use X instead or stated preferences, then lets you approve which ones get exported to CLAUDE.md.

This addresses the same problem space as [EchoVault](/notes/echovault/), [Episodic Memory](/notes/episodic-memory/), and [claude-supermemory](/notes/claude-supermemory/), but from a different angle: instead of instrumenting agents during sessions, [Retain](/notes/retain/) reads completed conversation history from multiple tools' local storage after the fact. The CLAUDE.md export loop is particularly practical — it turns conversation patterns into durable configuration that works without any new tooling installed.

## Key points

- Aggregates Claude Code, Cursor, Codex CLI, ChatGPT, and other AI conversations into one searchable database.
- FTS5 full-text search across 10,000+ conversations.
- Extracts corrections and preferences from conversation patterns.
- Exports approved learnings to CLAUDE.md — durable configuration without new agent tooling.
- Local-first: all storage on-device; optional cloud features available separately.
- From the creator of claude-reflect (300+ stars).

[Original](https://github.com/BayramAnnakov/retain)
