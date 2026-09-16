---
title: Distributed Systems for Fun and Profit
date: 2013-09-17
categories:
  - distributed-systems
  - consensus
  - replication
  - fault-tolerance
  - book
description: Mixu's free online book on distributed systems fundamentals — covering consistency models, CAP theorem, replication, and consensus — written for practitioners who want theoretical grounding without the academic overhead. One of the clearest introductions to the field that exists.
params:
  source: pinboard
  sourceUrl: http://book.mixu.net/distsys/single-page.html
---

## Summary

"Distributed Systems for Fun and Profit" by Mikito Takada (Mixu) is a free, concise online book that covers the core ideas in distributed systems with unusual clarity. It explains consistency models (strong, eventual, causal), the CAP theorem, replication strategies, fault tolerance, and consensus algorithms (Paxos, Raft) without drowning in academic formalism. The goal is to give practitioners the mental models they need to reason about distributed behavior.

The book's central thread is the fundamental tension in distributed systems: you want your system to behave like a single machine (consistency), but the physics of distributed hardware make this expensive or impossible under failure conditions. CAP theorem formalizes this — you can have at most two of consistency, availability, and partition tolerance. But the CAP framing, while useful, is often misapplied; the book is careful to note that partition tolerance isn't really optional, so the real tradeoff is between consistency and availability during network partitions.

The treatment of replication is particularly valuable: synchronous vs. asynchronous replication, primary-backup vs. multi-primary, and why eventual consistency systems (like Amazon Dynamo) require conflict resolution logic pushed to the application layer. This is the conceptual ground that explains why CRDTs, vector clocks, and last-write-wins registers exist.

## Key points

- CAP theorem: consistency/availability/partition tolerance — you get two, but partition tolerance is mandatory in practice, so it's really C vs. A under partition.
- Consistency models form a hierarchy: linearizability > sequential consistency > causal consistency > eventual consistency — weaker models allow more concurrency but require more application-level reasoning.
- Consensus algorithms (Paxos, Raft): how distributed nodes agree on a value despite failures — the foundation of distributed databases and coordination services like Apache Zookeeper.
- Replication tradeoffs: synchronous replication guarantees durability but adds latency; asynchronous loses durability guarantees but is faster.
- Amazon Dynamo-style systems (and later Cassandra, Riak) chose availability over consistency and pushed conflict resolution to application code.
- A canonical reference — cited for years as the best starting point for engineers needing distributed systems fundamentals.

[Original](http://book.mixu.net/distsys/single-page.html)
