---
title: Building a NAS with ZFS and AFP/Samba for Time Machine
date: 2022-11-28
categories:
  - nas
  - zfs
  - self-hosted
  - homelab
  - storage
description: A guide to building a NAS (Network Attached Storage) with ZFS and AFP/Samba configured as a Time Machine backup target — covering ZFS pool setup, share configuration, and macOS Time Machine integration. The self-hosted alternative to iCloud or Time Capsule for Mac backups.
params:
  source: pinboard
  sourceUrl: https://blog.gwlab.page/building-nas-with-zfs-afp-for-time-machine-d8d67add1980
---

![Building a NAS with ZFS and AFP/Samba for Time Machine](/images/notes/building-nas-zfs.png)

## Summary

This GWLab article walks through building a NAS (Network Attached Storage) device using ZFS as the filesystem, with AFP (Apple Filing Protocol) or Samba configured as a Time Machine backup target. The result is a self-hosted backup solution for macOS that replaces iCloud or Apple Time Capsule with local storage on your own hardware.

ZFS is the appropriate filesystem for a NAS for several reasons: it provides data integrity via checksumming (detects and corrects bit rot), supports RAID-like redundancy via RAIDZ, has efficient snapshots and replication, and handles large storage pools reliably. The alternative on Linux for a NAS is typically mdadm with ext4 or Btrfs — ZFS tends to be more mature and trusted for long-term data integrity, though it requires more memory.

The Time Machine integration requires configuring the share correctly: AFP was historically required (macOS-native protocol), but modern macOS accepts Samba (SMB) for Time Machine backups, which simplifies the setup since AFP support in Linux is through the aging Netatalk daemon. The guide covers creating a ZFS pool, configuring the share with appropriate permissions, advertising it via Avahi (mDNS) so macOS discovers it automatically, and configuring macOS to use it as the backup destination.

## Key points

- Builds a self-hosted Time Machine backup target using ZFS + Linux + AFP or Samba.
- ZFS advantages for NAS: checksumming for bit rot detection, RAIDZ redundancy, efficient snapshots.
- Modern macOS accepts Samba for Time Machine — avoids maintaining the legacy Netatalk/AFP stack.
- Avahi (mDNS) advertises the share so macOS discovers it automatically in System Preferences.
- Self-hosted alternative to iCloud backup or Apple Time Capsule hardware.
- ZFS on Linux via OpenZFS — same filesystem used in TrueNAS for full-featured NAS builds.

[Original](https://blog.gwlab.page/building-nas-with-zfs-afp-for-time-machine-d8d67add1980)
