---
title: "dmux: parallel AI agents in tmux worktrees"
date: 2026-02-19
categories:
  - ai-agents
  - developer-tools
  - git-worktrees
  - tmux
  - parallel-development
description: dmux lets you run multiple AI coding agents in isolated git worktrees, managing branch/develop/merge cycles in parallel. Another take on the same problem as Baton and cmux, specifically oriented around tmux-based workflows.
params:
  source: pinboard
  sourceUrl: http://dmux.ai/
---

![dmux: parallel AI agents in tmux worktrees](/images/notes/dmux.png)

## Summary

[dmux](/notes/dmux/) is a tool for managing multiple AI coding agents simultaneously, each isolated in its own git worktree. The design premise is simple: git worktrees give you branch isolation without the overhead of cloning the whole repo, and tmux gives you a multi-pane terminal session that can run those agents side by side.

The workflow follows a branch → develop → merge cycle. Each agent works on a separate branch in its own worktree, so parallel tasks can't step on each other's changes. When an agent finishes, you review the diff and merge. This is the same isolation primitive as Baton and [cmux](/notes/cmux/) — all three tools are exploring how tmux-style terminal multiplexing and git worktree isolation compose together as the default environment for parallel development with AI agents.

The difference from Baton is that dmux appears more terminal-native and tmux-first, whereas Baton is a cross-platform desktop app with a visual dashboard. The difference from [cmux](/notes/cmux/) is that cmux focuses on agent notification (knowing which agents need your attention) while dmux focuses on the worktree management lifecycle.

## Key points

- Uses git worktrees as the isolation primitive — each AI coding agent gets its own branch and working directory.
- tmux-native interface for managing multiple agents in terminal panes.
- Full cycle support: branch creation, parallel development, merge coordination.
- Shares design territory with Baton (desktop GUI) and [cmux](/notes/cmux/) (macOS terminal) for running parallel agents.
- Complements any CLI-based agent like Claude Code, Codex, or Gemini CLI.

[Original](http://dmux.ai/)
