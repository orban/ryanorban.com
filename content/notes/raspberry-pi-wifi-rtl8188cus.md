---
title: Configuring Wireless LAN on Raspberry Pi with RTL8188CUS WiFi Dongle
date: 2012-12-18
categories:
  - raspberry-pi
  - networking
  - linux
  - wifi
  - embedded-systems
description: A 2012 setup guide for adding WiFi to the Raspberry Pi using the RTL8188CUS USB dongle — one of the first supported cheap WiFi adapters. The Pi had no built-in wireless until the Pi 3 in 2016, so USB dongles were required for years.
params:
  source: pinboard
  sourceUrl: http://www.marcomc.com/2012/09/how-to-configure-wireless-lan-on-raspberrypi-with-raspbian-kernel-3-2-27-and-solwise-rtl8188cus-wifi-dongle/
---

## Summary

In 2012, the Raspberry Pi had no built-in WiFi (that wouldn't arrive until the Raspberry Pi 3 in 2016), so adding wireless connectivity required a USB dongle. The RTL8188CUS chipset from Realtek — used in the Solwise and various other cheap dongles — was one of the first to have working Linux kernel drivers for the Pi's ARM architecture.

Marco MC's guide covers configuring Raspbian kernel 3.2.27+ to connect to a wireless network using this dongle. The process involved editing `/etc/network/interfaces` and `/etc/wpa_supplicant/wpa_supplicant.conf` — no GUI, all text-file configuration. Getting WiFi working on the Pi in this era required genuine Linux knowledge: identifying the chipset, loading the right kernel module, and debugging `dmesg` output.

This kind of guide was invaluable in 2012 when the Pi community was small and the hardware was brand new. The RTL8188CUS became a popular choice specifically because of community-proven driver support, even though the chip required a patched driver (`8192cu`) rather than the mainline kernel module.

## Key points

- RTL8188CUS used the `8192cu` kernel module on early Raspbian — not the mainline `rtl8192cu` driver
- WiFi configuration via `/etc/network/interfaces` and `/etc/wpa_supplicant/wpa_supplicant.conf` — text-only on headless Pi
- The Raspberry Pi had no built-in WiFi until the Raspberry Pi 3 (2016)
- USB power draw was a real concern — powered USB hub sometimes necessary for WiFi dongles
- This guide reflects the early figuring it out as we go era of the Pi community

[Original](http://www.marcomc.com/2012/09/how-to-configure-wireless-lan-on-raspberrypi-with-raspbian-kernel-3-2-27-and-solwise-rtl8188cus-wifi-dongle/)
