---
title: "The Companion: web UI for Claude Code and Codex"
date: 2026-02-10
categories:
  - ai-agents
  - developer-tools
  - claude-code
  - web-ui
  - open-source
description: The Companion is a web UI for Claude Code and Codex sessions — parallel agents, full tool call timeline, permission gating, and session recovery. Replaces terminal tab management for multi-agent workflows.
params:
  source: pinboard
  sourceUrl: https://github.com/The-Vibe-Company/companion
---

![The Companion: web UI for Claude Code and Codex](/images/notes/the-companion.png)

## Summary

[The Companion](/notes/the-companion/) (by The Vibe Company) is a web interface for running and monitoring Claude Code and Codex agent sessions. It's built on a simple WebSocket bridge architecture: a Bun/Hono server connects the CLI agent's `--sdk-url` websocket to a React browser UI, passing NDJSON events through. The agent works exactly as it would in the terminal; you get a web view on top.

The value is in managing multiple concurrent sessions. You can run parallel agents, see each one's streaming output and tool call timeline in real time, and approve or deny sensitive operations from the UI rather than the terminal. Session recovery handles the case where your browser or server restarts — work is preserved and sessions can be restored. No agent code changes required; it works with any Claude Code or Codex invocation via the `--sdk-url` flag.

The permission control flow is the distinguishing feature compared to similar tools like Baton (which focuses on git worktree isolation) and [cmux](/notes/cmux/) (which focuses on notification state). The Companion is specifically about human-in-the-loop oversight: you watch what's happening and gate actions that seem risky. Install as a background service via launchd on macOS or systemd on Linux so it's always available.

## Key points

- WebSocket bridge between Claude Code/Codex CLI and a React web UI.
- Full timeline of streaming output, tool calls, and tool results in one view.
- Permission control: approve/deny sensitive operations from the UI.
- Parallel sessions without juggling terminals.
- Session recovery across browser/server restarts.
- Install as a background service (`the-companion install` for launchd/systemd).
- Also known as the claude-code-controller (original name before rename).

[Original](https://github.com/The-Vibe-Company/companion)
