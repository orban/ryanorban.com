---
title: "Hive: production runtime harness for AI agents"
date: 2026-02-12
categories:
  - ai-agents
  - orchestration
  - production
  - yc
  - open-source
description: "Hive (by Aden, YC-backed) is a production runtime harness for AI agents: state management, checkpoint-based crash recovery, cost enforcement, and self-healing through graph evolution. 102 MCP tools."
params:
  source: pinboard
  sourceUrl: https://github.com/adenhq/hive/blob/main/README.md
---

![Hive: production runtime harness for AI agents](/images/notes/hive-agent-harness.png)

## Summary

Hive is a production-grade AI agent runtime harness from Aden (YC-backed). Where most agent orchestration frameworks focus on workflow definition, Hive focuses on what breaks in production: state isolation, checkpoint-based crash recovery, cost enforcement, and observability. The framing is explicit — models are getting better on their own, the bottleneck is the infrastructure around them.

The architecture uses a \queen\ coding agent that generates an agent graph from natural language goal descriptions. During execution, the harness manages state isolation between agents, checkpoint-based crash recovery (when an agent fails, it captures the failure data and automatically evolves the graph via the coding agent before redeploying), and cost limits. Built-in human-in-the-loop nodes, browser control, credential management, and parallel execution are first-class features.

The 102 MCP tools give agents access to a wide range of capabilities without custom integration work. Hive also has HoneyComb — a community site styled as a \stock market for jobs\ showing what work categories are being automated by AI agents in real time. That's an unusual addition: operational transparency about what the system is doing, framed as a social layer.

## Key points

- Production runtime harness: state isolation, checkpoint crash recovery, cost enforcement, self-healing agents.
- Natural language goal → queen agent generates agent graph → harness manages execution.
- Self-healing: failure data captured, agent graph evolved automatically via coding agent before redeploy.
- Human-in-the-loop nodes, browser control, credential management, parallel execution built in.
- 102 MCP tools available.
- HoneyComb: community transparency layer showing what jobs agents are automating.
- YC-backed by Aden; Apache 2.0 license.

[Original](https://github.com/adenhq/hive/blob/main/README.md)
