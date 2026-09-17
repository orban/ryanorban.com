---
title: A Tour Inside CloudFlare's Latest Generation Servers
date: 2013-07-22
categories:
  - infrastructure
  - servers
  - cloudflare
  - hardware
  - data-center
description: CloudFlare's 2013 tour of their latest server hardware — SSDs, 10GigE NICs, DRAM cache tiers, and non-RAID storage architecture. Ryan's bookmark note compared it favorably to Nutanix's approach to hyper-converged storage.
params:
  source: pinboard
  sourceUrl: http://blog.cloudflare.com/a-tour-inside-cloudflares-latest-generation-servers
---

![A Tour Inside CloudFlare's Latest Generation Servers](/images/notes/cloudflare-latest-generation-servers.png)

## Summary

CloudFlare published a detailed look at the hardware architecture of their 2013 server generation. The design prioritized read latency and bandwidth over raw compute: each server uses SSD as a primary storage tier, with a large DRAM cache layer in front of it and 10 Gigabit Ethernet network interconnects. The non-RAID storage philosophy was deliberate — at CloudFlare's scale, software-level redundancy across many nodes is more reliable and cost-effective than hardware RAID within a single machine.

Ryan's bookmark note called it out as looking just like Nutanix — a reasonable comparison. Nutanix was commercializing a similar architectural philosophy for enterprise virtualization: collapse the SAN storage tier into compute nodes, use flash storage as the primary tier, and rely on software-defined replication rather than expensive hardware RAID controllers. Both designs reflected the same shift happening across the industry: commodity x86 hardware with NVMe/SATA SSD was becoming good enough to replace expensive specialized storage hardware.

The 2013 server generation also reflects the beginning of the commodity hardware inflection point: 10GigE was becoming affordable enough to use as a standard interconnect rather than a premium feature, which changed the economics of distributed storage significantly.

## Key points

- Non-RAID philosophy: redundancy at the fleet level, not the device level — avoids expensive RAID controllers and speeds up writes.
- SSD as primary storage tier plus DRAM cache: orders-of-magnitude better random read latency than spinning disk.
- 10 Gigabit Ethernet interconnects: high enough bandwidth to make software-defined replication practical without a dedicated storage network.
- Parallels to Nutanix's hyper-converged infrastructure approach: both eschewed traditional SAN architecture in favor of software-managed distributed storage on commodity hardware.
- This hardware generation reflected a broader shift: the gap between server and storage appliance was closing.

[Original](http://blog.cloudflare.com/a-tour-inside-cloudflares-latest-generation-servers)
