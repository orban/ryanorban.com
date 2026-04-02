---
title: "cmux: native macOS terminal for parallel AI coding agents"
date: 2026-02-26
categories:
  - developer-tools
  - terminal
  - ai-agents
  - macos
  - open-source
description: cmux is a native macOS terminal built on Ghostty specifically for running multiple AI coding agents in parallel. Sidebar tabs show which agents need attention, with notification rings and desktop alerts when an agent is waiting for input.
params:
  source: pinboard
  sourceUrl: https://www.cmux.dev/
---

![cmux: native macOS terminal for parallel AI coding agents](/images/notes/cmux.png)

## Summary

[cmux](/notes/cmux/) is a native macOS terminal application purpose-built for developers running multiple AI coding agents simultaneously. The core problem it addresses: when you have Claude Code, Codex, OpenCode, and Gemini CLI running in parallel, it's hard to tell at a glance which agents are waiting for input vs. still working. cmux solves this with notification rings that visually highlight panes when agents need attention, plus desktop alerts and unread badges on workspace tabs.

Built on Ghostty (the GPU-accelerated terminal library), it's native Swift + AppKit — no Electron. The sidebar shows vertical tabs with git branch, working directory, active ports, and notification text for each agent session. Workspaces group related agent sessions together. Split panes let you monitor multiple agents in one view.

The technical layer beyond the UI includes an in-app browser with scriptable API, a socket API and CLI for automation, and GPU-accelerated rendering. Works with any CLI-based agent — Claude Code, Codex, OpenCode, Gemini CLI, Aider, etc. — since it's fundamentally a terminal with orchestration features layered on top. Free, open-source, macOS 14+.

## Key points

- Built on Ghostty (GPU-accelerated terminal), native Swift/AppKit — no Electron overhead.
- Notification rings visually highlight which agent panes need input, with desktop alerts and unread badges.
- Sidebar tabs show git branch, working directory, ports, and notification text per session.
- Works with any CLI-based agent — Claude Code, Codex, Gemini CLI, Aider, etc.
- Socket API and CLI for programmatic control and automation.

[Original](https://www.cmux.dev/)
