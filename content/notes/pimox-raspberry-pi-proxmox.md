---
title: "Pimox: Proxmox Virtualization on Raspberry Pi 4B"
date: 2025-05-26
categories:
  - raspberry-pi
  - proxmox
  - virtualization
  - homelab
  - home-assistant
description: A comprehensive gist for turning a Raspberry Pi 4B into a Proxmox virtualization host using Pimox — covers Home Assistant VM, USB passthrough, SSD boot, and Docker. Practical homelab reference for ARM-based virtualization.
params:
  source: pinboard
  sourceUrl: https://gist.github.com/luckydonald/1849291fb5e19c87df8c8a1618e29eaa
---

![Pimox: Proxmox Virtualization on Raspberry Pi 4B](/images/notes/pimox-raspberry-pi-proxmox.png)

## Summary

Pimox is the port of Proxmox (the popular open-source virtualization platform) to Raspberry Pi ARM hardware. This gist by luckydonald is a battle-tested installation guide that covers everything from initial Pimox setup to running Home Assistant as a VM, USB passthrough, booting from SSD instead of SD card, LXC containers with ARM64 templates, and Docker integration.

The core value proposition: instead of repeatedly reformatting SD cards for each new experiment, you run Proxmox's hypervisor layer and spin up isolated VMs and containers for each purpose. Home Assistant in a dedicated VM, a separate Docker container environment, and other services all coexist on a single Raspberry Pi 4B without interfering with each other.

This is a practical homelab reference that addresses real pain points: USB passthrough (essential for Zigbee and Z-Wave dongles used with Home Assistant), the kernel workarounds required by Pimox, and network configuration issues that commonly arise in Debian containers on ARM. The guide includes community contributions that surface solutions to those edge cases.

## Key points

- Pimox: Proxmox hypervisor running on Raspberry Pi ARM hardware.
- Enables multi-VM/container setup: Home Assistant, Docker, LXC, all isolated on one Pi.
- Covers USB passthrough — essential for Zigbee/Z-Wave hardware with Home Assistant.
- SSD boot configuration: faster and more reliable than SD card for a server.
- LXC containers with ARM64 rootfs templates for lightweight workloads.
- Practical homelab setup guide with community-contributed troubleshooting.

[Original](https://gist.github.com/luckydonald/1849291fb5e19c87df8c8a1618e29eaa) → GitHub
