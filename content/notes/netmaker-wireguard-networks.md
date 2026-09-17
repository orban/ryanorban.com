---
title: "Netmaker: WireGuard Network Automation"
date: 2022-01-22
categories:
  - networking
  - wireguard
  - vpn
  - self-hosted
  - mesh-networking
  - open-source
description: Netmaker automates the creation of fast, secure, distributed virtual networks using WireGuard — with an admin UI, access control, private DNS, and support for mesh, site-to-site, and Kubernetes networking. More featureful than Headscale, trades simplicity for capability.
params:
  source: pinboard
  sourceUrl: https://github.com/gravitl/netmaker
---

## Summary

Netmaker is an open-source platform that automates WireGuard network creation and management, handling the coordination work that WireGuard deliberately leaves to the user. Raw WireGuard is fast and secure but requires manual configuration of public keys, allowed IPs, and peer lists on every node. Netmaker provides a controller (server + admin UI) that handles this automatically across any number of nodes.

The networking configurations it supports go well beyond simple VPN: peer-to-peer mesh networks (every node connects directly to every other), site-to-site networks (connecting separate subnets), and Kubernetes overlay networking. It adds features that organizations typically need: access control lists (ACLs) for per-node traffic control, private DNS for name resolution within the network, an OAuth integration for auth, and remote access gateways.

Compared to Headscale (which mimics the Tailscale control server for simplicity), Netmaker is more opinionated and featureful — it's designed for teams and organizations, not just individual self-hosters. The tradeoff: more moving parts. Available as both self-hosted open-source and a managed SaaS if you don't want to run the controller yourself.

## Key points

- Automates WireGuard peer configuration across nodes — eliminates the manual key exchange and peer list management that makes raw WireGuard operationally painful.
- Supports mesh, site-to-site, and Kubernetes overlay networking configurations.
- ACLs, private DNS, OAuth, remote access gateways — organizational feature set beyond basic VPN.
- Self-hosted (open source) or managed SaaS options.
- Compare to Headscale: more featureful and organizational-focused; Tailscale: managed, simpler, same WireGuard foundation.

[Original](https://github.com/gravitl/netmaker) → GitHub
