---
title: "SketchyBar: Highly Customizable macOS Status Bar Replacement"
date: 2024-06-09
categories:
  - macos
  - customization
  - open-source
  - status-bar
  - homelab
  - ricing
description: SketchyBar is a highly customizable macOS status bar replacement that lets you build a fully custom top bar with scripts, widgets, and plugins. The starting point for anyone who wants a custom macOS desktop setup.
params:
  source: pinboard
  sourceUrl: https://github.com/FelixKratz/SketchyBar
---

![SketchyBar: Highly Customizable macOS Status Bar Replacement](/images/notes/sketchybar-macos-status-bar.png)

## Summary

SketchyBar by Felix Kratz replaces the default macOS menu bar with a fully scriptable, composable status bar. You define items — spaces indicator, app menus, clock, system stats, music playback, custom widgets — using a configuration file and shell scripts. Items can be updated on events (space change, app focus) or on timers (CPU usage every 5 seconds). The result is a status bar that shows exactly what you want, styled exactly how you want.

The tool is part of the macOS ricing ecosystem alongside yabai (tiling window manager), skhd (hotkey daemon), and Raycast. Felix Kratz built it alongside JankyBorders (adds colored borders to windows). The typical setup: disable the native menu bar, run SketchyBar as a replacement, configure yabai for tiling, and end up with a desktop that looks completely custom — more like a Linux tiling WM setup than a standard Mac.

SketchyBar has an active community with shared configs and plugins on GitHub. The configuration API is Lua-scriptable (as of recent versions), giving you full programmability without shell script overhead. The project is a good example of the kind of powerful, unopinionated tool that appears in the macOS power-user ecosystem — it does one thing (status bar rendering and scripting) extremely well and stays out of the way for everything else.

## Key points

- Fully replaces the macOS menu bar with a scripted, composable replacement.
- Items defined in config + shell/Lua scripts; updates driven by events or timers.
- Pairs with yabai (tiling WM) and skhd (hotkeys) for a full custom desktop setup.
- By Felix Kratz; active community with shared plugins on GitHub.
- Lua scripting API for performant event-driven updates.
- Pairs naturally with Loop for a complete keyboard-driven macOS workflow.

[Original](https://github.com/FelixKratz/SketchyBar) → GitHub
