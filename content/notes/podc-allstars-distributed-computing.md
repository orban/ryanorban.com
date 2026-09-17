---
title: Principles of Distributed Computing — ETH Zurich All-Stars
date: 2014-12-23
categories:
  - distributed-systems
  - algorithms
  - lectures
  - education
description: ETH Zurich's Principles of Distributed Computing lecture series — foundational theory covering consensus, fault tolerance, and distributed algorithms. The "all-stars" edition collects contributions from leading researchers in the field.
params:
  source: pinboard
  sourceUrl: http://dcg.ethz.ch/lectures/podc_allstars/
---

## Summary

ETH Zurich's Distributed Computing Group (DCG) runs one of the most rigorous graduate courses on distributed systems theory. The all-stars lecture series at `dcg.ethz.ch/lectures/podc_allstars/` is a special edition that incorporates lecture material from prominent researchers in the field, covering the theoretical foundations of distributed computing.

The core topics in PODC-style courses include: consensus algorithms (how do distributed nodes agree when some may fail?), the CAP theorem (consistency, availability, partition tolerance — pick two), fault tolerance (Byzantine faults vs. crash faults), distributed clocks and time (Lamport timestamps, vector clocks), leader election, and distributed hash tables.

This type of theoretical grounding was increasingly relevant in 2014 as Apache Spark, Apache Kafka, and ZooKeeper were becoming the infrastructure stack of choice for large-scale data systems. Understanding why these systems make the design choices they do requires knowing the underlying impossibility results — particularly FLP impossibility (no deterministic algorithm can solve consensus in an asynchronous system if even one node may fail) and Paxos/Raft as practical workarounds.

## Key points

- ETH Zurich DCG offers one of the strongest academic programs in distributed systems theory.
- Core topics: consensus, fault tolerance, Lamport clocks, vector clocks, leader election, distributed hash tables.
- FLP impossibility: no deterministic consensus is possible in asynchronous networks with even one faulty node.
- Paxos and Raft are practical consensus algorithms that work around FLP by making timing assumptions.
- CAP theorem: distributed systems can guarantee at most two of consistency, availability, and partition tolerance.
- Theoretical foundation for understanding Apache ZooKeeper, etcd, and distributed database design.

[Original](http://dcg.ethz.ch/lectures/podc_allstars/)
