---
title: "amla-sandbox: WASM capability sandbox for AI agents"
date: 2026-01-30
categories:
  - ai-agents
  - security
  - sandbox
  - wasm
  - developer-tools
description: amla-sandbox is a WASM sandbox with capability enforcement for AI coding agents — no Docker, no VM, one binary. Agents can only call explicitly provided tools. Addresses the arbitrary code execution risk in most agent frameworks.
params:
  source: pinboard
  sourceUrl: https://github.com/amlalabs/amla-sandbox
---

![amla-sandbox: WASM capability sandbox for AI agents](/images/notes/amla-sandbox.png)

## Summary

[amla-sandbox](/notes/amla-sandbox/) is a WebAssembly (WASM) sandbox that enforces strict capability limits for AI agents executing code. The security case it makes is pointed: most popular agent frameworks run LLM-generated code via `subprocess` or `exec()` — that's arbitrary code execution on your host machine. LangChain has a CVE for it ([CVE-2025-68664](https://github.com/advisories/GHSA-c67j-w6g6-q2cm)). AutoGen uses `subprocess.run()`. SWE-Agent uses `subprocess.run(["bash", ...])`. One prompt injection and you're done.

The WASM approach provides a sandboxed virtual filesystem with no network access and no shell escape — agents can only call tools you explicitly provide with constraints you define. Unlike Docker-based isolation (used by OpenHands, AutoGen), no Docker daemon is required. No VM either. One binary, works everywhere.

The API is clean: `create_sandbox_tool()` takes a list of allowed tools and returns a sandbox that agents write single scripts against, rather than making many sequential tool calls. It supports JavaScript, Python, and shell-pipeline execution within the sandbox.

## Key points

- WASM sandbox with capability enforcement — agents can only access explicitly granted tools.
- No network, no shell escape, sandboxed virtual filesystem.
- Addresses arbitrary code execution risk in LangChain, AutoGen, and SWE-Agent.
- No Docker, no VM — single binary, cross-platform.
- Agents write scripts against defined tools; `create_sandbox_tool()` is the main API.
- Lighter-weight isolation than container-based approaches while providing stronger guarantees than `exec()`.

[Original](https://github.com/amlalabs/amla-sandbox)
