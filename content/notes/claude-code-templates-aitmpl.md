---
title: "Claude Code Templates (aitmpl.com): marketplace for Claude Code components"
date: 2026-02-10
categories:
  - claude-code
  - developer-tools
  - templates
  - open-source
description: Claude Code Templates is a CLI tool and marketplace (aitmpl.com) for installing agents, commands, hooks, MCPs, and settings into Claude Code. 100+ pre-built components installable with a single npx command.
params:
  source: pinboard
  sourceUrl: https://github.com/davila7/claude-code-templates
---

![Claude Code Templates (aitmpl.com): marketplace for Claude Code components](/images/notes/claude-code-templates-aitmpl.png)

## Summary

Claude Code Templates by davila7 is a CLI tool and accompanying marketplace at aitmpl.com for installing pre-built components into Claude Code. The components span the full range of Claude Code extensibility: AI agents (specialized domain experts like security auditors or React performance optimizers), custom slash commands, MCP integrations with external services (GitHub, PostgreSQL, Stripe, AWS), settings configurations, hooks for automation triggers, and skills for reusable capabilities.

Installation works via `npx claude-code-templates@latest` — either interactively or with specific flags. You can install a complete development stack in one command. The marketplace at aitmpl.com has a web interface with 100+ components, trending sections, and a Stack Builder for curating custom combinations before installing. The same project runs the aitmpl.com/skills URL as a browsable skills directory.

The project includes a Claude Code Analytics tool for monitoring agent sessions in real-time — live state detection and performance metrics. It's sponsored by Z.AI and is part of the Claude for Open Source program. Related to but distinct from the official Claude Code marketplace — this is community-developed, not Anthropic's own component registry.

## Key points

- CLI (`npx claude-code-templates`) + aitmpl.com marketplace for Claude Code components.
- Components: agents, commands, MCP integrations, settings, hooks, skills.
- 100+ pre-built components, installable in one command.
- Stack Builder lets you curate multi-component installs before running.
- Also includes Claude Code Analytics for session monitoring.
- Community-built; not the official Claude Code marketplace.

[Original](https://github.com/davila7/claude-code-templates)
