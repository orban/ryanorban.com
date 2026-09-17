---
title: Nutanix Complete Hadoop Appliance
date: 2012-08-14
categories:
  - nutanix
  - hadoop
  - big-data
  - appliance
  - enterprise
description: Ryan's own SlideShare presentation for a Nutanix webinar on the Complete Hadoop Appliance — Nutanix's pitch for running Hadoop workloads on hyper-converged infrastructure instead of dedicated Hadoop clusters. This was Ryan's role at Nutanix circa 2012.
params:
  source: pinboard
  sourceUrl: http://www.slideshare.net/ryanorban/nutanix-complete-hadoop-appliance
---

![Nutanix Complete Hadoop Appliance](/images/notes/nutanix-complete-hadoop-appliance.png)

## Summary

Ryan's SlideShare presentation for a Nutanix webinar on the "Complete Hadoop Appliance" — Nutanix's pitch for running Hadoop workloads on hyper-converged infrastructure instead of dedicated Hadoop clusters with separate storage and compute hardware. The webinar was co-presented with Carahsoft, a government IT solutions provider, suggesting Nutanix was pursuing federal market opportunities alongside commercial enterprise.

The pitch for running Hadoop on Nutanix was that the traditional Hadoop deployment model — a cluster of commodity servers with HDFS for distributed storage — had painful operational characteristics. Every node in the cluster needed to be identically configured, scaling required careful rack-and-network planning, and the separation of HDFS data nodes from MapReduce task trackers created data locality issues that hurt performance. Nutanix's approach collocated compute and storage in each node and handled data locality automatically via NDFS.

This reflects Ryan's role at Nutanix circa 2012 — part of the team evangelizing the platform to enterprise and government customers and producing technical content like webinars and slideshares. The "Complete Hadoop Appliance" framing was typical Nutanix positioning: take a complex, multi-component open-source stack and deliver it as a turnkey appliance that IT teams could deploy without deep Hadoop expertise.

## Key points

- Nutanix pitch: run Hadoop on hyper-converged infrastructure instead of dedicated Hadoop clusters.
- Traditional Hadoop had operational pain: complex node configuration, data locality issues between HDFS and MapReduce.
- Nutanix auto-handles data locality via NDFS — no separate HDFS cluster needed.
- Carahsoft partnership suggests Nutanix pursuing federal/government market in 2012.
- "Complete Appliance" framing: turnkey delivery of complex open-source infrastructure as a managed product.
- Ryan's own presentation — reflects his role evangelizing Nutanix big data solutions.

[Original](http://www.slideshare.net/ryanorban/nutanix-complete-hadoop-appliance)
