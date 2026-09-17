---
title: "zclaw: ESP32-resident AI assistant"
date: 2026-03-03
categories:
  - embedded-systems
  - ai-agents
  - esp32
  - iot
  - open-source
description: zclaw is an AI assistant that runs on an ESP32 microcontroller within a strict 888 KiB firmware budget. Handles natural language scheduling, GPIO control, memory, and tool calling — written in C with ESP-IDF.
params:
  source: pinboard
  sourceUrl: https://zclaw.dev/
---

![zclaw: ESP32-resident AI assistant](/images/notes/zclaw-esp32.png)

## Summary

zclaw is a lightweight AI agent that runs on ESP32 microcontrollers within a strict 888 KiB firmware budget — that's the entire stack, not just the application. Written in C using ESP-IDF and FreeRTOS, it handles natural language commands for embedded automation: scheduling tasks ("Water the plants every day at 8:15), GPIO control (Set GPIO 5 high"), persistent memory of device configurations, and tool calling that maps natural language to executable functions.

The hardware constraint is the interesting design challenge. Running an LLM inference layer on a microcontroller means connecting to remote LLM providers (Anthropic, OpenAI, OpenRouter, Ollama) rather than running models locally. The agent handles the natural language interpretation and tool dispatch; the LLM call goes out over network. The 888 KiB budget covers firmware, FreeRTOS scheduler, ESP-IDF networking stack, and the zclaw application logic.

Interface options include Telegram messaging and an optional web relay. A USB-based recovery plane handles safe mode and local admin functions that work without network connectivity — important for field deployments where the network may be unavailable when you need to recover a misconfigured device.

## Key points

- Entire firmware stack (including FreeRTOS + ESP-IDF) fits in 888 KiB — extreme resource constraint engineering.
- Natural language → GPIO control, scheduling, and tool dispatch on embedded hardware.
- Connects to Anthropic, OpenAI, OpenRouter, or Ollama for LLM inference — no on-device model.
- Telegram interface and web relay as interaction surfaces.
- USB recovery plane for network-independent safe mode — critical for field-deployed embedded systems.

[Original](https://zclaw.dev/)
