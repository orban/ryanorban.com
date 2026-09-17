---
title: "CMU 15-721: Advanced Database Systems"
date: 2021-05-23
categories:
  - database
  - systems
  - cmu
  - courses
  - performance
description: CMU 15-721 is Andy Pavlo's advanced database systems course covering in-memory databases, query compilation, concurrency control, and storage engines — the internals that most engineers never see. Free lectures, reading list of seminal papers, and a reputation as one of the best systems courses available.
params:
  source: pinboard
  sourceUrl: https://15721.courses.cs.cmu.edu/spring2020/
---

## Summary

CMU 15-721 is Andy Pavlo's graduate-level advanced database systems course at Carnegie Mellon University, focused on the internals of modern high-performance database systems — the layer below SQL that most application engineers never need to understand but that determines system-level performance. The Spring 2020 edition videos and reading materials are freely available online.

The course covers topics like in-memory databases (DRAM-based storage models, why disk-based assumptions break down), query compilation (converting query plans to native code via LLVM), vectorized execution (processing batches of rows rather than one at a time, as in systems like DuckDB and Vectorwise), multi-version concurrency control (MVCC), and lock-free data structures for high-throughput transaction processing. Each topic is accompanied by a seminal paper from the database literature.

Andy Pavlo is known for both his technical depth and his willingness to have opinions about database systems — the lectures include commentary on what approaches he thinks actually worked and which turned out to be dead ends. The reading list alone is valuable: papers on C-Store, Hekaton, H-Store, Peloton, and other influential systems form a compressed history of the last 20 years of database research.

## Key points

- Covers in-memory databases, query compilation, vectorized execution, MVCC, and lock-free concurrency.
- By Andy Pavlo (CMU) — free lectures, recorded and published; strong paper reading list.
- Query compilation via LLVM lets modern databases generate native code for query plans — 10-100x speedups over interpretation.
- Vectorized execution: batch-processing tuples (used by DuckDB, Vectorwise) vs. Volcano-style tuple-at-a-time.
- Pairs with CMU 15-445 (intro database systems) for a complete picture.

[Original](https://15721.courses.cs.cmu.edu/spring2020/)
