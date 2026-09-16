---
title: Apache Incubator Giraph
date: 2012-07-07
categories:
  - hadoop
  - graph-processing
  - distributed-systems
  - big-data
  - apache
description: Apache Giraph's incubator homepage from 2012 — the open-source implementation of Google's Pregel bulk-synchronous-parallel graph processing model. Bookmarked during an early phase of the Hadoop ecosystem expansion into graph workloads.
params:
  source: pinboard
  sourceUrl: https://giraph.apache.org/
---

## Summary

Apache Giraph entered the Apache Incubator as the open-source community's answer to Google Pregel — Google's internal system for running iterative graph algorithms at massive scale. The basic problem: MapReduce handles batch processing well but is a poor fit for graph computation, where algorithms like PageRank and shortest paths require many iterations, each needing to pass state between neighboring vertices. Running each iteration as a separate MapReduce job means repeated disk I/O between every step — prohibitively slow for large graphs.

Giraph's model is vertex-centric programming: you write a `compute()` function from the perspective of a single vertex. That vertex receives messages from its neighbors, updates its own value, and sends messages to its neighbors for the next round. The framework runs these compute phases in synchronous supersteps across a distributed cluster — a bulk synchronous parallel (BSP) execution model. When no vertex has messages to process, the algorithm halts. This makes it efficient for iterative graph algorithms: message passing happens in-memory between supersteps, no disk required.

In 2012, Facebook was the primary industrial contributor to Giraph, using it for social graph analytics at the billion-node scale — friend recommendations, spam detection, community identification. The Apache Hadoop infrastructure meant Giraph could run on existing Hadoop clusters without separate hardware. The main competitor that emerged was GraphX (Apache Spark's graph library, launched 2013), which offered a more ergonomic API on top of Spark's RDD model. See also the earlier Google Pregel paper and the later Beyond Hadoop survey linking Pregel, Dremel, and Percolator as the generation of Google systems that MapReduce couldn't replicate.

## Key points

- Vertex-centric programming: write `compute()` per vertex; the framework handles distribution, superstep coordination, fault tolerance.
- Bulk synchronous parallel (BSP) model: all vertices compute in parallel, exchange messages at barriers — efficient for iterative graph workloads where MapReduce requires a full job per iteration.
- Runs on Apache Hadoop infrastructure — no separate cluster needed for graph workloads.
- Facebook primary contributor in 2012; used for social graph analytics at billion-node scale.
- Superseded in practice by GraphX (Apache Spark) after 2013 — Spark's model is more ergonomic and general.
- Connected to the broader 2012 big data ecosystem expansion: Apache Hive, Apache HBase, YARN, Dremel/Google BigQuery all emerging simultaneously.

[Original](https://giraph.apache.org/)
