---
title: "CCPM: Spec-Driven Project Management for Claude Code"
date: 2025-08-20
categories:
  - claude-code
  - ai-agents
  - project-management
  - github
  - git-worktrees
description: CCPM is an agent skill that orchestrates spec-driven software development using GitHub Issues as project state and git worktrees for parallel agent execution, reducing wall time 5x by running independent tasks simultaneously. The anti-vibe-coding project manager.
params:
  source: pinboard
  sourceUrl: https://github.com/automazeio/ccpm
---

![CCPM: Spec-Driven Project Management for Claude Code](/images/notes/ccpm-claude-code-project-management.png)

## Summary

CCPM (Claude Code Project Management) is an agent SKILL that implements a structured, specification-driven development workflow for Claude Code, using GitHub Issues as the source of truth and git worktrees for parallel agent execution. The fundamental principle is that "every line of code must trace back to a specification" — an explicit rejection of ad-hoc AI-assisted development.

The workflow is five-phase: brainstorm → document (PRDs) → plan (technical epics → granular issues) → execute (parallel agents) → track (GitHub Issues as audit trail). The parallel execution innovation is the key performance gain: CCPM analyzes the dependency graph of open issues, identifies independent work streams, and launches multiple agents simultaneously in isolated git worktrees. The result is reportedly 5x reduction in wall time when scaling from 1 to 5 agents.

GitHub Issues serve as the persistent context mechanism between sessions — issue comments record decisions, agent handoffs, and progress without requiring the agent to hold state in memory. Local `.claude/` directories store PRDs, epics, and task files as plain markdown, synchronized with GitHub issue numbers. This creates a coherent project state visible to both humans and agents.

## Key points

- Five-phase workflow: brainstorm → PRD → epics → parallel execution → GitHub tracking.
- Git worktrees for parallel agent execution — isolated branches, no conflicts.
- 5x wall time reduction reported when scaling from 1 to 5 agents.
- GitHub Issues as persistent context: audit trail, handoffs, progress tracking.
- Spec-first principle: every code change traces to an issue/PRD.
- Works as a Claude Code agent skill — not a separate tool.

[Original](https://github.com/automazeio/ccpm) → AI agent
