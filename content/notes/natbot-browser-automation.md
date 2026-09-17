---
title: "NatBot: GPT-3-Driven Browser Automation"
date: 2022-10-05
categories:
  - llm
  - browser-automation
  - ai-agents
  - gpt-3
  - open-source
description: NatBot is an early LLM-driven browser automation bot by Nat Friedman — it takes a natural language task, drives a Chromium browser via Playwright, and completes multi-step web tasks. A 2022 proof-of-concept for what later became the AI browser agent category.
params:
  source: pinboard
  sourceUrl: https://github.com/nat/natbot
---

## Summary

NatBot is a browser automation bot built by Nat Friedman (former GitHub CEO) that uses GPT-3 to translate natural language instructions into web interactions. The bot drives Chromium through Playwright, takes screenshots of the current page state, sends those to GPT-3 with a description of the task, and executes the resulting action (click, type, navigate).

The core loop: observe the current page state → describe it textually to the LLM → ask what should I do next? → execute → repeat. NatBot was written in 2022 as a proof-of-concept that GPT-3 had enough world knowledge to navigate real websites without task-specific training. The code is under 200 lines — the simplicity is the point.

Looking back from 2024, NatBot is a historical artifact that anticipated the AI agent browser automation category: Anthropic Claude's computer use, Browser Use, Playwright MCP servers, and commercial products like Adept and MultiOn. The architecture pattern (screenshot → LLM → action) is still at the core of modern computer-use agents, though the execution is now far more sophisticated.

## Key points

- GPT-3 + Playwright loop: screenshot → text description → LLM action → execute.
- Written by Nat Friedman in ~200 lines of Python — deliberately minimal.
- One of the first public demonstrations of LLM-driven browser automation.
- Proof-of-concept that anticipated AI agent browser control by 2+ years.
- Directly ancestral to modern computer-use models and browser agent products.
- Open-source on GitHub.

[Original](https://github.com/nat/natbot)
