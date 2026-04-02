---
title: "Baton: parallel AI agent orchestration via git worktrees"
date: 2026-04-01
categories:
  - ai-agents
  - developer-tools
  - git-worktrees
  - parallel-development
description: Desktop app for running multiple AI coding agents in parallel using git worktrees. Solves the coordination problem that kills most multi-agent dev workflows.
params:
  source: pinboard
  sourceUrl: https://getbaton.dev/
---

## Summary

Baton is a desktop app that lets you run multiple AI agents (like Claude Code, Gemini CLI, Codex) simultaneously on different features, each in its own git worktree. The core insight is that git worktrees provide natural isolation — each agent gets its own branch and working directory, so they can't step on each other's changes.

The app wraps CLI-native agents with a visual dashboard that shows status badges (input needed, completed, error) for each workspace. You spawn agents in seconds, monitor their progress, review diffs before merging, and manage pull request workflows from one interface. It runs on Mac, Windows, and Linux.

What makes this interesting compared to just running multiple terminal sessions: Baton handles the orchestration overhead. Creating worktrees, assigning branches, tracking which agent is doing what, and coordinating the merge-back are all managed by the app rather than by you juggling terminals.

## Key points

- Uses git worktrees as the isolation primitive — each AI agent gets its own branch and directory, preventing merge conflicts between parallel tasks.
- Supports any agent that runs in a terminal, including Claude Code, Gemini CLI, and Codex.
- Visual dashboard with status tracking replaces the cognitive overhead of managing multiple terminal sessions.
- Handles the full workflow from task assignment through diff review to pull request creation.
- Cross-platform desktop app (Mac, Windows, Linux).

[Original](https://getbaton.dev/)
