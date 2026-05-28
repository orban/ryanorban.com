---
title: "nextjs-chatgpt-app: Open-Source GPT-4 Chat Interface"
date: 2023-03-19
categories:
  - chatgpt
  - next-js
  - react
  - open-source
  - developer-tools
description: An open-source ChatGPT web app built with Next.js and React featuring response streaming, code highlighting, and developer-focused presets — a template for building GPT-4-powered interfaces before this became commoditized.
params:
  source: pinboard
  sourceUrl: https://github.com/enricoros/nextjs-chatgpt-app
---

![nextjs-chatgpt-app: Open-Source GPT-4 Chat Interface](/images/notes/nextjs-chatgpt-app.png)

## Summary

enricoros/nextjs-chatgpt-app is an open-source ChatGPT-style web application built with Next.js, React, and Joy UI (MUI's experimental design library). It connects to the OpenAI API to power GPT-4 conversations, with features aimed at developers: response streaming, syntax-highlighted code blocks, conversation export, and system prompt presets for different use cases.

Released in March 2023 when OpenAI's API was newly accessible and the default ChatGPT interface lacked several features developers wanted, repos like this became popular as starting points. The streaming response rendering was a meaningful improvement over waiting for full completions — making the interface feel significantly faster. Code highlighting made it genuinely useful for programming assistance.

The presets for developers angle positioned it for the audience who needed more control than the consumer ChatGPT offered: custom system prompts, conversation management, and direct API access rather than going through a web interface. This category of open-source GPT-4 chat apps proliferated rapidly in early 2023 — BetterChatGPT, ChatKit, and dozens of similar repos. They're largely obsolete now that ChatGPT has improved and the interface has been commoditized.

## Key points

- Open-source ChatGPT interface with response streaming, code highlighting, and developer system prompt presets.
- Built on Next.js + React + Joy UI — a clean starting point for building OpenAI API-powered apps.
- Released when official ChatGPT lacked streaming UI and developer customization.
- Part of the early 2023 wave of open-source GPT-4 frontends, now largely superseded.
- Demonstrates Server-Sent Events (SSE) streaming with the OpenAI API in a Next.js app.

[Original](https://github.com/enricoros/nextjs-chatgpt-app) → GitHub
