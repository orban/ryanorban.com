---
title: "Augment Intent: coordinator-plus-specialist agent orchestration"
date: 2026-02-06
categories:
  - ai-agents
  - orchestration
  - developer-tools
  - coding-agent
  - living-specs
description: Augment Intent is a desktop app where a coordinator agent breaks tasks into living specs, then delegates to specialist agents working in parallel. The specs stay current as code evolves — avoiding the documentation decay that makes most spec-driven workflows impractical.
params:
  source: pinboard
  sourceUrl: https://www.augmentcode.com/product/intent
---

![Augment Intent: coordinator-plus-specialist agent orchestration](/images/notes/augment-intent.png)

## Summary

[Augment Intent](/notes/augment-intent/) is Augment Code's desktop environment for multi-agent software development, currently in public beta on macOS. The central idea is a coordinator agent that decomposes tasks into "living specifications" — specs that update as code changes, not static documents that rot the moment implementation begins. Specialist agents then work in parallel, each acting on their part of the spec.

The workspace integrates code editing, browser preview, terminal, and Git in a single window, which addresses a real pain point: modern development already requires constant context-switching across too many surfaces. Persistent sessions let developers close the app and resume exactly where they left off. The Context Engine underpinning all agents draws from Augment's existing code intelligence work — the same system that powers their IDE extensions.

What distinguishes Intent from simpler agentic coding tools is the living spec concept. Most spec-driven AI coding workflows degrade because specs drift from reality as agents make changes. Intent's claim is that specs update automatically to reflect what's been done, keeping the coordinator and all downstream agents aligned throughout a session.

## Key points

- Coordinator AI agent breaks tasks into living specifications that stay current as code evolves.
- Specialist agents work in parallel, coordinated through the living spec as a shared source of truth.
- Unified workspace: code editor, browser preview, terminal, Git management in one window.
- Persistent sessions — state survives closing the app and reopening the next day.
- Augment Context Engine gives all agents shared codebase understanding from thousands of sources.
- Flexible model selection: different models for different tasks (e.g., Opus for architecture, Sonnet for iteration).

[Original](https://www.augmentcode.com/product/intent)
