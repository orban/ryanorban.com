---
title: "tapes: transparent AI agent telemetry"
date: 2026-02-10
categories:
  - ai-agents
  - observability
  - telemetry
  - developer-tools
description: Tapes introduces transparent telemetry for AI agents — a structured trace format that makes agent execution auditable without requiring a full observability platform. Good complement to heavier tools like Arize AX or Phoenix.
params:
  source: pinboard
  sourceUrl: https://johncodes.com/archive/2026/02-09-introducing-tapes/
---

![tapes: transparent AI agent telemetry](/images/notes/tapes-agent-telemetry.png)

## Summary

tapes is an observability tool for AI agents focused on transparency — making what agents actually do legible to the developer without requiring a full observability stack. The name is evocative: a tape is a complete, sequential record of what happened, preserved and replayable. Applied to agents, this means structured traces of agent actions that you can inspect, replay, and audit.

The observability problem for agents has multiple layers. There's the raw API call level (what [Agent Super Spy](/notes/agent-super-spy/) and mitmproxy capture), the structured span/trace level (what OpenTelemetry and Phoenix track), and the higher-level behavioral level (what was the agent trying to do, what decisions did it make). tapes appears to target a readable middle ground — not raw HTTP dumps, not enterprise-scale dashboards, but a transparent trace format that works for individual developers building agents locally.

This fits alongside [Arize AX CLI](/notes/arize-ax-cli/) and AgentLogs in the broader category of tools making AI agent behavior inspectable. The trend is agents becoming primary development subjects that need the same observability investment as production services.

## Key points

- Structured trace format for AI agent execution — transparent and replayable without enterprise tooling.
- Targets individual developers building agents locally rather than production observability stacks.
- Complements [Agent Super Spy](/notes/agent-super-spy/) (raw HTTP), Phoenix/Opik (structured traces), and [Arize AX CLI](/notes/arize-ax-cli/) (terminal-accessible LLM observability).
- Part of the broader trend toward agent telemetry as a first-class developer tool.
- The tape metaphor: a complete sequential record you can inspect and replay.

[Original](https://johncodes.com/archive/2026/02-09-introducing-tapes/)
