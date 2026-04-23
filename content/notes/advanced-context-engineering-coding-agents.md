---
title: Advanced Context Engineering for Coding Agents
date: 2025-09-23
categories:
  - ai-agents
  - context-engineering
  - coding-agents
  - developer-tools
description: A practical guide to making AI coding agents effective in large production codebases through deliberate context management — research/plan/implement phases, 40-60% context utilization, and subagents for isolation. The author shipped 35k LOC in 7 hours using these techniques.
params:
  source: pinboard
  sourceUrl: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md
---

![Advanced Context Engineering for Coding Agents](/images/notes/advanced-context-engineering-coding-agents.png)

## Summary

This guide from HumanLayer addresses a real limitation of AI coding agents: they work well on greenfield projects but can reduce productivity on large, complex production codebases. The thesis is that better outcomes come from deliberate context management rather than waiting for smarter models.

The central technique is splitting work into three phases with explicit context boundaries. **Research**: understand architecture, file locations, information flow — output a detailed map. **Plan**: outline precise implementation steps, testing approaches, and edge cases — output is validated before any code is written. **Implement**: execute the plan phase-by-phase with verification. Keeping context utilization at 40-60% prevents degradation from overfull context windows.

The most counterintuitive insight: **review the plan, not the code**. A bad line in a plan leads to hundreds of bad lines of code. High-leverage human review happens at the planning stage, not the code review stage. Subagents handle search and summarization, keeping the primary agent's context clean for focused execution.

The results are striking: the author contributed to a 300k LOC Rust codebase as a non-expert and shipped 35k LOC of complex features in seven hours through paired work.

## Key points

- Research → Plan → Implement phases with explicit context window boundaries between them.
- Keep context utilization at 40-60% to prevent window degradation.
- Review plans, not code — bad plan lines multiply into bad code lines.
- Subagents for search/summarization keep the primary agent's context focused.
- Works on large production codebases where naive AI agent usage hurts productivity.
- HumanLayer authored; validated against a 300k LOC Rust codebase.

[Original](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) → GitHub
