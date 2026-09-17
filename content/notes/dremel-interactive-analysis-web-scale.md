---
title: "Dremel: Interactive Analysis of Web-Scale Datasets"
date: 2012-07-07
categories:
  - distributed-systems
  - big-data
  - google
  - sql
  - columnar-storage
  - research
description: Google's Dremel paper — the system that enabled sub-second SQL queries over petabyte datasets via columnar storage and a multi-level serving tree. The direct precursor to BigQuery, and the inspiration behind Apache Parquet's nested record encoding.
params:
  source: pinboard
  sourceUrl: http://research.google.com/pubs/pub36632.html
---

![Dremel: Interactive Analysis of Web-Scale Datasets](/images/notes/dremel-interactive-analysis-web-scale.png)

## Summary

Google Dremel is the system Google built for interactive analysis of petabyte-scale datasets — enabling sub-second SQL-like queries that would take hours on MapReduce. Published at VLDB 2010, the Dremel paper described three innovations that together made this possible: columnar storage for nested data, a multi-level serving tree for parallel query execution, and a novel encoding for nested records that later became Apache Parquet.

Columnar storage is the foundational insight: rather than storing records row by row (where reading one field means reading all fields in the record), store each field in its own column. A query that touches only 3 of 100 fields reads 3% of the data. For analytical queries — which almost always aggregate across many records on a few fields — this is a dramatic I/O reduction. Dremel extended this to nested records (think JSON-like structures with repeated and optional fields) using a repetition/definition level encoding that encodes the full structure without storing record boundaries.

The multi-level serving tree is the execution model: a root server receives a query, rewrites it into sub-queries, and dispatches them to intermediate servers that further fan out to leaf servers that scan actual data. Results aggregate up the tree. This lets a single query mobilize thousands of machines simultaneously. Combined with columnar I/O that reads minimal data, the result was queries that completed in seconds where Hadoop MapReduce would take minutes to hours. Dremel was the direct predecessor to Google BigQuery (launched publicly in 2012), and its columnar encoding became Apache Parquet — now the standard format for analytical data lakes.

## Key points

- Columnar storage for nested records: store fields separately, encode nesting with repetition/definition levels — the foundation of Apache Parquet.
- Multi-level serving tree: hierarchical fan-out dispatches query fragments to thousands of leaf servers simultaneously; results aggregate up the tree.
- Sub-second queries at petabyte scale — orders of magnitude faster than MapReduce for analytical workloads.
- Published at VLDB 2010; the direct precursor to Google BigQuery (public launch 2012).
- Columnar encoding became Apache Parquet — now the dominant format for data lake and analytics workloads.
- Influenced Apache Drill, Amazon Athena, and modern OLAP query engines — the Dremel serving tree model is now standard for distributed SQL.

[Original](http://research.google.com/pubs/pub36632.html)
