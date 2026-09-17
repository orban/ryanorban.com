---
title: "claude-sneakpeek: unlock feature-flagged Claude Code capabilities"
date: 2026-01-25
categories:
  - claude-code
  - swarm-mode
  - multi-agent
  - feature-flags
  - developer-tools
description: claude-sneakpeek installs a feature-flagged parallel build of Claude Code that unlocks swarm mode, delegate mode, and team coordination — capabilities built into Claude Code but not yet publicly released.
params:
  source: pinboard
  sourceUrl: https://github.com/mikekelly/claude-sneakpeek
---

![claude-sneakpeek: unlock feature-flagged Claude Code capabilities](/images/notes/claude-sneakpeek.png)

## Summary

[claude-sneakpeek](/notes/claude-sneakpeek/) installs an isolated parallel instance of Claude Code with feature flags unlocked that aren't available in the standard release. The headlining feature is swarm mode — native multi-agent orchestration via `TeammateTool`. Also unlocked: delegate mode (the Task tool can spawn background agents) and team coordination (teammate messaging and task ownership).

The install is a single `npx` command that creates a completely separate instance: separate config, sessions, MCP servers, and credentials. The existing Claude Code installation is untouched. Running `claudesp` launches the feature-flagged version.

The features being unlocked are notable. Swarm mode and `TeammateTool` are built into Claude Code's source but gated behind flags not accessible in the production release. This is the same territory that [Claude Code Unpacked](/notes/claude-code-unpacked/) documents — capabilities visible in the source that aren't yet publicly exposed. [claude-sneakpeek](/notes/claude-sneakpeek/) makes them usable rather than just visible, for developers who want to experiment with multi-agent orchestration built natively into Claude Code.

## Key points

- Installs a feature-flagged Claude Code instance that unlocks unreleased capabilities.
- **Swarm mode**: native multi-agent orchestration with `TeammateTool`.
- **Delegate mode**: Task tool can spawn background agents.
- **Team coordination**: teammate messaging and task ownership primitives.
- Completely isolated install — separate config, sessions, MCP servers, and credentials from main instance.
- Capabilities are built into Claude Code source but gated; [claude-sneakpeek](/notes/claude-sneakpeek/) unlocks the flags.

[Original](https://github.com/mikekelly/claude-sneakpeek)
