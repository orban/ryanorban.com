---
title: Nutanix Hadoop Solution Brief
date: 2013-07-16
categories:
  - nutanix
  - hadoop
  - ndfs
  - infrastructure
  - enterprise
description: Nutanix's Hadoop solution brief describing how NDFS (Nutanix Distributed File System) enables running Hadoop workloads on hyper-converged infrastructure. Marketing collateral saved during Ryan's time at Nutanix.
params:
  source: pinboard
  sourceUrl: http://go.nutanix.com/rs/nutanix/images/Hadoop_Solution_Brief.pdf
---

## Summary

This Nutanix solution brief described how NDFS (Nutanix Distributed File System) enabled running Hadoop workloads on Nutanix hyper-converged infrastructure. The bookmark content is a tweet from Josh Odgers asking about NDFS backing for Hadoop — part of the technical community discussion around Nutanix's Hadoop positioning in 2013.

NDFS was Nutanix's distributed file system layer that provided the same semantics as HDFS while running on the same hardware nodes used for virtualization workloads. The solution brief made the case that this convergence offered real operational advantages: one platform to manage rather than separate Hadoop clusters and virtualization infrastructure, with Nutanix Prism providing unified visibility.

The key technical claim: NDFS handled the data locality problem that critics raised against running Hadoop on converged infrastructure. By ensuring that Hadoop's compute tasks were scheduled on the same nodes as the data they needed, Nutanix could deliver performance comparable to dedicated clusters while sharing hardware with other workloads.

## Key points

- NDFS as HDFS replacement: Nutanix's distributed file system implemented the same interface as Hadoop's native storage layer.
- Convergence argument: one hardware pool for both analytics (Hadoop) and virtualization, managed via Prism — lower operational overhead than separate stacks.
- Data locality in a converged environment: NDFS's scheduler placed compute jobs on nodes with local data copies to preserve Hadoop's locality advantage.
- Business context: saved from a tweet during Nutanix's push to certify with Hortonworks and Cloudera — Ryan was working at Nutanix at this time.

[Original](http://go.nutanix.com/rs/nutanix/images/Hadoop_Solution_Brief.pdf)
