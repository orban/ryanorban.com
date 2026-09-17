---
title: "Context Lens: see what's filling your context window"
date: 2026-02-10
categories:
  - claude-code
  - developer-tools
  - context-window
  - observability
  - llm
description: "Context Lens is a local LLM API proxy that shows what's filling your context window — system prompts vs. tool definitions vs. conversation history vs. tool results. Answers the question every developer asks: why is this session so expensive?"
params:
  source: pinboard
  sourceUrl: https://github.com/larsderidder/context-lens
---

![Context Lens: see what's filling your context window](/images/notes/context-lens.png)

## Summary

[Context Lens](/notes/context-lens/) is a local proxy that sits between your coding tools and LLM APIs, capturing calls and showing you a composition breakdown of what's consuming your context window. The breakdown covers: system prompts, tool definitions, conversation history, tool results, and thinking blocks. It answers a question that comes up constantly in agent development: \"why is this session so expensive?\"

It works without any code changes. You run `context-lens claude` (or codex, gemini, cline, etc.) and it starts the proxy, opens a web UI, sets the right environment variables, and runs your tool. The tool routes through the proxy without knowing — the proxy intercepts, analyzes, and visualizes. This is similar to what [Agent Super Spy](/notes/agent-super-spy/) and Context Mode do, but the specific focus here is token composition analysis rather than raw traffic inspection or context compression.

The LHAR format (similar to HAR but for LLM sessions) enables exporting and sharing session data. Team dashboards are on the roadmap. The tool supports privacy modes (minimal/standard/full) and redaction for PII or secrets before capture. Supports Claude Code, Codex, Gemini CLI, Cline, Aider, and anything that talks to OpenAI/Anthropic/Google APIs.

## Key points

- Local proxy that intercepts LLM API calls and visualizes context window composition.
- Breakdown by type: system prompts, tool definitions, conversation history, tool results, thinking blocks.
- No code changes needed — wraps your existing tool invocation.
- Supports Claude Code, Codex, Gemini CLI, Cline, Aider, and more.
- Privacy modes: minimal/standard/full, with PII redaction options.
- LHAR export format for sharing and comparing sessions.

[Original](https://github.com/larsderidder/context-lens)
