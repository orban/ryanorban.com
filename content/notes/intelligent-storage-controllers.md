---
title: How Intelligent Storage Controllers Have Revolutionized the Industry
date: 2013-04-16
categories:
  - storage
  - hardware
  - data-center
  - infrastructure
  - flash
description: DatacenterKnowledge on how intelligent storage controllers — combining flash cache, tiering, and deduplication — changed enterprise storage from dumb arrays into software-defined platforms. A 2013 snapshot of the transition away from spinning-disk-only storage architectures.
params:
  source: pinboard
  sourceUrl: http://www.datacenterknowledge.com/archives/2013/04/15/how-intelligent-storage-controllers-have-revolutionized-the-industry/
---

## Summary

By 2013, enterprise storage was in the middle of a major architectural shift. Traditional SAN and NAS arrays used dumb RAID controllers — hardware that managed parity and mirroring across spinning disks but did little else. The new generation of intelligent storage controllers added flash as a first-class tier, inline deduplication and compression, thin provisioning, and automated data tiering — moving hot data to SSD and cold data to high-capacity HDD without manual intervention.

EMC, NetApp, Pure Storage, and Violin Memory were competing in this space, each with different architectures for integrating flash. EMC FAST (Fully Automated Storage Tiering) and NetApp Flash Cache represented the hybrid approach — flash as an intelligent cache in front of disk. Pure Storage and Violin Memory went all-flash. The intelligent controller was the differentiator: the same NAND flash could perform very differently depending on how well the controller managed wear leveling, garbage collection, and I/O scheduling.

The business impact was real for virtualization-heavy data centers. VMware workloads with random I/O patterns — terrible for spinning disk latency — became much more tractable with flash-backed controllers. VDI (Virtual Desktop Infrastructure) was a particularly acute case: dozens of virtual desktops doing simultaneous random reads at boot time would saturate a traditional array, but an intelligent flash-backed controller could absorb the I/O storm.

## Key points

- Storage tiering: automated movement of hot data to SSD, warm data to high-capacity HDD — intelligent controllers do this transparently.
- Inline deduplication and compression: reduce effective storage cost, but require significant controller compute — why flash matters for controller performance.
- All-flash arrays (Pure Storage, Violin Memory) vs. hybrid arrays (EMC, NetApp): architectural split that defined the storage industry through 2016.
- VMware workload compatibility: random I/O from virtualized workloads drove flash adoption — the pain was acute enough to justify premium pricing.
- IOPS as the new unit: the industry shifted from GB/TB pricing conversations to IOPS/latency conversations as flash changed the bottleneck.

[Original](http://www.datacenterknowledge.com/archives/2013/04/15/how-intelligent-storage-controllers-have-revolutionized-the-industry/)
