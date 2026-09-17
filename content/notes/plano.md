---
title: "Plano: AI-native proxy and data plane for agents"
date: 2026-02-07
categories:
  - ai-agents
  - proxy
  - orchestration
  - observability
  - developer-tools
description: Plano is an AI-native proxy and data plane for agentic apps — centralized routing, guardrails, observability, and LLM switching so you don't re-implement plumbing in every codebase. Decouples agents from brittle framework abstractions.
params:
  source: pinboard
  sourceUrl: https://github.com/katanemo/plano
---

![Plano: AI-native proxy and data plane for agents](/images/notes/plano.png)

## Summary

[Plano](/notes/plano/) is an AI agent infrastructure layer positioned as the missing data plane for production agentic applications. The core argument: every team building agents ends up reimplementing the same plumbing — LLM routing, observability, guardrails, safety filters — from scratch, tightly coupled to whatever framework they started with. Plano pulls all of that out into a centralized proxy layer so individual agent codebases can stay focused on logic.

The architecture is a reverse proxy that sits between your application code and the LLM APIs. It handles multi-agent routing, captures rich agentic signals and traces for continuous improvement, applies guardrail filters for safety and moderation, and provides smart LLM routing APIs for model agility — letting you switch between models without touching agent code. It supports any language or AI framework, with a Quickstart documented in their docs.

The framing aligns with the broader pattern of agent infrastructure maturing: as agentic apps go to production, the just build it per-project approach breaks down. [Plano](/notes/plano/) is Katanemo's bet that a standalone data plane, similar to what service meshes did for microservices, is the right abstraction level.

## Key points

- AI-native proxy positioned between agent code and LLM APIs — handles routing, observability, safety without per-project reimplementation.
- Smart LLM routing enables model agility: switch providers or versions without touching application code.
- Captures rich agentic signals and traces to support continuous improvement of agent behavior.
- Guardrail filters for safety and moderation applied at the proxy layer rather than per-agent.
- Use any language or AI framework — Plano doesn't require framework lock-in.

[Original](https://github.com/katanemo/plano)
