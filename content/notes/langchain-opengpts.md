---
title: "OpenGPTs: Open-Source Custom AI Assistants"
date: 2023-11-12
categories:
  - llm
  - agents
  - langchain
  - open-source
  - chatbot
description: OpenGPTs is LangChain's open-source alternative to OpenAI's GPT builder — create custom AI assistants with configurable tools, instructions, and memory backends. Released the same week as OpenAI's GPT Store announcement.
params:
  source: pinboard
  sourceUrl: https://github.com/langchain-ai/opengpts
---

![OpenGPTs: Open-Source Custom AI Assistants](/images/notes/langchain-opengpts.png)

## Summary

OpenGPTs is LangChain's open-source response to OpenAI's GPT builder — released the same week in November 2023 when OpenAI announced custom GPTs at DevDay. Where OpenAI's product locked you into their platform and models, OpenGPTs is self-hostable and model-agnostic.

The feature set mirrors what OpenAI offered: create custom assistants with specific instructions (system prompts), tool integrations (web search, code execution, custom APIs), knowledge files (RAG over uploaded documents), and persistent memory. But you can run it on any LLM — Anthropic, Mistral, local models via Ollama — and deploy it on your own infrastructure.

OpenGPTs sits on top of LangGraph and LangChain, using their agent and tool abstractions. The memory backend is pluggable (Redis, PostgreSQL). The full-stack includes a Next.js frontend, FastAPI backend, and the LangChain agent runtime — more infrastructure than a typical toy project, reflecting LangChain's production-oriented positioning.

## Key points

- Self-hostable alternative to OpenAI GPT builder — model-agnostic, runs on any LLM.
- Configurable tools: web search, code execution, custom APIs, RAG over uploaded files.
- Built on LangGraph — uses graph-based agent execution model.
- Next.js frontend + FastAPI backend + LangChain agent runtime.
- Pluggable memory backends: Redis, PostgreSQL.
- Released in direct response to OpenAI DevDay 2023 GPT Store announcement.

[Original](https://github.com/langchain-ai/opengpts) → GitHub
