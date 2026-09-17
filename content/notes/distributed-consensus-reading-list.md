---
title: Distributed Consensus Reading List
date: 2024-10-19
categories:
  - distributed-systems
  - consensus
  - reading-list
  - papers
  - research
description: Heidi Howard's curated list of papers on distributed consensus — organized from foundational Paxos through Multi-Paxos, Raft, flexible quorums, and Byzantine fault tolerance. The definitive paper trail for understanding how consensus algorithms actually work.
params:
  source: pinboard
  sourceUrl: https://github.com/heidihoward/distributed-consensus-reading-list
---

![Distributed Consensus Reading List](/images/notes/distributed-consensus-reading-list.png)

## Summary

Heidi Howard (Microsoft Research, known for Flexible Paxos) maintains this curated GitHub list of papers specifically about distributed consensus — the hardest and most fundamental problem in distributed systems: how do independent nodes agree on a single value in the face of failures?

The list covers the full lineage: Leslie Lamport's original Paxos paper (notoriously difficult to read), the more accessible Multi-Paxos formulations, Diego Ongaro's Raft (explicitly designed to be understandable), Heidi Howard's own Flexible Paxos (shows that Paxos's quorum requirements are more flexible than originally stated), PBFT (Byzantine fault tolerant consensus), and newer work on leader-free consensus and blockchain consensus.

Understanding consensus deeply matters because it underlies almost everything that requires coordination: distributed locks, leader election, replicated state machines, etcd, ZooKeeper, and every database that claims strong consistency. The Raft paper is the right starting point — it was explicitly designed to be understandable by PhD students who found Paxos opaque. After Raft, reading the original Paxos Made Simple reveals what Raft simplified. Then Flexible Paxos opens up the design space beyond the standard quorum model.

## Key points

- Organized from foundational Paxos through Raft, Flexible Paxos, and Byzantine fault tolerance
- Raft is the recommended entry point before tackling original Paxos papers
- Heidi Howard's Flexible Paxos is the key extension showing quorum requirements are more flexible than assumed
- Covers BFT (Byzantine fault tolerant) consensus needed for untrusted node environments and blockchains
- Pairs with Fred Hebert's broader distributed systems list and Designing Data-Intensive Applications

[Original](https://github.com/heidihoward/distributed-consensus-reading-list)
