---
title: "Timely Dataflow: An Introduction"
date: 2013-09-18
categories:
  - distributed-systems
  - streaming
  - dataflow
  - microsoft-research
  - big-data
description: An introduction to Timely Dataflow, the distributed computation model developed at Microsoft Research that unified batch and streaming processing through a novel timestamp-based progress tracking system. A technically significant but underappreciated alternative to the Spark/Storm paradigm.
params:
  source: pinboard
  sourceUrl: http://bigdataatsvc.wordpress.com/2013/09/18/an-introduction-to-timely-dataflow/
---

![Timely Dataflow: An Introduction](/images/notes/timely-dataflow-introduction.png)

## Summary

Timely Dataflow is a distributed computation model developed at Microsoft Research by Frank McSherry, Murray Langdale, and colleagues. It was designed to unify batch and streaming computation under a single, general framework — a goal that Apache Spark Streaming pursued via micro-batches, but which Timely Dataflow addressed through a more principled abstraction: logical timestamps that track progress through iterative and cyclic dataflow graphs.

The core insight is that dataflow computations can be expressed as graphs where messages carry timestamps that encode both position in a stream and iteration count in a loop. By tracking the frontier of outstanding timestamps, the system can determine when a given computation epoch is complete — without the global synchronization barriers that made batch systems expensive. This enables incremental computation, iterative algorithms (like PageRank or gradient descent) and streaming pipelines to coexist in the same framework.

Timely Dataflow emerged from Naiad — the Microsoft Research system that first implemented these ideas at scale. The research was presented at SOSP 2013 and represented a genuine theoretical advance over the MapReduce model and its direct successors. Where Hadoop required separate batch and interactive stacks, and Storm handled streams without iteration, Naiad/Timely unified them at the cost of a more complex programming model.

## Key points

- Unified batch + streaming: the same code handles both by varying timestamp structure — no mode switch or separate stacks required.
- Logical timestamps as progress mechanism: messages carry `(time, iteration)` tuples; the runtime tracks the frontier to know when epochs complete.
- Enables efficient iterative computation — gradient descent, graph algorithms — without barriers, unlike Hadoop MapReduce.
- Predecessor to Differential Dataflow (also by McSherry) — which extended the model to incremental maintenance of arbitrary computations.
- Naiad was the production system; Timely Dataflow is the abstract model. Later re-implemented in Rust as the `timely` crate.
- Historically significant as a counter-narrative to Apache Spark's rise — Spark won mindshare through simplicity, but Timely was more expressive.

[Original](http://bigdataatsvc.wordpress.com/2013/09/18/an-introduction-to-timely-dataflow/)
