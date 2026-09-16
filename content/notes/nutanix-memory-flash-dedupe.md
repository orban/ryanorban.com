---
title: Nutanix Adds Memory and Flash De-duplication
date: 2013-08-20
categories:
  - nutanix
  - hyperconvergence
  - storage
  - deduplication
  - enterprise
description: The Register covering Nutanix OS adding memory and flash deduplication — plus the detail that EMC chairman Joe Tucci personally flew in to save a deal Nutanix won anyway. A snapshot of Nutanix disrupting legacy storage incumbents in 2013.
params:
  source: pinboard
  sourceUrl: http://www.theregister.co.uk/2013/08/20/nutanix_os_converged_system_update/
---

![Nutanix Adds Memory and Flash De-duplication](/images/notes/nutanix-memory-flash-dedupe.png)

## Summary

The Register reported on Nutanix OS updates adding deduplication at both the memory (RAM) and flash tiers of their hyper-converged infrastructure platform. Memory-tier deduplication is particularly valuable in VDI (Virtual Desktop Infrastructure) environments: when hundreds of VMs run the same operating system, identical memory pages can share physical RAM rather than being duplicated per-VM. Flash deduplication reduces write amplification and extends SSD lifespan.

The more memorable detail: "At one point, EMC chairman Joe Tucci was flown in to try to save the seven-figure deal, but Nutanix prevailed." This vignette captured the disruption dynamic perfectly — EMC, then the dominant enterprise storage vendor, was so threatened by Nutanix winning enterprise accounts that their chairman personally intervened. A startup beating incumbents at the executive level was a strong signal that HCI was genuinely threatening the traditional SAN/NAS model.

Nutanix in 2013 was still pre-IPO (IPO in 2016) but already winning against EMC, NetApp, and HP in storage procurement. The software-defined, scale-out approach was simpler to manage and cheaper to scale than three-tier architecture. Adding deduplication made the cost comparison even more favorable — less raw flash needed per workload.

## Key points

- Memory deduplication: identical VM pages share physical RAM — critical for VDI where many VMs share the same OS image.
- Flash deduplication: reduces write amplification and effective capacity requirements — key for economics of all-flash deployments.
- EMC chairman Joe Tucci personally intervening in deals: concrete evidence that Nutanix was winning enterprise-scale accounts, not just SMB.
- NOS (Nutanix OS) was the differentiator — the hardware was commodity x86; the value was entirely in the software stack.
- VMware vSAN was also emerging as a competing HCI option — Nutanix needed to differentiate on features and operational simplicity.
- Context: Nutanix founded 2009, still 3 years from IPO — this phase was proving enterprise viability at scale.

[Original](http://www.theregister.co.uk/2013/08/20/nutanix_os_converged_system_update/)
