---
title: "Google Spanner: Globally Distributed Transactions (OSDI 2012)"
date: 2012-09-16
categories:
  - distributed-systems
  - databases
  - google
  - transactions
  - consistency
description: Google's Spanner paper from OSDI 2012 — the design of Google's globally distributed SQL database with externally consistent transactions. TrueTime, the GPS/atomic-clock-based approach to distributed timestamps, is the paper's most memorable technical contribution.
params:
  source: pinboard
  sourceUrl: https://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en/us/archive/spanner-osdi2012.pdf
---

## Summary

Google Spanner is Google's globally distributed database, described in this OSDI 2012 paper by Jeff Dean and others. The paper's central contribution is demonstrating that it's possible to build a globally distributed database with external consistency — the strongest form of consistency, where transactions behave as if they executed sequentially even when physically distributed across data centers on multiple continents.

The mechanism that makes this possible is TrueTime — Google's infrastructure for bounded-uncertainty timestamps. Most distributed systems have to deal with clock skew: clocks on different machines drift, and you can't know exactly how much. TrueTime doesn't eliminate uncertainty; it quantifies it. Each TrueTime API call returns an interval $[t_{earliest}, t_{latest}]$ that is guaranteed to contain the true absolute time, using GPS receivers and atomic clocks deployed across Google's data centers. The uncertainty bound is typically a few milliseconds. By waiting out the uncertainty before committing a transaction, Spanner can guarantee that a transaction's commit timestamp is later than any transaction that committed before it — external consistency without magic.

Spanner also uses Paxos groups for replication within each shard, and the combination of Paxos, two-phase commit, and TrueTime produces a system that behaves like a SQL database from the user's perspective — full ACID transactions — while distributing data globally. This was a counterpoint to the NoSQL trend of the era: Google's internal evidence that strong consistency and global scale were compatible, just expensive to build correctly.

## Key points

- TrueTime: GPS + atomic clock infrastructure giving bounded-uncertainty timestamps — $[t_{early}, t_{late}]$ with guaranteed true time inside the interval
- External consistency: strongest isolation level — transactions appear to execute sequentially regardless of global distribution
- Architecture: Paxos groups for per-shard replication + two-phase commit across shards + TrueTime for commit ordering
- Spanner was later made available as Cloud Spanner (Google Cloud) — the first commercially available externally-consistent globally distributed SQL database
- Counterpoint to NoSQL era: proved global distribution and strong ACID transactions are compatible — just require serious infrastructure investment

[Original](https://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en/us/archive/spanner-osdi2012.pdf)
