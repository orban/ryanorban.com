---
title: "Dalai: Run LLaMA Locally with One Command"
date: 2023-03-13
categories:
  - llm
  - llama
  - local-llm
  - developer-tools
  - open-source
description: Dalai is a one-command installer for running LLaMA models locally — npm install to set up, then query models via CLI or socket server. One of the first tools to make local LLM inference accessible to developers without ML expertise.
params:
  source: pinboard
  sourceUrl: https://github.com/cocktailpeanut/dalai
---

![Dalai: Run LLaMA Locally with One Command](/images/notes/dalai-llama-local-runner.png)

## Summary

Dalai by cocktailpeanut made running LLaMA models locally as simple as `npx dalai llama` — a single command that downloads, quantizes, and sets up a LLaMA model, then starts a local server with a web UI and socket API. No Python environment setup, no CUDA configuration, no manual weight conversion. Just `npm` and a working model in minutes.

The approach was deliberately developer-friendly: Node.js as the runtime (ubiquitous, no separate install), a clean web interface for interactive chat, and a Socket.IO API for building applications against the local model. Dalai wrapped llama.cpp under the hood — Georgi Gerganov's C++ implementation that enabled CPU inference on consumer hardware — making the hard part invisible.

In March 2023, running an LLM locally required significant technical SKILL: cloning repos, installing Python dependencies, converting model formats, understanding quantization. Dalai compressed that into one command, opening local LLM access to the much larger population of Node.js developers. It was part of the same wave as Ollama (which later became the dominant local runner) but predated it by nearly a year.

## Key points

- One `npx` command installs, quantizes, and starts a LLaMA local server — no ML environment setup.
- Wraps llama.cpp for CPU inference — runs on consumer hardware without CUDA.
- Node.js-based with Socket.IO API — accessible to web developers without ML background.
- Web UI included for interactive chat; socket API for building applications.
- Early entrant in local LLM runners — predates Ollama by ~9 months; same democratization goal.

[Original](https://github.com/cocktailpeanut/dalai) → GitHub
