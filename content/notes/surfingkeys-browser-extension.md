---
title: "Surfingkeys: Vim Keybindings for the Browser"
date: 2021-03-21
categories:
  - browser
  - keyboard
  - productivity
  - vim
  - developer-tools
description: Surfingkeys is a browser extension that adds Vim-style keyboard navigation to Chrome and Firefox — configurable with JavaScript and more extensible than Vimium. For keyboard-first developers who want to browse without reaching for the mouse.
params:
  source: pinboard
  sourceUrl: https://github.com/brookhong/Surfingkeys
---

![Surfingkeys: Vim Keybindings for the Browser](/images/notes/surfingkeys-browser-extension.png)

## Summary

Surfingkeys is an open-source browser extension that brings Vim-style keyboard navigation to Chrome and Firefox. The core idea: a keyboard-first developer shouldn't need to reach for the mouse to follow a link, scroll a page, switch tabs, or navigate browser history. Surfingkeys maps these actions to Vim-inspired key chords.

The key feature distinguishing Surfingkeys from similar tools like Vimium is extensibility: configuration is done in JavaScript rather than a custom config format, and you can write custom mappings, create omnibar commands, and script browser interactions. This gives developers the full power of JS for customizing navigation behavior — binding keys to arbitrary scripts, not just built-in commands.

Core key bindings: `f` to bring up link hints (press the letter next to a link to follow it), `b` for bookmarks search, `t` for tab search, `j`/`k` to scroll, `H`/`L` for back/forward, `gt`/`gT` for tab navigation, and `:` to open a command bar. The extension also provides a Vim-style visual mode for selecting and copying text with keyboard navigation.

## Key points

- Adds Vim-style keyboard navigation to Chrome/Firefox — follow links without a mouse using link hints.
- Configurable in JavaScript — more powerful than Vimium's simpler config format.
- Core bindings: `f` (link hints), `j`/`k` (scroll), `H`/`L` (back/forward), `b` (bookmarks), `t` (tabs).
- Pairs naturally with other keyboard-first tools: tmux, Neovim, i3 window manager.
- By Brook Hong — active open-source project on GitHub.

[Original](https://github.com/brookhong/Surfingkeys)
