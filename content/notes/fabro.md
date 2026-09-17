---
title: "Fabro: AI agent workflow graph orchestrator"
date: 2026-03-18
categories:
  - ai-agents
  - workflow
  - rust
  - developer-tools
  - open-source
description: Fabro defines AI agent workflows as Graphviz DOT graphs with git checkpointing, cloud sandboxes, and human-in-the-loop gates. It occupies the space between micromanaging an agent line-by-line and blindly accepting a 500-line diff.
params:
  source: pinboard
  sourceUrl: https://github.com/fabro-sh/fabro
---

![Fabro: AI agent workflow graph orchestrator](/images/notes/fabro.png)

## Summary

[Fabro](/notes/fabro/) is an open-source framework for defining AI agent workflows as directed graphs using Graphviz DOT notation. The core design philosophy is to solve the micromanagement problem: you don't want to babysit an agent step-by-step, but you also don't want to accept a 500-line diff you can't audit. Fabro lets you define the process as a graph, let agents execute it, and intervene only at gates you designate in advance.

Workflows are declared in DOT notation as nodes (tasks like planning, implementation, review) connected by edges (transitions). You can define branching, loops, and human approval gates, and version-control the whole thing as a source file. Each stage can be assigned a different model via CSS-like routing rules, so you can use a cheap fast model for planning and a more capable one for implementation. Agents run in isolated cloud sandboxes with configurable network and filesystem access, and every stage gets a git checkpoint for complete traceability.

It ships as a single Rust binary with no dependencies, plus a REST API with SSE streaming and a React web UI for programmatic access. The automatic retrospectives — cost, duration, changes per stage — give you data to optimize future runs. SSH access into live sandboxes lets you debug what's actually happening inside an agent's execution environment.

## Key points

- Workflow graphs in Graphviz DOT notation — version-controllable, branchable, and composable with standard git tooling.
- CSS-like model routing: assign different LLMs to different stages within a single workflow.
- Git checkpointing at each stage for complete traceability and rollback.
- Human-in-the-loop gates: predefined intervention points without requiring real-time babysitting.
- Single compiled Rust binary, zero dependencies — unusually easy to install and run.

[Original](https://github.com/fabro-sh/fabro)
