---
title: "yabai on macOS: Proof That macOS Can Look Good"
date: 2021-10-16
categories:
  - macos
  - window-management
  - tiling
  - unix
  - productivity
description: A Reddit r/unixporn showcase of a yabai + skhd setup on macOS, demonstrating that macOS can match the aesthetic and workflow density of Linux tiling window managers. Good reference for the kind of setup possible with yabai.
params:
  source: pinboard
  sourceUrl: https://reddit.com/r/unixporn/comments/mvuplf/yabaimacos_proof_that_macos_can_look_good/
---

## Summary

This r/unixporn post (1,392 votes) showcases a yabai + skhd setup on macOS that demonstrates how close macOS can get to the tight keyboard-driven workflows common in Linux tiling window manager setups. The setup integrates with Neovim for text editing and uses a minimal bar to achieve the clean tiling aesthetic popular in the r/unixporn community.

Yabai is an open-source tiling window manager for macOS by Felix Kratz. Unlike AltTab (which just improves the switcher), yabai fundamentally changes how windows are laid out: windows are automatically tiled to fill the screen without gaps, and you navigate between them with keyboard shortcuts defined in skhd (Simple Hotkey Daemon). The combination replaces macOS window dragging with a fully keyboard-driven workflow.

Yabai requires disabling System Integrity Protection (SIP) for full functionality, which makes it more niche than GUI window managers like Rectangle or Moom. The tradeoff: much more powerful keyboard-driven tiling (including moving windows between spaces, setting split ratios, and scripting layouts) at the cost of reduced security boundaries. Some features work without SIP disabled; others don't.

## Key points

- Yabai is a tiling window manager for macOS — automatically arranges windows and enables keyboard navigation between them.
- Requires disabling System Integrity Protection for full feature set, which limits adoption vs. simpler alternatives.
- Paired with skhd for hotkey configuration — each shortcut defined in a separate config file.
- The r/unixporn community treats macOS setups as a specific challenge: can it look as good as a Linux rice?
- Sits alongside AltTab, Rectangle, and Moom in the macOS window management ecosystem but offers more power.

[Original](https://reddit.com/r/unixporn/comments/mvuplf/yabaimacos_proof_that_macos_can_look_good/)
