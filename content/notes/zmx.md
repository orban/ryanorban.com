---
title: "zmx: session persistence for terminal processes"
date: 2026-01-29
categories:
  - developer-tools
  - terminal
  - session-persistence
  - tmux-alternative
description: zmx persists terminal shell sessions independently of client connections — attach and detach without killing the process, restore scrollback history in plain text, and share sessions across multiple users. Focused on session continuity without terminal multiplexer complexity.
params:
  source: pinboard
  sourceUrl: https://zmx.sh/
---

![zmx: session persistence for terminal processes](/images/notes/zmx.png)

## Summary

[zmx](/notes/zmx/) is a focused terminal session persistence tool: shell sessions survive independently of client connections. You can detach from a session without killing it, reconnect later with full scrollback history restored in plain text, and have multiple users connect to the same session simultaneously. It's a single-purpose tool — no window management, no tabs, no splits.

The deliberate restraint is notable. tmux and screen offer full terminal multiplexing (session persistence plus window management), which is powerful but comes with complexity. [zmx](/notes/zmx/) is just the persistence layer: if you want to attach and detach without consequence, that's the whole feature set. This makes it lighter and easier to reason about for use cases where multiplexing is overkill.

For AI coding agent workflows specifically, session persistence matters when agents run long tasks. Rather than keeping a terminal open or risking process death on disconnect, [zmx](/notes/zmx/) lets the agent continue running in a detached session while the developer does other things. The plain-text scrollback means you can also send commands to sessions remotely without attaching.

## Key points

- Terminal sessions persist independently of client connections — detach without killing processes.
- Reconnecting restores previous terminal state and full scrollback history in plain text.
- Multiple users can connect to the same session simultaneously.
- Deliberately excludes window management, tabs, and splits — pure session persistence.
- Send commands to sessions remotely without connecting interactively.
- Cross-platform: macOS and Linux.

[Original](https://zmx.sh/)
