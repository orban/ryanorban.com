---
title: "How to Build an Agent: Minimal Code-Editing Agent in <400 Lines"
date: 2025-07-22
categories:
  - ai-agents
  - developer-tools
  - tutorial
  - coding-agent
  - open-source
description: A practical tutorial showing how to build a fully functional code-editing agent in under 400 lines of code. Worth reading as a minimal reference implementation that strips the problem down to its essential loop.
params:
  source: pinboard
  sourceUrl: https://ampcode.com/how-to-build-an-agent
---

![How to Build an Agent: Minimal Code-Editing Agent in <400 Lines](/images/notes/how-to-build-an-agent.png)

## Summary

This tutorial from Amp Code walks through building a fully functional, code-editing AI agent in under 400 lines. The goal is deliberately minimal: rather than wrapping a framework, the tutorial builds the agent loop from scratch so the reader can see exactly what a functional agent requires and nothing more.

The core loop is simple. An agent is: read the current state, decide what tool to call, call the tool, observe the result, repeat until the task is done. The code-editing version adds: read files, write files, run commands, present results. What makes the tutorial valuable is how little code it takes to get something genuinely useful — the 400-line constraint forces every design decision to earn its place.

This connects directly to how Claude Code and similar agents work. The agent loop Amp describes is structurally identical to what runs inside production coding agents. Understanding the minimal version makes it easier to reason about the design of larger systems. Compare to [AgentFlow](/notes/agentflow/), which scales the same loop to hundreds of parallel agents.

## Key points

- Full code-editing agent in <400 lines — read files, write files, run commands, loop.
- Reveals the essential structure of an agent loop without framework noise.
- The read → decide → act → observe cycle is the same pattern used by Claude Code and production agents.
- Minimal implementation as a learning and reference artifact — not for production use.
- From Amp, a coding agent tool competing in the same space as Claude Code and Cursor.

[Original](https://ampcode.com/how-to-build-an-agent)
