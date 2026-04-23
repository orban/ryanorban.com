---
title: "Documentor: documentation aggregator for AI assistants"
date: 2025-11-24
categories:
  - developer-tools
  - documentation
  - ai-agents
  - llm
  - open-source
description: Documentor is a tool for aggregating external documentation into a format optimized for LLM consumption — crawling docs sites, building search indexes, and storing structured outputs that AI assistants can query during development work.
params:
  source: pinboard
  sourceUrl: https://github.com/agentsea/documentor
---

![Documentor: documentation aggregator for AI assistants](/images/notes/agentsea-documentor.png)

## Summary

Documentor by AgentSea is a tool for aggregating external documentation and preparing it for consumption by AI assistants and LLM systems. The workflow: a `doc-aggregator` tool spiders documentation sites, stores the content in `docs/external/`, and creates grep indexes and other search structures that AI systems can query during development work.

The problem this solves is well-known to anyone who has used Claude Code or other coding agents: these systems have training data cutoffs and don't have access to the current version of your dependencies' documentation. When you ask Claude to use a new feature of some library, it may hallucinate an API that doesn't exist or miss a new capability it hasn't seen. Documentor creates a local, always-current reference that AI agents can search.

This is a lightweight alternative to MCP-based approaches like Context7 (which fetches docs on demand from a hosted service) — it's a local, self-managed documentation store. The `docs/external/` directory structure means the docs live alongside your code, are auditable, and can be committed to version control so the whole team's AI tools have access to the same reference material.

## Key points

- Crawls external documentation sites and stores them in structured format for AI tool consumption.
- Creates grep indexes optimized for LLM search — not just raw HTML.
- Local approach vs. hosted alternatives like Context7: stays in your repo, auditable.
- Part of AgentSea's ecosystem for agent infrastructure tooling.
- Solves the documentation cutoff problem for AI coding agents working with third-party libraries.
- Committable to version control — consistent docs across the team's AI tooling.

[Original](https://github.com/agentsea/documentor) → GitHub
