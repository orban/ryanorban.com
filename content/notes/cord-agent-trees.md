---
title: "Cord: dynamic task trees for coordinating AI agents"
date: 2026-02-21
categories:
  - ai-agents
  - orchestration
  - mcp
  - multi-agent
description: Cord is a framework for dynamic task trees of AI agents — agents decompose goals into subtasks at runtime, not at design time. Built on five MCP primitives with spawn/fork context primitives for controlling information flow between agents.
params:
  source: pinboard
  sourceUrl: https://www.june.kim/cord
---

![Cord: dynamic task trees for coordinating AI agents](/images/notes/cord-agent-trees.png)

## Summary

Cord is a multi-agent orchestration framework that lets agents decompose complex goals into hierarchical task trees at runtime — not at design time. The problem it solves is real: most agent orchestration frameworks require you to pre-define the workflow graph. Cord flips this, letting the first agent read a goal and dynamically decide "I need to do research before I can answer this," then spawn subtasks for each step it identifies.

The framework introduces two primitives for context flow that address a subtle but important problem in multi-agent coordination. Spawn gives child agents only their specific prompt and the results of explicitly declared dependencies — clean isolation. Fork gives child agents all completed sibling results, enabling context-aware work where downstream agents can see what predecessors found. Choosing between them is a design decision about how much context downstream agents should inherit.

The implementation is five core MCP tools managing task creation, human interaction, and tree visibility. The system handles dependency resolution, parallel execution, and sequential blocking based on task prerequisites. The proof of concept runs on Claude Code CLI with SQLite, but the protocol is technology-agnostic. This is the same design territory as [AgentFlow](/notes/agentflow/) and Baton, but Cord's distinguishing feature is runtime decomposition rather than pre-defined graphs.

## Key points

- Runtime task decomposition: agents decide their own subtask structure rather than following a pre-defined graph.
- **Spawn** = clean context isolation; **Fork** = full sibling context inheritance — two explicit primitives for controlling information flow.
- Five MCP tools manage the full protocol: task creation, dependency resolution, human interaction, tree visibility.
- Handles parallelism and sequential blocking automatically based on declared dependencies.
- Protocol is framework-agnostic; proof of concept uses Claude Code + SQLite.

[Original](https://www.june.kim/cord)
