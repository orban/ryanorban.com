---
title: Indexing 1,600,000,000 Keys with Automata and Rust
date: 2021-08-21
categories:
  - data-structures
  - algorithms
  - rust
  - search
  - computer-science
description: Andrew Gallant's deep technical post on using finite state transducers to index 1.6 billion keys in a compact data structure — the basis for ripgrep and the fst crate. A masterclass in how the right data structure unlocks orders-of-magnitude improvements.
params:
  source: pinboard
  sourceUrl: https://blog.burntsushi.net/transducers/
---

## Summary

Andrew Gallant (BurntSushi), author of ripgrep and regex crate, describes how finite state transducers (FSTs) can index 1.6 billion keys in a few gigabytes — orders of magnitude more memory-efficient than hash maps or B-trees for certain workloads. This post is the documentation for the fst Rust crate, but it reads as a self-contained explanation of why FSTs matter and when to use them.

The key insight: a finite state automaton (FSA) can represent a set of strings compactly by sharing common prefixes and suffixes across all strings in the set. A finite state transducer extends this to map strings to values, making it usable as a key-value store. For workloads with many similar keys (URLs, natural language words, code identifiers), the sharing is extreme — you can represent millions of strings in megabytes rather than gigabytes.

The fst crate enables efficient operations over these structures: membership testing (is this key in the set?), ordered iteration (keys in lexicographic order), range queries, fuzzy search (keys within edit distance N), and regex queries — all operating directly on the FST without decompressing to a flat structure. This combination of compactness and query expressiveness makes FSTs ideal for search engine dictionary indexes, spell-checkers, and autocomplete systems. Elasticsearch and Lucene both use FSTs internally.

## Key points

- Finite state transducer (FST): a DAG that encodes a sorted string map with maximum prefix/suffix sharing.
- Memory efficiency: 1.6B keys in a few GB — possible because common prefix/suffix structure is shared, not repeated.
- Operations on the FST directly: membership, ordered iteration, range, fuzzy search, regex — no decompression step.
- Used internally by Elasticsearch/Lucene for their inverted index term dictionary.
- fst crate by Andrew Gallant — production-quality implementation in Rust.

[Original](https://blog.burntsushi.net/transducers/)
