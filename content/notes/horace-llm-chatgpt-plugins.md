---
title: "Horace: Self-Hosted LLM Chatbot with ChatGPT Plugin Support"
date: 2023-04-08
categories:
  - llm
  - chatgpt-plugins
  - chatbot
  - open-source
  - tool-use
description: Horace is an open-source LLM chatbot server that supports ChatGPT plugins — letting you run a self-hosted chatbot that can use the growing ecosystem of ChatGPT plugin tools. An early attempt to bring plugin-based tool use outside of OpenAI's walled garden.
params:
  source: pinboard
  sourceUrl: https://github.com/artmatsak/horace
---

![Horace: Self-Hosted LLM Chatbot with ChatGPT Plugin Support](/images/notes/horace-llm-chatgpt-plugins.png)

## Summary

Horace is an open-source LLM chatbot server that implements the ChatGPT plugins protocol, allowing it to use tools and services built for OpenAI's plugin ecosystem. When ChatGPT plugins launched in early 2023, the plugin interface became a de facto standard for extending LLM chatbots with external tools — but the plugins only worked inside ChatGPT Plus. Horace was an early attempt to make that plugin ecosystem accessible from a self-hosted chatbot.

The architectural idea: the ChatGPT plugins protocol is an open specification (plugins are just REST APIs with a manifest file). If a self-hosted LLM server implements the client side of that protocol, it can consume any plugin without routing through OpenAI. Horace built this client layer, enabling users to connect tools like web browsing, code execution, and search plugins to their own LLM deployments.

In retrospect, Horace represents an early form of the tool-use standardization problem that took years to resolve. ChatGPT plugins never became the universal standard — they were shut down in 2024 in favor of GPTs and OpenAI Assistants. The underlying insight proved correct: LLMs need standardized tool interfaces. MCP (Model Context Protocol from Anthropic) eventually provided this in a more principled way in late 2024.

## Key points

- Self-hosted LLM chatbot server that implements the ChatGPT plugins protocol on the client side.
- Enables tool use from outside OpenAI's platform — run plugins without ChatGPT Plus.
- ChatGPT plugins are REST APIs with a manifest — the protocol is open and implementable.
- Early (2023) attempt at LLM tool-use standardization; ChatGPT plugins themselves were deprecated in 2024.
- The problem it addresses — standard interfaces for LLM tools — was later solved by MCP.
- Historical artifact: shows the standardization pressure that eventually produced MCP and OpenAI Assistants.

[Original](https://github.com/artmatsak/horace) → GitHub
