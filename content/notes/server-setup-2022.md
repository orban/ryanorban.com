---
title: Server Setup 2022
date: 2022-02-28
categories:
  - self-hosting
  - homelab
  - linux
  - server
  - infrastructure
description: TheOrangeOne's 2022 server setup overview — hardware, OS, containerization, monitoring, backup strategy. A well-documented example of a mature home server stack with emphasis on reliability and observability.
params:
  source: pinboard
  sourceUrl: https://theorangeone.net/posts/server-setup-2022/
---

## Summary

A blog post from TheOrangeOne documenting their home server setup as of 2022 — the hardware, OS choice, containerization strategy, monitoring, and backup setup. These server setup posts are a genre in the self-hosting community: documenting your stack forces you to think through your choices, and the posts become useful reference points for others building similar setups.

The 2022 vintage is interesting because it represents a moment when the self-hosting tooling had matured significantly. Docker Compose had become the dominant deployment format for home server services (easier than plain Docker, less heavyweight than Kubernetes). Traefik or Caddy had largely replaced manually-configured nginx as reverse proxy, with automatic Let's Encrypt certificate management. Uptime Kuma or Grafana for monitoring. Restic or BorgBackup for backup with Backblaze B2 or Wasabi as cheap object storage.

The post likely covers the specific hardware (server-grade vs. consumer hardware, storage setup), OS choice (typically Ubuntu Server, Debian, or sometimes NixOS), container orchestration (Docker Compose or Portainer), network configuration (Tailscale or WireGuard for remote access, VLANs for security), and backup strategy (the 3-2-1 rule: 3 copies, 2 media types, 1 offsite).

The emphasis on monitoring and observability distinguishes a mature home lab from a collection of ad-hoc experiments. Uptime Kuma in particular became popular in 2022 as a simple, self-hosted Statuspage alternative.

## Key points

- Home server stack circa 2022: Docker Compose, Traefik reverse proxy, Let's Encrypt, Tailscale.
- Monitoring stack: typically Grafana + Prometheus, or simpler tools like Uptime Kuma.
- Backup strategy: 3-2-1 rule with Restic or BorgBackup to Backblaze B2.
- The 2022 tooling generation made self-hosting significantly more accessible than 2018-era setups.
- Hardware decisions: balance between power consumption (24/7 uptime), storage capacity, and compute needs.

[Original](https://theorangeone.net/posts/server-setup-2022/)
