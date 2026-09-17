---
title: "Pig Not-So-Foreign Language: Paper Notes"
date: 2014-02-10
categories:
  - hadoop
  - pig
  - mapreduce
  - data-engineering
  - distributed-systems
description: "Bugra Akyildiz's notes on the 'Pig Latin: A Not-So-Foreign Language for Data Processing' paper by Yahoo! Research — explaining how Pig Latin compiles high-level data flow operations to MapReduce jobs. Captures why Pig was a meaningful step up from raw MapReduce for ETL work."
params:
  source: pinboard
  sourceUrl: http://bugra.github.io/work/notes/2014-02-09/pig-not-so-foreign-language-paper-notes/
---

## Summary

Bugra Akyildiz summarized the foundational "Pig Latin: A Not-So-Foreign Language for Data Processing" paper by Christopher Olston et al. from Yahoo! Research. Pig was Yahoo's answer to a recurring problem: MapReduce is powerful but tedious to write. Even simple data transformations — filter records by condition, join two datasets, group and aggregate — required writing Java code with explicit map and reduce functions. Pig Latin is a declarative data flow language that compiles to MapReduce jobs automatically.

The language design is intentionally SQL-adjacent but not SQL: instead of relational algebra on tables, it operates on bags (unordered collections of tuples with potentially heterogeneous schemas). `LOAD`, `FILTER`, `GROUP`, `FOREACH`, `JOIN`, `ORDER`, and `STORE` are the core operations. Each statement transforms a bag into another bag; the Pig compiler figures out the optimal MapReduce execution plan. The not-so-foreign in the title acknowledges that the language is familiar to programmers coming from Python or SQL without being identical to either.

In 2014, Pig was a significant part of the Hadoop ecosystem — used at Yahoo, Twitter, LinkedIn, and others for ETL pipelines. The competition was Hive (SQL-on-Hadoop), which proved more popular long-term because the SQL interface was more familiar. Both Pig and Hive were eventually supplanted by Apache Spark with its DataFrame API, which runs in-memory and handles both batch and interactive workloads.

## Key points

- Pig Latin: declarative data flow language that compiles to MapReduce — removes the need to write Java map/reduce functions for common data transformations.
- Bags of tuples (vs SQL's rows in tables): Pig's data model is more flexible than relational — tuples in the same bag can have different fields.
- Core operations: LOAD, FILTER, GROUP, FOREACH (apply transforms per record), JOIN, ORDER, STORE — compose to express complex data pipelines.
- Pig vs Hive: Pig is a data flow language (imperative feel), Hive is SQL (declarative) — Hive won the popularity contest because SQL was more familiar.
- Historical position: Pig bridged raw MapReduce and modern DataFrame APIs — the abstraction level it provided (Apache Spark's RDD API later went further).

[Original](http://bugra.github.io/work/notes/2014-02-09/pig-not-so-foreign-language-paper-notes/) → GitHub
