---
title: Data Centers Waste Vast Amounts of Energy
date: 2012-09-23
categories:
  - data-centers
  - energy
  - cloud-computing
  - sustainability
  - infrastructure
description: NYT investigation into the massive energy waste inside data centers — servers running at 6-12% utilization, backup systems idling on standby, cooling systems sized for peak loads that rarely arrive. Exposed the gap between the clean, efficient image of cloud computing and the physical reality.
params:
  source: pinboard
  sourceUrl: http://www.nytimes.com/2012/09/23/technology/data-centers-waste-vast-amounts-of-energy-belying-industry-image.html
---

![Data Centers Waste Vast Amounts of Energy](/images/notes/data-centers-energy-waste.png)

## Summary

The NYT's James Glanz reported in September 2012 that data centers were consuming enormous amounts of electricity while using only a fraction of their capacity. The industry figure that stood out: servers typically ran at 6–12% CPU utilization, burning full power while doing almost nothing. The cause was a structural incentive problem — IT departments were penalized far more for downtime than for energy waste, so they grossly over-provisioned capacity and left machines idling rather than risk being under-resourced.

The scale was significant. Data centers in the US consumed roughly 76 billion kilowatt-hours per year at the time — about 2% of total US electricity consumption — with much of it powering idle machines and cooling systems sized for theoretical peak loads. Diesel generators sat in standby for emergency power, adding to the environmental footprint. The disconnect between the cloud computing industry's image (efficient, virtualized, green) and the physical reality (refrigerated buildings packed with underutilized machines) was the story.

The piece appeared just as Nutanix, VMware, and others were pushing server virtualization and hyperconverged infrastructure as solutions to exactly this problem — concentrating workloads on fewer, more heavily utilized machines. Amazon Web Services and Google were also building their own efficiency gains at scale. But the broader enterprise data center landscape lagged significantly behind the hyperscalers' efficiency metrics.

## Key points

- Average data center server utilization rate: 6–12% of capacity — the rest wasted while burning full power
- Overcapacity incentive: IT departments bear 100% of downtime cost but shared/diffuse energy cost, so over-provisioning is rational locally but wasteful in aggregate
- US data center electricity consumption ≈76 billion kWh/year in 2012 — comparable to 5.8 million average American homes
- Server virtualization (VMware, Hyper-V) and hyperconverged infrastructure were emerging as technical solutions to the utilization problem
- PUE (Power Usage Effectiveness) was becoming the standard metric — hyperscalers like Google and Facebook ran PUEs near 1.1, enterprise data centers often 1.7–2.0

[Original](http://www.nytimes.com/2012/09/23/technology/data-centers-waste-vast-amounts-of-energy-belying-industry-image.html)
