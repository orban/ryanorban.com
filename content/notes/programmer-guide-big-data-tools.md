---
title: "A Programmer's Guide to Big Data: 12 Tools to Know"
date: 2012-12-19
categories:
  - big-data
  - hadoop
  - tools
  - data-engineering
  - reference
description: GigaOM's 2012 reference guide to 12 big data tools a programmer should know — covering Hadoop, Pig, Hive, HBase, Storm, and emerging alternatives. A snapshot of the Hadoop ecosystem at its peak complexity, before Spark simplified much of it.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/data/a-programmers-guide-to-big-data-12-tools-to-know/
---

![A Programmer's Guide to Big Data: 12 Tools to Know](/images/notes/programmer-guide-big-data-tools.png)

## Summary

GigaOM published this reference guide in late 2012 covering the tools that defined the Hadoop ecosystem at the time. The 2012 big data stack was complex: Apache Hadoop (HDFS + MapReduce) was the foundation, but building practical data systems required a constellation of additional tools for querying, streaming, coordination, and storage. This guide attempted to map the ecosystem for programmers who knew traditional databases but were encountering big data infrastructure for the first time.

The tools covered included: Apache Hive (SQL-like queries on Hadoop), Apache Pig (dataflow scripting language for MapReduce), HBase (column-oriented NoSQL database on HDFS), Apache Storm (real-time stream processing), Apache ZooKeeper (distributed coordination), Cassandra (distributed database, not Hadoop-native), MongoDB (document store), and Apache Spark (just emerging from UC Berkeley AMPlab — described as fast in-memory MapReduce).

The 2012 ecosystem was significantly more fragmented than today. Spark was not yet mainstream; most teams were using Pig or Hive for batch processing with long iteration times. The guide's description of Spark as a promising but unproven tool captures the pre-dominance moment. By 2015, Spark had replaced MapReduce for most workloads and simplified the stack considerably.

## Key points

- 2012 Hadoop ecosystem: HDFS + MapReduce as foundation, then a layer of specialized tools (Hive for SQL, Pig for dataflow, Storm for streaming, HBase for random access)
- Apache Spark: mentioned as an emerging fast-in-memory alternative; would dominate the category within 3 years
- Apache Storm: real-time stream processing; later competed with Spark Streaming, Flink, and Kafka Streams
- The complexity tax: the 2012 stack required knowing 5-10 separate systems to build a complete pipeline; Spark simplified this significantly
- Historical inflection: this guide is a snapshot of peak Hadoop complexity, just before the consolidation around Spark

[Original](http://gigaom.com/data/a-programmers-guide-to-big-data-12-tools-to-know/)
