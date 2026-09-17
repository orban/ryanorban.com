---
title: "Par: Parallel Worktree and Session Manager"
date: 2025-08-22
categories:
  - developer-tools
  - git
  - git-worktrees
  - tmux
  - ai-agents
  - cli
description: Par is a CLI that combines git worktrees with tmux sessions to manage parallel development workstreams — each task gets an isolated directory and persistent terminal. Built for concurrent AI-assisted development where multiple agents run simultaneously.
params:
  source: pinboard
  sourceUrl: https://github.com/coplane/par
---

![Par: Parallel Worktree and Session Manager](/images/notes/par-parallel-worktree-manager.png)

## Summary

Par is a CLI tool that manages parallel development by combining git worktrees with tmux sessions. Each development task gets an isolated directory (via git worktree) and a persistent background terminal session (via tmux), and Par provides a unified interface to create, list, and control these environments from anywhere on the system. The motivation is that traditional branch switching is "not ideal for handling multiple concurrent workstreams on the same repository."

The tool directly addresses the workflow of concurrent AI agent development — when running multiple agents in parallel on different tasks, you need isolation between workstreams and persistent terminal environments where agents can operate in the background. Git worktrees provide the filesystem isolation; tmux provides the session persistence; Par manages both together.

Feature highlights: VSCode and Cursor integration for multi-repo editing, `.par.yaml` configuration for automatic environment initialization, and bulk command execution across all sessions simultaneously. Multi-repository workspaces let full-stack features spanning multiple codebases be managed as a single logical unit.

## Key points

- Git worktree + tmux + unified CLI = isolated parallel development environments.
- Persistent background terminal sessions: agents run without blocking your main terminal.
- `.par.yaml` configuration for automatic environment setup when creating sessions.
- VSCode and Cursor integration for multi-repo editing.
- Bulk command execution across all active sessions.
- Built for concurrent AI agent development and full-stack multi-repo feature work.

[Original](https://github.com/coplane/par) → GitHub
