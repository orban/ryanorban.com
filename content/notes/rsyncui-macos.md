---
title: "RsyncUI: SwiftUI GUI for rsync on macOS"
date: 2025-05-29
categories:
  - macos
  - rsync
  - backup
  - swiftui
  - open-source
description: RsyncUI is a SwiftUI macOS GUI for rsync that makes the powerful but intimidating CLI tool accessible without touching the terminal. Requires macOS Sonoma or later.
params:
  source: pinboard
  sourceUrl: https://github.com/rsyncOSX/RsyncUI
---

![RsyncUI: SwiftUI GUI for rsync on macOS](/images/notes/rsyncui-macos.png)

## Summary

RsyncUI is a native macOS GUI for rsync, built with SwiftUI. rsync is one of the most powerful file synchronization tools available — incremental transfers, efficient delta encoding, remote sync over SSH, flexible include/exclude rules — but its CLI interface and flag complexity put it out of reach for users who don't want to memorize man pages.

RsyncUI wraps this power in a graphical interface: task organization, visual parameter configuration, and management of multiple sync profiles without writing shell commands. Requires macOS Sonoma (14+).

For users who manage backups, sync folders between machines, or mirror to remote servers, rsync does the job better than most commercial backup tools — RsyncUI removes the barrier that keeps most people from using it. It sits alongside tools like Arq and Carbon Copy Cloner in the macOS backup ecosystem but stays closer to the raw rsync model rather than inventing its own abstractions.

## Key points

- Native macOS GUI (SwiftUI) for rsync — no terminal required for typical use.
- Task organization and profile management for multiple sync configurations.
- Requires macOS Sonoma (14+).
- Keeps the power of rsync (SSH, delta sync, flexible rules) accessible.
- Open-source; available on GitHub.
- Complementary to rsync itself — doesn't hide the tool, surfaces it graphically.

[Original](https://github.com/rsyncOSX/RsyncUI)
