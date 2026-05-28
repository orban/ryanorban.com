---
title: Suffix Trees in Computational Biology
date: 2012-06-04
categories:
  - algorithms
  - bioinformatics
  - data-structures
  - string-matching
  - computational-biology
description: A course page on suffix trees in computational biology from the University of Saskatchewan. Suffix trees are the data structure behind fast substring search in genomic sequences — O(n) construction, O(m) query — making genome-scale string matching tractable.
params:
  source: pinboard
  sourceUrl: http://homepage.usask.ca/~ctl271/857/suffix_tree.shtml
---

## Summary

A suffix tree is a compressed trie of all suffixes of a given string. For a string of length n, it can be built in O(n) time (via Ukkonen's algorithm) and enables O(m) substring search (where m is the query length) regardless of the text size. This makes it the fundamental data structure for pattern matching in large genomic sequences — a genome with billions of base pairs is still searchable in microseconds once the suffix tree is built.

The University of Saskatchewan course page (likely from a bioinformatics or algorithms course) covered suffix trees in the context of sequence alignment, repeat finding, and related computational biology problems. Key applications include: finding all occurrences of a pattern in a genome, identifying tandem repeats and interspersed repeats, computing longest common substrings between sequences, and serving as the index structure in read mapping tools.

Before FM-index and Burrows-Wheeler transform-based tools like BWA and Bowtie largely displaced them for short-read alignment (because BWT is more memory-efficient), suffix trees were central to tools like MUMmer for whole-genome alignment. The suffix tree lineage now lives in suffix arrays and FM-indices, which trade some query flexibility for dramatic memory reduction.

## Key points

- Suffix tree: compressed trie of all suffixes, O(n) build (Ukkonen's algorithm), O(m) pattern search.
- Critical for genome-scale string searching: a 3 billion base-pair human genome is still searchable quickly with a prebuilt index.
- Applications: pattern matching, repeat detection, longest common substring, genome comparison.
- Ukkonen's algorithm (1995) enabled linear-time construction — the breakthrough that made suffix trees practical.
- Largely succeeded by FM-index / BWT-based tools (BWA, Bowtie) for short-read alignment due to memory efficiency.

[Original](http://homepage.usask.ca/~ctl271/857/suffix_tree.shtml)
