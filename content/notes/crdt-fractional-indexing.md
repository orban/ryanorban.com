---
title: "CRDT: Fractional Indexing"
date: 2022-11-27
categories:
  - crdt
  - distributed-systems
  - algorithms
  - collaborative-editing
description: Evan Wallace's visual explainer of fractional indexing as a CRDT technique for ordered lists — items get floating-point positions between existing neighbors. A clean conceptual foundation for understanding how collaborative list ordering works without central coordination.
params:
  source: pinboard
  sourceUrl: https://madebyevan.com/algos/crdt-fractional-indexing/
---

## Summary

Fractional indexing is a technique for representing ordered lists in CRDT (Conflict-free Replicated Data Type) systems. The core idea: instead of using integer positions that would require renumbering on insertion, assign each item a fractional coordinate between its neighbors. Inserting between items at positions 0.5 and 1.0 yields a new item at 0.75 — no other items need to change. This means concurrent insertions from different peers can be merged without conflict.

Evan Wallace (co-creator of Figma and esbuild) built this interactive explainer to show how the algorithm works visually. The demo lets you insert items and watch position values evolve. The connection to Figma's multiplayer is direct — fractional indexing is one of the foundational primitives for collaborative layer ordering and list operations in real-time apps.

The limitation is coordinate growth: if you keep inserting between the same two items, the fractional part gets longer. Real systems address this with coordinate compression (periodically rebalancing positions when no peers are active) or switching to a more sophisticated sequence CRDT like RGA or LSEQ that avoids unbounded growth. For many practical use cases — reordering todo items, layers in a design tool — fractional indexing is sufficient and much simpler to implement than full sequence CRDTs like Automerge.

## Key points

- Fractional indexing: assign items float positions between neighbors, enabling conflict-free concurrent insertions.
- No renumbering on insert — adjacent items are unaffected, making it CRDT-compatible without complex logic.
- Used in practice by Figma and tools like Linear for list ordering and layer stacks.
- Limitation: repeated insertions at the same position produce increasingly long fractional coordinates.
- Simpler alternative to sequence CRDTs like RGA; pairs with local-first software architectures.

[Original](https://madebyevan.com/algos/crdt-fractional-indexing/)
