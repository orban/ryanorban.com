---
title: AltTab — Windows-style alt-tab for macOS
date: 2022-01-15
categories:
  - macos
  - productivity
  - open-source
  - tools
description: AltTab is an open-source macOS utility that replaces the default Cmd+Tab app switcher with a Windows-style window previewer showing actual window thumbnails. Fixes the longstanding macOS pain point where Cmd+Tab cycles apps rather than windows.
params:
  source: pinboard
  sourceUrl: https://alt-tab-macos.netlify.app/
---

## Summary

AltTab is a free, open-source macOS utility that overrides the native Cmd+Tab application switcher with a Windows-style window switcher showing live thumbnails of each open window. The native macOS behavior cycles through applications rather than individual windows — if you have three Chrome windows open, Cmd+Tab only shows one Chrome icon. AltTab shows all three windows as separate switchable targets.

The tool is built in Swift and distributed as a native macOS app. It integrates at the accessibility API level to enumerate windows and generate previews. The UI is configurable: thumbnail size, appearance, which windows appear (minimized, hidden, by app), keyboard shortcuts, and behavior on multi-monitor setups. It can replicate the Windows Alt+Tab behavior almost exactly, or be tuned to different preferences.

For anyone coming from Windows or Linux who found macOS's window management opinionated to the point of being limiting, AltTab solves the most common complaint without requiring a full tiling window manager like Yabai or Amethyst.

## Key points

- Replaces Cmd+Tab with a window-level switcher showing live thumbnails — not app-level
- Open-source, free, actively maintained, written in Swift
- Highly configurable: appearance, which windows shown, shortcuts, per-monitor behavior
- Works alongside Raycast, Alfred, and other launcher tools — different use case
- Part of a category of macOS utilities (alongside Rectangle, Karabiner-Elements) that address macOS UX gaps

[Original](https://alt-tab-macos.netlify.app/)
