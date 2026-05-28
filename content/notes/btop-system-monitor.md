---
title: "btop: Beautiful Terminal System Monitor"
date: 2023-06-26
categories:
  - developer-tools
  - terminal
  - monitoring
  - linux
  - system-resources
description: btop is a beautiful, feature-rich terminal system monitor — a modern successor to top and htop with GPU monitoring, process management, and excellent UI. Cross-platform, low-overhead, and configurable.
params:
  source: pinboard
  sourceUrl: https://github.com/aristocratos/btop
---

![btop: Beautiful Terminal System Monitor](/images/notes/btop-system-monitor.png)

## Summary

btop by aristocratos is a terminal-based system resource monitor that modernizes the classic `top` and `htop` utilities with a significantly richer interface and broader hardware coverage. Written in C++, it's designed to be both visually appealing and practically useful — showing CPU, memory, disk, network, and process information in a well-organized TUI with real-time graphs.

What distinguishes btop from older alternatives: the visual design is intentionally more polished (using ANSI color and box-drawing characters to create a dashboard-like layout), it includes GPU monitoring (NVIDIA and AMD supported), and the process management features are more comprehensive (sorting, filtering, sending signals, setting priorities). It works across Linux, macOS, and BSD without significant feature loss on each platform.

The practical value is mostly day-to-day developer use: checking CPU usage spikes, watching memory under load, monitoring disk I/O during builds, and inspecting which processes are consuming resources. btop competes with htop (still excellent and more widely available), glances (Python-based, more metrics), and bottom (Rust-based alternative). The main reason to prefer btop is the visual quality and the GPU support — both of which matter for ML/GPU workloads where you're watching multiple resources simultaneously.

## Key points

- CPU, memory, disk, network, and process monitoring in a polished TUI with real-time graphs.
- GPU support (NVIDIA and AMD) — important for ML and gaming workloads.
- Cross-platform: Linux, macOS, and BSD with consistent feature set.
- Written in C++ — minimal overhead even while monitoring a loaded system.
- Visual design: box-drawing, ANSI color, dashboard layout — more legible than `htop` at a glance.
- Competes with htop (simpler, ubiquitous), glances (more metrics), and bottom (Rust).

[Original](https://github.com/aristocratos/btop)
 → GitHub
