---
title: "Matchlock: AI agents in ephemeral microVMs"
date: 2026-02-08
categories:
  - ai-agents
  - security
  - sandboxing
  - microvm
  - developer-tools
description: Matchlock runs AI agents in ephemeral microVMs with network allowlisting and MITM-based secret injection — your API keys never enter the VM. Full Linux environment that boots under a second, vanishes when done.
params:
  source: pinboard
  sourceUrl: https://github.com/jingkaihe/matchlock
---

![Matchlock: AI agents in ephemeral microVMs](/images/notes/matchlock.png)

## Summary

[Matchlock](/notes/matchlock/) is a CLI tool for running AI agents in ephemeral microVMs with network isolation and credential protection. The core guarantee: your secrets never enter the VM. You pass `--allow-host` to specify which hosts the agent can reach; everything else is blocked. When you pass `--secret`, credentials are injected in-flight by the MITM proxy at the host boundary — the agent inside sees a placeholder.

The microVM approach is similar to Safe Yolo Mode but packaged as a proper CLI tool rather than a manual setup guide. Both use virtualization for isolation. Matchlock's specific design choices: sub-second boot times (so it's practical to spin up a fresh VM per task), overlay volume mounts that vanish when you're done (so there's no accumulation of state), and identical behavior whether you're on a Linux server with KVM or a macOS Apple Silicon machine.

Inside the VM, the agent has a full Linux environment. It can install packages, write files, make network calls to allowlisted hosts — normal agent behavior, contained. The overlay mounts mean changes are isolated snapshots; they don't persist to your host. This addresses the same threat model as [Destructive Command Guard](/notes/destructive-command-guard/) (protecting your host system from agent mistakes), but at the infrastructure layer rather than the command interception layer.

## Key points

- Ephemeral microVMs that boot in under a second — practical for per-task isolation.
- Network allowlisting: only `--allow-host` destinations can be reached; all else blocked.
- MITM proxy injects real credentials in-flight; the VM only ever sees placeholders.
- Overlay volume mounts: changes are isolated snapshots that vanish when done.
- Works on Linux (KVM required) and macOS (Apple Silicon).
- Installable via Homebrew, .deb, or .rpm.

[Original](https://github.com/jingkaihe/matchlock)
