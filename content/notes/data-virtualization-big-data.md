---
title: Why Data Virtualization Is Good for Big Data Analytics
date: 2013-08-06
categories:
  - data-virtualization
  - big-data
  - analytics
  - data-architecture
  - sql
description: Data-Informed's case for data virtualization in big data analytics — querying data in-place across Hadoop, relational databases, and other sources without physical ETL. A precursor to the 'data fabric' and 'data mesh' concepts that would emerge years later.
params:
  source: pinboard
  sourceUrl: http://data-informed.com/why-data-virtualization-is-good-for-big-data-analytics/
---

![Why Data Virtualization Is Good for Big Data Analytics](/images/notes/data-virtualization-big-data.png)

## Summary

Data virtualization is an approach where a query layer presents a unified view over multiple heterogeneous data sources — Hadoop, relational databases, NoSQL stores, cloud APIs — without physically moving data into a single repository first. This data-informed.com post argued that as big data architectures diversified (data living in HDFS, Amazon S3, MySQL, MongoDB simultaneously), the cost of ETL pipelines to consolidate everything became untenable, and virtualization was the answer.

The data virtualization vendors in 2013 — Denodo, Composite Software, TIBCO Data Virtualization — provided SQL interfaces over federated sources, handling query pushdown (pushing computation to the source system where possible), caching, and data access governance. The pitch was: analysts write standard SQL; the virtualization layer figures out where each table actually lives and how to optimally execute the query.

This concept predates and influenced the data lake architecture's development. Where data lakes tried to solve the heterogeneity problem by physically centralizing data into HDFS, data virtualization said "leave it where it is, just provide a unified query interface." In 2013, both approaches were being explored; data lakes won the ingest-and-store battle, but virtualization concepts resurfaced in Presto/Trino, Apache Arrow Flight, and eventually data mesh architectures.

## Key points

- Data virtualization: query multiple heterogeneous sources (Hadoop, RDBMS, APIs) through a single SQL interface without physical data movement.
- Query pushdown: the virtualization layer translates queries into source-specific operations — pushing aggregations and filters to where data lives reduces transfer volume.
- Governance argument: if all data access goes through the virtualization layer, you get a single point for data access control and audit logging — harder to enforce across scattered sources.
- Denodo and Composite Software were the 2013 leaders; Cisco later acquired Composite.
- Historical thread: Presto (Facebook, open-sourced 2013) and Trino represent the distributed query engine evolution of the same idea without the proprietary virtualization layer.
- Data mesh connection: the "leave data where it is, provide federated queries" principle is architecturally similar to data mesh's domain-oriented data ownership model.

[Original](http://data-informed.com/why-data-virtualization-is-good-for-big-data-analytics/)
