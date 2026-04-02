---
title: Whosthere
date: 2026-01-23
categories:
  - networking
  - go
  - tui
  - cli
  - tools
  - lan
description: Whosthere is a Go TUI/CLI tool that discovers devices on a local area network using mDNS, SSDP, and ARP scanning without requiring root privileges. It's a practical home network visibility tool that also runs as a headless daemon with a simple HTTP API.
params:
  source: pinboard
  sourceUrl: https://github.com/ramonvermeulen/whosthere
---

![Whosthere](/images/notes/whosthere.png)

## Summary

Whosthere is a Go-based LAN discovery tool with an interactive TUI (terminal user interface) built with the tview library. It performs concurrent, unprivileged scans using mDNS, SSDP, and ARP cache reading to enumerate devices on the local subnet. It enriches results with manufacturer names via OUI (Organizationally Unique Identifier) lookups from the IEEE database.

The unprivileged approach is the key design decision: instead of sending raw packets (which requires root), it sweeps the subnet with TCP/UDP connection attempts to trigger ARP resolution, then reads the OS ARP cache. No `sudo` required. This makes it safe to install and run casually on a home network without worry.

Beyond interactive TUI use, Whosthere supports a daemon mode that exposes a lightweight HTTP API (`/devices`, `/device/{ip}`, `/health`), enabling integration with other tooling. Configuration is hierarchical—CLI flags beat environment variables beat a YAML config file—and themes are customizable at runtime via `CTRL+t`.

## Key points

- Discovers LAN devices via mDNS, SSDP, and ARP cache without elevated privileges
- Built in Go with an interactive TUI; installable via Homebrew, Nix, Arch Linux AUR, or `go install`
- OUI lookup enriches each device entry with manufacturer info
- Daemon mode exposes a simple REST API for integration with external tools
- Includes an optional port scanner (run only on devices you own) and configurable YAML theming

[Original](https://github.com/ramonvermeulen/whosthere)
