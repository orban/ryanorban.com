---
title: "Nutanix: My Experience on a Recent VDI POC"
date: 2013-04-26
categories:
  - nutanix
  - vdi
  - hyperconverged-infrastructure
  - vmware
  - enterprise-it
description: An end-user IT practitioner's honest review of a Nutanix proof-of-concept for VDI workloads in 2013 — notable for being a real hands-on assessment rather than vendor marketing, at a time when Nutanix was still establishing itself in enterprise IT.
params:
  source: pinboard
  sourceUrl: http://infrastructureguy.wordpress.com/2013/04/25/nutanix-my-experience-on-a-recent-vdi-poc/
---

## Summary

This infrastructureguy WordPress blog post was a practitioner-written review of a Nutanix proof-of-concept for Virtual Desktop Infrastructure (VDI) in 2013. Its value was being an independent, no-bullshit assessment from someone who actually ran the workload — at a time when most Nutanix content was vendor-produced. The author tested a Nutanix cluster running VMware View and assessed it against the traditional approach of separate compute (Cisco UCS) and storage (EMC or NetApp).

Nutanix was founded in 2009 and was at this point in early enterprise adoption — proving the hyperconverged infrastructure (HCI) concept against incumbents. Their architecture co-located storage and compute in the same nodes, with a distributed Controller VM on each node providing a unified storage layer. For VDI, the key benefits were: fast local I/O for boot storms (thousands of VMs starting simultaneously), simplified operations (one vendor instead of separate compute and storage), and linear scale (add nodes to add both compute and storage together).

The POC review noted both strengths (the boot storm performance was notably better than traditional SAN-backed configurations; the simplicity was real) and limitations (the vendor lock-in to Nutanix hardware, the learning curve of the Nutanix CLI and Prism management interface, and the premium cost versus traditional infrastructure). This kind of honest practitioner review was valuable for the enterprise IT community navigating whether HCI was real or hype.

## Key points

- Hyperconverged infrastructure value proposition for VDI: co-located storage eliminates SAN I/O bottleneck during boot storms — the killer VDI workload
- Nutanix vs. traditional: simpler (one vendor, one management plane) at the cost of vendor lock-in and higher per-node price
- Prism management UI: central control plane for the cluster, ahead of traditional server management interfaces at the time
- Controller VM (CVM): runs on every node, provides the storage abstraction layer — the architectural element that enables local reads without application awareness
- Context: Nutanix was in the process of displacing EMC VxRail, Dell PowerEdge, and traditional 3-tier architecture (separate compute/network/storage) in enterprise VDI deployments
- HCI market proved real: Nutanix and VMware vSAN became dominant in enterprise virtualization by 2017-2018

[Original](http://infrastructureguy.wordpress.com/2013/04/25/nutanix-my-experience-on-a-recent-vdi-poc/)
