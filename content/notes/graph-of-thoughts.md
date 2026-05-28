---
title: "Graph of Thoughts: Solving Elaborate Problems with LLMs"
date: 2023-08-24
categories:
  - llm
  - reasoning
  - prompting
  - research
  - graph
description: Graph of Thoughts (GoT) extends chain-of-thought and tree-of-thought prompting to arbitrary graph structures — letting LLM reasoning steps combine, branch, and loop rather than just proceeding linearly. More expressive than CoT or ToT for complex multi-step problems.
params:
  source: pinboard
  sourceUrl: https://github.com/spcl/graph-of-thoughts
---

![Graph of Thoughts: Solving Elaborate Problems with LLMs](/images/notes/graph-of-thoughts.png)

## Summary

[Graph of Thoughts](/notes/graph-of-thoughts/) (GoT) is a prompting and reasoning framework from ETH Zurich (SPCL lab) that extends the chain-of-thought and tree-of-thought paradigms to arbitrary directed acyclic graph structures. Where chain-of-thought produces a linear sequence of reasoning steps, and tree-of-thought produces a branching tree, [Graph of Thoughts](/notes/graph-of-thoughts/) allows reasoning nodes to merge (combining insights from multiple branches), loop, and form arbitrary dependency graphs.

The motivation: many complex problems don't decompose into linear or tree structures. Sorting a large list requires merging sorted sublists — a pattern that's natural in a graph (outputs of parallel sort subproblems feed into a merge node) but awkward to express in a linear chain. Multi-step planning with backtracking, scientific hypothesis generation with cross-referencing, and document summarization with synthesis all have similar graph-like dependency structures.

GoT achieves this by representing the reasoning process as a graph of thought operations — each node is an LLM call that can take multiple inputs (from preceding nodes) and produce multiple outputs (feeding into subsequent nodes). The implementation provides infrastructure for defining these graphs, executing them via LLM API calls, and backtracking when nodes fail. This is a generalization that subsumes CoT, ToT, and similar frameworks as special cases.

## Key points

- Generalizes chain-of-thought and tree-of-thought to arbitrary graph structures — merge, branch, loop.
- Enables reasoning patterns like: parallel subproblem solving → merging results → iterative refinement.
- More expressive than linear or tree reasoning for problems with complex dependency structures.
- From ETH Zurich SPCL lab; open-source implementation on GitHub.
- Subsumes CoT and ToT as special cases — a more general framework for LLM reasoning.

[Original](https://github.com/spcl/graph-of-thoughts)
