---
title: Mellanox Introduces RDMA-Based Virtual SAN Software Appliance
date: 2012-08-27
categories:
  - storage
  - networking
  - rdma
  - infiniband
  - san
  - infrastructure
description: Mellanox announced a Virtual SAN software appliance built on RDMA that claimed 6x the performance of traditional Fibre Channel SAN hardware. A signal that software-defined storage was coming for legacy enterprise SAN.
params:
  source: pinboard
  sourceUrl: http://ir.mellanox.com/releasedetail.cfm?ReleaseID=702438
---

![Mellanox Introduces RDMA-Based Virtual SAN Software Appliance](/images/notes/mellanox-rdma-vsan.png)

## Summary

Mellanox Technologies announced a new Virtual SAN (vSAN) software appliance built on RDMA (Remote Direct Memory Access) networking, claiming 6x higher performance than Fibre Channel SAN hardware. The move was surprising because Mellanox Technologies was primarily a networking vendor — their entry into storage software signaled the blurring of boundaries between networking and storage infrastructure.

RDMA enables direct memory-to-memory transfers across a network without CPU involvement, dramatically reducing latency and CPU overhead compared to iSCSI or Fibre Channel. By building a virtual SAN on top of InfiniBand or RDMA over Converged Ethernet (RoCE), Mellanox Technologies achieved throughput that traditional SAN hardware couldn't match. The VSA ran as software on commodity servers, eliminating the need for dedicated storage hardware.

The broader context: 2012 was the year software-defined storage began seriously challenging SAN hardware vendors. Nutanix was gaining traction with their hyper-converged infrastructure approach, VMware was building their own vSAN, and now a networking vendor was doing it too. The message was clear: dedicated storage appliances from legacy vendors like EMC, NetApp, and Hitachi were facing software-defined disruption from multiple directions simultaneously.

## Key points

- RDMA-based virtual SAN delivers 6x performance over Fibre Channel SAN hardware at significantly lower cost.
- Mellanox Technologies crossing from networking into storage software — a telling category boundary violation.
- RDMA eliminates CPU involvement in data transfer, enabling microsecond-level storage latency that traditional SAN protocols couldn't achieve.
- InfiniBand and RoCE (RDMA over Converged Ethernet) as the physical transport layers.
- Signals the accelerating shift from dedicated SAN hardware to software-defined storage running on commodity servers.

[Original](http://ir.mellanox.com/releasedetail.cfm?ReleaseID=702438)
