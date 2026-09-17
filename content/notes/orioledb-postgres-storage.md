---
title: "OrioleDB: Modern Cloud-Native PostgreSQL Storage Engine"
date: 2022-02-25
categories:
  - postgresql
  - databases
  - storage-engine
  - open-source
  - performance
description: OrioleDB is a PostgreSQL table access method (storage engine) built to solve PostgreSQL's wicked scalability problems — bloat, vacuum overhead, lock contention — by using a copy-on-write B-tree and row-level WAL. Aims to make PostgreSQL cloud-native without forking it.
params:
  source: pinboard
  sourceUrl: https://github.com/orioledb/orioledb
---

## Summary

OrioleDB is an alternative storage engine for PostgreSQL — a table access method (TAM) that replaces the default heap storage with a new design built for modern hardware and cloud environments. PostgreSQL's default storage engine was designed decades ago and has accumulated technical debt that manifests as real operational pain: table bloat (dead rows accumulate until VACUUM reclaims them), VACUUM contention (VACUUM needs to scan tables, which competes with queries), buffer manager contention (the shared buffer cache uses coarse-grained locks), and poor multi-core scaling at high concurrency.

OrioleDB addresses these with a fundamentally different architecture: a copy-on-write B-tree structure that eliminates the bloat/vacuum cycle by design, row-level WAL (write-ahead logging) instead of block-level WAL (smaller logs, faster recovery), and undo chains for MVCC that don't rely on dead tuple accumulation. The result is an engine that can handle high-write workloads with much less operational overhead than standard PostgreSQL.

The approach — extending PostgreSQL via its table access method API rather than forking it — is deliberate. OrioleDB wants to be a drop-in storage upgrade, not a new database. You can mix regular heap tables and OrioleDB tables in the same database. This makes adoption incremental rather than all-or-nothing.

The project was created by Alexander Korotkov, one of PostgreSQL's major committers, which gives it significant technical credibility. The wicked problems framing in the GitHub description acknowledges that these are not simple bugs — they're design constraints in PostgreSQL's architecture that can't be fixed without substantial changes to the storage layer.

## Key points

- Implements PostgreSQL table access method (storage engine) interface — extends PostgreSQL without forking.
- Copy-on-write B-tree eliminates table bloat and the vacuum overhead cycle that plagues write-heavy PostgreSQL.
- Row-level WAL vs. block-level WAL: smaller logs, faster crash recovery.
- MVCC via undo chains — reads don't need to scan dead tuples to check visibility.
- Created by Alexander Korotkov, a core PostgreSQL committer — high technical credibility.
- Directly addresses cloud-native pain points: bloat accumulation in long-running services, vacuum contention under load.

[Original](https://github.com/orioledb/orioledb)
