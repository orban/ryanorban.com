---
title: Big Data Explained
date: 2013-03-18
categories:
  - big-data
  - hadoop
  - explainer
description: BlazeClan's explainer on big data for a general technical audience — covering the 4 Vs framework and why traditional databases couldn't handle the scale. A typical 2013 entry-level primer during peak big data hype.
params:
  source: pinboard
  sourceUrl: http://blog.blazeclan.com/big-data-explained/
---

## Summary

BlazeClan's introductory explainer on big data represents a genre that was ubiquitous in 2013: enterprise IT vendors and consultancies publishing accessible introductions to help their clients understand why they needed to modernize their data infrastructure. The framing was almost always the same: traditional relational database systems couldn't handle data at the scale that internet-era businesses were generating.

The canonical framework of this period was the 4 Vs of big data: **Volume** (more data than fits in a single machine), **Velocity** (data arriving faster than batch processing can handle), **Variety** (structured relational data plus unstructured text, logs, clickstreams, sensor data), and **Value** (the business justification for the infrastructure investment). Apache Hadoop was the standard answer to Volume and Variety; Apache Kafka and real-time processing would later address Velocity.

The significance of 2013 as the bookmark date: this was when big data crossed from early adopters (web-scale companies) to enterprise mainstream. The consulting class — firms like BlazeClan — were publishing primers precisely because their enterprise clients were asking "what is this, and do we need it?"

## Key points

- The 4 Vs of big data framework (Volume, Velocity, Variety, Value) dominated how the category was explained to non-technical stakeholders
- RDBMS systems like Oracle and SQL Server hit practical limits at petabyte scale — motivating adoption of Hadoop and NoSQL databases
- Apache Hadoop (HDFS + MapReduce) was the primary infrastructure answer in 2013
- Hive added SQL-like query capability over Hadoop data, enabling analysts to work without writing Java MapReduce jobs
- The enterprise Hadoop market was bifurcating: managed services (Amazon EMR) vs on-premises distributions (Cloudera, Hortonworks)

[Original](http://blog.blazeclan.com/big-data-explained/)
