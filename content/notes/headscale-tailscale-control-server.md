---
title: "Headscale: Self-Hosted Tailscale Control Server"
date: 2022-01-22
categories:
  - networking
  - vpn
  - tailscale
  - wireguard
  - self-hosted
  - open-source
description: Headscale is an open-source, self-hosted implementation of the Tailscale control server — the missing piece that lets you run a fully private Tailscale network without depending on Tailscale's managed infrastructure. The self-sovereignty option for Tailscale users.
params:
  source: pinboard
  sourceUrl: https://github.com/juanfont/headscale
---

## Summary

Headscale is an open-source reimplementation of the Tailscale control server — the proprietary coordination layer that Tailscale uses to manage WireGuard key exchange, IP assignment, and access control across a tailnet. While Tailscale's client software is open source, the control plane remained closed. Headscale fills that gap, enabling fully self-hosted Tailscale networks.

The relationship to Tailscale is worth understanding precisely. Tailscale works by building a WireGuard mesh where each node has a public/private key pair and connects to a control server to exchange public keys and discover routes. Headscale replaces that control server — you run it yourself, and your Tailscale clients connect to it instead of `controlplane.tailscale.com`. The WireGuard mesh itself still runs client-side; Headscale just coordinates it.

The use case is self-hosters who want Tailscale's excellent NAT traversal and zero-config mesh networking but don't want their network metadata (who connected to whom, when) going to Tailscale Inc. It also enables organizations that can't use a managed service for compliance reasons. Works with standard Tailscale clients on Linux, macOS, iOS, Android, and Windows — no custom client needed.

## Key points

- Replaces the Tailscale control plane: manages WireGuard key exchange, IP assignment, and access control in a self-hosted deployment.
- Standard Tailscale clients connect to Headscale — no custom client required, works on all platforms.
- Use case: privacy (network metadata stays on your infrastructure), compliance (no third-party data flows), or pure self-sovereignty.
- WireGuard mesh itself is still peer-to-peer after coordination — Headscale isn't a traffic relay.
- Related: Netmaker for a different approach to WireGuard network automation.

[Original](https://github.com/juanfont/headscale) → GitHub
