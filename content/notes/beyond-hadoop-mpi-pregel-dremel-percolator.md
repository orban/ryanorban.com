---
title: "Beyond Hadoop: Next-Generation Big Data Architectures"
date: 2013-03-14
categories:
  - hadoop
  - big-data
  - distributed-systems
  - pregel
  - dremel
  - mapreduce
description: GigaOM's 2010 survey of Google's next-generation big data architectures — MPI, Pregel, Dremel, and Percolator — that were being developed as alternatives or complements to MapReduce. The paper that first systematically articulated why MapReduce wasn't sufficient for everything.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/2010/10/23/beyond-hadoop-next-generation-big-data-architectures/
---

## Summary

This GigaOM piece from 2010 (bookmarked in 2013 when these ideas were entering wider discussion) surveyed the four Google systems that were redefining what large-scale data processing could look like beyond MapReduce. While Hadoop was becoming the industry standard for batch ETL, Google had already built specialized systems for graph processing, interactive queries, incremental updates, and tightly-coupled parallel computation — none of which MapReduce handled well.

Google Pregel (published 2010) solved the problem of running iterative graph algorithms at scale. MapReduce is a poor fit for graph processing because each iteration (e.g., one step of PageRank or shortest-path propagation) requires a full MapReduce job — disk I/O between every step, no way to preserve state across iterations. Pregel uses a bulk synchronous parallel (BSP) model: vertices compute in parallel, exchange messages at synchronization barriers, and the system handles fault tolerance via checkpointing. Apache Giraph and later Apache Spark's GraphX were open-source implementations.

Google Dremel (published 2010) enabled sub-second SQL-like queries over petabyte-scale datasets stored in columnar format. The key innovations: columnar storage (only read the columns you need), a tree-structured query execution model (multi-level serving tree parallelizes both scanning and aggregation), and the nested record encoding that became the foundation of Apache Parquet. Dremel was the precursor to Google BigQuery.

Google Percolator (published 2010) was built for incremental web index updates — re-processing only the changed portion of the web rather than doing a full MapReduce pass over everything. It provided distributed ACID transactions over Bigtable, using a snapshot isolation model with two-phase commit. The ideas influenced Apache HBase, Google Spanner, and modern streaming systems.

## Key points

- MPI (Message Passing Interface): scientific computing's parallel paradigm — fine-grained control, no fault tolerance, tightly coupled. MapReduce sacrificed performance for fault tolerance; MPI was the opposite trade-off.
- Google Pregel: BSP graph processing — vertices as units of computation, message passing between supersteps, fault tolerance via checkpoints. Implemented open-source as Apache Giraph.
- Google Dremel: columnar interactive queries at petabyte scale — the architecture behind BigQuery and the source of Apache Parquet's encoding scheme.
- Google Percolator: distributed ACID transactions on Bigtable for incremental processing — avoid recomputing everything when only a fraction of inputs changed.
- The unifying insight: MapReduce is one programming model, not the universal model. Different workloads (graph, interactive OLAP, streaming updates, HPC) need different abstractions.
- Historical significance: by 2013 these Google papers were motivating YARN (to support multiple frameworks), Apache Spark (in-memory iterative), and eventually the broader disaggregation of the Hadoop monolith.

[Original](http://gigaom.com/2010/10/23/beyond-hadoop-next-generation-big-data-architectures/)
