---
title: Enabling vSphere Content-Based Read Cache for Citrix XenDesktop
date: 2013-02-14
categories:
  - vmware
  - vsphere
  - citrix
  - xendesktop
  - vdi
  - caching
description: Technical guide to enabling VMware vSphere's Content-Based Read Cache (CBRC) for Citrix XenDesktop VDI deployments — a storage performance optimization for virtual desktop infrastructure using host-side SSD caching.
params:
  source: pinboard
  sourceUrl: http://blog.whatwoulddando.com/2012/03/19/enabling-vsphere-content-based-read-cache-for-citrix-xendesktop/
---

## Summary

This technical guide covered enabling VMware vSphere's Content-Based Read Cache (CBRC) feature — also known as vFlash Read Cache in later versions — specifically for Citrix XenDesktop VDI (Virtual Desktop Infrastructure) deployments. CBRC was a host-side caching mechanism that used SSD capacity on ESXi hosts to cache frequently read storage blocks, reducing read latency for storage-intensive workloads.

VDI was one of the most storage-intensive enterprise workloads in 2012-2013. Booting hundreds of virtual desktops simultaneously created boot storms — massive spikes in IOPS on the shared SAN that overwhelmed traditional spinning disk arrays. CBRC addressed this by keeping frequently-accessed read blocks (OS pages, application binaries) cached on the ESXi host's SSD, so boot storm reads hit local SSD rather than the SAN over the network.

The specific combination of VMware vSphere + Citrix XenDesktop was very common in enterprise desktop virtualization. VMware provided the hypervisor layer; Citrix provided the connection brokering and protocol (ICA/HDX). Enabling CBRC required vSphere 5.x and appropriate SSD hardware on the host.

## Key points

- CBRC/vFlash Read Cache: host-side SSD cache for read-heavy VDI workloads — significantly reduces SAN IOPS demand during boot storms
- VDI boot storms: hundreds of simultaneous desktop boots create synchronized IOPS spikes — the primary storage design challenge for VDI
- The VMware+Citrix stack was the dominant enterprise VDI architecture in 2012-2013: vSphere + XenDesktop + Citrix NetScaler
- SSD price curves in 2012-2013 were making host-side SSD caching practical — SSDs were still expensive but affordable for this use case
- Replaced by purpose-built hyperconverged solutions (Nutanix, VMware vSAN) and cloud VDI services (Azure Virtual Desktop) over the following years

[Original](http://blog.whatwoulddando.com/2012/03/19/enabling-vsphere-content-based-read-cache-for-citrix-xendesktop/)
