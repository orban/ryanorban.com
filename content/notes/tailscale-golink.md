---
title: "Tailscale golink: Private Shortlinks for Tailnets"
date: 2022-12-01
categories:
  - tailscale
  - internal-tools
  - productivity
  - go
  - open-source
description: golink is Tailscale's open-source private URL shortener for tailnets — lets your team use short go/links (like go/slack, go/docs) that resolve inside your Tailscale network. A small but sharp internal productivity tool.
params:
  source: pinboard
  sourceUrl: https://github.com/tailscale/golink
---

![Tailscale golink: Private Shortlinks for Tailnets](/images/notes/tailscale-golink.png)

## Summary

golink is Tailscale's open-source private URL shortener designed for tailnets (Tailscale private networks). It gives teams the ability to create short, memorable go-links — `go/docs`, `go/slack`, `go/oncall`, `go/deploy` — that resolve to full URLs inside the Tailscale network. The links only work for devices on your tailnet, making it a purely internal tool with no public exposure.

The go-link pattern has a long history in larger tech companies (Google famously runs an internal go-link service; Notion, Linear, Figma all have equivalents as engineering culture artifacts). The problem it solves: shared internal URLs are long, unmemorable, and hard to keep updated as destinations change. A go-link creates a stable, memorable shortcut where the destination can be updated without breaking everyone's bookmarks or Slack messages. `go/design` can point to different Figma files as the design evolves.

golink brings this pattern to small teams using Tailscale for their private network. It runs as a small Go service on any Tailscale node, uses SQLite for storage, and requires no infrastructure beyond a device that's already on your tailnet. The name resolution trick: browsers on Tailscale devices can be configured to resolve `go/*` URLs against the golink service via MagicDNS. This is a clean example of Tailscale's philosophy — expose infrastructure capabilities (private DNS, private routing) to build useful internal tools.

## Key points

- Private URL shortener for Tailscale tailnets — `go/docs`, `go/slack` resolve inside your private network only.
- Go-link pattern: stable, memorable internal shortcuts where destinations can be updated centrally.
- Go service + SQLite — minimal infrastructure, runs on any Tailscale node.
- Name resolution via MagicDNS — browsers on tailnet resolve `go/*` automatically.
- Classic internal productivity tool scaled down to small teams; previously only common at large companies.
- Demonstrates Tailscale's strategy: expose routing primitives for teams to build internal tooling.

[Original](https://github.com/tailscale/golink) → GitHub
