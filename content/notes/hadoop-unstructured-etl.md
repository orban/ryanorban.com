---
title: "Hadoop's Unsung Sweet Spot: Unstructured ETL"
date: 2013-08-14
categories:
  - hadoop
  - etl
  - unstructured-data
  - data-engineering
  - big-data
description: A LinkedIn discussion arguing that Hadoop's real sweet spot wasn't analytics but unstructured ETL — transforming messy, heterogeneous data into structured forms before loading into traditional data warehouses. A nuanced counterpoint to the 'Hadoop replaces SQL' narrative of 2013.
params:
  source: pinboard
  sourceUrl: http://www.linkedin.com/groups/Hadoop-uberalles-Unstructured-ETL-is-35222.S.265755437
---

![Hadoop's Unsung Sweet Spot: Unstructured ETL](/images/notes/hadoop-unstructured-etl.png)

## Summary

This LinkedIn discussion argued that Hadoop's dominant use case wasn't replacing SQL analytics or running MapReduce jobs for data scientists — it was unstructured ETL (Extract, Transform, Load). Specifically: ingesting heterogeneous, messy data from disparate sources (logs, clickstreams, social media, sensor data), applying transformation logic, and loading clean structured data into traditional data warehouses like Teradata, Oracle, or the emerging Amazon Redshift.

This was a more pragmatic view of Hadoop than the Hadoop replaces everything narrative. Most enterprises weren't running sophisticated ML on Hadoop in 2013; they were using it as a scalable preprocessing stage. The HDFS/MapReduce stack was genuinely better than the alternatives for parsing billions of log lines, joining semi-structured JSON from multiple sources, and handling schema-on-read flexibility that relational data warehouses couldn't match.

The unstructured ETL framing also explained why Hadoop vendors like Cloudera and Hortonworks were winning in enterprises with strong data warehouse investments — the pitch wasn't replacement but augmentation. Hadoop as a landing zone and preprocessing layer, Teradata for the analytics queries.

## Key points

- Unstructured ETL use case: ingesting heterogeneous sources (JSON, logs, clickstreams) at scale, transforming to structured form, loading into a data warehouse or data mart.
- Schema-on-read vs. schema-on-write: HDFS accepts any data format; the schema is applied at query time — perfect for ingesting diverse sources before you know the full structure.
- Hadoop as augmentation, not replacement: sitting upstream of Teradata/Oracle to handle preprocessing that those systems handled poorly at scale.
- ETL at scale: traditional ETL tools (Informatica, DataStage) were expensive and slow at the file volumes web companies were producing.
- Hive and Pig as ETL layers: both provided higher-level abstractions over MapReduce that made ETL jobs expressible without Java code.
- Historically accurate: the "Hadoop for unstructured ETL" use case is exactly what Apache Spark later absorbed and made much more ergonomic.

[Original](http://www.linkedin.com/groups/Hadoop-uberalles-Unstructured-ETL-is-35222.S.265755437)
