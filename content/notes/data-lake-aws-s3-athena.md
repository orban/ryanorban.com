---
title: Building a Data Lake with AWS S3 and Athena
date: 2020-09-22
categories:
  - data-engineering
  - aws
  - cloud
  - data-lake
  - sql
description: A tutorial on replacing a costly Redshift cluster with a serverless data lake using AWS S3 and Athena — demonstrating 16-minute queries reduced to 11 seconds at 10 cents a run using Parquet, partitioning, and Glue ETL. Practical architectural migration case study.
params:
  source: pinboard
  sourceUrl: https://medium.com/swlh/tutorial-build-your-data-lake-using-aws-s3-athena-150c1aaa44cf
---

## Summary

This tutorial documents migrating from a 32-node Redshift cluster (expensive, tightly coupled storage and compute) to a serverless data lake architecture using AWS S3, Amazon Athena, and AWS Glue. The result: a 16–17 minute query reduced to 11 seconds at 10 cents per run — a 90x speedup and dramatic cost reduction.

The architecture separates storage from compute, which is the fundamental move. Raw data lives in S3 as cheap object storage. Athena is a managed Presto-based query engine that queries S3 data directly without provisioning infrastructure — you pay $5/TB scanned, so minimizing data scanned is the optimization target. AWS Glue Catalog provides the schema metadata that lets Athena understand file structure, column types, and partitioning.

Four optimizations compound to get the query time from minutes to seconds: **columnar format** (converting CSV/JSON to Apache Parquet so only needed columns are read), **partitioning** (organizing data by frequently-filtered fields like year/month so Athena skips irrelevant partitions), **compression** (Snappy reduces file sizes without impacting speed), and **file sizing** (128MB+ per file for efficient distributed processing). AWS Glue jobs apply these transformations using Apache Spark.

## Key points

- Apache Parquet is the key format choice: columnar storage means analytical queries that use only a few columns don't pay the cost of reading all columns — especially important at 8B+ record scale.
- Partitioning in S3 is physical folder organization: `s3://bucket/year=2020/month=10/` means Athena skips all other months entirely. Design partitions around your most common filter dimensions.
- AWS Glue bookmarks track which data has been processed — ensures ETL jobs don't redundantly reprocess records.
- The Athena + S3 pattern has become the canonical serverless analytics architecture; alternatives include BigQuery, Snowflake External Tables, and DuckDB for smaller-scale queries.
- Trade-off vs. Redshift: Athena is slower for sub-second query latency, better for ad-hoc analytics on large infrequently-queried datasets.

[Original](https://medium.com/swlh/tutorial-build-your-data-lake-using-aws-s3-athena-150c1aaa44cf)
