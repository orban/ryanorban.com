---
title: "Agentboard: web-based tmux GUI for AI agent sessions"
date: 2026-02-06
categories:
  - ai-agents
  - developer-tools
  - tmux
  - mobile
  - open-source
description: Agentboard is a web GUI for tmux optimized for AI agent TUIs — run Claude Code or Codex on your server and interact from your phone via iOS Safari. Status inference, session pinning, and a shared workspace across devices.
params:
  source: pinboard
  sourceUrl: https://github.com/gbasin/agentboard
---

![Agentboard: web-based tmux GUI for AI agent sessions](/images/notes/agentboard.png)

## Summary

[Agentboard](/notes/agentboard/) is a web frontend for tmux built specifically for AI coding agent workflows. The core use case: run Claude Code, Codex, or other agents on a remote server or desktop, then connect and interact from any device including iOS Safari. It's a lighter-weight alternative to tools like Blink or Termux that's oriented around multi-agent session management rather than general terminal use.

The agent status inference is the most practically useful feature. [Agentboard](/notes/agentboard/) reads Claude Code and Codex JSONL log files to determine whether each agent is *working*, *waiting for input*, or *asking for permission* — and surfaces this as session labels visible from the session list. Combined with last user prompt display, you can tell at a glance what each of your agents is doing without attaching to every terminal. Session pinning auto-resumes agents after server restarts.

The architecture streams terminal I/O over WebSockets from a local or remote tmux session through a small Node server to a React+xterm.js browser client. Works over Tailscale or LAN. This fills a real gap in vibe coding at scale: when you're running many agents in parallel, you need a dashboard more than a terminal emulator.

## Key points

- Web GUI for tmux with iOS Safari mobile support — paste, touch scrolling, virtual d-pad.
- Reads Claude Code and Codex JSONL logs to infer agent status: working / waiting / permission needed.
- Shows last user prompt per session — so you remember what each agent is doing without attaching.
- Session pinning auto-resumes agents when server restarts or tmux dies.
- Connects to remote hosts over SSH; works over Tailscale or LAN.
- Built with React + xterm.js, streams I/O over WebSockets.

[Original](https://github.com/gbasin/agentboard)
