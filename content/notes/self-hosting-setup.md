---
title: Screw It, I'll Host It Myself
date: 2022-02-25
categories:
  - self-hosting
  - homelab
  - linux
  - infrastructure
  - personal
description: A personal account of moving from cloud services to self-hosted alternatives — the motivations, the setup, and the tradeoffs. Captures the early-2022 wave of interest in digital self-sovereignty driven by concerns about SaaS pricing and data privacy.
params:
  source: pinboard
  sourceUrl: https://www.markozivanovic.com/screw-it-ill-host-it-myself/
---

## Summary

A personal post by Marko Živanović documenting his decision to move from cloud-hosted SaaS tools to self-hosted alternatives, and the resulting home server setup. The title captures the sentiment of the self-hosting movement well: at some point, the combination of cost, privacy concerns, vendor dependency, and feature limitations tips the calculus toward running your own infrastructure.

The post likely covers the typical self-hosting stack from 2022: a home server (often a repurposed PC or NAS), Docker containers for services, a reverse proxy (nginx or Traefik) for routing, Let's Encrypt for TLS certificates, and a VPN or tunnel (Tailscale, WireGuard) for remote access. Common services replaced include Nextcloud (for Google Drive/Docs), Bitwarden/Vaultwarden (for 1Password), Immich or PhotoPrism (for Google Photos), and Jellyfin (for streaming).

The motivations for self-hosting in 2022 were converging: SaaS costs were rising as "free" tiers were deprecated, privacy concerns about cloud providers were growing, and the tooling for self-hosting had become accessible enough that a motivated non-expert could run a reliable home server. Communities like r/selfhosted and tools like Portainer lowered the barrier further.

The tradeoffs are real: you're responsible for uptime, backups, security patches, and storage. But for many use cases, especially personal data like photos and documents, the control and cost savings outweigh the maintenance burden — especially once you've invested in the initial setup.

## Key points

- Self-hosted stack circa 2022: Docker + reverse proxy + Let's Encrypt + Tailscale or WireGuard for remote access.
- Common replacements: Nextcloud for Google Drive, Vaultwarden for password managers, Jellyfin for media.
- Motivations: rising SaaS costs, privacy concerns, vendor lock-in, desire for control over personal data.
- Tradeoff: you own the uptime, backups, and security — not just the data.
- Part of the broader digital sovereignty movement, growing in visibility in 2021-2022.

[Original](https://www.markozivanovic.com/screw-it-ill-host-it-myself/)
