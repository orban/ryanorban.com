---
title: "Destructive Command Guard (dcg): hook for blocking dangerous agent commands"
date: 2026-02-10
categories:
  - ai-agents
  - security
  - developer-tools
  - claude-code
  - hooks
description: Destructive Command Guard (dcg) is a sub-millisecond hook that intercepts dangerous commands before AI agents execute them — git resets, rm -rf, DROP TABLE, kubectl deletes. 49+ security packs, SIMD-accelerated, never false-blocks.
params:
  source: pinboard
  sourceUrl: https://github.com/Dicklesworthstone/destructive_command_guard
---

![Destructive Command Guard (dcg): hook for blocking dangerous agent commands](/images/notes/destructive-command-guard.png)

## Summary

[Destructive Command Guard](/notes/destructive-command-guard/) (dcg) is a high-performance hook that intercepts destructive commands before AI agents execute them. The problem is real: agents like Claude Code, Codex, and Cursor occasionally run commands like `git reset --hard`, `rm -rf ./src`, or `DROP TABLE users` — destroying uncommitted work or data in seconds. dcg sits in front of command execution and blocks these before they run.

The implementation is SIMD-accelerated for sub-millisecond latency — you don't feel it in your workflow. The pattern detection is context-aware: it distinguishes `grep "rm -rf"` (data) from `rm -rf /` (execution) and won't false-block. Heredoc and inline script scanning catches embedded dangerous commands like `python -c "os.remove(...)"`. The default configuration protects against common git/filesystem destructive operations; 49+ security packs extend coverage to databases (PostgreSQL, MySQL), Kubernetes, Docker, AWS/GCP/Azure, Terraform, and more.

It works as a fail-open system: if dcg encounters a timeout or parse error, it passes the command through rather than blocking your workflow. The `explain` mode shows exactly why something would be blocked. This is complementary to VM-level isolation tools like [Matchlock](/notes/matchlock/) and Safe Yolo Mode — dcg operates at the command level within your existing environment, while VM tools provide full infrastructure isolation.

## Key points

- Intercepts destructive commands before execution: `git reset --hard`, `rm -rf`, `DROP TABLE`, `kubectl delete namespace`.
- SIMD-accelerated: sub-millisecond latency, won't affect workflow.
- Context-aware: distinguishes execution from data; catches heredoc and inline script injection.
- 49+ security packs for databases, Kubernetes, Docker, cloud CLIs, Terraform.
- Fail-open: never blocks on timeout or parse error.
- Works with Claude Code, Gemini CLI, GitHub Copilot CLI, Cursor, Codex, Aider.

[Original](https://github.com/Dicklesworthstone/destructive_command_guard)
