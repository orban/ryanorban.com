---
title: Amethyst — macOS Tiling Window Manager
date: 2014-12-18
categories:
  - macos
  - productivity
  - developer-tools
  - window-management
description: Amethyst is a free tiling window manager for macOS that automatically arranges windows in configurable layouts without manual dragging. For developers who live in the terminal and editor, it eliminates the cognitive overhead of window placement.
params:
  source: pinboard
  sourceUrl: http://ianyh.com/amethyst/
---

## Summary

Amethyst is an open-source tiling window manager for macOS by Ian Ying. It sits in the menu bar and automatically arranges all open windows into non-overlapping tile layouts — similar to i3 on Linux or xmonad for those who know their way around Haskell. The big practical difference from typical macOS window management: windows never overlap, so you never spend time manually arranging them.

Tiling window managers operate on a layout algorithm that fills the screen with windows according to a predefined pattern (tall, wide, full, grid). When you open a new window, the layout recalculates and everything reflows. This workflow is particularly appealing to developers who spend their day split between a terminal, editor, and browser — the common two-up or three-up layouts become automatic.

Amethyst takes heavy inspiration from xmonad — its keyboard shortcuts and layout philosophy are similar — but is built as a native macOS app rather than requiring X11. This made it the practical choice for developers on Mac who wanted tiling behavior without the complexity of XQuartz.

## Key points

- Free, open-source tiling window manager for macOS — automatically tiles all open windows.
- Inspired by xmonad — same keyboard-centric, layout-algorithm approach, native macOS implementation.
- Layouts: tall, wide, full, grid, floating — configurable per space.
- Works alongside native macOS Spaces and Mission Control.
- Particularly useful for developers: terminal + editor + browser in fixed positions eliminates context-switching friction.
- Alternative to paid tools like Divvy and Moom that require manual window placement.

[Original](http://ianyh.com/amethyst/)
