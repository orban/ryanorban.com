---
title: Nutanix Engineer Explains Why His Appliance Makes Sense for Analytics
date: 2013-07-17
categories:
  - nutanix
  - analytics
  - hadoop
  - infrastructure
  - data-center
description: SiliconAngle interview with a Nutanix engineer making the case for why hyper-converged infrastructure is well-suited to analytics workloads in 2013. Nutanix was positioning its appliances as a natural home for Hadoop alongside traditional virtualization.
params:
  source: pinboard
  sourceUrl: http://siliconangle.com/blog/2013/07/16/nutanix-engineer-explains-why-his-companys-appliance-makes-sense-for-analytics/
---

![Nutanix Engineer Explains Why His Appliance Makes Sense for Analytics](/images/notes/nutanix-analytics-appliance.png)

## Summary

This SiliconAngle piece featured a Nutanix engineer explaining the technical case for running analytics workloads — specifically Hadoop — on Nutanix's hyper-converged infrastructure appliances. The argument ran against the prevailing assumption that Hadoop required dedicated commodity servers rather than a converged virtualization platform.

The core technical claim: Nutanix's NDFS (Nutanix Distributed File System) could serve as a drop-in replacement for HDFS in a Hadoop deployment, while sharing the same hardware as the virtualization workloads running on the same cluster. This meant an organization didn't need separate physical infrastructure for analytics vs. production — the same Nutanix nodes could run VMware vSphere VMs and Hadoop jobs in isolated but co-located workloads.

The counter-argument from pure-play Hadoop operators: data locality — placing compute tasks on the same node as the data — was harder to guarantee in a converged setup than in a dedicated Hadoop cluster where data placement was tightly controlled. Nutanix's response was that their distributed file system handled this transparently and that operational simplicity of a single platform outweighed the theoretical locality advantage of dedicated hardware.

## Key points

- NDFS (Nutanix Distributed File System) positioned as an HDFS-compatible layer — enabling Hadoop workloads on Nutanix hardware without a dedicated cluster.
- Convergence pitch: fewer hardware silos, single management plane via Prism, linear scale-out for both analytics and virtualization.
- The data locality tension: Hadoop was designed around moving compute to data; Nutanix's model required the distributed file system to handle locality transparently.
- Hortonworks certification partnership (announced around this time) gave enterprise credibility to Nutanix's Hadoop story.

[Original](http://siliconangle.com/blog/2013/07/16/nutanix-engineer-explains-why-his-companys-appliance-makes-sense-for-analytics/)
