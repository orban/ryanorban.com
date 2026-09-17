---
title: Advanced Algorithms and Data Structures
date: 2022-04-04
categories:
  - algorithms
  - data-structures
  - computer-science
  - book
  - manning
description: Marcello La Rocca's Manning textbook on advanced algorithms and data structures, organized around practical problems like caching, nearest-neighbor search, clustering, and graph planarity. A useful reference for engineers who have outgrown intro-level algorithms and need principled solutions to real design challenges.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Marcello La Rocca - Advanced Algorithms and Data Structures-Manning Publications (2021).pdf
---

## Summary

*Advanced Algorithms and Data Structures* by Marcello La Rocca (Manning, 2021) takes a problem-first approach: each chapter introduces a practical engineering problem — caching, spell-check, nearest-neighbor search, clustering — then develops the data structure or algorithm that solves it. The book covers a wide arc from foundational structures like priority queues, treaps, and bloom filters to more advanced territory including k-d trees, clustering algorithms, and graph planarity detection.

The organization mirrors how algorithmic problems actually arise in practice. A chapter on distributed caching follows from the single-node caching chapter; distributed clustering follows from single-machine clustering. This makes it useful as a reference during system design, not just as exam preparation.

The final chapters address shortest path algorithms on dynamic maps and techniques for visualizing graph structures in 2D planes — topics that seldom appear in introductory texts but come up constantly in geospatial and infrastructure engineering.

## Key points

- Problem-driven structure: each chapter starts with a real scenario (spell-check, autocomplete, T9 keyboards) before introducing the algorithm that addresses it
- Covers bloom filters, treaps, skip lists, and radix trees as space-efficient alternatives to standard containers
- Dedicated chapters on k-d trees and R-trees for spatial data, with applications to nearest-neighbor and similarity search in high dimensions
- Graph chapters cover Dijkstra's algorithm variants, A* search, and planar graph embedding — including segment intersection and graph drawing on a 2D plane
- Clustering section distinguishes between local (single-machine) and distributed clustering approaches

[Original document](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/Marcello%20La%20Rocca%20-%20Advanced%20Algorithms%20and%20Data%20Structures-Manning%20Publications%20(2021).pdf)
