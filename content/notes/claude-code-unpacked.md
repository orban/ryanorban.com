---
title: "Claude Code Unpacked: reverse-engineering the agent harness"
date: 2026-04-01
categories:
  - claude-code
  - ai-agents
  - reverse-engineering
  - developer-tools
description: Deep reverse-engineering of Claude Code's internals — the agent loop, 50+ tools, and multi-agent orchestration. The closest thing to a technical spec for how it actually works.
params:
  source: pinboard
  sourceUrl: https://ccunpacked.dev/
---

![Claude Code Unpacked: reverse-engineering the agent harness](/images/notes/claude-code-unpacked.png)

## Summary

[Claude Code Unpacked](/notes/claude-code-unpacked/) is a community project that maps Claude Code's internals by analyzing its source code. It documents the agent loop, the 50+ built-in tools, the multi-agent orchestration system, and several unreleased features — essentially producing the technical documentation that Anthropic hasn't published.

The project covers how Claude Code processes each message through its agent loop, how tools are selected and executed, how sub-agents are spawned and coordinated, and how the permission system gates dangerous operations. For anyone building on top of Claude Code or trying to understand why it behaves certain ways, this is the most detailed public reference available.

## Key points

- Maps the full agent loop that runs when you send a message to Claude Code — from message parsing through tool selection to response generation.
- Documents 50+ built-in tools and how they're registered, dispatched, and sandboxed.
- Covers the multi-agent orchestration system used for parallel task execution.
- Identifies unreleased features visible in the source but not yet exposed to users.
- Community-maintained, produced by reverse-engineering rather than official documentation.

[Original](https://ccunpacked.dev/)
