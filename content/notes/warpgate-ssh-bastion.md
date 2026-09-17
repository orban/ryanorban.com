---
title: "Warpgate: Smart SSH Bastion"
date: 2022-04-18
categories:
  - ssh
  - security
  - infrastructure
  - rust
  - open-source
description: Warpgate is an open-source SSH bastion server written in Rust — sits in front of your SSH targets, handles authentication centrally, and records sessions. Unlike traditional bastion hosts, it works with any standard SSH client without requiring a custom client or VPN.
params:
  source: pinboard
  sourceUrl: https://github.com/warp-tech/warpgate
---

## Summary

Warpgate is an open-source SSH bastion server written in Rust by warp-tech. A bastion host sits between users and internal SSH targets — instead of connecting directly to a server, you connect to the bastion, which proxies the connection after authentication and authorization checks. This centralizes access control: you can revoke access to all internal servers by removing one user from the bastion, rather than hunting down their public key across every machine.

What makes Warpgate notable is that it works with any standard SSH client — no custom software, no VPN, no agent setup required. You connect to Warpgate using regular `ssh`, but you embed the target in the username (`user@target:warpgate-port`). Warpgate handles the routing, authenticates you (via password, SSH key, or TOTP), checks if you're authorized for that target, and proxies the session. Sessions can be recorded for audit purposes — complete terminal session recordings that can be played back.

The Rust implementation is significant for a security-critical component: memory safety eliminates whole classes of vulnerabilities that plague C-based SSH implementations. Warpgate competes with tools like Teleport, Boundary (HashiCorp), and Jump Server, but positions itself as a simpler, self-hostable option with less operational overhead. The no-client-required design is a real differentiator — adoption friction is low because there's nothing to install on the connecting machines.

## Key points

- SSH bastion that works with any standard SSH client — no custom client, agent, or VPN required.
- Authentication: SSH key, password, and TOTP two-factor supported; centralized for all targets.
- Session recording: full terminal session capture with playback — audit trail for compliance.
- Written in Rust — memory safety for a security-critical network daemon.
- Target embedding via username syntax: `ssh user@target@warpgate-host` — standard client, smart routing.
- Self-hostable alternative to Teleport and HashiCorp Boundary — simpler operational footprint.

[Original](https://github.com/warp-tech/warpgate) → GitHub, AI agent
