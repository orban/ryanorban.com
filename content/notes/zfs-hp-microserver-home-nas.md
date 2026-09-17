---
title: "How I Store My 1's and 0's: ZFS + Bargain HP Microserver = JOY"
date: 2012-06-17
categories:
  - storage
  - zfs
  - home-lab
  - nas
  - self-hosting
  - hardware
description: A practical guide to building a home NAS with ZFS on a cheap HP ProLiant Microserver N36L — a popular entry-level home server that punched above its weight for storage. ZFS's data integrity features made it the file system of choice for anyone who cared about bit-rot.
params:
  source: pinboard
  sourceUrl: http://mocko.org.uk/b/2012/06/17/how-i-store-my-1s-and-0s-zfs-bargain-hp-microserver-joy/
---

![How I Store My 1's and 0's: ZFS + Bargain HP Microserver = JOY](/images/notes/zfs-hp-microserver-home-nas.png)

## Summary

The HP ProLiant Microserver N36L was a cult favorite in home-lab circles around 2011-2012: cheap (often under $200 after rebate), quiet, small, and capable of holding 4 drives plus an optical bay. Combined with ZFS — the filesystem originally from Sun Microsystems that became available on Linux via ZFS on Linux (ZoL) and illumos distributions — it was a DIY NAS solution that matched or exceeded purpose-built NAS appliances from Synology or QNAP at lower cost.

ZFS was attractive for home storage because of its data integrity guarantees. Traditional filesystems trust the disk controller and RAID adapter to faithfully report what they store; ZFS uses checksums on every block and validates data on every read. Silent data corruption — bit rot from cosmic rays, flipped bits, or faulty drives — is caught and corrected. Combined with RAIDZ (ZFS's software RAID that avoids the RAID-5 write hole), ZFS gave home users enterprise-grade data protection without enterprise-grade hardware.

The tradeoff was RAM appetite — ZFS's adaptive replacement cache (ARC) is aggressive about using RAM for read caching, and the rule of thumb was 1GB RAM per 1TB of storage. On a Microserver limited to 8GB, this constrained pool sizes. But for a home NAS serving a few terabytes, it worked.

## Key points

- HP ProLiant Microserver N36L: ~$200 after rebate, 4 drive bays, AMD Turion, 2GB RAM expandable to 8GB — the entry point for serious home NAS builds circa 2012.
- ZFS data integrity: checksums on every block, detects and corrects silent corruption that RAID alone misses.
- RAIDZ1/RAIDZ2: ZFS software RAID without the write-hole problem of hardware RAID-5.
- ARC (adaptive replacement cache): ZFS uses RAM aggressively for caching — 1GB per 1TB rule of thumb.
- FreeNAS (now TrueNAS) provided the OS; ZFS on Linux brought ZFS to Debian/Ubuntu for those preferring Linux.

[Original](http://mocko.org.uk/b/2012/06/17/how-i-store-my-1s-and-0s-zfs-bargain-hp-microserver-joy/)
