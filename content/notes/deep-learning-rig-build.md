---
title: Building a Deep Learning Rig (Part 2)
date: 2024-02-25
categories:
  - hardware
  - gpu
  - deep-learning
  - home-lab
  - training
description: "Part 2 of building a home deep learning rig: upgrading to a Threadripper 1920X to support three RTX 3090s with full PCIe bandwidth. Total cost €2,379. Key lesson: GPU peer-to-peer DDP failures were fixed by downgrading the NVIDIA driver, not hardware changes."
params:
  source: pinboard
  sourceUrl: https://samsja.github.io/blogs/rig/part_2/
---

![Building a Deep Learning Rig (Part 2)](/images/notes/deep-learning-rig-build.png)

## Summary

This is the second part of a home GPU cluster build, documenting an upgrade to a Threadripper 1920X + X399 motherboard to properly support three RTX 3090s with adequate PCIe bandwidth. The previous setup had limited bandwidth sharing between GPUs; the Threadripper platform provides enough PCIe lanes to feed three cards properly for distributed training.

The most instructive part of the post is the debugging story: peer-to-peer GPU communication was failing during DDP (Distributed Data Parallel) training, which seemed like a hardware or BIOS configuration issue. After working through IOMMU settings and kernel parameters, the fix turned out to be simply downgrading from NVIDIA driver version 545 to 535. Driver version incompatibilities causing subtle multi-GPU failures are notoriously hard to diagnose — this is a useful data point.

A 285W power cap per card (vs. 350W default) produced minimal performance loss while keeping temperatures under 70°C and enabling quiet home operation. Total build cost was €2,379. The author notes that cloud GPU costs are competitive once you factor in electricity and hardware risk, but the home rig provides deeper engagement with optimization.

## Key points

- Threadripper 1920X + X399 motherboard for adequate PCIe bandwidth across three RTX 3090s.
- Total build: €2,379 (CPU/mobo €425 secondhand, 2TB NVMe €119, accessories €254, plus existing GPUs).
- DDP peer-to-peer failures fixed by driver downgrade (545 → 535) — not hardware.
- 285W power cap per GPU: minimal performance loss, under 70°C, quiet home operation.
- Home rigs pay off for learning and optimization; cloud remains competitive on cost/risk.

[Original](https://samsja.github.io/blogs/rig/part_2/) → GitHub
