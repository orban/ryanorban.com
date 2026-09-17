---
title: Running local LLMs with Claude Code via Unsloth
date: 2026-03-10
categories:
  - claude-code
  - local-llm
  - llama-cpp
  - developer-tools
  - performance
description: "How to run local LLMs with Claude Code via llama.cpp and Unsloth's GGUF models. The critical fix: Claude Code added an attribution header that breaks KV cache and causes 90% slower inference — must be disabled in settings.json."
params:
  source: pinboard
  sourceUrl: https://unsloth.ai/docs/basics/claude-code
---

![Running local LLMs with Claude Code via Unsloth](/images/notes/unsloth-local-llm-claude-code.png)

## Summary

Unsloth's documentation covers how to run local LLMs through Claude Code by pointing the agent at a local llama.cpp server instead of Anthropic's API. The setup is: install llama.cpp, download a GGUF quantized model (Unsloth recommends models like Qwen3.5-35B or GLM-4.7-Flash), start `llama-server` on port 8001, and set `ANTHROPIC_BASE_URL="http://localhost:8001"` to redirect Claude Code's requests to the local server.

The critical fix documented here is important: Claude Code added an attribution header that breaks KV cache continuity, causing inference to run approximately 90% slower on local models. The fix requires editing `~/.claude/settings.json` to disable the attribution header — setting the environment variable alone doesn't work because the header is injected before the environment is read.

This setup enables fully local, private coding sessions with no cloud dependency. The GGUF quantization format from Unsloth is optimized for inference efficiency, with Q4_K_XL quantization hitting a good balance between quality and memory usage for typical 24GB VRAM setups. The Unsloth fine-tuning pipeline also lets you train specialized models for specific codebases.

## Key points

- Set `ANTHROPIC_BASE_URL="http://localhost:8001"` to redirect Claude Code to a local llama.cpp server.
- Critical: the attribution header introduced to Claude Code breaks KV cache and causes 90% slower local inference — must be disabled in `settings.json`, not just as an env var.
- Unsloth's GGUF models (Q4_K_XL) are recommended for 24GB VRAM systems.
- Enables fully private coding sessions with no API costs.
- Sampling parameters differ by model: Qwen3.5 uses temperature 0.6, GLM-4.7-Flash uses 1.0.

[Original](https://unsloth.ai/docs/basics/claude-code)
