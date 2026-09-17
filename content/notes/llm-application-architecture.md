---
title: The Architecture of Today's LLM Applications
date: 2023-11-19
categories:
  - llm
  - architecture
  - applications
  - rag
  - reference
description: GitHub's overview of LLM application architecture patterns as of late 2023 — the standard components (inference, context, orchestration, state, tools) and how they fit together. A useful snapshot of the consensus architecture before it fragmented into frameworks.
params:
  source: pinboard
  sourceUrl: https://github.blog/2023-10-30-the-architecture-of-todays-llm-applications/
---

![The Architecture of Today's LLM Applications](/images/notes/llm-application-architecture.png)

## Summary

This GitHub blog post from October 2023 maps the architecture of LLM applications at the inflection point when the patterns were solidifying but hadn't yet fragmented into a hundred competing frameworks. It describes five layers that compose most LLM applications: the inference model itself, context management (what you feed the model), orchestration (how you chain calls), state (memory and persistence), and tools (external API access).

The post is valuable as a historical document: this was the moment when RAG, chain-of-thought, function calling, and agent patterns were being synthesized into a coherent architectural vocabulary. LangChain, LlamaIndex, and AutoGPT had established these concepts; the post codifies what practitioners had assembled empirically.

The five-layer breakdown still holds: you need an inference provider (OpenAI, Anthropic, local), a way to inject relevant context (RAG or few-shot examples), orchestration logic (a framework or custom code to chain calls), state persistence (conversation history, user memory), and tool integrations (web search, code execution, databases). The complexity lives in how these interact.

## Key points

- Five architectural layers: inference, context, orchestration, state, tools.
- RAG is the dominant context injection pattern; few-shot examples are the alternative.
- Function calling / tool use is the interface between LLMs and external systems.
- State management (conversation history, user memory) is the layer most teams underinvest in.
- Frameworks like LangChain and LlamaIndex abstract orchestration but add their own complexity.
- Published before the AI agent framework proliferation of 2024 — a cleaner moment to read the map.

[Original](https://github.blog/2023-10-30-the-architecture-of-todays-llm-applications/) → GitHub
