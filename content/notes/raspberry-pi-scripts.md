---
title: Raspberry Pi Setup Scripts
date: 2012-12-18
categories:
  - raspberry-pi
  - linux
  - shell
  - embedded-systems
  - maker
description: A GitHub Gist with setup scripts for the Raspberry Pi, including the essential dd command for writing a Raspbian image to an SD card. A practical reference from 2012 when the Pi was new and setup guides were scarce.
params:
  source: pinboard
  sourceUrl: https://gist.github.com/4322201
---

![Raspberry Pi Setup Scripts](/images/notes/raspberry-pi-scripts.png)

## Summary

A practical GitHub Gist containing shell scripts and commands for setting up a Raspberry Pi, saved in late 2012 — shortly after the Pi launched in February of that year. The most fundamental snippet is the dd command for flashing a Raspbian disk image to an SD card:

```bash
sudo dd bs=1m if=raspbian.img of=/dev/rdisk1
```

This was the canonical way to write the OS image before tools like Balena Etcher existed. Using `/dev/rdisk1` (the raw disk device) instead of `/dev/disk1` significantly speeds up the write on macOS by bypassing kernel buffering.

In 2012, the Raspberry Pi community was newly forming and setup documentation was scattered across forums. Gists like this were a primary knowledge-sharing mechanism — developers collected the commands that actually worked and published them for others.

## Key points

- `dd bs=1m if=raspbian.img of=/dev/rdisk1` — the essential SD card flash command on macOS
- `/dev/rdisk` vs `/dev/disk` — raw device is significantly faster on macOS for large sequential writes
- Raspbian (now Raspberry Pi OS) was the recommended distribution from day one
- The Raspberry Pi launched February 2012; by December 2012 the ecosystem was still very early
- SSH and GPIO access were the primary entry points for Pi projects at this stage

[Original](https://gist.github.com/4322201)
