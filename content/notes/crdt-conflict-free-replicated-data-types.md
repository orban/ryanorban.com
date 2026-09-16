---
title: "CRDTs: Conflict-free Replicated Data Types"
date: 2022-04-02
categories:
  - distributed-systems
  - data-structures
  - collaboration
  - consistency
  - computer-science
description: crdt.tech is the canonical reference hub for Conflict-free Replicated Data Types — the data structures that enable real-time collaborative editing without central coordination. The math guarantees eventual consistency even when network partitions split collaborators.
params:
  source: pinboard
  sourceUrl: https://crdt.tech/
---

## Summary

CRDTs (Conflict-free Replicated Data Types) are data structures designed for distributed systems where multiple nodes need to update shared state without coordinating through a central server. The defining property: any two replicas that have received the same set of operations will converge to the same state, regardless of the order those operations arrived. This makes CRDTs the mathematical foundation for real-time collaborative applications — the technology behind collaborative text editors, shared todo lists, and offline-first apps.

The crdt.tech site aggregates research papers, blog posts, and implementations into a single reference point for the field. CRDTs come in two main flavors. State-based CRDTs (CvRDTs) merge full replica states — nodes gossip their complete state and merge using a join semilattice operation that must be commutative, associative, and idempotent. Operation-based CRDTs (CmRDTs) broadcast individual operations — the operations themselves must be commutative. The tradeoff is communication overhead: state-based requires sending full state (larger messages, simpler delivery guarantees), operation-based requires reliable exactly-once delivery (smaller messages, harder guarantees).

Practical examples make this concrete: a G-Counter (grow-only counter) is a simple CRDT where each node maintains its own counter and the merged value is the max of each node's count. An OR-Set (observed-remove set) lets nodes add and remove elements, with the twist that removes only apply to additions the node has observed — concurrent add/remove on different nodes resolves toward keep. These primitives compose into more complex structures. Yjs and Automerge are popular CRDT implementations that power real-world collaborative tools.

## Key points

- CRDTs guarantee eventual consistency without a central coordination point — they just work across partitions and concurrent edits.
- State-based CRDTs merge full replica states; operation-based CRDTs broadcast individual updates — different tradeoffs in message size vs. delivery guarantees.
- Idempotency, commutativity, and associativity are the algebraic properties that make convergence proofs work.
- Yjs and Automerge are the most widely deployed CRDT libraries — used in tools like Obsidian, Notion, and various collaborative editors.
- Alternative to OT (Operational Transformation — used in Google Docs) — CRDTs are simpler to implement correctly and don't require a central server.
- Active research area: text CRDTs that preserve user intent, sequence CRDTs with good performance, rich-text support.

[Original](https://crdt.tech/)
