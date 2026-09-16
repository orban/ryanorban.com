---
title: "Virtualization Performance: Zones, KVM, Xen"
date: 2013-03-19
categories:
  - virtualization
  - performance
  - kvm
  - xen
  - systems
  - brendan-gregg
description: Brendan Gregg's benchmark comparing the performance overhead of Solaris Zones, KVM, and Xen virtualization at Joyent. A rare empirical comparison from someone with the systems instrumentation expertise (DTrace) to measure what actually matters.
params:
  source: pinboard
  sourceUrl: http://dtrace.org/blogs/brendan/2013/01/11/virtualization-performance-zones-kvm-xen/
---

## Summary

Brendan Gregg, then a senior performance engineer at Joyent, used DTrace to measure the actual performance overhead of three virtualization approaches: Solaris Zones (OS-level containers), KVM (kernel-based virtual machine, full hardware virtualization on Linux), and Xen (the hypervisor used by early Amazon EC2). The post provided something rare in 2013: empirical numbers from someone with both the tooling and the expertise to instrument the full software stack.

The fundamental tradeoff being measured is virtualization overhead — the tax on CPU, memory, network, and disk I/O that tenants pay for the isolation guarantee. Solaris Zones achieve isolation at the OS level: all zones share a kernel, so there's almost no overhead for CPU-bound workloads, but the isolation boundary is weaker (a kernel vulnerability affects all zones). KVM runs a full guest OS on top of hardware virtualization extensions (Intel VT-x / AMD-V), adding meaningful overhead for I/O-heavy workloads but providing stronger isolation. Xen uses a hypervisor that sits below all guest OSes, with para-virtualization reducing I/O overhead compared to full hardware emulation.

The practical context for this post was Joyent's SmartOS and its hosting platform (later SmartDataCenter). Joyent was competing with Amazon EC2 (Xen-based) and offering Zones-based containers as a higher-performance alternative. Docker did not yet exist — containerization was not yet mainstream — and this was the era when operators were actively comparing hypervisor approaches for cloud IaaS. The benchmarks covered CPU microbenchmarks, memory bandwidth, network throughput, and disk I/O latency, using DTrace to trace kernel internals and identify where overhead was coming from.

## Key points

- Solaris Zones: near-zero overhead for CPU/memory workloads (shared kernel), meaningful isolation boundary — predecessor to modern Linux containers (LXC, Docker)
- KVM: full guest OS on hardware virtualization extensions — higher overhead for I/O-heavy workloads vs. containers, but stronger tenant isolation
- Xen: hypervisor below all guests; para-virtualization (paravirt drivers) reduces I/O overhead vs. full emulation — architecture Amazon EC2 used through 2017
- DTrace provided the instrumentation depth to see where overhead actually occurs, not just black-box throughput numbers
- Brendan Gregg later produced *Systems Performance* (2013), the definitive reference on using these techniques at scale — this post reflects that methodology
- Historical note: by 2015, Docker had shifted the industry toward container-based isolation, and by 2017 AWS had migrated EC2 to its Nitro hypervisor; the landscape these benchmarks described was in transition

[Original](http://dtrace.org/blogs/brendan/2013/01/11/virtualization-performance-zones-kvm-xen/)
