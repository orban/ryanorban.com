---
title: "smasher164/nas: Personal NAS Configuration"
date: 2022-01-22
categories:
  - nas
  - homelab
  - nixos
  - self-hosting
  - configuration
  - reference
description: A personal NAS configuration repository (smasher164) — useful as a reference implementation for how someone configured their network-attached storage, likely using NixOS for reproducible system configuration. Bookmarked the same day as homelab, Headscale, and Netmaker notes.
params:
  source: pinboard
  sourceUrl: https://github.com/smasher164/nas
---

## Summary

This GitHub repository by smasher164 contains configuration files for a personal NAS (Network Attached Storage) setup. It was bookmarked on the same day as the khuedoan/homelab project, Headscale, and Netmaker — part of an evident homelab research session in January 2022.

Personal NAS configuration repositories are useful reference material for the self-hosting community: they show real-world decisions about filesystem choice (ZFS, Btrfs, ext4), drive layout and RAID configuration, network share setup (SMB, NFS, AFP), and any automation or configuration management tooling. Many homelab enthusiasts prefer NixOS for NAS builds because its declarative configuration model makes the system fully reproducible — a useful property when you care about data integrity.

The value of referencing other people's NAS configurations isn't copying them directly but understanding the decision space: what filesystem, what RAID level, what services (Plex, Nextcloud, Time Machine target), what backup strategy. Each configuration embodies a set of tradeoffs that the builder made consciously.

## Key points

- Personal NAS config reference — useful for understanding real-world homelab storage decisions.
- Bookmarked alongside khuedoan/homelab, Headscale, Netmaker — part of a homelab research session.
- Configuration repositories like this show filesystem choice, drive layout, share setup, and automation tooling.
- Common homelab NAS pattern: ZFS for data integrity + NixOS for reproducibility.
- Related: [building-nas-zfs](/notes/building-nas-zfs/) note for a fuller treatment of NAS filesystem and share configuration.

[Original](https://github.com/smasher164/nas)
