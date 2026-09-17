---
title: Advent of Distributed Systems
date: 2023-12-14
categories:
  - distributed-systems
  - education
  - computer-science
  - advent-of-code
  - challenges
description: Advent of Distributed Systems is a coding challenge series in the style of Advent of Code but focused on distributed systems problems — consensus, replication, fault tolerance, and network partitions. Hands-on learning for distributed concepts that are hard to study from papers alone.
params:
  source: pinboard
  sourceUrl: https://aods.cryingpotato.com/
---

![Advent of Distributed Systems](/images/notes/advent-of-distributed-systems.png)

## Summary

[Advent of Distributed Systems](/notes/advent-of-distributed-systems/) is a coding challenge series in the style of Advent of Code but focused specifically on distributed systems problems. Rather than algorithmic puzzles, each challenge requires implementing a distributed systems concept: leader election, consensus via Raft or Paxos, causal broadcast, vector clocks, CRDTs, fault-tolerant replication, and similar foundational distributed primitives.

The value of challenges over textbooks for distributed systems is that implementation forces precision. You can read about Raft consensus in the paper and understand the algorithm abstractly, but implementing it — handling node crashes, network partitions, log replication edge cases — reveals the gaps in your understanding. Maelstrom (the distributed systems challenge framework from Kyle Kingsbury/Jepsen) uses a similar approach.

Distributed systems is one of those domains where the gap between understands the concepts and can build reliable systems is large and consequential. The Byzantine generals problem, CAP theorem, and PACELC give you vocabulary; building a working distributed counter or implementing linearizable read-write registers gives you intuition. Challenge-based learning bridges that gap.

## Key points

- Coding challenges for distributed systems — consensus, vector clocks, CRDTs, fault tolerance, replication.
- Implementation-first learning: building the primitive forces precision that reading papers doesn't.
- In the style of Advent of Code — digestible, progressive, with clear problem statements.
- Connects to Maelstrom (Jepsen testing framework) for similar hands-on distributed systems practice.
- Particularly useful for: engineers building distributed databases, event sourcing systems, or distributed AI agent infrastructure.

[Original](https://aods.cryingpotato.com/)
