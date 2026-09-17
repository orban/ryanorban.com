---
title: "Shuru: local-first microVM sandbox for AI agents"
date: 2026-02-23
categories:
  - ai-agents
  - security
  - sandbox
  - macos
  - infrastructure
description: Shuru is a local-first microVM sandbox for AI agents on macOS — gives agents an isolated environment to execute code without touching the host system. Addresses the core risk of agents with shell access running on your actual machine.
params:
  source: pinboard
  sourceUrl: https://shuru.run/
---

![Shuru: local-first microVM sandbox for AI agents](/images/notes/shuru-microvm.png)

## Summary

Shuru is a local-first microVM sandbox for running AI agents on macOS. The core problem it solves: agents with shell access, file write permissions, and tool-calling capabilities running directly on your host machine are a meaningful security risk. A sandboxed agent that misbehaves, gets confused, or is manipulated via prompt injection can only damage what's inside the VM — not your actual system.

The local-first framing positions it against cloud sandbox approaches (E2B, etc.): your code and data don't leave the machine, there's no round-trip latency to a remote VM, and you retain control of the execution environment. MicroVMs (think Firecracker-style) are faster to spin up and lighter than full VMs, making the per-session isolation cost practical rather than prohibitive.

For developers using Claude Code or other agents that execute shell commands, install packages, or modify files, this provides the blast-radius containment that makes it safer to grant agents broad permissions. The agent operates with full capabilities inside the VM, but the host system is protected.

## Key points

- MicroVM isolation on macOS — agents operate inside a VM, not on the host system.
- Local-first: code and data stay on the machine, no cloud round-trip like E2B.
- Addresses prompt injection and agent misbehavior risks by limiting blast radius.
- Practical for per-session isolation — microVMs spin up fast compared to full VMs.
- Enables granting agents broad shell/file permissions without full host system exposure.

[Original](https://shuru.run/)
