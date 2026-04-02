---
title: "IronClaw: secure personal AI assistant from NEAR AI"
date: 2026-02-13
categories:
  - ai-agents
  - security
  - privacy
  - open-source
  - rust
description: IronClaw is a privacy-focused personal AI assistant from NEAR AI, implemented in Rust with WASM sandboxing for untrusted tools, credential protection at the host boundary, and hybrid search memory. Your data never leaves your control.
params:
  source: pinboard
  sourceUrl: https://github.com/nearai/ironclaw
---

![IronClaw: secure personal AI assistant from NEAR AI](/images/notes/ironclaw.png)

## Summary

[IronClaw](/notes/ironclaw/) is an OpenClaw-inspired personal AI assistant from NEAR AI, rewritten in Rust with privacy and security as the primary design goals. The core philosophy: your AI assistant should work for you, not harvest your data. Everything is stored locally and encrypted; there's no telemetry or data collection.

The security architecture is layered. Untrusted tools run in isolated WebAssembly (WASM) containers with capability-based permissions — a tool can only access what it's explicitly granted. Credentials are never exposed to tools; they're injected at the host boundary with leak detection, so a compromised tool can't steal your API keys. HTTP requests are restricted to an explicit allowlist. Prompt injection gets multiple defenses: pattern detection, content sanitization, and policy enforcement.

The memory system uses hybrid full-text and vector search with Reciprocal Rank Fusion — the same retrieval approach used by more specialized tools like [Remind](/notes/remind/). [IronClaw](/notes/ironclaw/) goes further with a workspace filesystem for structured storage (notes, logs, context) and identity files that maintain personality and preferences across sessions. New tools can be built dynamically: describe what you need and the assistant builds it as a WASM tool at runtime. MCP protocol support extends capabilities further.

## Key points

- Privacy-first: all data stored locally and encrypted, no telemetry.
- WASM sandbox for untrusted tools with capability-based permissions — tools can't access what they're not granted.
- Credentials injected at host boundary with leak detection — never exposed inside the VM.
- Hybrid search memory (full-text + vector with Reciprocal Rank Fusion) + workspace filesystem.
- Dynamic tool building: describe what you need, [IronClaw](/notes/ironclaw/) builds a WASM tool at runtime.
- MCP protocol support for extending capabilities.
- Written in Rust, MIT OR Apache 2.0 license.

[Original](https://github.com/nearai/ironclaw)
