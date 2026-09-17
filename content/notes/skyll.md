---
title: "Skyll: runtime skill discovery for AI agents"
date: 2026-02-03
categories:
  - ai-agents
  - skills
  - mcp
  - open-source
  - runtime-discovery
description: Skyll is a REST API and MCP server that lets any AI agent discover and learn skills at runtime, without pre-installation. Aggregates SKILL.md files from GitHub and returns structured JSON for context injection.
params:
  source: pinboard
  sourceUrl: https://github.com/assafelovic/skyll
---

![Skyll: runtime skill discovery for AI agents](/images/notes/skyll.png)

## Summary

[Skyll](/notes/skyll/) is a REST API and MCP server that enables AI agents to discover and load agent skills at runtime, without requiring any pre-installation. It aggregates SKILL.md files from GitHub sources, fetches full content, and returns structured JSON ready for context injection. Any agent that can call an API can now access skills from any source — including the AgentSkills.io registry and community repos.

The problem it solves is distribution friction. Claude Code skills work well for developers who already know which skills they need and install them manually before a session. But agents can't anticipate which skills they'll need for arbitrary tasks. [Skyll](/notes/skyll/) flips the model: agents can query the registry during a session, read about available skills, and pull in the ones relevant to the task at hand. No human has to know what skills exist in advance.

The MCP interface means this works with Claude Code, Cursor, Codex, and any other MCP-compatible tool without modification. There's also a PyPI package for Python agents that don't use MCP. Combined with AgentSkills.io's open format, [Skyll](/notes/skyll/) forms the discovery and delivery layer for a skill ecosystem that could span multiple agent platforms.

## Key points

- MCP server and REST API for discovering and loading agent skills at runtime.
- No pre-installation required — agents query and pull skills during a session.
- Fetches SKILL.md content from GitHub and serves structured JSON for context injection.
- Works with Claude Code, Cursor, Codex, and any MCP-compatible tool.
- PyPI package available for Python agents without MCP support.
- Pairs with AgentSkills.io as the format standard; [Skyll](/notes/skyll/) handles discovery and delivery.

[Original](https://github.com/assafelovic/skyll)
