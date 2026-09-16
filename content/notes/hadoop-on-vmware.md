---
title: "Hadoop on VMware: Another Workload Conquered?"
date: 2013-05-22
categories:
  - hadoop
  - vmware
  - virtualization
  - infrastructure
  - big-data
description: EMC's Chuck Hollis on running Hadoop workloads on VMware virtualization — the argument that bare-metal Hadoop deployments could be replaced by virtualized clusters with manageable performance trade-offs. A 2013 salvo in the bare-metal vs. virtualization debate for big data workloads.
params:
  source: pinboard
  sourceUrl: http://chucksblog.emc.com/chucks_blog/2013/05/hadoop-on-vmware-another-workload-conquered.html
---

## Summary

Chuck Hollis (EMC's CTO of global marketing) argued in this 2013 post that Hadoop workloads had been successfully virtualized on VMware, challenging the conventional wisdom that Hadoop required bare-metal deployment for performance reasons. The traditional concern: Hadoop's performance depends on local disk I/O (data locality principle — move the compute to the data, not the data to the compute), and VMware's virtualization layer adds overhead that disrupts this.

The EMC/VMware position: the overhead is modest and manageable, and the operational benefits of virtualization (live migration, resource pooling, simpler management, multi-tenancy) outweigh the performance cost for many workloads. They published benchmark numbers showing virtualized Hadoop clusters performing within 10-15% of bare-metal for typical MapReduce jobs.

This debate resolved over the following years in a different direction: neither bare-metal nor VMware became the dominant Hadoop deployment model. Instead, cloud-managed services (Amazon EMR, Google Dataproc, Azure HDInsight) replaced both, and eventually Apache Spark on Kubernetes became the modern stack. The Hadoop-on-VMware argument became moot.

## Key points

- Hadoop's data locality principle assumes local disk reads — virtualization can disrupt this, adding network overhead
- EMC/VMware claimed <15% performance overhead for virtualized Hadoop vs bare-metal in benchmarks
- The operational argument: VM live migration, resource pooling, and multi-tenancy simplify Hadoop cluster management
- Nutanix's hyper-converged infrastructure was an alternative that collapsed storage and compute at the hardware level
- Both VMware-Hadoop and bare-metal Hadoop lost to cloud-managed services by 2016-2018
- A 2013 snapshot of incumbents trying to absorb the Hadoop disruption into existing sales motions

[Original](http://chucksblog.emc.com/chucks_blog/2013/05/hadoop-on-vmware-another-workload-conquered.html)
