---
title: "AgentSkills.io: open format for agent capabilities"
date: 2026-02-03
categories:
  - ai-agents
  - skills
  - open-format
  - developer-tools
description: AgentSkills.io is a simple open format for giving AI agents new capabilities and expertise — a registry and spec for agent skill files. Makes skills portable and discoverable across agent frameworks.
params:
  source: pinboard
  sourceUrl: https://agentskills.io/home
---

![AgentSkills.io: open format for agent capabilities](/images/notes/agentskills.png)

## Summary

AgentSkills.io is a registry and specification for agent skills — a simple, open format for extending what AI agents can do. The concept maps directly to what Claude Code calls skills (SKILL.md files), but positioned as a cross-framework standard rather than tool-specific. Any agent that implements the format can discover and use skills from the registry.

This connects to [Skyll](/notes/skyll/) (assafelovic/skyll), a complementary project that is an MCP server for discovering skills at runtime. Both are working on the same problem: agent capabilities shouldn't require manual installation before a session, and skills should be discoverable across frameworks rather than siloed in specific tools.

The open format approach is significant. Right now, skills and prompts that extend coding agents are scattered across GitHub repos, individual CLAUDE.md files, and tool-specific marketplaces. A shared spec creates the possibility of a skill working in Claude Code, Cursor, Codex, and OpenCode without adaptation.

## Key points

- Open format for agent skills — capabilities defined in a portable spec, not tool-specific configuration.
- Cross-framework: skills should work across Claude Code, Cursor, Codex, and other AI coding agents.
- Registry model: skills are discoverable rather than requiring prior knowledge or manual installation.
- Complements [Skyll](/notes/skyll/) (runtime skill discovery via MCP) in the skill portability ecosystem.
- Addresses fragmentation: agent capabilities currently siloed per tool or scattered across GitHub.

[Original](https://agentskills.io/home)
