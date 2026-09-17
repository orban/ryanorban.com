---
title: "Parquet: Columnar Storage for Hadoop"
date: 2013-03-12
categories:
  - parquet
  - columnar-storage
  - hadoop
  - big-data
  - file-formats
description: The original announcement of Apache Parquet, the columnar storage format Twitter and Cloudera jointly released for Hadoop in 2013. Parquet became the dominant format for analytical workloads in the Hadoop/Spark ecosystem and remains ubiquitous in modern data lakes.
params:
  source: pinboard
  sourceUrl: http://parquet.github.com/
---

## Summary

Apache Parquet was announced in March 2013 as a joint project between Twitter and Cloudera, addressing a fundamental inefficiency in how Hadoop stored analytical data. The existing dominant format — SequenceFile (row-oriented) — was well-suited for bulk processing where every column was needed, but terrible for analytical queries that touch only a subset of columns. Google Dremel's 2010 paper had described a columnar format capable of answering nested record queries over terabytes in seconds; Parquet was the open-source implementation of those ideas for the Hadoop ecosystem.

Columnar storage stores each column's values contiguously on disk rather than storing each row together. For a query like `SELECT user_id, revenue WHERE country = 'US'`, a columnar store only reads the three relevant columns instead of scanning every row's full record. For wide tables with dozens of columns — common in OLAP workloads — this can mean reading 5-10% of the data. Parquet combined column-level compression (values in a column are often highly redundant, so run-length encoding and dictionary encoding work well) with predicate pushdown, meaning the storage layer can skip entire column chunks whose statistics (min/max per row group) can't satisfy the query predicate.

The encoding scheme in Parquet was based on Google Dremel's repetition and definition levels for representing nested structures (Protocol Buffers, Thrift schemas) in a flat columnar layout without losing structural information. This was non-trivial — the insight was that you could encode the nesting depth and whether each value was repeated or optional with just two small integers per value, adding back the nesting structure on read without the storage overhead of fully materializing nested records.

## Key points

- Columnar storage means per-query I/O reduction proportional to column projection width — typical analytical queries read 5–15% of data vs. row-oriented full scan
- Row-group level min/max statistics enable predicate pushdown: the reader skips entire blocks of rows that can't match a filter — without reading them
- Nested schemas (Protocol Buffers, Avro, Thrift) encoded via Google Dremel's repetition/definition level scheme — flat columnar storage with structural fidelity
- Dictionary and run-length encoding per column — consecutive repeated values common in low-cardinality columns (country codes, status enums) compress dramatically
- Became the lingua franca of the data lake era: Apache Spark, Apache Hive, Apache Impala, Presto, DuckDB, BigQuery all read/write Parquet natively
- Historical arc: Parquet (2013) → Apache Arrow (2016, in-memory columnar) → Delta Lake / Apache Iceberg (2020s, ACID transactions over Parquet) — each layer built on the previous

[Original](http://parquet.github.com/)
 → GitHub
