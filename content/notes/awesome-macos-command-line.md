---
title: Awesome macOS Command Line
date: 2022-12-07
categories:
  - macos
  - terminal
  - cli
  - developer-tools
  - reference
description: A comprehensive collection of macOS terminal commands and shell tricks — covering everything from hidden system preferences to networking, filesystem, and app configuration via the command line. The definitive reference for power users who prefer the terminal over System Preferences.
params:
  source: pinboard
  sourceUrl: https://git.herrbischoff.com/awesome-macos-command-line/about/
---

## Summary

[Awesome macOS Command Line](/notes/awesome-macos-command-line/) (by Marcel Bischoff) is a curated collection of macOS-specific terminal commands, defaults write settings, and shell tricks organized by category. It covers a wide range of system capabilities accessible only via the command line: Bluetooth toggles, hidden Finder settings, network configuration, disk operations, app-specific settings, screenshot behavior, and hundreds of other system preferences that have no GUI equivalent in System Preferences (now System Settings).

The defaults write system is the core mechanism: macOS stores most application preferences in plist files, and `defaults write <domain> <key> <value>` can modify them programmatically. Many developer-friendly settings (showing full file paths in Finder title, disabling `.DS_Store` on network shares, changing screenshot format/location) are only exposed this way. The collection documents these settings comprehensively in a format that's easy to search and copy-paste.

This kind of reference is particularly useful during system setup — when configuring a new Mac or creating dotfiles / Brewfile automation, having a searchable list of terminal-accessible settings saves hours of searching individual Stack Overflow answers. Many developers incorporate selections from this list into their dotfiles repos alongside their `.zshrc`, `.gitconfig`, and app configuration files. The collection is maintained on a self-hosted cgit instance rather than GitHub, reflecting the author's preference for independence from platform dependency.

## Key points

- Curated collection of macOS terminal commands and `defaults write` system preference overrides.
- Covers Bluetooth, Finder, network, disk, screenshots, app settings — many with no GUI equivalent.
- Core pattern: defaults write modifies app preference plists programmatically.
- Essential reference for dotfiles and new Mac setup automation.
- Self-hosted on cgit rather than GitHub — part of the author's platform independence ethos.
- Companion to tools like mackup, Homebrew, and dotfiles managers.

[Original](https://git.herrbischoff.com/awesome-macos-command-line/about/)
