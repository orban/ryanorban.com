---
title: "Working with Big Data: Assembling Your Toolkit"
date: 2013-03-18
categories:
  - big-data
  - hadoop
  - tools
  - data-pipeline
description: Acquia's guide to assembling a big data toolkit in 2013 — walking through the layered stack from storage to analysis. Practical survey of the Hadoop ecosystem components a team would actually need to evaluate.
params:
  source: pinboard
  sourceUrl: http://www.acquia.com/blog/working-big-data-assembling-your-toolkit
---

## Summary

Acquia (a Drupal-focused web company) published this practical guide during the period when enterprise teams were trying to understand which pieces of the Hadoop ecosystem they actually needed to assemble a functional big data pipeline. The ecosystem had grown complex fast: by 2013 there were dozens of Apache projects, commercial tools, and cloud services occupying overlapping niches.

The typical toolkit being assembled in 2013 started with HDFS for distributed storage, MapReduce or Hive for batch processing, Sqoop for data ingestion from relational databases, Flume or Kafka for streaming ingest, HBase for low-latency read/write, and some visualization layer on top. Each component solved a specific problem in the data pipeline, but integrating them was non-trivial.

The fact that Acquia — a web CMS company — was publishing on this topic illustrates how broadly big data demand had spread by 2013. Web companies processing user behavior logs, content analytics, and recommendation data were all facing the same scaling problems.

## Key points

- The Hadoop ecosystem in 2013 required assembling multiple components: storage (HDFS), batch compute (MapReduce/Hive), stream ingest (Flume/Kafka), and NoSQL read (HBase)
- Sqoop was the standard connector for pulling data from existing RDBMS databases into Hadoop
- Pig Latin abstracted MapReduce for data transformation pipelines; Hive added SQL-style access for analysts
- The ecosystem complexity drove demand for commercial distributions: Cloudera CDH and Hortonworks HDP tried to make the toolkit coherent
- By 2015-2016, Apache Spark would replace most of this stack with a simpler programming model

[Original](http://www.acquia.com/blog/working-big-data-assembling-your-toolkit)
