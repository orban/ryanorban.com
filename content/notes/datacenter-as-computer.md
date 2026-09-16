---
title: "The Datacenter as a Computer: Warehouse-Scale Machines"
date: 2013-08-24
categories:
  - data-center
  - infrastructure
  - google
  - warehouse-scale-computing
  - distributed-systems
description: High Scalability's coverage of Google's 'The Datacenter as a Computer' second edition — Barroso and Hölzle's canonical text on warehouse-scale machine design. Defined the vocabulary and engineering tradeoffs for operating entire buildings as programmable compute platforms.
params:
  source: pinboard
  sourceUrl: http://highscalability.com/blog/2013/8/22/the-datacenter-as-a-computer-an-introduction-to-the-design-o.html
---

## Summary

"The Datacenter as a Computer" by Luiz André Barroso and Urs Hölzle of Google (second edition, 2013) is the foundational text on warehouse-scale computing — designing and operating data centers where the entire facility is the unit of computation. [High Scalability](/notes/high-scalability/) covered the second edition's release, which added chapters on power efficiency, network topology, and a decade of lessons from Google's hyperscale operations.

The central insight: at Google scale, design problems shift completely. Individual server reliability matters less than aggregate reliability across thousands of nodes. Power and cooling become dominant cost constraints. Tail latency — the 99th percentile response time — matters more than average latency because large fan-out requests complete only when the slowest sub-request finishes. Software must assume hardware failures are the norm.

The second edition updated with energy proportionality improvements (servers drawing power proportional to load), advances in network fabric (fat-tree and Clos topologies for uniform bandwidth), and the growing value of custom silicon for specific workloads. The book directly influenced how AWS, Azure, and Facebook designed their infrastructure and gave the industry a shared vocabulary for hyperscale infrastructure.

## Key points

- Warehouse-scale computing: the datacenter is a single programmable machine — software abstracts over thousands of physical nodes.
- Energy proportionality: most 2013 servers drew 60-70% of max power even at low load — a major efficiency and cost problem.
- Tail latency: in large fan-out systems, p99 latency dominates — requires hedged requests and cancellation strategies.
- Network topology: Clos topology and fat-tree fabrics provide uniform bisection bandwidth, avoiding oversubscription in traditional 3-tier architectures.
- Custom silicon trend: general-purpose CPUs are inefficient for specific workloads; Google TPU and AWS Nitro followed this logic.
- Written by Google engineers — gave the industry shared vocabulary for hyperscale infrastructure design tradeoffs.

[Original](http://highscalability.com/blog/2013/8/22/the-datacenter-as-a-computer-an-introduction-to-the-design-o.html)
