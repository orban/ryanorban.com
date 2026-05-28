---
title: A tmux Primer
date: 2014-08-05
categories:
  - tmux
  - terminal
  - developer-tools
  - productivity
  - linux
description: Daniel Miessler's comprehensive tmux primer — covering sessions, windows, panes, and key bindings. The reference guide for learning tmux from scratch, particularly useful for data scientists who spend significant time in SSH sessions on remote servers.
params:
  source: pinboard
  sourceUrl: http://danielmiessler.com/study/tmux/
---

![A tmux Primer](/images/notes/tmux-primer.png)

## Summary

tmux is a terminal multiplexer — it lets you run multiple terminal sessions within a single window, detach from them (keeping processes running), and reattach later. Daniel Miessler's primer is one of the most-bookmarked introductions to tmux because it covers the full mental model before diving into commands.

The core value proposition: sessions survive disconnection. When you're running a long computation on a remote server via SSH, closing your laptop or losing the connection kills the process. With tmux, the session keeps running on the server; you reconnect and reattach to find it exactly where you left it. This was particularly valuable for data scientists in 2014 who ran training jobs on EC2 instances or university compute clusters over SSH.

The tmux hierarchy: **sessions** (persist independently), **windows** (tabs within a session), **panes** (split views within a window). The default prefix key is `Ctrl-b`, followed by a command key. Common operations: `Ctrl-b c` new window, `Ctrl-b %` split vertical, `Ctrl-b "` split horizontal, `Ctrl-b d` detach, `tmux attach` reconnect.

## Key points

- tmux sessions persist after SSH disconnection — processes keep running, reattach to resume.
- Three-level hierarchy: sessions → windows → panes.
- `Ctrl-b d`: detach (session keeps running). `tmux attach` or `tmux a -t <session>`: reattach.
- `Ctrl-b %` / `Ctrl-b "`: split pane vertically/horizontally — run parallel processes in the same view.
- `tmux new -s <name>`: create named session — essential for managing multiple long-running jobs.
- Common `.tmux.conf` customizations: rebind prefix to `Ctrl-a` (screen compatibility), enable mouse mode, set vi key bindings.
- Alternative: screen (older, less featured). Modern workflows also use zellij as a Rust-based alternative.

[Original](http://danielmiessler.com/study/tmux/)
