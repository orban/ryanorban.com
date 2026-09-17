---
title: Best Linux Commands for Advanced Hardware and System Info
date: 2022-06-27
categories:
  - linux
  - sysadmin
  - hardware
  - cli
  - reference
description: A reference list of Linux commands for querying hardware and system information — CPU, memory, disks, PCI devices, USB, BIOS. The kind of cheat sheet you bookmark once and pull up whenever you're debugging a server or setting up a new machine.
params:
  source: pinboard
  sourceUrl: https://nixsanctuary.com/best-linux-hardware-system-info-commands/
---

## Summary

This NixSanctuary article compiles the most useful Linux commands for querying hardware and system information — the commands you reach for when you need to know what's actually in a machine. These are particularly useful when working with servers, homelabs, or unfamiliar hardware where you can't look up specs elsewhere.

Key commands covered: `lshw` (comprehensive hardware listing, tree format), `lscpu` (CPU architecture, cores, cache topology), `lspci` (PCI bus devices — GPUs, NICs, storage controllers), `lsusb` (USB device tree), `dmidecode` (BIOS/UEFI information, memory slot details, system serial numbers), `hwinfo` (detailed hardware probe), `inxi` (concise system summary designed for forum support), and `/proc` filesystem reads for runtime kernel views of hardware.

These commands matter most in contexts where you don't have vendor documentation: bare-metal servers, second-hand hardware, and environments where `uname -a` gives you a kernel version but not the full picture. `dmidecode --type memory` tells you exactly how many memory slots are populated and at what speed. `lspci -v` tells you which driver is bound to which PCI device. This is the level of detail you need when debugging driver issues or planning hardware upgrades.

## Key points

- `lshw -short` — one-liner hardware tree across CPU, memory, storage, network, GPU
- `dmidecode` — reads DMI/SMBIOS tables: memory slots, BIOS version, chassis serial numbers, system manufacturer
- `lspci -k` — shows which kernel module is handling each PCI device, essential for driver debugging
- `inxi -Fxz` — condensed full-system summary, widely used format for Linux forums and support requests
- `/proc/cpuinfo`, `/proc/meminfo` — raw kernel views; useful in containers where `lshw` may not be available

[Original](https://nixsanctuary.com/best-linux-hardware-system-info-commands/)
