---
title: A Library for Representing Python Programs as Graphs for Machine Learning
date: 2022-08-24
categories:
  - program-analysis
  - machine-learning
  - graph-neural-networks
  - code
  - research
description: Google Research library paper introducing python_graphs — an open-source tool for constructing graph representations of Python programs via static analysis, producing control flow graphs, data flow graphs, and program dependence graphs. Standardizes the infrastructure for ML-on-code research so researchers don't each rebuild the graph extraction layer.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2208.07461v1.pdf
---

## Summary

David Bieber, Kensen Shi, Petros Maniatis, Charles Sutton, Daniel Johnson, Vincent Hellendoorn, and Daniel Tarlow at Google Research and Carnegie Mellon University introduce `python_graphs` — an open-source Python library for constructing graph representations of programs via static analysis. The library is designed specifically for machine learning on code research, where graph-structured program representations feed into graph neural networks (GNNs).

The core representations the library produces: control flow graphs (CFGs), data flow graphs (DFGs), and program dependence graphs (PDGs), each capturing different aspects of program semantics. CFGs capture execution order; DFGs capture how data values propagate through the program; PDGs combine both into a unified representation. These graphs serve as input to downstream ML tasks: bug detection, code completion, type inference, variable naming.

The motivation is infrastructure: every research group building ML-for-code systems independently reimplements program graph extraction, introducing inconsistencies and wasted effort. `python_graphs` provides a canonical, reusable implementation. The Google Research group behind it (Bieber, Tarlow, Sutton et al.) had been working on program synthesis and program understanding for years, and several of their papers depended on this kind of representation — codifying it as a library makes the work reproducible and extensible.

## Key points

- `python_graphs`: library for constructing CFG, DFG, and PDG representations of Python programs via static analysis
- Targets ML on code research — standard graph inputs for GNN-based program analysis models
- Eliminates duplicated infrastructure across research groups — shared canonical implementation
- Relevant to bug detection, type inference, variable naming, and other code intelligence tasks
- Google Research team includes Vincent Hellendoorn — also author of DIFFUSER, showing overlap between code and text generation research
- Static analysis approach: no execution required, works on syntactically valid Python

[Original (arXiv 2208.07461)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2208.07461v1.pdf)
