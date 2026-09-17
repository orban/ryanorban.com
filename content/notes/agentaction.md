---
title: "agentaction: Action Chaining and History for LLM Agents"
date: 2023-08-25
categories:
  - ai-agents
  - python
  - open-source
  - tool-use
  - action-history
description: agentaction is a Python library for action chaining and history management in LLM agents — a lightweight abstraction for defining, executing, and tracking sequences of agent actions with persistent history. An early building block for agent frameworks.
params:
  source: pinboard
  sourceUrl: https://github.com/AutonomousResearchGroup/agentaction
---

![agentaction: Action Chaining and History for LLM Agents](/images/notes/agentaction.png)

## Summary

[agentaction](/notes/agentaction/) is a Python library from AutonomousResearchGroup that provides action chaining and history tracking for LLM AI agents. The core abstraction: define actions as functions with typed inputs and outputs, chain them into sequences, and maintain a persistent history of what was called and what returned. This is the plumbing layer that sits underneath higher-level agent frameworks.

The history component is the key differentiator from just calling functions in sequence. [agentaction](/notes/agentaction/) records a log of all actions taken, their inputs, and their outputs in a structured format — creating an auditable, inspectable record that the LLM can reference when deciding what to do next. This addresses a common problem in early AI agent implementations where the agent loses track of what it's already tried, causing infinite loops or repeated failed attempts.

This library is from the same wave of early 2023 agent tooling that produced AutoGPT, LangChain agents, and similar frameworks — DIY building blocks before the major frameworks had stabilized their APIs. The AutonomousResearchGroup was building related infrastructure (agent memory, action history, planning) at a time when these primitives weren't well-covered in existing tools. Many of these early libraries were superseded by more comprehensive frameworks, but they contributed the conceptual vocabulary.

## Key points

- Defines agent actions as typed functions with persistent execution history.
- History log enables the LLM to inspect what was already tried — prevents repeated failures and loops.
- Lightweight plumbing library: lower-level than LangChain agents or AutoGPT.
- From the 2023 wave of DIY AI agent building blocks before framework consolidation.
- Part of AutonomousResearchGroup's suite of agent infrastructure primitives.

[Original](https://github.com/AutonomousResearchGroup/agentaction)
 → GitHub
