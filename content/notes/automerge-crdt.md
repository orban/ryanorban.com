---
title: "Automerge: CRDTs for Collaborative Applications"
date: 2022-12-06
categories:
  - crdt
  - collaboration
  - distributed-systems
  - local-first
  - open-source
description: Automerge is a CRDT (Conflict-free Replicated Data Type) library for building collaborative applications that work offline and sync automatically without conflicts. The technical foundation of the local-first software movement.
params:
  source: pinboard
  sourceUrl: https://automerge.org/docs/hello/
---

## Summary

Automerge is a CRDT (Conflict-free Replicated Data Type) library for JavaScript and Rust that provides a JSON-like data structure that can be modified concurrently by multiple users, synced peer-to-peer or via a server, and always merged deterministically without conflicts. The design goal is to enable local-first software — applications that store data locally, work offline, and sync when connected, giving users full ownership of their data.

The mathematical property that makes this work: CRDTs guarantee that any two replicas that have seen the same set of operations will be in the same state, regardless of the order operations arrived. Unlike Operational Transformation (OT) used by Google Docs, CRDTs don't require a central server to mediate conflict resolution — they can sync peer-to-peer. Automerge implements a specific CRDT design (based on the RGA algorithm for sequences) that handles text, lists, and maps.

Automerge is associated with the local-first software movement articulated by Martin Kleppmann (who co-created Automerge) and colleagues in their 2019 paper. The vision: applications that are as collaborative as Google Docs but as private and ownership-preserving as local files. Ink & Switch (the research lab behind the local-first ideas) used Automerge as the foundation for several experimental apps. Automerge 2.0 (released 2023) rewrote the core in Rust with WASM bindings for a 10x performance improvement. Tools like Liveblocks and PartyKit offer hosted infrastructure for similar use cases with less manual CRDT management.

## Key points

- CRDT library enabling conflict-free collaborative data structures that sync without a central coordinator.
- Works offline — syncs when connected; data lives locally, can sync peer-to-peer or via relay.
- JSON-like data model (maps, lists, text) with deterministic merge semantics.
- Created by Martin Kleppmann and associated with the local-first software research movement.
- Automerge 2.0 (2023) rewrote core in Rust with WASM — 10x performance over original.
- Competes with approaches like hosted Liveblocks, PartyKit, and Yjs (another CRDT library).

[Original](https://automerge.org/docs/hello/)
