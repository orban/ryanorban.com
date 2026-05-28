---
title: GNU Readline Keyboard Shortcuts
date: 2022-11-29
categories:
  - terminal
  - readline
  - emacs
  - productivity
  - cli
description: A comprehensive reference for GNU Readline keyboard shortcuts — the Emacs-style keybindings available in bash, python, psql, and most other readline-enabled programs. The most leverage-per-keystroke investment for anyone who spends time in the terminal.
params:
  source: pinboard
  sourceUrl: https://www.masteringemacs.org/article/keyboard-shortcuts-every-command-line-hacker-should-know-about-gnu-readline
---

![GNU Readline Keyboard Shortcuts](/images/notes/gnu-readline-keyboard-shortcuts.png)

## Summary

This Mastering Emacs article documents the GNU Readline keyboard shortcuts available in any Readline-enabled program — bash, zsh, python REPL, psql, redis-cli, gdb, and many others. Readline is the line-editing library that underlies most interactive terminal programs on Unix systems, and it exposes a set of Emacs-style keybindings (plus optional vi mode) for moving, editing, and managing command history.

The core movements: `Ctrl-a` (beginning of line), `Ctrl-e` (end of line), `Ctrl-f`/`Ctrl-b` (character forward/back), `Alt-f`/`Alt-b` (word forward/back), `Ctrl-k` (kill to end of line), `Ctrl-u` (kill to beginning), `Ctrl-y` (yank killed text), `Ctrl-r` (reverse history search). These work identically in bash, python REPL, psql, and most other interactive tools. Learning them once gives you consistent navigation everywhere.

The Emacs connection is real: Richard Stallman designed Readline to use Emacs keybindings, so familiarity with Emacs movement transfers directly. The vi mode alternative (`set -o vi` in bash) is less commonly learned but equally powerful for people already fluent in Vim. The sister project referenced in the adjacent bookmark — alexdavid/keybindings — extends these shortcuts into macOS text inputs more broadly via a configuration file, so they work in browser text fields too. Together these two resources cover the full scope of terminal and system-wide text navigation.

## Key points

- GNU Readline keybindings work in bash, python REPL, psql, redis-cli, and most terminal programs.
- Core shortcuts: `Ctrl-a`/`Ctrl-e` (line edges), `Alt-f`/`Alt-b` (word movement), `Ctrl-k`/`Ctrl-u`/`Ctrl-y` (kill and yank).
- `Ctrl-r`: reverse incremental history search — arguably the single most valuable readline shortcut.
- Emacs mode is default; vi mode available via `set -o vi` for Vim users.
- Mastering Emacs is the authoritative reference — applies to any Readline-linked program.
- Companion to alexdavid/keybindings which extends these to macOS system-wide text inputs.

[Original](https://www.masteringemacs.org/article/keyboard-shortcuts-every-command-line-hacker-should-know-about-gnu-readline)
