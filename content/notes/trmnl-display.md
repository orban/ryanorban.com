---
title: "TRMNL Display: e-paper and LCD display software for single-board computers"
date: 2025-11-21
categories:
  - hardware
  - e-paper
  - raspberry-pi
  - display
  - local-first
description: TRMNL is a display software project for single-board computers (Raspberry Pi, Orange Pi) supporting both HDMI/LCD and e-paper displays. v0.1.0 introduced a build script for choosing display mode and runs in the background so the device stays useful for other tasks.
params:
  source: pinboard
  sourceUrl: https://github.com/usetrmnl/trmnl-display/releases/tag/v0.1.0
---

![TRMNL Display: e-paper and LCD display software for single-board computers](/images/notes/trmnl-display.png)

## Summary

TRMNL is a display software project for Raspberry Pi and other single-board computers that supports both e-paper displays and traditional HDMI/LCD output. The v0.1.0 release introduced a `build.sh` script that lets users choose between display modes, tested across Raspberry Pi 4B, Zero, Zero 2W, and Orange Pi variants.

The design goal is non-intrusive: TRMNL runs in the background, leaving the device available for other workloads. This makes it useful for dashboards that sit alongside other services on the same Raspberry Pi — a home automation hub, a Home Assistant node, a Pi-hole instance. The e-paper support is particularly useful for always-on status displays where power consumption matters; e-paper draws power only when refreshing.

The `usetrmnl` organization builds consumer products alongside this open-source display software — the hardware product is a standalone e-paper device with a subscription service for managed content. The open-source `trmnl-display` component is the DIY path, letting people build their own TRMNL-style dashboard on existing hardware.

## Key points

- Supports e-paper (Waveshare) and HDMI/LCD displays on Raspberry Pi and Orange Pi.
- Runs in background — device stays available for other services.
- v0.1.0: `build.sh` script for display mode selection, tested on Pi 4B, Zero, Zero 2W.
- Low-power e-paper mode ideal for always-on dashboards.
- DIY path for the consumer TRMNL e-paper display product.
- open-source component in the usetrmnl ecosystem.

[Original](https://github.com/usetrmnl/trmnl-display/releases/tag/v0.1.0) → GitHub
