---
title: "Dexto: intelligence layer for AI agents"
date: 2025-10-28
categories:
  - ai-agents
  - orchestration
  - llm
  - open-source
  - developer-tools
description: Dexto is an open-source AI agent orchestration platform that adds stateful memory, tool management, and error recovery to LLMs — supporting 50+ models, 30+ MCP tools, and deployment across web UI, CLI, REST API, and Discord. A production-oriented agent infrastructure layer.
params:
  source: pinboard
  sourceUrl: https://github.com/truffle-ai/dexto
---

![Dexto: intelligence layer for AI agents](/images/notes/dexto-agent-orchestration.png)

## Summary

Dexto is an open-source AI agent orchestration platform from Truffle AI that transforms LLMs into stateful, tool-using agents capable of recovering from errors. It's positioned as "the orchestration layer" — the infrastructure between raw model calls and a deployed, reliable agent.

The platform ships with a production-ready coding agent and supports 50+ language models across providers, with model switching that doesn't require code changes. It ships with 30+ MCP tool integrations, YAML-based agent configuration, and deployment across multiple interfaces: web UI, CLI, REST API, and Discord.

Dexto sits in a growing space of agentic AI infrastructure alongside LangChain, LlamaIndex, and similar frameworks. The YAML configuration approach and multi-interface deployment are oriented at teams building internal tools or production agents rather than researchers. The MCP integration means it can leverage the growing ecosystem of Model Context Protocol tool servers.

## Key points

- Open-source AI agent orchestration — state management, tool use, error recovery over raw LLM calls.
- 50+ LLM providers supported; switch models without code changes.
- 30+ MCP tool integrations out of the box.
- YAML-configured agents deployable as web UI, CLI, REST API, or Discord bot.
- From Truffle AI; production-oriented rather than research-oriented.

[Original](https://github.com/truffle-ai/dexto) → GitHub
