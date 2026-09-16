---
title: "Tunneling Tunnels: Multi-Hop VPN with Multitun"
date: 2022-02-12
categories:
  - privacy
  - vpn
  - networking
  - anonymity
  - security
description: cryptostorm's writeup on multitun — nesting multiple VPN tunnels inside each other for layered anonymity. The multi-hop VPN pattern separates entry and exit knowledge, so no single provider can link your identity to your traffic.
params:
  source: pinboard
  sourceUrl: https://cryptostorm.is/blog/multitun
---

## Summary

This cryptostorm blog post covers multitun — a technique for nesting VPN tunnels inside each other to create layered anonymity. The core insight: a single VPN provider knows both your real IP (entry) and your destination (exit), so they can link your identity to your activity if compelled to or compromised. Multi-hop VPN separates this: the entry node knows your IP but not your destination; the exit node knows your destination but not your IP.

Tor achieves a three-hop version of this by default, but with significant latency cost. Multitun is a lighter-weight approach: chain two or three VPN connections, each through a different provider, so no single point has complete information. The tradeoff versus Tor: faster and less obvious to network observers (VPN traffic is more normalized than Tor), but weaker — only as strong as the weakest provider in the chain.

The broader context: cryptostorm was known for taking the threat model analysis of VPN usage seriously, publishing technical details about how their infrastructure worked and what it could and couldn't protect against. This post reflects the operational security thinking that distinguishes serious privacy tooling from just turn on a VPN advice. Related concepts: Tor, I2P, onion routing, and the traffic analysis attacks that multi-hop addresses.

## Key points

- Multi-hop VPN: chain multiple VPN providers so no single one sees both your IP and destination.
- Entry/exit separation: entry node knows who you are; exit node knows where you're going — neither has both.
- Tradeoff vs Tor: faster, less fingerprinting risk, but fewer hops and less protection against coordinated adversaries.
- Relevant threat model: protects against VPN provider compromise or legal coercion, not active network adversaries.
- cryptostorm philosophy: publish the threat model, not just the product.

[Original](https://cryptostorm.is/blog/multitun)
