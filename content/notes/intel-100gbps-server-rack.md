---
title: Intel Wants to Kill the Traditional Server Rack with 100Gbps Links
date: 2013-04-10
categories:
  - networking
  - hardware
  - data-center
  - intel
  - silicon-photonics
description: Ars Technica on Intel's push to replace copper Ethernet in server racks with 100Gbps silicon photonics links — the argument that data center networking bandwidth was the bottleneck for distributed computing in 2013. Intel's bid to own the rack interconnect layer.
params:
  source: pinboard
  sourceUrl: http://arstechnica.com/information-technology/2013/04/intel-wants-to-kill-the-traditional-server-rack-with-100gbps-links/
---

![Intel Wants to Kill the Traditional Server Rack with 100Gbps Links](/images/notes/intel-100gbps-server-rack.png)

## Summary

In 2013, Intel was pushing silicon photonics as the technology that would replace copper-based Ethernet for in-rack and top-of-rack server interconnects. The claim: as servers added more cores and memory, the bottleneck for distributed workloads was shifting from compute to network — and the 10GbE standard of the time was already a constraint. Silicon photonics could deliver 100Gbps links (vs. 10Gbps copper Ethernet) at lower power and over longer distances by transmitting data as light through optical waveguides etched directly into silicon chips.

Intel's Light Peak (later Thunderbolt) and silicon photonics programs aimed to make optical interconnects cheap enough for data center racks. The vision was a disaggregated rack architecture where servers, memory, storage, and accelerators connected over extremely high-speed optical links — eliminating the constraints of physical proximity and PCI-E bus bandwidth. This would allow, for example, pooling flash storage or GPU accelerators across many servers dynamically rather than requiring each server to have its own set.

From a big data perspective, this was directly relevant: Apache Hadoop and MapReduce were notoriously network-bound — the shuffle phase moved enormous amounts of data across switches, and link speed was a real throughput constraint for large clusters. 100Gbps rack interconnects would change the economics of data-intensive distributed computing, making it feasible to move more data between nodes without the shuffle becoming the bottleneck.

## Key points

- Silicon photonics: transmits data as light through optical waveguides in silicon — same fab process as CMOS, making it cost-competitive with copper.
- 100Gbps vs. 10GbE: a 10x bandwidth jump that Intel argued would become necessary as servers scaled cores and memory.
- Disaggregated rack vision: high-speed optical links allow storage, compute, and accelerators to be pooled across racks rather than dedicated per server.
- Network bottleneck in distributed computing: MapReduce shuffle phase and other data-intensive workloads were increasingly bottlenecked by switch bandwidth.
- Intel's motivation: owning the interconnect layer in data centers, not just the CPU — optical would prevent Ethernet commodity pricing from eroding margins.

[Original](http://arstechnica.com/information-technology/2013/04/intel-wants-to-kill-the-traditional-server-rack-with-100gbps-links/)
