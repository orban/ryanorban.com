---
title: "Claw-Code: cleanroom agent harness reimplementation in Rust"
date: 2026-04-01
categories:
  - rust
  - ai-agents
  - reverse-engineering
  - open-source
description: Cleanroom Rust reimplementation of an AI agent harness, built from reverse-engineered architecture. Hit 50K GitHub stars in 2 hours.
params:
  source: pinboard
  sourceUrl: https://github.com/instructkr/claw-code
---

![Claw-Code: cleanroom agent harness reimplementation in Rust](/images/notes/claw-code.png)

## Summary

[Claw-Code](/notes/claw-code/) is a cleanroom reimplementation of an AI agent harness system, written primarily in Rust (93%) with Python components. Rather than distributing leaked source code, the maintainers reverse-engineered the architectural patterns and rebuilt from scratch using AI-assisted development tools like oh-my-codex to scaffold the work across multiple Rust crates.

The project provides infrastructure for building AI agent workflows with tool orchestration, command systems, and plugin support. It covers API clients, runtime state management, and interactive CLI interfaces — essentially the plumbing needed to build something like Claude Code or similar agent harnesses.

It became the fastest repository in GitHub history to hit 50K stars, reaching the milestone just 2 hours after publication. The speed reflects both the community's appetite for open agent infrastructure and the controversy around how the architectural knowledge was obtained.

## Key points

- Cleanroom Rust reimplementation — not a fork or copy of leaked source, but a ground-up rebuild from reverse-engineered architecture.
- Covers the full agent harness stack: API clients, runtime state, tool orchestration, command systems, plugin support, and interactive CLI.
- Built using AI agents (oh-my-codex) to assist with the porting work across multiple Rust crates.
- Hit 50K GitHub stars in 2 hours, making it the fastest repo to reach that milestone.
- Written in Rust (93%) with Python (7%) components.

[Original](https://github.com/instructkr/claw-code)
