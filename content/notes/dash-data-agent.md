---
title: "Dash: self-learning data agent with 6-layer context"
date: 2026-02-03
categories:
  - ai-agents
  - data-analysis
  - self-learning
  - open-source
  - agno
description: Dash is a self-learning data agent from Agno that grounds answers in 6 layers of context, inspired by OpenAI's in-house implementation. Each query improves the agent's performance via adaptive memory.
params:
  source: pinboard
  sourceUrl: https://github.com/agno-agi/dash
---

![Dash: self-learning data agent with 6-layer context](/images/notes/dash-data-agent.png)

## Summary

Dash is Agno's open-source data analysis agent, described as self-learning and designed to ground its answers in six layers of context. The project is explicitly inspired by OpenAI's in-house data agent implementation — a relatively rare case of an open-source project naming a proprietary system as direct inspiration.

The 6 layers of context framing suggests a hierarchy of information sources the agent uses when answering queries: likely some combination of schema knowledge, historical queries, user preferences, domain knowledge, retrieved data, and agent-generated insights. The self-learning aspect means each interaction improves future performance through adaptive memory rather than requiring explicit configuration.

Agno (the organization behind Dash) builds AI agent infrastructure, and Dash fits their broader pattern of opinionated agents with explicit design choices about how context should be structured. For data analysis specifically, this matters: pure RAG-based approaches often miss nuance about schema relationships or business logic that an agent needs to give useful answers.

## Key points

- Self-learning data agent that adapts with each query via accumulated memory.
- 6 layers of context provide structured grounding — not just RAG retrieval.
- Explicitly inspired by OpenAI's internal data analysis agent implementation.
- Open-source from Agno, who builds AI agent infrastructure.
- Adaptive memory means the agent improves performance without explicit reconfiguration.

[Original](https://github.com/agno-agi/dash)
