---
title: Get Started With Tmux
date: 2021-04-04
categories:
  - terminal
  - tmux
  - developer-tools
  - linux
  - productivity
description: Sunaina Pai's beginner-friendly tmux guide — covering sessions, windows, panes, and the key bindings needed to make tmux a productive part of a terminal workflow. Good first-stop reference for anyone new to terminal multiplexing.
params:
  source: pinboard
  sourceUrl: https://sunainapai.in/blog/get-started-with-tmux/
---

## Summary

Sunaina Pai's guide introduces tmux — a terminal multiplexer — to developers who haven't used it. Tmux solves several problems: keeping long-running processes alive when you disconnect from SSH, splitting a single terminal window into multiple panes, and maintaining persistent terminal sessions that survive connection drops.

The core concepts: sessions (the top-level unit, survives disconnection), windows (like tabs within a session), and panes (splits within a window). The default prefix key is `Ctrl-b`, after which you press a single key to perform actions: `c` for new window, `%` for vertical split, `"` for horizontal split, `d` to detach (leave the session running), and `[` to enter copy mode for scrollback.

The practical value of tmux is highest for server administration and remote development: you SSH in, attach to a named session, and even if your connection drops, everything keeps running. The session is still there when you reconnect. For local use, it competes with terminal emulators that natively support tabs and splits (iTerm2, Alacritty, Wezterm) — but tmux's config portability means the same setup works identically on any machine.

## Key points

- Sessions survive SSH disconnection — long-running jobs keep running when connection drops.
- Three levels: sessions → windows (tabs) → panes (splits). Detach/reattach workflow is the core use case.
- Default prefix: `Ctrl-b`. Key bindings: `c` (new window), `%`/`"` (splits), `d` (detach), `[` (copy mode).
- `.tmux.conf` for customization — most users remap prefix to `Ctrl-a` and enable mouse support.
- Competes with native terminal tab/split support for local use; dominant for SSH/server workflows.

[Original](https://sunainapai.in/blog/get-started-with-tmux/)
