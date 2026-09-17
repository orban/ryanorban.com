---
title: "Home Lab Beginners Guide: Hardware"
date: 2022-04-22
categories:
  - homelab
  - self-hosted
  - hardware
  - networking
  - guide
description: A beginner's hardware guide to setting up a home lab — covers server options (used enterprise gear vs. mini PCs), networking basics (managed switches, VLANs), and storage. Entry point to the homelab community's approach to learning infrastructure hands-on.
params:
  source: pinboard
  sourceUrl: https://haydenjames.io/home-lab-beginners-guide-hardware/
---

## Summary

Hayden James's homelab hardware guide targets people setting up their first home server environment — the subset of the self-hosted community who want to learn networking, storage, and virtualization hands-on rather than renting cloud resources. The guide covers the core hardware decisions: server form factor (rack-mounted enterprise gear vs. tower vs. mini PC), networking equipment (managed switch, router, VLANs), and storage options (direct-attached vs. NAS).

The case for used enterprise servers (Dell PowerEdge, HP ProLiant) is the central recommendation for people who want to learn seriously: you get hardware with redundant power supplies, remote management (IPMI/iDRAC), ECC memory, and hot-swap drives for a fraction of the original cost. The tradeoff is power consumption and noise — enterprise servers designed for data center environments are loud and draw significant wattage, which adds up on a residential electricity bill. Mini PCs (Intel NUC, Beelink, etc.) are quieter and cheaper to run but lack the expansion slots and enterprise features.

The homelab community represents a particular approach to learning infrastructure: hands-on experience with real hardware teaches things that cloud consoles don't — physical networking, storage failure modes, hardware compatibility, power and thermal management. The community around tools like Proxmox (hypervisor), TrueNAS (storage), pfSense (router/firewall), and services like Nextcloud, Plex, and Home Assistant has grown substantially through the 2020s as home internet speeds improved and used server hardware became inexpensive.

## Key points

- Server options: used Dell/HP enterprise gear (feature-rich, loud, power-hungry) vs. mini PCs (quiet, efficient, limited expansion).
- Managed switches: enable VLAN segmentation — important for isolating IoT devices, lab environments, and guest networks.
- Remote management: iDRAC, IPMI — access server console without monitor/keyboard, critical for headless operation.
- ECC memory and hot-swap drives: enterprise reliability features that matter when the server runs 24/7.
- The homelab learning path: Proxmox → VMs → Docker containers → networking → storage → monitoring.
- Power cost math: a used enterprise server at 150W costs ~$150/year in electricity — factor into TCO.

[Original](https://haydenjames.io/home-lab-beginners-guide-hardware/)
