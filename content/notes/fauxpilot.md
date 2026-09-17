---
title: "FauxPilot: Open-Source GitHub Copilot Server"
date: 2022-08-03
categories:
  - code-generation
  - open-source
  - github-copilot
  - llm
  - self-hosted
description: FauxPilot is an open-source, self-hosted alternative to GitHub Copilot that runs Salesforce's CodeGen models locally via Triton Inference Server. Built in response to privacy concerns about Copilot sending code to OpenAI's servers.
params:
  source: pinboard
  sourceUrl: https://github.com/moyix/fauxpilot
---

## Summary

[FauxPilot](/notes/fauxpilot/) (github.com/moyix/fauxpilot) is an open-source, self-hostable alternative to GitHub Copilot built by Brendan Dolan-Gavitt (moyix). It runs Salesforce's CodeGen models through NVIDIA Triton Inference Server and exposes a Copilot-compatible API, so you can point the official Copilot VS Code extension at your own server instead of OpenAI's infrastructure.

The motivation was straightforward: GitHub Copilot sends your code to OpenAI's servers for every completion. For engineers at companies with IP concerns, regulated industries, or air-gapped environments, this is a non-starter. [FauxPilot](/notes/fauxpilot/) let those teams run an equivalent tool on their own hardware. The CodeGen models it used (1B, 2B, 6B, 16B parameters from Salesforce Research) were state-of-the-art code completion models available as open weights.

FauxPilot was one of the first meaningful self-hosted Copilot alternatives. It appeared before Tabby, Continue.dev, or Ollama made the experience turnkey. The setup was non-trivial — you needed a GPU server, NVIDIA's Triton container, and some configuration — but it worked. In retrospect it's an early datapoint in the broader trend of open-weight code models enabling private, on-premise AI coding assistance that has since matured significantly.

## Key points

- Self-hosted GitHub Copilot alternative — routes completions to your own server instead of OpenAI
- Uses Salesforce CodeGen models: 1B, 2B, 6B, or 16B parameters; all open weights
- Runs via NVIDIA Triton Inference Server for high-throughput inference
- Exposes Copilot-compatible API — works with the official VS Code extension without modification
- Privacy/IP motivation: code never leaves your infrastructure
- Precursor to the current ecosystem: Tabby, Continue.dev, Ollama + code models

[Original](https://github.com/moyix/fauxpilot)
