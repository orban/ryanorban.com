---
title: Basic Configuration of the Nutanix 2RU Block
date: 2012-10-24
categories:
  - nutanix
  - hyperconverged
  - data-center
  - configuration
  - storage
description: An overview of what to expect when deploying a new Nutanix 2U block in 2012 — the physical setup, node configuration, and initial software steps for the hyperconverged appliance that was then challenging traditional SAN/NAS architectures.
params:
  source: pinboard
  sourceUrl: http://coogee.wordpress.com/2012/10/23/basic-configuration-of-the-nutanix-2ru-block/
---

## Summary

This post by ccstockwell on the Classical Data blog walks through the initial configuration of a Nutanix 2U (two rack unit) block when it first arrives. In 2012, Nutanix was shipping its early hardware — a 2U chassis containing 4 nodes, each a complete compute and storage unit that participated in the hyperconverged infrastructure cluster. Getting one of these into production required understanding the physical layout, networking configuration, and the Nutanix Distributed File System (NDFS) that tied the nodes together.

The post was written at a time when Nutanix was moving from early adopters to more mainstream enterprise deployments, and practitioners were sharing configuration knowledge publicly — there wasn't yet a large body of vendor documentation or community guides. The content was valuable because Nutanix's architecture was genuinely novel: traditional SAN deployments had separate storage configuration steps (zone the array, provision LUNs, configure HBAs), but Nutanix collapsed this into a unified setup where compute and storage were configured together through the same interface.

The Nutanix 2RU block represented the hyperconverged infrastructure value proposition in hardware form: replace a separate server, network switch, and storage array with a single dense appliance that scaled horizontally by adding nodes. The Controller VM (CVM) running on each node provided the storage layer, while VMware vSphere or Hyper-V ran the workload VMs alongside it.

## Key points

- The Nutanix 2U block contains 4 independent nodes — each with its own CPU, RAM, and flash/disk — managed as a unified cluster.
- Controller VM (CVM) per node: a dedicated VM that provides the storage layer for the whole cluster, abstracting the physical drives.
- Initial setup in 2012 required network configuration, IPMI access, and cluster formation through Nutanix's management interface.
- NDFS (Nutanix Distributed File System) replicates data across nodes for redundancy — no separate SAN required.
- Community-written guides like this were essential in early Nutanix adoption; vendor documentation hadn't caught up to practitioner needs.

[Original](http://coogee.wordpress.com/2012/10/23/basic-configuration-of-the-nutanix-2ru-block/)
