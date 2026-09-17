---
title: How Pivotal Labs Uses tmux for Remote Pair Programming
date: 2012-07-18
categories:
  - tmux
  - pair-programming
  - remote-work
  - developer-tools
  - terminal
description: Pivotal Labs' guide to using tmux shared sessions for remote pair programming — both developers attach to the same terminal session and see identical output. Low-latency, tool-agnostic, and still one of the most effective remote pairing setups available.
params:
  source: pinboard
  sourceUrl: http://pivotallabs.com/users/joe/blog/articles/2199-how-we-use-tmux-for-remote-pair-programming-
---

## Summary

Pivotal Labs was one of the early adopters of systematic pair programming — it was baked into their engineering culture, not an occasional practice. When remote work required adapting the practice, they built a workflow around tmux shared sessions: both developers SSH into the same remote machine, attach to the same tmux session, and experience identical terminal output. One types, both see. Control passes back and forth through simple handoff.

The setup is low-tech by design. Unlike screen-sharing tools that add video and audio encoding overhead, tmux shared sessions are pure terminal I/O — the latency is limited only by network speed, not processing. For developers comfortable in terminal-based editors (Vim, Emacs) and command-line tools, this produced a pairing experience close to in-person. The shared terminal is the shared environment.

Pivotal Labs used this for both synchronous remote pairing and occasional async review (leaving context notes in the tmux session). Their setup typically involved a shared cloud instance — both developers SSH in from wherever they are. The session persists even if one drops, which adds resilience. This technique predates modern remote work tooling by years: Tuple, Pop (formerly Screenhero), and VS Code Live Share are all heavier alternatives that emerged later to serve less terminal-native teams.

## Key points

- tmux `attach-session` with `session-sharing` enabled: both users attach to the same session — completely synchronized terminal state, no replication.
- Requires both developers to be comfortable in terminal-based editors — Vim or Emacs; not suitable for GUI-only workflows.
- Latency is near-zero for local network connections; comparable to in-person for fast internet — much better than video screen-sharing.
- The persistent session model: if one person drops, the session continues; reconnecting restores state exactly.
- Predates modern remote pairing tools (Tuple, VS Code Live Share) — still valid and used in 2024 for terminal-native teams.

[Original](http://pivotallabs.com/users/joe/blog/articles/2199-how-we-use-tmux-for-remote-pair-programming-)
