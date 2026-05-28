---
title: "OpenChat: LLM Custom Chatbot Console"
date: 2023-06-07
categories:
  - llm
  - chatbot
  - open-source
  - rag
  - self-hosting
description: OpenChat is an open-source LLM chatbot console with document ingestion and custom bot creation — an early self-hosted alternative to ChatGPT for teams wanting to deploy domain-specific chatbots over their own data.
params:
  source: pinboard
  sourceUrl: https://github.com/openchatai/OpenChat
---

![OpenChat: LLM Custom Chatbot Console](/images/notes/openchat-llm-chatbot.png)

## Summary

OpenChat by openchatai is an open-source platform for building and deploying custom LLM-powered chatbots — a self-hosted alternative to ChatGPT with document ingestion, bot management, and a chat interface. The core use case: upload your documentation, configure a bot persona and behavior, and give users a chat interface over your specific content rather than the general-purpose model.

The platform functions as a lightweight RAG application with a multi-bot management layer. You can create multiple bots with different document sets and configurations — a customer support bot over your product docs, a technical assistant over your API documentation, an HR bot over your employee handbook. Each bot maintains its own document collection and system prompt.

OpenChat launched in the mid-2023 wave of self-hosted chatbot platforms (alongside AnythingLLM, PrivateGPT, and similar tools) that responded to enterprise demand for ChatGPT-like functionality without sending proprietary data to OpenAI. The platform has a lighter architecture than AnythingLLM — simpler multi-user management — which made it accessible for smaller teams to deploy.

## Key points

- Self-hosted multi-bot platform: create separate bots with different document sets and personas.
- RAG-powered: ingest documents, query against them in chat — not general-purpose LLM conversation.
- Lightweight deployment: simpler than AnythingLLM for single-team or small-scale use cases.
- Part of the 2023 wave responding to enterprise demand for private, self-hosted ChatGPT alternatives.
- Configurable bot behavior: system prompt, temperature, data sources per bot.

[Original](https://github.com/openchatai/OpenChat) → GitHub
