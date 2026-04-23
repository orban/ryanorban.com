---
title: "Extrakto: fuzzy text extraction from tmux terminal output"
date: 2025-02-10
categories:
  - cli
  - tmux
  - developer-tools
  - productivity
  - terminal
description: Extrakto is a tmux plugin that extracts text from terminal output using fuzzy search — select any visible URL, path, or word and insert it into the current prompt without mouse or manual retyping. Removes a consistent terminal friction point.
params:
  source: pinboard
  sourceUrl: https://github.com/laktak/extrakto
---

![Extrakto: fuzzy text extraction from tmux terminal output](/images/notes/extrakto-tmux-text-extraction.png)

## Summary

Extrakto is a tmux plugin that solves a specific but persistent terminal friction: you see a file path, URL, or other piece of text in terminal output above your cursor, and you need to use it in the next command. Without extrakto, you either use the mouse to select it (breaking keyboard flow) or retype it manually (error-prone).

Extrakto binds a key (default: `prefix + tab`) that opens a fzf fuzzy search over the visible terminal content — paths, URLs, words — and inserts the selection at the current cursor position. It's context-aware: it can extract specifically URLs, file paths, or general words depending on mode. The selection happens entirely via keyboard with fuzzy filtering.

This fits into the broader pattern of terminal tools that eliminate friction specific to the terminal workflow — alongside tmux copy mode improvements, fzf keybindings, and zoxide for directory navigation. Small quality-of-life improvements that compound over a day of terminal use.

## Key points

- tmux plugin: opens fuzzy search over terminal output to select and insert text at cursor.
- Extracts URLs, file paths, or words depending on mode.
- Uses fzf as the fuzzy selection interface.
- Default keybinding: `prefix + tab`.
- Eliminates mouse usage or manual retyping for terminal output text.

[Original](https://github.com/laktak/extrakto) → GitHub
