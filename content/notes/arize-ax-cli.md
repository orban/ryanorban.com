---
title: "Arize AX CLI: LLM observability for AI coding agents"
date: 2026-03-05
categories:
  - llm-observability
  - developer-tools
  - ai-agents
  - claude-code
description: Arize AX CLI makes LLM traces, spans, and experiments machine-readable so AI coding agents can run the same observability analysis as the browser UI. Closes the loop between observability data and the agents that produced it.
params:
  source: pinboard
  sourceUrl: https://arize.com/blog/ax-cli-dev-preview
---

![Arize AX CLI: LLM observability for AI coding agents](/images/notes/arize-ax-cli.png)

## Summary

The [Arize AX CLI](/notes/arize-ax-cli/) makes LLM traces, spans, and experiments machine-readable from the terminal — so Claude Code, Cursor, or any AI coding agent can analyze the same observability data that Alyx (Arize's AI assistant) handles in the browser UI. The key insight is that your coding agent and your LLM observability data should be able to talk to each other directly.

The current workflow without this tool: an agent produces a trace, the trace lands in Arize's browser UI, a human has to read it and translate findings back to the agent. With the AX CLI, the agent can query trace data directly, run the same analysis as the UI, and act on the results — closing the feedback loop for agents that are debugging their own LLM applications.

This is part of the observability layer for AI agent development maturing. Tools like [Agent Super Spy](/notes/agent-super-spy/) and OpenTelemetry-based stacks capture what agents do; the AX CLI is specifically aimed at making that data actionable within coding agents rather than requiring a human intermediary.

## Key points

- Exposes Arize observability data (traces, spans, experiments) as machine-readable terminal output.
- Claude Code, Cursor, or any coding agent can run LLM analysis without opening the browser UI.
- Closes the feedback loop: agents can inspect their own traces and act on what they find.
- Part of the broader LLM observability tooling maturing to serve agent-native development workflows.
- Released as a dev preview by Arize (makers of Phoenix and Alyx).

[Original](https://arize.com/blog/ax-cli-dev-preview)
