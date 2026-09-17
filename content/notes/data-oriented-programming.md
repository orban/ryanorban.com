---
title: Data-Oriented Programming
date: 2020-10-05
categories:
  - programming
  - software-design
  - data-oriented-programming
  - functional-programming
  - architecture
description: Yehonathan Sharvit's book on Data-Oriented Programming — four principles for separating code from data, using generic structures, embracing immutability, and decoupling schema from representation. A response to the complexity of OOP.
params:
  source: pinboard
  sourceUrl: https://blog.klipse.tech//data-oriented-programming-book.html
---

## Summary

[Data-Oriented Programming](/notes/data-oriented-programming/) (DOP) is a paradigm described by Yehonathan Sharvit in his Manning Publications book as an alternative to object-oriented programming for managing system complexity. The paradigm rests on four principles: separate code from data, represent data with generic data structures, embrace immutability, and decouple schema from representation.

The key move is rejecting the OOP practice of bundling data and behavior into objects with encapsulated state. Instead, DOP keeps functions and data separate — data is passed into functions, which are stateless. Generic data structures (maps, lists, sets) replace custom classes, making data uniformly accessible without a class hierarchy. Immutability eliminates the class of bugs where shared state changes unexpectedly; persistent data structures (structural sharing) make this practical without copying entire objects.

The schema-representation decoupling principle is subtler: what data means (its schema) is separate from how it's physically stored. This enables flexible data evolution — you can validate, coerce, and document data shape without it being baked into class definitions.

The book positions DOP as complementary to functional programming (shared emphasis on immutability and pure functions) but language-agnostic — the principles apply in Python, Java, JavaScript, or Clojure, not just functional languages.

## Key points

- Separating code from data makes functions more reusable and testable — a function that takes a generic map is easier to compose than one that requires a specific object type.
- Generic data structures (maps and lists) unlock generic tooling: serialization, logging, diffing, merging — all work without custom code per type.
- Immutability eliminates a large class of concurrency bugs — concurrent reads of immutable data need no locking.
- Decoupled schema validation (e.g., via JSON Schema or clojure.spec) allows runtime validation without compile-time class coupling.
- This is a direct critique of the complexity OOP introduces: deep class hierarchies, mutable shared state, and the god object anti-pattern.

[Original](https://blog.klipse.tech//data-oriented-programming-book.html)
