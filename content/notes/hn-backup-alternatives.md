---
title: "Backup Tool Alternatives: HN Thread"
date: 2021-07-26
categories:
  - backup
  - tools
  - linux
  - sysadmin
  - open-source
description: Hacker News thread cataloging backup tool alternatives — attic, borg, restic, and others — with practitioner perspectives on which holds up at scale. The comment thread is where the real comparison happens.
params:
  source: pinboard
  sourceUrl: https://news.ycombinator.com/item?id=27958996
---

## Summary

This Hacker News thread aggregates practitioner views on backup tool alternatives, specifically listing attic, BorgBackup (borg), restic, and similar tools. The HN community is particularly good at producing comparative tool discussions: you get people who've run each option in production at scale, with real opinions about reliability, performance edge cases, and operational overhead.

The key tools in this space as of 2021:

- BorgBackup: fork of attic that became the community standard after attic development stalled. Deduplicating, compressing, encrypting backups. Strong compression ratios for typical file backups.
- restic: Go-based, designed with cloud backends in mind (S3, B2, Google Cloud, etc.). Snapshot-based, content-addressed, encrypted by default. Often faster for cloud targets.
- Duplicati: More user-friendly UI, cross-platform, designed for less technical users.
- ZFS send/receive: For ZFS users, often the best option — snapshots are first-class, incremental sends are efficient.

The tradeoffs: BorgBackup is the strongest for local/SSH targets and has excellent deduplication. restic wins when your target is cloud object storage. ZFS wins if your data is already on ZFS. None of them is universally better.

## Key points

- BorgBackup (borg): attic successor, best-in-class deduplication and compression for local/SSH backup.
- restic: Go-based, cloud-native (S3/B2/GCS), encrypted by default — better for cloud targets than borg.
- ZFS send/receive: best option if already on ZFS; snapshot-based and very efficient incrementally.
- Deduplication matters at scale: borg/restic both content-address data so identical chunks aren't stored twice.
- HN threads on tool comparisons are often more useful than official documentation for understanding real-world tradeoffs.

[Original](https://news.ycombinator.com/item?id=27958996)
