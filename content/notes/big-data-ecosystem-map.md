---
title: Big Data Ecosystem Map (2013)
date: 2013-08-05
categories:
  - big-data
  - ecosystem
  - hadoop
  - landscape
  - reference
description: A map of the big data ecosystem as it existed in 2013 — an attempt to catalog the dozens of Hadoop-adjacent tools, databases, analytics platforms, and services that had emerged. A useful historical artifact of the big data vendor explosion before consolidation.
params:
  source: pinboard
  sourceUrl: http://www.bigdatanews.com/profiles/blogs/big-data-ecosystem
---

![Big Data Ecosystem Map (2013)](/images/notes/big-data-ecosystem-map.png)

## Summary

This big data ecosystem map was an attempt to organize the rapidly proliferating landscape of tools, platforms, and vendors that had sprung up around Hadoop and big data analytics by 2013. By this point, the ecosystem had expanded well beyond core HDFS/MapReduce — it included query layers (Hive, Impala, Drill), workflow schedulers (Oozie, Azkaban), stream processing (Storm, Samza), machine learning (Mahout), serialization (Avro, Parquet, Thrift), coordination (Zookeeper), and NoSQL databases (HBase, Cassandra, MongoDB) all overlapping in complex ways.

The tweet saving this described it as "making sense of Big Data and its burgeoning ecosystem" — the framing was explicitly navigational, not evaluative. The map served as a reference for practitioners trying to understand where a specific tool fit and what alternatives existed. In 2013, choosing a big data stack required orienting yourself in this landscape before you could make rational architectural decisions.

This type of ecosystem landscape diagram became a recurring genre in data infrastructure, replicated annually as the landscape evolved: Matt Turck's Data & AI Landscape series from FirstMark Capital became the canonical version, growing to hundreds of logos by 2020. The 2013 version was simpler — the explosion hadn't yet peaked — but still complex enough to require a map.

## Key points

- 2013 Hadoop ecosystem: HDFS core + query layers (Hive, Impala) + schedulers (Oozie) + streaming (Storm) + NoSQL (HBase, Cassandra) + serialization (Avro, Parquet).
- Hortonworks vs. Cloudera vs. MapR: the three major Hadoop distributions, each curating slightly different stacks — the landscape map helped vendors position their choices.
- Consolidation didn't happen yet: by 2013, the ecosystem had dozens of competing solutions in every category — most would eventually lose to Apache Spark or cloud managed services.
- Data & AI Landscape genre: Matt Turck at FirstMark Capital took this concept and evolved it into an annual benchmark of the data infrastructure ecosystem.
- Historical value: comparing 2013's map to 2020's shows both explosive growth and significant consolidation — Apache Spark absorbed most of the batch/streaming processing landscape.
- Navigation function: ecosystem maps serve practitioners orienting in a new space, not experts — they signal "this is complex, here's a starting map."

[Original](http://www.bigdatanews.com/profiles/blogs/big-data-ecosystem)
