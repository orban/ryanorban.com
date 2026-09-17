---
title: "AltTab: Windows-style alt-tab for macOS"
date: 2021-12-11
categories:
  - macos
  - productivity
  - open-source
  - tools
  - window-management
description: AltTab brings Windows-style alt-tab window switching to macOS — full window previews, keyboard navigation, and extensive customization. The missing window manager feature that Apple never added.
params:
  source: pinboard
  sourceUrl: https://github.com/lwouis/alt-tab-macos
---

## Summary

AltTab is an open-source macOS utility by Luc Wois that replaces the native ⌘+Tab switcher with a Windows-style overlay showing live window previews. The core problem it solves: macOS's built-in app switcher shows app icons but not window thumbnails, and switches between apps rather than windows — so if you have five browser windows open, ⌘+Tab gives you one Firefox icon, not five preview thumbnails.

The tool hooks into macOS's Accessibility API to enumerate all windows and renders a thumbnail grid that updates in real-time. It's configurable: you can set which keyboard shortcut triggers it, how windows are sorted (by recency, by space, by application), whether to include minimized windows, and how large thumbnails should be. It also supports multiple monitors.

AltTab sits in the broader macOS window management space alongside tools like Raycast, Rectangle, and Yabai. Unlike Yabai which is a full tiling window manager, AltTab makes a smaller intervention — it just improves the switcher experience without changing how windows are arranged.

## Key points

- Replaces macOS ⌘+Tab with a Windows-like switcher showing live window thumbnails.
- Built on the macOS Accessibility API; works across all apps without special permissions beyond accessibility access.
- Highly configurable: sorting, filtering minimized/hidden windows, shortcut keys, thumbnail sizes.
- Open source (GPL-3.0), available via Homebrew: `brew install --cask alt-tab`.
- Complements but doesn't replace window management tools like Yabai or Rectangle.

[Original](https://github.com/lwouis/alt-tab-macos) → GitHub
