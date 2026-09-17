---
title: "Axe: lightweight CLI for single-purpose AI agents"
date: 2026-03-13
categories:
  - ai-agents
  - cli
  - unix-philosophy
  - developer-tools
  - open-source
description: "Axe is a minimal CLI for single-purpose LLM agents defined in TOML — composable like Unix pipes, triggerable from git hooks or cron, supporting Anthropic/OpenAI/Ollama. The anti-chatbot: each agent does one thing."
params:
  source: pinboard
  sourceUrl: https://github.com/jrswab/axe
---

![Axe: lightweight CLI for single-purpose AI agents](/images/notes/axe-agent-cli.png)

## Summary

Axe is a minimal CLI tool for defining and running focused LLM-powered agents using TOML configuration files. The design philosophy is explicit Unix philosophy: each agent does one thing well, agents compose together like Unix pipes, and there's no daemon, GUI, or framework lock-in — just a binary and TOML configs.

Each agent definition includes a system prompt, model selection, skill files, and context. You invoke agents from the terminal, pipe data through them, or trigger them from git hooks and cron jobs. Multiple providers are supported: Anthropic, OpenAI, Ollama, and AWS Bedrock. Agents can delegate to sub-agents via LLM tool use, creating composable chains. Token budgets cap cumulative usage per run.

The persistent memory model is interesting: timestamped Markdown logs carry context across runs. This is simpler than a vector database but practical for most agent use cases — you can review and edit the memory directly since it's just a file. The TOML configs are version-controllable, and built-in tools cover file operations, shell commands, URL fetching, and web search with SSRF protections baked in.

## Key points

- TOML-based agent definitions — version-controllable, minimal, no proprietary format.
- Composable like Unix pipes: pipe data through agents and chain them together.
- Triggerable from git hooks, cron, terminal, or pipelines — fits into existing dev workflows.
- Persistent memory via timestamped Markdown logs — editable and auditable, unlike opaque databases.
- Multi-provider: Anthropic, OpenAI, Ollama, AWS Bedrock.

[Original](https://github.com/jrswab/axe)
