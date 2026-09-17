---
title: Implementing Hadoop for Big Data Projects
date: 2013-07-17
categories:
  - hadoop
  - big-data
  - implementation
  - enterprise
  - infrastructure
description: Inside Analysis piece on practical considerations for implementing Hadoop in enterprise big data projects circa 2013 — covering organizational readiness, hardware choices, and the gap between Hadoop's promise and production reality.
params:
  source: pinboard
  sourceUrl: http://insideanalysis.com/2013/07/implementing-hadoop/
---

![Implementing Hadoop for Big Data Projects](/images/notes/implementing-hadoop-big-data.png)

## Summary

This Inside Analysis piece covered the practical realities of implementing Hadoop in enterprise environments — the gap between the marketing narrative ("store and process anything at commodity cost") and the operational complexity of actually running a production Hadoop cluster in 2013.

By mid-2013, enterprises were in their first wave of Hadoop adoption. Cloudera and Hortonworks distributions had professionalized deployment; the talent market for Hadoop engineers was tight; and organizations were learning that the skills gap was often more constraining than the technology gap. Hadoop required operational expertise (HDFS tuning, YARN capacity scheduling, NameNode HA configuration) that most IT departments didn't have.

The piece likely covered the standard implementation challenges: data governance (what data goes in the cluster and how is it catalogued), security (Kerberos was notoriously painful to configure), workload management (balancing batch analytics jobs against interactive queries), and the organizational question of where Hadoop sat in the IT org — under the data warehouse team, the infrastructure team, or a new big data org.

## Key points

- Skills gap dominated early Hadoop implementations: finding engineers who knew HDFS, MapReduce, and cluster operations was harder than buying the hardware.
- Cloudera and Hortonworks distributions: enterprise-packaged Hadoop with vendor support, simplified deployment, and security features — competing against DIY Apache Hadoop.
- Kerberos for security: Hadoop's authentication story was complex enough that many early clusters ran insecure — a significant enterprise adoption barrier.
- NameNode HA: the original Hadoop design had a single NameNode as a point of failure — HA configurations added operational complexity.
- Workload types drove architecture: batch ETL favored large sequential scans; interactive queries (Impala, Hive) needed different storage and scheduling optimizations.

[Original](http://insideanalysis.com/2013/07/implementing-hadoop/)
