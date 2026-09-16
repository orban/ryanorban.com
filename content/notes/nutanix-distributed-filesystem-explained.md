---
title: Simple Explanation of How Nutanix Works
date: 2013-05-22
categories:
  - nutanix
  - distributed-systems
  - storage
  - hyperconvergence
  - explainer
description: A YouTube explainer of how Nutanix's distributed file system works — covering the Curator distributed metadata service, erasure coding, data placement, and how Nutanix collocates compute and storage in a hyper-converged node. Simple enough for sales conversations, technically accurate.
params:
  source: pinboard
  sourceUrl: http://www.youtube.com/watch?v=nSqwAxhFpA8
---

## Summary

This YouTube video provides an accessible explanation of Nutanix's distributed file system — the Nutanix Distributed File System (NDFS) that underlies their hyper-converged infrastructure platform. The explanation covers how Nutanix collocates compute and storage in each node, how data is replicated across the cluster, and how the Curator distributed metadata service manages data placement.

The core architectural insight: rather than having a centralized SAN (Storage Area Network) that all compute nodes access over a network, Nutanix puts storage and compute in the same physical node. VMs read from local flash storage (fast) and writes are replicated asynchronously to other nodes for redundancy. The controller VM in each node manages the storage stack; there's no external storage controller.

This architecture is what makes Nutanix feel like a storage appliance that's also a compute platform — they're inseparable. Adding a node to the cluster adds both compute and storage capacity simultaneously. The Acropolis hypervisor (introduced later) and AHV management layer added full stack control, but the storage architecture was always the differentiating layer.

## Key points

- Each Nutanix node = compute (CPU/RAM) + storage (SSD + HDD) + Controller VM (CVM)
- Controller VM manages local storage; presents it as a distributed block/file/object store to hosted VMs
- Replication factor 2 or 3: data is written to local SSD + replicated to 1-2 other nodes automatically
- Curator service: distributed metadata manager, handles data placement, rebalancing, and deduplication jobs
- Read performance: local flash (microseconds); write performance: local flash + async replication
- Scale-out: adding nodes increases both compute and storage — no separate storage scaling step

[Original](http://www.youtube.com/watch?v=nSqwAxhFpA8)
