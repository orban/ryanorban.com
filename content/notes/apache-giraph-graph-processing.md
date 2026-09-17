---
title: Apache Incubator Giraph — Distributed Graph Processing on Hadoop
date: 2013-03-31
categories:
  - hadoop
  - graph-processing
  - distributed-systems
  - big-data
  - apache
description: Apache Giraph is a graph processing framework built on Hadoop — an open-source implementation of Google's Pregel model for iterative graph algorithms at scale. The Apache answer to graph-scale problems like PageRank, community detection, and shortest paths on billion-node graphs.
params:
  source: pinboard
  sourceUrl: https://incubator.apache.org/giraph/
---

![Apache Incubator Giraph — Distributed Graph Processing on Hadoop](/images/notes/apache-giraph-graph-processing.png)

## Summary

Apache Giraph was an open-source implementation of Google Pregel — Google's internal bulk synchronous parallel (BSP) graph processing system described in a 2010 paper. Pregel solved the problem of running iterative graph algorithms (like PageRank, shortest paths, or community detection) on graphs with billions of nodes and edges, where the data doesn't fit in memory on a single machine and the iterative nature of graph algorithms makes MapReduce extremely inefficient (each iteration requires a new MapReduce job with full disk I/O).

Giraph ran on Apache Hadoop's infrastructure but used a fundamentally different computation model: the vertex-centric (or think like a vertex) model where each vertex executes a user-defined `compute()` function, can send messages to neighboring vertices, and the framework coordinates synchronous supersteps between iterations. This is far more efficient than MapReduce for graph workloads: vertices only process messages from their neighbors, message passing happens in-memory between supersteps, and the algorithm terminates when no vertex has messages to process.

Facebook was the primary corporate contributor to Giraph, using it internally for social graph analytics at scale. The use case: analyzing Facebook's social graph (at the time, ~1 billion users and their connections) for friend recommendations, spam detection, and community identification. Yahoo contributed improvements around the time of the bookmark. The main competition to Giraph was GraphX (Apache Spark's graph library), which launched in 2013 and offered a more ergonomic API by leveraging Spark's RDD model.

## Key points

- Google Pregel model: bulk synchronous parallel (BSP) computation — vertices execute in parallel supersteps, exchanging messages with neighbors.
- Vertex-centric programming: users implement `compute()` for each vertex; the framework handles distribution, fault tolerance, and superstep coordination.
- Facebook production use: social graph analytics at billion-node scale — community detection, friend recommendations, spam signals.
- Compared to MapReduce: Giraph avoids repeated disk I/O for iterative algorithms — supersteps communicate via in-memory message passing.
- Superseded by GraphX (Apache Spark): Spark's 2013 graph library offered similar algorithms with a more ergonomic DataFrame-style API.

[Original](https://incubator.apache.org/giraph/)
