---
title: "sandbox-agent: universal sandbox API for coding agents"
date: 2026-02-02
categories:
  - ai-agents
  - sandbox
  - developer-tools
  - open-source
  - universal-api
description: sandbox-agent is a universal API for running coding agents in sandboxes — works with Claude Code, Codex, OpenCode, and Amp with a single interface. Rivet's contribution to the fragmented coding agent sandbox space.
params:
  source: pinboard
  sourceUrl: https://github.com/rivet-dev/sandbox-agent
---

![sandbox-agent: universal sandbox API for coding agents](/images/notes/sandbox-agent.png)

## Summary

[sandbox-agent](/notes/sandbox-agent/) from Rivet provides a unified API for running AI coding agents in sandboxed environments. The supported agents are Claude Code, Codex, OpenCode, and Amp — covering the current major entries in the terminal AI coding agent space. One interface, multiple agent backends.

The problem it addresses is real: each coding agent has different setup requirements, environment assumptions, and invocation patterns. If you want to run multiple agents in automated pipelines — comparing outputs, parallelizing tasks, swapping backends — you currently need to handle each agent's idiosyncrasies separately. [sandbox-agent](/notes/sandbox-agent/) abstracts that away.

Sandbox execution specifically (rather than just a unified API) matters for automated testing, CI/CD integration, and scenarios where you're running agents on untrusted code or tasks. Isolation prevents agents from having unintended side effects on the host system.

## Key points

- Unified API for running Claude Code, Codex, OpenCode, and Amp in sandboxes.
- Abstracts per-agent environment differences — one interface for all backends.
- Sandbox isolation important for automated pipelines, CI/CD, and multi-agent comparison.
- From Rivet, a platform working in the agent infrastructure space.
- Open-source — enables community contribution across multiple agent backends.

[Original](https://github.com/rivet-dev/sandbox-agent)
