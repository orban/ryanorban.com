---
title: "py-caskdb: Educational Disk-Based Key-Value Store"
date: 2022-05-08
categories:
  - databases
  - storage-engines
  - education
  - python
  - open-source
description: py-caskdb is an educational Python implementation of the Bitcask storage model — a log-structured, append-only disk-based key-value store. A hands-on way to understand how real KV stores like Riak's Bitcask backend achieve fast writes with crash safety.
params:
  source: pinboard
  sourceUrl: https://github.com/avinassh/py-caskdb
---

## Summary

[py-caskdb](/notes/py-caskdb/) is an educational Python implementation of the Bitcask storage model — the log-structured, append-only key-value store originally developed for Riak. The goal is explicitly pedagogical: by building a working key-value store from scratch, you understand how real storage systems achieve their properties. The code is intentionally minimal and readable, designed to be studied rather than deployed.

The Bitcask model is elegant: all writes go to the end of an append-only log file on disk, which makes write performance predictable (always sequential, never random). An in-memory hash table (the keydir) maps every key to its latest value's location in the log — byte offset, file ID, and size. A read is one disk seek to that offset. This makes both reads and writes O(1) in the common case. The tradeoff: the keydir must fit in memory, so Bitcask is bounded by the size of your key set. Compaction (merging in Bitcask terminology) periodically rewrites log files to reclaim space from overwritten/deleted keys.

Building this yourself teaches the gap between a simple hash map and a production storage engine: crash recovery (replaying the log on startup), write-ahead logging, file rotation when log files grow too large, and the careful ordering of disk fsyncs needed for durability. These same patterns appear in LevelDB, RocksDB, SQLite (WAL mode), and essentially every serious storage system. py-caskdb makes the concepts concrete with a codebase you can actually read in an afternoon.

## Key points

- Bitcask model: append-only log for writes + in-memory keydir (key → disk offset) for fast reads — both ops are O(1).
- Crash recovery: rebuild the keydir by replaying the on-disk log on startup.
- Compaction: periodic log rewriting to reclaim space from stale entries — a core LSM-tree operation.
- Teaches storage engine fundamentals: WAL, log-structured writes, durability semantics, file rotation.
- Educational Python implementation by Avinash Sajjan — meant to be read, not scaled.
- Foundation for understanding LevelDB, RocksDB, and SQLite's WAL mode at a conceptual level.

[Original](https://github.com/avinassh/py-caskdb) → GitHub
