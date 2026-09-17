---
title: "Fusion-io Acquires ID7: Doubling Down on Software-Defined Storage"
date: 2013-03-18
categories:
  - storage
  - flash
  - software-defined-storage
  - fusion-io
  - enterprise-it
description: Fusion-io's 2013 acquisition of ID7 to expand into software-defined storage — a flash storage vendor trying to move up the stack. The bookmark's annotation noted skepticism about the iSCSI dependency.
params:
  source: pinboard
  sourceUrl: http://siliconangle.com/blog/2013/03/18/fusion-io-acquires-id7-delves-deeper-into-software-defined-storage/
---

![Fusion-io Acquires ID7: Doubling Down on Software-Defined Storage](/images/notes/fusion-io-software-defined-storage.png)

## Summary

Fusion-io was the dominant PCIe flash card vendor in 2013 — their ioMemory cards were used by Facebook, Apple, and other hyperscalers to eliminate storage bottlenecks for latency-sensitive workloads. The ID7 acquisition was an attempt to move up the stack from raw flash hardware into software-defined storage (SDS) — a trend that was gaining traction as the industry recognized that storage value was moving from hardware to the software managing it.

Software-defined storage in 2013 meant decoupling storage control logic from proprietary hardware appliances — letting commodity servers with flash or spinning disk run storage software that previously ran on expensive purpose-built arrays. VMware's VSAN, Ceph, GlusterFS, and ScaleIO were all competing in this space. For Fusion-io, SDS was a natural extension: their hardware gave you the raw performance; the SDS software layer gave you the data management, deduplication, tiering, and replication features that enterprises needed.

The bookmark's annotation called out that the approach was still iSCSI-dependent — a meaningful criticism. iSCSI is a protocol that runs block storage over standard IP networking, making it cheaper than Fibre Channel SAN but still carrying the overhead of a network protocol stack. For a company whose value proposition was NVMe-speed flash, building a product on iSCSI was architecturally conservative. The industry was moving toward NVMe-oF (NVMe over Fabrics) for exactly this reason, though that standard wouldn't be finalized until 2016.

## Key points

- Fusion-io was a PCIe flash card vendor moving up the stack into software-defined storage via the ID7 acquisition.
- Software-defined storage decouples storage management software from proprietary hardware — a major enterprise IT trend in 2013–2015.
- iSCSI dependency was a legitimate criticism: for flash performance to shine, the network protocol overhead of iSCSI is a bottleneck vs. NVMe-oF.
- Fusion-io was acquired by SanDisk in 2014, which was then acquired by Western Digital in 2016 — the flash consolidation wave.
- The SDS market split between open-source (Ceph, GlusterFS) and commercial (Pure Storage, Nutanix, VMware VSAN) — most proprietary vendors lost.

[Original](http://siliconangle.com/blog/2013/03/18/fusion-io-acquires-id7-delves-deeper-into-software-defined-storage/)
