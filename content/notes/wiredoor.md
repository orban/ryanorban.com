---
title: "Wiredoor: Self-Hosted Ingress with SSL and VPN"
date: 2025-04-27
categories:
  - networking
  - self-hosted
  - wireguard
  - ingress
  - iot
description: Wiredoor is a self-hosted ingress-as-a-service platform that exposes private services over the internet via a WireGuard-powered reverse VPN — SSL included. It's a self-hostable Ngrok/Cloudflare Tunnel alternative with IoT and Kubernetes support.
params:
  source: pinboard
  sourceUrl: https://www.wiredoor.net/
---

![Wiredoor: Self-Hosted Ingress with SSL and VPN](/images/notes/wiredoor.png)

## Summary

[Wiredoor](/notes/wiredoor/) is a self-hosted ingress-as-a-service platform that lets you expose private services publicly using WireGuard as the transport layer. The mechanism is a reverse VPN tunnel: services behind NAT or firewalls connect out to a [Wiredoor](/notes/wiredoor/) server, which handles inbound HTTPS and routes traffic back through the tunnel. SSL terminates at the Wiredoor edge.

This positions Wiredoor against ngrok, Cloudflare Tunnel, and similar tunnel as a service tools — but self-hosted. You run the Wiredoor server on a VPS with a public IP, and your private services establish WireGuard tunnels to it. Services can be anything: internal web apps, Kubernetes ingress, databases, IoT devices. The WireGuard choice is smart here — it's lightweight enough for resource-constrained IoT hardware and has better performance than OpenVPN-based alternatives.

The IoT emphasis is notable. IoT devices behind home networks or cellular connections are a natural fit for this pattern: they can't accept inbound connections but need to be reachable. WireGuard's efficiency and mobile-platform support make it more viable than heavier VPN protocols.

## Key points

- Self-hosted ingress-as-a-service powered by WireGuard reverse VPN — own server, your data.
- Exposes private services (internal apps, Kubernetes, databases, IoT) over internet with SSL.
- Direct alternative to ngrok and Cloudflare Tunnel for the self-hosted crowd.
- WireGuard choice: lightweight enough for constrained IoT devices, better performance than OpenVPN.
- Simple deployment on a public VPS, private services connect outbound through tunnel.

[Original](https://www.wiredoor.net/)
