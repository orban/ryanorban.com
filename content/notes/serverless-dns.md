---
title: "RethinkDNS: Serverless DNS Resolver"
date: 2022-07-31
categories:
  - dns
  - privacy
  - serverless
  - cloudflare-workers
  - open-source
description: RethinkDNS is an open-source, serverless DNS resolver with built-in ad and tracker blocking that deploys to Cloudflare Workers, Deno Deploy, or Fly.io — giving you a private, self-hosted DNS-over-HTTPS endpoint for free on serverless infrastructure.
params:
  source: pinboard
  sourceUrl: https://github.com/serverless-dns/serverless-dns
---

## Summary

[serverless-dns](/notes/serverless-dns/) (also known as RethinkDNS) is an open-source DNS resolver with blocklist support that deploys to Cloudflare Workers, Deno Deploy, or Fly.io. The appeal is privacy without infrastructure: run your own DNS-over-HTTPS or DNS-over-TLS endpoint with ad and tracker blocking, for free, on serverless infrastructure that you control. No VPS to maintain, no uptime worries — your DNS resolver runs on Cloudflare's global edge.

DNS is a privacy weak point in internet infrastructure: every domain you resolve goes to your DNS provider, which has a complete record of every website you visit. Most users use their ISP's DNS or Google's 8.8.8.8, both of which log queries. The privacy-preserving alternative is encrypted DNS (DoH or DoT) pointed at a resolver you trust. Running your own resolver is the highest-trust option, and serverless-dns makes that achievable without server administration.

The blocklist support covers ad networks, tracking scripts, and malware domains — implemented as a fast lookup against blocklist databases. The Cloudflare Workers deployment is particularly elegant: Cloudflare's edge runs your resolver in PoPs worldwide, so DNS resolution is fast from anywhere. The companion Android app, RethinkDNS + Firewall, adds per-app DNS control and firewall capabilities on top of the resolver backend.

## Key points

- Open-source DNS-over-HTTPS / DNS-over-TLS resolver with ad and tracker blocklist support
- Deploys to Cloudflare Workers, Deno Deploy, or Fly.io — serverless, no server management
- Privacy motivation: encrypts DNS queries so ISP and network operators can't see your browsing
- Blocklists: ad networks, trackers, malware — configurable via URL parameters
- Companion Android app: RethinkDNS + Firewall with per-app DNS and firewall rules
- Free on Cloudflare Workers free tier — self-hosted privacy DNS with no infrastructure cost

[Original](https://github.com/serverless-dns/serverless-dns) → GitHub
