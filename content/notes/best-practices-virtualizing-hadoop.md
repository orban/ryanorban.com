---
title: Best Practices for Virtualizing Hadoop
date: 2013-05-01
categories:
  - hadoop
  - vmware
  - virtualization
  - hortonworks
  - infrastructure
description: Hadoop Summit presentation on best practices for running Hadoop on VMware HVE (Hadoop Virtualization Extensions) with Hortonworks HDP — addressing the core tension between virtualization flexibility and Hadoop's data locality requirements.
params:
  source: pinboard
  sourceUrl: http://www.slideshare.net/Hadoop_Summit/best-practices-for-virtualizing-hadoop
---

![Best Practices for Virtualizing Hadoop](/images/notes/best-practices-virtualizing-hadoop.png)

## Summary

This Hadoop Summit presentation covered running Apache Hadoop workloads on VMware infrastructure using Hadoop Virtualization Extensions (HVE) with Hortonworks Data Platform (HDP). In 2013 this was a contested topic: the conventional wisdom was that Hadoop should run on bare metal because virtualization overhead degraded the I/O-intensive HDFS and MapReduce workloads. HVE was VMware's answer — a set of extensions specifically designed to preserve data locality when running Hadoop in VMware vSphere VMs.

The core challenge: HDFS data locality (running map tasks on the nodes that hold the data replicas) is one of Hadoop's primary performance optimizations. In a virtualized environment, VMs can migrate between physical hosts via vMotion, breaking the co-location assumption. HVE addressed this by exposing rack topology information to the Hadoop namenode through a custom rack awareness plugin, and by pinning data-intensive VMs to the physical hosts holding their HDFS data.

The case for virtualization despite these complications: operational flexibility (standard VM management, snapshot, HA, and DRS tooling), resource sharing between Hadoop and other workloads, and multi-tenancy. Running separate Hadoop and OLTP clusters on dedicated bare metal meant low utilization during off-peak hours; virtualization allowed resource pooling. The tradeoff was real but manageable for many workloads.

## Key points

- HVE (Hadoop Virtualization Extensions): VMware extensions exposing physical topology to Hadoop's rack awareness mechanism — preserves data locality hints even when VMs could migrate
- vMotion is the enemy of data locality: when VMs migrate to different physical hosts, map tasks lose co-location with their data
- **CPU overhead**: minimal for Hadoop (CPU isn't the bottleneck); **I/O overhead**: significant — VMware's VMDK storage layer adds latency vs. direct disk access
- PVSCSI (paravirtual SCSI) and VMXNET3 network adapter recommendations: para-virtualized drivers substantially reduce virtualization overhead vs. emulated devices
- **Sizing**: Hadoop VMs benefit from large sizes (8-16 vCPU, 32-64GB RAM) that map closely to physical partitions — avoids NUMA splits and network overhead
- Context: this debate was settled by cloud Hadoop services (AWS EMR, GCP Dataproc) which demonstrated that managed virtualized Hadoop at scale was viable

[Original](http://www.slideshare.net/Hadoop_Summit/best-practices-for-virtualizing-hadoop)
