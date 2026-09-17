---
title: "HBase vs Cassandra: Why We Moved"
date: 2012-08-25
categories:
  - nosql
  - hbase
  - cassandra
  - databases
  - distributed-systems
description: "A firsthand account of migrating from HBase to Cassandra, written in 2010 but widely read through 2012. The core finding: Cassandra was operationally simpler and more resilient to node failures, while HBase required careful HDFS management and had more complex failure modes."
params:
  source: pinboard
  sourceUrl: https://ria101.wordpress.com/2010/02/24/hbase-vs-cassandra-why-we-moved/
---

![HBase vs Cassandra: Why We Moved](/images/notes/hbase-vs-cassandra.png)

## Summary

Dominic Williams's firsthand account of migrating production systems from HBase to Cassandra, written in 2010 but widely circulated through 2012 as a definitive practitioner comparison of the two dominant column-family databases. The central finding: Cassandra's peer-to-peer architecture was fundamentally more operationally resilient than HBase's master-worker model.

HBase was built on top of HDFS (Hadoop Distributed File System), which meant it inherited HDFS's operational complexity. HBase had a single active master node, and node failures triggered complex recovery processes involving ZooKeeper, the HBase master, and HDFS region server reassignment. In practice, node failures were stressful operational events that required close monitoring and careful intervention. The HDFS dependency also meant running a full Hadoop cluster just to get a NoSQL database.

Cassandra, by contrast, was designed as a peer-to-peer system with no single point of failure — a direct lineage from Amazon Dynamo. Any node could serve any read or write. Node failures were handled by gossip protocol and automatic data redistribution. The tradeoff was eventual consistency (versus HBase's stronger consistency model via HDFS and ZooKeeper), but for most web application workloads, eventual consistency was acceptable and the operational simplicity was a decisive advantage.

## Key points

- HBase's master-worker model with ZooKeeper coordination made node failures operationally complex.
- HBase required a full Hadoop/HDFS stack as a dependency — significant operational overhead for just a database.
- Cassandra's peer-to-peer gossip protocol means any node can handle any request — no single point of failure.
- Cassandra offers eventual consistency (tunable); HBase offers stronger consistency via HDFS write-ahead logging.
- For most web workloads, Cassandra's operational simplicity outweighed HBase's stronger consistency guarantees.
- The Amazon Dynamo paper was the architectural ancestor of Cassandra; Google Bigtable was the ancestor of HBase.

[Original](https://ria101.wordpress.com/2010/02/24/hbase-vs-cassandra-why-we-moved/)
