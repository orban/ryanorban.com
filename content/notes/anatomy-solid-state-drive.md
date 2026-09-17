---
title: Anatomy of a Solid-State Drive
date: 2012-10-20
categories:
  - storage
  - hardware
  - ssd
  - flash-memory
  - computer-architecture
description: ACM Queue deep dive into SSD internals — NAND flash cells, wear leveling, garbage collection, and how the FTL (Flash Translation Layer) hides the physical complexity from software. Essential for understanding why SSDs behave differently from spinning disks.
params:
  source: pinboard
  sourceUrl: https://queue.acm.org/detail.cfm?id=2385276
---

![Anatomy of a Solid-State Drive](/images/notes/anatomy-solid-state-drive.png)

## Summary

This ACM Queue article dissects the internal architecture of solid-state drives (SSDs), explaining how NAND flash memory cells work and how the controller firmware translates the block storage interface (which SSDs inherit from spinning hard disk drives) into the very different physical operations flash requires.

The fundamental mismatch is the unit of operation: SSDs can read or write at the page level (4–16 KB) but must erase at the block level (128–512 pages). You can't overwrite a page — you have to erase the whole block first, then write the new data. This constraint drives almost all SSD controller complexity. The Flash Translation Layer (FTL) handles this by maintaining a mapping table that translates logical block addresses (what the OS sees) to physical flash locations, enabling the controller to spread writes around and avoid overwriting active data in place.

Wear leveling is the other major mechanism. Each flash cell can only be erased and rewritten a finite number of times (10,000–100,000 times depending on cell type — MLC vs. SLC vs. TLC). The controller actively distributes writes across all flash blocks to ensure even wear, moving cold data around to give hot cells a rest. Garbage collection runs in the background to consolidate valid pages from partially-erased blocks so erase operations can proceed cleanly. These operations sometimes cause the write amplification phenomenon — where a single write from the OS triggers multiple internal writes.

## Key points

- NAND flash writes at page granularity but erases at block granularity — the core asymmetry that drives all SSD controller design.
- The Flash Translation Layer (FTL) maintains a logical-to-physical address map, enabling efficient write distribution and out-of-place updates.
- Wear leveling distributes writes to extend drive lifetime — each cell has a finite erase cycle count (MLC: ~10K, SLC: ~100K cycles).
- Write amplification: a single OS write can trigger multiple physical write operations due to garbage collection and page consolidation.
- SSDs inherit the block storage interface from HDDs for compatibility, but the underlying model is fundamentally different — which is why TRIM commands exist to help the FTL know which blocks are free.

[Original](https://queue.acm.org/detail.cfm?id=2385276)
