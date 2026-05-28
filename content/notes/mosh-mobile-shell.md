---
title: "Mosh: The Mobile Shell"
date: 2012-04-09
categories:
  - terminal
  - ssh
  - networking
  - developer-tools
  - mobile
description: Mosh (mobile shell) is a UDP-based replacement for SSH that maintains connections across network changes, provides instant local echo even on high-latency links, and never drops a session when you close your laptop. The right tool for anyone working over unreliable or mobile connections.
params:
  source: pinboard
  sourceUrl: http://mosh.mit.edu/
---

![Mosh: The Mobile Shell](/images/notes/mosh-mobile-shell.png)

## Summary

Mosh (mobile shell) is a remote terminal application built as a modern replacement for SSH. The core problem it solves: SSH is built on TCP and requires a persistent connection — close your laptop, change WiFi networks, or lose signal on a train and your session dies. Mosh stays connected through all of that by using UDP with stateless authentication on each datagram, combined with a synchronization protocol that reconciles state rather than requiring a continuous byte-stream.

The technical architecture is meaningfully different from SSH. Both client and server maintain snapshots of the screen state and synchronize them using a diff-based State Synchronization Protocol (SSP). This means Mosh can display your keystrokes instantly without waiting for server confirmation — even on high-latency connections, the terminal feels snappy. When you're working on a satellite or cellular link with 500ms latency, this matters enormously.

MIT built Mosh and released it as free software. It uses SSH for the initial authentication handshake (so your existing keys and passwords work), then hands off to its own UDP-based transport. It's been a staple tool for developers who work remotely or travel — essentially anyone who has ever lost a terminal session mid-work.

## Key points

- UDP-based transport instead of TCP — sessions survive network changes, sleep/wake cycles, and IP address changes.
- Instant local echo with predictive display — types feel responsive even on high-latency connections.
- SSH for authentication, then hands off to its own protocol — no new key infrastructure needed.
- Both client and server maintain screen state snapshots; only diffs are sent (State Synchronization Protocol).
- Fixes Unicode handling bugs present in many other terminal emulators.
- Available on all major platforms; install via package manager on server, app on mobile.

[Original](http://mosh.mit.edu/)
