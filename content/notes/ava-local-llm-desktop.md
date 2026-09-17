---
title: "Ava: All-in-One Desktop App for Running LLMs Locally"
date: 2023-12-09
categories:
  - llm
  - local-ai
  - desktop-app
  - privacy
  - open-source
description: Ava is an all-in-one desktop app for running LLMs locally — chat, image generation, and model management in a single native application. An alternative to LM Studio targeting users who want everything bundled together without CLI setup.
params:
  source: pinboard
  sourceUrl: https://github.com/cztomsik/ava
---

![Ava: All-in-One Desktop App for Running LLMs Locally](/images/notes/ava-local-llm-desktop.png)

## Summary

Ava is a desktop application for running LLMs locally, positioned as an all-in-one tool that bundles chat, model management, and other AI capabilities without requiring any command-line setup. It targets users who want local AI capabilities but don't want to configure llama.cpp, Ollama, or LM Studio manually.

The local LLM desktop app space was crowded in late 2023: LM Studio, GPT4All, Jan, and several others competed for the same audience — people who wanted ChatGPT-like functionality without sending data to the cloud. The differentiators were model library breadth, UI quality, performance tuning, and bundled features (image generation, embeddings, API serving). Ava added image generation alongside text generation, which some competitors lacked.

The technical architecture for all these tools is similar: a native shell around llama.cpp (for CPU/GPU inference of GGUF quantized models) with a web-based UI, model download management from Hugging Face or a curated library, and optional local REST API serving for connecting to other apps. The differentiation is mostly UX and what batteries are included.

## Key points

- Desktop app wrapping llama.cpp for local GGUF model inference — no cloud, no API keys.
- Bundles text generation and image generation in one application.
- Targets non-technical users who want local AI without CLI configuration.
- Written in TypeScript/Zig — lightweight native wrapper around inference backends.
- Competes with LM Studio, Jan, GPT4All in the local AI desktop app space.
- Privacy: all inference local, nothing sent externally.

[Original](https://github.com/cztomsik/ava) → GitHub
