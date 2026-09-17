---
title: Dheeraj Pandey on Making Computing and Storage Converge
date: 2012-08-16
categories:
  - nutanix
  - hyperconverged
  - storage
  - compute
  - founders
description: TechCrunch 'In the Studio' interview with Nutanix CEO Dheeraj Pandey explaining the hyper-converged infrastructure vision — collapsing the traditional three-tier data center into a single software-defined appliance. Ryan noted it was a fantastic video at the time.
params:
  source: pinboard
  sourceUrl: http://techcrunch.com/2012/08/16/in-the-studio-nutanixs-dheeraj-pandey-is-making-computing-and-storage-converge/
---

## Summary

TechCrunch's In the Studio segment featuring Dheeraj Pandey, CEO and co-founder of Nutanix, explaining the convergence thesis that drove the company. The core idea: traditional enterprise data centers were built around three separate tiers — compute servers, storage (typically a SAN or NAS from EMC or NetApp), and a dedicated storage network (often Fibre Channel). Each tier required specialized hardware, specialized expertise, and separate management. Nutanix proposed collapsing all three into a single software-defined appliance.

Dheeraj Pandey's pitch was that the three-tier separation was an artifact of 1980s and 1990s technology constraints. When disk drives and compute lived on different hardware, a dedicated storage network and appliance made sense. But with commodity servers now shipping with enough local flash and disk, and with software sophisticated enough to manage distributed storage across a cluster (NDFS), there was no reason to maintain the separation. Every Nutanix node ran both compute workloads and a Controller VM (CVM) that presented virtualized storage to the hypervisor.

The video articulated a vision that hyper-converged infrastructure would eventually replace most traditional SAN deployments for enterprise virtualization workloads — a prediction that proved largely correct. Nutanix competed primarily with VMware vSAN, which followed a similar architectural approach within VMware's ecosystem.

## Key points

- Dheeraj Pandey explained the convergence thesis: compute + storage + networking in a single software-managed appliance.
- Traditional three-tier architecture (compute / SAN / Fibre Channel network) was a legacy of 1980s–90s hardware constraints.
- Each Nutanix node runs a Controller VM (CVM) that provides virtualized storage to the hypervisor.
- NDFS (Nutanix Distributed File System) handles data distribution, replication, and erasure coding across nodes.
- Competition primarily with VMware vSAN, which followed the same HCI convergence model within VMware's stack.

[Original](http://techcrunch.com/2012/08/16/in-the-studio-nutanixs-dheeraj-pandey-is-making-computing-and-storage-converge/)
