---
title: Brave Browser Hardening Guide
date: 2022-05-29
categories:
  - privacy
  - browser
  - brave
  - security
  - hardening
description: CHEF-KOCH's GitLab guide for hardening Brave Browser beyond its defaults — covering flags, extension recommendations, and configuration changes to minimize fingerprinting and data leakage. Useful reference for privacy-focused browser setup.
params:
  source: pinboard
  sourceUrl: https://gitlab.com/CHEF-KOCH/brave-browser-hardening
---

## Summary

CHEF-KOCH is a prolific privacy and security GitHub/GitLab contributor known for hardening guides across various browsers and operating systems. This repository covers hardening Brave Browser beyond its already privacy-forward defaults — specifically the configuration changes, feature flags, and extension setup that reduce remaining fingerprinting surface and data flows.

Brave already blocks ads, trackers, and most fingerprinting by default, which makes it a strong baseline compared to Chrome or Firefox without extensions. The hardening guide targets the residual exposure: Brave's built-in Chromium components that still phone home, the privacy tradeoffs in Brave Shields settings (aggressive vs. standard blocking), and the optional Brave Rewards / BAT token system which — while opt-in — has its own telemetry.

Key areas the guide covers: disabling Google Safe Browsing (sends URL hashes to Google), disabling crash reporting and metrics, configuring DNS-over-HTTPS with a privacy-respecting resolver (NextDNS, Cloudflare 1.1.1.1), disabling WebRTC to prevent IP leakage, and managing the `brave://flags` settings that affect fingerprinting resistance. The guide also addresses extension choices — given that extensions have access to all page content, minimizing the number installed is itself a hardening step.

## Key points

- Brave Browser hardening: targeting residual Chromium data flows and fingerprinting surface beyond Brave's defaults
- Disable Google Safe Browsing to prevent URL hash reporting; substitute with local blocklists or NextDNS
- WebRTC leak prevention: WebRTC can expose real IP through VPNs/proxies — requires explicit disabling in Brave settings
- DNS-over-HTTPS with privacy-respecting resolver (NextDNS, 1.1.1.1) prevents ISP-level DNS logging
- Minimal extensions: each extension is a trusted-code injection point — fewer is more secure
- Brave Shields aggressive mode: breaks some sites but maximizes tracker/fingerprint blocking; per-site override as needed

[Original](https://gitlab.com/CHEF-KOCH/brave-browser-hardening)
