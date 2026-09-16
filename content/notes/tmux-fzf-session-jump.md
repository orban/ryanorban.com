---
title: tmux fzf Session Jumper
date: 2022-05-08
categories:
  - tmux
  - fzf
  - terminal
  - productivity
  - shell
description: A guide to building a fuzzy session-switcher for tmux using fzf — bind a key to pop up a searchable list of all open tmux sessions and jump to the selected one instantly. Small workflow improvement with a surprisingly large quality-of-life payoff for heavy tmux users.
params:
  source: pinboard
  sourceUrl: https://waylonwalker.com/tmux-fzf-session-jump/
---

## Summary

Waylon Walker's guide to building a fuzzy session-switcher for tmux using fzf — the command-line fuzzy finder. The setup is a keybinding that, when triggered, lists all open tmux sessions in an fzf popup, lets you type to filter, and jumps to the selected session on enter. For anyone managing many simultaneous tmux sessions across projects, this eliminates the friction of `tmux ls` + `tmux attach -t` or cycling through sessions blindly.

The implementation is a short shell function: call `tmux list-sessions`, pipe to fzf, and pass the result to `tmux switch-client`. The interesting part is making it a popup inside tmux itself (using `tmux popup`) rather than a full-terminal takeover — you get a floating window that dismisses on selection, keeping your current context intact. Bind it to a key like `prefix + s` and it's essentially a project switcher.

This pattern (pipe output to fzf → act on selection) generalizes broadly: fzf works the same way for file navigation, git branch switching, process killing, docker container selection, and most other cases where you need to choose from a list. The tmux session jumper is a clean introductory example because the state management is simple — sessions are independent and named.

## Key points

- Pattern: `tmux list-sessions | fzf | tmux switch-client` — list, filter, act.
- tmux popup mode keeps the jumper as a floating overlay rather than hijacking the terminal.
- Bind to `prefix + s` (or similar) for instant access — replaces manual `tmux ls && tmux attach -t`.
- fzf pattern generalizes: same approach works for git branches, files, docker containers, processes.
- From Waylon Walker's blog — he writes frequently about productive tmux + terminal workflows.
- Requires tmux 3.2+ for popup support.

[Original](https://waylonwalker.com/tmux-fzf-session-jump/)
