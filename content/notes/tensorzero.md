---
title: TensorZero
date: 2024-09-26
categories:
  - llm
  - mlops
  - observability
  - optimization
  - infrastructure
  - open-source
description: "TensorZero is a self-hosted LLMOps platform that unifies gateway, observability, evaluation, optimization, and A/B testing in one Rust-built system. The feedback loop: production inference data flows back into prompt and model improvement automatically."
params:
  source: pinboard
  sourceUrl: https://github.com/tensorzero/tensorzero
---

![TensorZero](/images/notes/tensorzero.png)

## Summary

[TensorZero](/notes/tensorzero/) is an open-source LLMOps platform for managing the full lifecycle of LLM applications in production — from inference routing to observability, evaluation, optimization, and experimentation. It's self-hosted (no vendor lock-in), built primarily in Rust for performance (sub-1ms p99 gateway latency), and provider-agnostic across OpenAI, Anthropic, AWS Bedrock, Google, and 15+ others.

The core architecture is a feedback loop: the gateway receives inferences and logs them with user feedback to your own database, the evaluation layer benchmarks outputs using heuristics or [LLM-as-a-judge](/notes/llm-as-a-judge/), and the optimization layer uses production data and feedback to improve prompts, models, and inference strategies. Each component can be adopted independently rather than requiring all-or-nothing adoption — you can start with just the gateway and add optimization later.

[TensorZero](/notes/tensorzero/) positions itself against the fragmented LLMOps tooling landscape where teams typically stitch together separate tools for routing (LiteLLM), observability (LangSmith, Opik), and evaluation. Unifying these creates the feedback loop that makes production data directly improve model behavior — the kind of self-improving cycle that's difficult to build with disconnected tools. The self-hosted, Rust-based approach appeals to teams with data residency requirements who can't send inference data to third-party observability platforms.

## Key points

- 5 integrated capabilities: gateway, observability, evaluation, optimization, experimentation — all in one system.
- Sub-1ms p99 latency gateway; built in Rust — production-grade performance, not prototype tooling.
- Self-hosted with full data ownership; no inference data leaves your infrastructure.
- [LLM-as-a-judge](/notes/llm-as-a-judge/) evaluation integrated natively alongside heuristic benchmarks.
- A/B testing, routing, fallbacks, and retries for safe deployment decisions.
- Incremental adoption: use just the gateway, then layer on other components over time.
- Contrast with: LiteLLM (gateway only), LangSmith (observability only), Opik (observability only).

[Original](https://github.com/tensorzero/tensorzero) → GitHub
