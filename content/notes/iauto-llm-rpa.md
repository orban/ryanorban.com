---
title: "iauto: Low-Code LLM + RPA Automation Engine"
date: 2024-02-26
categories:
  - rpa
  - llm
  - automation
  - multi-agent
  - open-source
description: iauto is a low-code automation engine that combines LLMs with RPA tools (Appium, Playwright) in YAML-defined workflows. Bridges AI reasoning with traditional robotic process automation for adaptive task execution.
params:
  source: pinboard
  sourceUrl: https://github.com/shellc/iauto
---

![iauto: Low-Code LLM + RPA Automation Engine](/images/notes/iauto-llm-rpa.png)

## Summary

iauto is a low-code engine that bridges LLM reasoning with robotic process automation (RPA) by combining both in YAML-defined agent workflows. Traditional RPA tools like Appium and Playwright handle deterministic interaction sequences well but break on unexpected UI states. LLMs add adaptive reasoning. iauto wires them together so agents can make decisions and then execute them through controlled browser or app interactions.

Workflows are defined in YAML rather than code, which lowers the entry barrier for people who know automation concepts but aren't deep programmers. The Python API is available for extension. The multi-agent support comes via AutoGen, allowing collaborative agent workflows where multiple specialized agents hand off tasks.

LLM support includes both cloud models and local models via llama.cpp, which matters for automation workflows involving sensitive documents or internal systems where external API calls are undesirable.

## Key points

- Combines LLM reasoning with RPA frameworks (Appium for mobile, Playwright for web).
- YAML-based workflow definition — low-code, no deep programming required.
- Multi-agent support via AutoGen for collaborative automation pipelines.
- Local LLM support via llama.cpp — runs without external API calls.
- Python API for extensibility beyond YAML configuration.
- Fills the gap between pure RPA (rigid) and pure LLM agents (no UI interaction layer).

[Original](https://github.com/shellc/iauto) → GitHub, AI agent
