---
title: "Agent Super Spy: LLM observability for local agent development"
date: 2026-04-01
categories:
  - ai-agents
  - observability
  - llm
  - developer-tools
  - docker
description: Local LLM proxy stack that gives you full visibility into what your AI agents actually do. Dual-layer observability via OpenTelemetry traces and raw HTTP capture.
params:
  source: pinboard
  sourceUrl: https://github.com/simple10/agent-super-spy
---

![Agent Super Spy: LLM observability for local agent development](/images/notes/agent-super-spy.png)

## Summary

[Agent Super Spy](/notes/agent-super-spy/) is a local development stack by simple10 that gives you full visibility into what your AI agents are actually doing under the hood. The core problem it addresses: when you're building with LLMs locally, it's hard to see exactly what API calls your agents make, what traffic they generate, and how they interact with external services. This tool puts all of that in one place.

The architecture centers on a custom LLM proxy (written in TypeScript) that sits between your agents and the upstream LLM providers. You point your agent's base URL at the proxy (e.g., `ANTHROPIC_BASE_URL=http://localhost:4000/anthropic`), and it handles path-based routing to different providers, transparently swaps placeholder API keys for real credentials via a `keys.jsonc` config, and exports OpenTelemetry traces. Alongside the proxy, mitmproxy captures raw HTTPS traffic for low-level inspection, while Opik and Phoenix provide structured trace visualization and analysis.

Everything runs in Docker containers networked together, so setup is a `docker compose up` away. The dual-layer approach (raw HTTP via mitmproxy plus structured traces via OpenTelemetry) means you can debug at whatever level of abstraction you need -- from individual HTTP headers to high-level agent reasoning chains.

## Key points

- Acts as a reverse proxy for LLM API calls, supporting provider-specific paths (`/anthropic`, `/openai`) and generic hostname-based routing for any LLM API.
- Centralizes API key management so real credentials never leak into agent config -- the proxy swaps placeholder keys for real ones at request time.
- Exports OpenTelemetry traces to Opik and Phoenix for structured observability, while mitmproxy gives you raw traffic inspection through a web UI.
- Built with TypeScript, Shell, Docker, and Python -- runs as a Docker Compose stack with minimal setup.
- Useful during local AI agent development when you need to understand and debug the full chain of LLM calls your system makes.

[Original](https://github.com/simple10/agent-super-spy)
