---
title: "alexdavid/keybindings: Readline Keybindings System-Wide on macOS"
date: 2022-11-29
categories:
  - macos
  - keybindings
  - emacs
  - readline
  - productivity
description: alexdavid/keybindings is a macOS configuration that extends basic readline/Emacs keybindings to every text input on macOS — browser text fields, native app inputs, everything. A one-file setup that makes system-wide text editing consistent with terminal behavior.
params:
  source: pinboard
  sourceUrl: https://github.com/alexdavid/keybindings
---

![alexdavid/keybindings: Readline Keybindings System-Wide on macOS](/images/notes/alexdavid-keybindings-macos.png)

## Summary

alexdavid/keybindings is a macOS configuration project that installs Emacs-style / GNU Readline keybindings into the system-wide `~/Library/KeyBindings/DefaultKeyBinding.dict` file. This makes macOS text inputs — browser text fields, app inputs, anything using the native text editing stack — respond to the same shortcuts you'd use in the terminal: `Ctrl-a`/`Ctrl-e` for line start/end, `Ctrl-k` to kill forward, `Ctrl-y` to yank, `Alt-f`/`Alt-b` for word movement.

macOS has a built-in keybinding system that most users don't know about. The `DefaultKeyBinding.dict` file in `~/Library/KeyBindings/` maps key combinations to NSResponder selectors — standard macOS text actions. This means any application that uses the native text rendering stack (which is most non-Electron apps) will respond to custom keybindings. The alexdavid/keybindings repo provides a pre-built config that maps Readline-style shortcuts to their macOS equivalents.

The benefit: if you've invested in learning GNU Readline shortcuts in the terminal (or learned Emacs editing), this makes that muscle memory apply everywhere rather than just in readline-enabled programs. The limitation: Electron apps (many modern tools — VS Code, Slack, Discord, Notion) bypass the native text stack and don't respect these bindings. For native apps and browsers it works well. It pairs naturally with the GNU Readline shortcuts reference from Mastering Emacs.

## Key points

- Installs Emacs/Readline keybindings system-wide via macOS `DefaultKeyBinding.dict`.
- Works in any native-stack app: browser text fields, native inputs — not Electron apps.
- `Ctrl-a`/`Ctrl-e`, `Ctrl-k`/`Ctrl-y`, `Alt-f`/`Alt-b` work consistently across apps.
- macOS `DefaultKeyBinding.dict` maps key combos to NSResponder selectors — largely unknown feature.
- Limitation: Electron apps (VS Code, Slack, Notion) bypass the native text stack.
- Pairs with GNU Readline shortcuts as the terminal complement — same shortcuts everywhere.

[Original](https://github.com/alexdavid/keybindings) → GitHub
