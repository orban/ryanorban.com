---
title: "Dashy: Self-Hosted Personal Dashboard"
date: 2022-05-09
categories:
  - self-hosted
  - dashboard
  - homelab
  - open-source
  - productivity
description: Dashy is an open-source, self-hosted personal homepage and service dashboard — a customizable start page for your homelab or self-hosted services with widgets, status checks, and icon integration. Popular in the homelab and self-hosted communities.
params:
  source: pinboard
  sourceUrl: https://dashy.to/
---

## Summary

[Dashy](/notes/dashy/) is an open-source, highly customizable self-hosted homepage and service dashboard. It's designed to be the launchpad for a personal homelab or self-hosted service setup — a single page that aggregates links to all your services (Plex, Nextcloud, Grafana, Home Assistant, Portainer, etc.) with icons, status monitoring, search, widgets, and themes. Configuration is via a YAML file, and the Vue.js frontend is deployable via Docker in minutes.

The homelab community has been drawn to [Dashy](/notes/dashy/) because the combination of services in a typical setup makes a launch page genuinely useful: you might have 15-20 internal services running across multiple machines, and navigating to them individually is friction. Dashy collapses them into a single bookmark. The status checking feature (health pings on each service) turns it into lightweight monitoring — you can see at a glance if something is down without opening a full dashboard like Grafana or Uptime Kuma.

The competition in this space includes Homer (simpler, static), Heimdall (features comparable to Dashy), Flame (minimalist), and Organizr (tabbed multi-user interface). Dashy's niche is the most feature-rich option with the highest customizability — it's the "if you want to configure everything" choice. The self-hosted movement that drove demand for these tools is partly a reaction to increased cloud service pricing and privacy concerns, but mostly hobbyist enthusiasm for running your own infrastructure.

## Key points

- Self-hosted personal dashboard aggregating homelab and self-hosted service links in one page.
- Configuration via YAML; deployed via Docker — minutes to get running.
- Status checking: health pings for each service, lightweight uptime monitoring without a full stack.
- Alternatives: Homer (minimal), Heimdall (balanced), Flame (aesthetic), Organizr (multi-user).
- Vue.js frontend; highly themeable — dozens of community themes available.
- Popular in homelab and self-hosted communities alongside Nextcloud, Plex, Home Assistant stacks.

[Original](https://dashy.to/)
