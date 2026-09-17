---
title: "SmoothWAN: Router for Speedify WAN Bonding"
date: 2022-03-14
categories:
  - networking
  - self-hosting
  - speedify
  - vpn
  - router
description: SmoothWAN is an OpenWrt-based router firmware that makes setting up Speedify for WAN bonding simple — combining multiple internet connections (4G, cable, DSL) for higher bandwidth and resilience. A practical project for anyone with unreliable internet.
params:
  source: pinboard
  sourceUrl: https://github.com/TalalMash/SmoothWAN
---

## Summary

SmoothWAN is an OpenWrt-based router firmware distribution that simplifies setting up Speedify — a channel bonding service that combines multiple internet connections into a single, faster and more reliable connection. The project provides a pre-configured, minimal router OS that does one thing well: multi-WAN bonding via Speedify.

WAN bonding (also called multi-WAN or link aggregation) is valuable when you have access to multiple internet connections — a cable modem, a 4G/5G mobile hotspot, a DSL line, a satellite connection — and want to use them simultaneously rather than failing over. Speedify does this via a VPN tunnel that routes traffic across all available connections intelligently: if one goes down, traffic shifts to the others. The combined bandwidth is roughly additive for independent streams (downloads from separate servers), though a single connection's speed is bounded by the VPN's session management.

Use cases include: work-from-home setups where connectivity reliability is critical (using both home broadband and a mobile data plan), rural/suburban locations with poor single-ISP options, travel setups (combining hotel WiFi with a mobile hotspot), and any scenario where total uptime matters more than peak speed.

SmoothWAN's contribution is packaging OpenWrt with Speedify integration and a clean setup interface, removing the technical complexity of configuring OpenWrt manually. The project assumes Speedify subscription (monthly paid service).

## Key points

- WAN bonding: combine multiple internet connections (cable + 4G + DSL) for bandwidth and resilience.
- SmoothWAN = OpenWrt + Speedify pre-configured — significantly lowers the setup barrier.
- Use cases: WFH reliability, rural connectivity, travel (hotel WiFi + mobile hotspot).
- Speedify does traffic distribution across connections via an encrypted tunnel.
- Requires a Speedify subscription — SmoothWAN is the open-source wrapper, not a replacement for the service.

[Original](https://github.com/TalalMash/SmoothWAN) → GitHub
