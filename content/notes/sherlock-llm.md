---
title: "Sherlock: real-time LLM API traffic interceptor and dashboard"
date: 2026-01-29
categories:
  - developer-tools
  - llm
  - observability
  - token-usage
  - debugging
description: Sherlock intercepts LLM API traffic and shows token usage, costs, and context window consumption in a real-time terminal dashboard. Debug prompts and track costs across AI development sessions without adding SDK instrumentation.
params:
  source: pinboard
  sourceUrl: https://github.com/jmuncor/sherlock
---

![Sherlock: real-time LLM API traffic interceptor and dashboard](/images/notes/sherlock-llm.png)

## Summary

Sherlock intercepts LLM API traffic at the network level and surfaces token usage, costs, and context window consumption in a real-time terminal dashboard. No SDK changes or instrumentation code needed — it sits between your application and the LLM API, capturing traffic transparently.

The use case is AI development debugging and cost tracking. When working with Claude Code or building LLM-powered applications, token costs and context window usage are often opaque until you get a bill or hit a limit. Sherlock makes them visible session-by-session, in the terminal, while the work is happening.

This sits in the lightweight end of LLM observability tooling. Tools like Arize and OpenTelemetry-based solutions provide structured traces and production-scale analytics; Sherlock is for the individual developer who wants to see what's going on right now in their terminal without setting up infrastructure. The interception-without-instrumentation approach means it works with any tool that makes LLM API calls — Claude Code, Cursor, custom scripts, or any framework.

## Key points

- Intercepts LLM API traffic at network level — no SDK changes or instrumentation required.
- Real-time terminal dashboard showing token usage, costs, and context window consumption.
- Works across any tool making LLM API calls: Claude Code, Cursor, custom code.
- Lightweight alternative to full LLM observability platforms — designed for individual developer debugging.
- Tracks across AI development sessions for cumulative cost visibility.

[Original](https://github.com/jmuncor/sherlock)
