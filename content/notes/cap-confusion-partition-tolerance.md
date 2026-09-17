---
title: "CAP Confusion: Problems with 'Partition Tolerance'"
date: 2013-05-05
categories:
  - distributed-systems
  - cap-theorem
  - consistency
  - availability
  - database
description: "Cloudera's clarification of the most common CAP theorem misreading: partition tolerance isn't a feature you choose — it's a property you must accept because network partitions happen. The real CAP choice is between consistency and availability when partitions occur."
params:
  source: pinboard
  sourceUrl: http://blog.cloudera.com/blog/2010/04/cap-confusion-problems-with-partition-tolerance/
---

## Summary

This Cloudera blog post (by Henry Robinson) corrected the most persistent misunderstanding of the CAP theorem that was widespread in the industry around 2010. Brewer's CAP theorem states you can only have two of: Consistency, Availability, and Partition Tolerance. The common misreading treated this as a three-way menu — including the idea that you could choose to sacrifice partition tolerance in exchange for both consistency and availability.

The problem: network partitions aren't optional. If your system spans multiple nodes communicating over a network, partitions will happen — links fail, switches crash, packets get dropped. You cannot choose not to support partition tolerance any more than you can choose not to have gravity. Partition tolerance means your system continues to operate (possibly with degraded behavior) when partitions occur. If you say "I don't need partition tolerance, you're actually saying my system will halt when any partition occurs" — which is a worse outcome than explicitly trading consistency for availability.

The real CAP choice, properly understood, is between consistency and availability during the inevitable periods when partitions occur. A CP system (like HBase or Zookeeper) will refuse requests or return errors during a partition to preserve consistency. A CA system under partition is really just a C system or just an A system depending on how it degrades. The practical framing is: when a partition happens, do you want your system to return stale data (eventually consistent, high availability) or return an error/wait (strongly consistent, lower availability)?

## Key points

- Partition tolerance is not optional for distributed systems — network partitions are an inherent property of multi-node systems
- The real CAP theorem choice is between consistency and availability *during partitions*
- CP systems (HBase, ZooKeeper, traditional RDBMS in distributed configs): reject requests during partitions to preserve consistency
- AP systems (Amazon Dynamo, Cassandra, CouchDB): return potentially stale data during partitions to stay available
- This insight predates but directly informs later frameworks like PACELC (which also models latency-consistency tradeoffs in the normal case)
- The confusion was widespread in 2010 — many engineers thought choose CA was a valid distributed database design decision

[Original](http://blog.cloudera.com/blog/2010/04/cap-confusion-problems-with-partition-tolerance/)
