---
title: "AgentFlow: dependency graph orchestration for AI agents"
date: 2026-04-01
categories:
  - ai-agents
  - orchestration
  - python
  - developer-tools
description: Orchestrate thousands of AI agents as dependency graphs with parallel fanout and remote execution. Like make/Airflow but for LLM agents.
params:
  source: pinboard
  sourceUrl: https://github.com/shouc/agentflow
---

## Summary

[AgentFlow](/notes/agentflow/) is a Python framework for orchestrating multiple AI agents as dependency graphs. You define agents and their relationships as a DAG (directed acyclic graph), and [AgentFlow](/notes/agentflow/) handles parallel fanout, iterative cycles (write-review-fix loops), and remote execution across SSH, EC2, and ECS.

The framework supports Codex, Claude Code, and Kimi agents out of the box, with the ability to add custom agent types. You can fan out work across files or tasks in parallel, define iterative refinement loops where one agent reviews another's output, and scale execution from local to cloud infrastructure. The README shows systems scaling up to 94-node graphs.

Think of it as Airflow or Make but for LLM agent workflows — you declare what depends on what, and the framework handles scheduling, parallelism, and failure recovery.

## Key points

- Orchestrates AI agents as dependency graphs with parallel fanout, sequential pipelines, and iterative cycles.
- Supports Codex, Claude Code, and Kimi agents natively, with extensible agent types.
- Handles remote execution across SSH, EC2, and ECS for scaling beyond a single machine.
- Iterative refinement loops (write → review → fix) are first-class primitives, not bolted on.
- Written in Python, designed for workflows that go well beyond simple linear agent chains.

[Original](https://github.com/shouc/agentflow)
