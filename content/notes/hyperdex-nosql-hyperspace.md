---
title: "HyperDex: NoSQL Database Based in Hyperspace"
date: 2012-08-12
categories:
  - nosql
  - databases
  - distributed-systems
  - hyperspace
  - research
description: The HyperDex academic paper introducing a NoSQL key-value store that used hyperspace hashing to support efficient secondary attribute searches — the main weakness of most key-value stores at the time. An elegant theoretical approach that didn't achieve mainstream adoption.
params:
  source: pinboard
  sourceUrl: http://hyperdex.org/papers/hyperdex.pdf
---

## Summary

The HyperDex academic paper introduced a distributed key-value store with a novel approach to secondary attribute search. The central problem HyperDex solved: most key-value stores (like Cassandra, Riak, or Redis) are fast at lookup by primary key, but searching by any non-key attribute requires a full table scan or maintaining separate secondary indexes. HyperDex addressed this with hyperspace hashing — a technique that maps objects with multiple attributes into a multi-dimensional hyperspace where each attribute defines a dimension.

The hyperspace hashing idea: instead of hashing objects to a 1D ring (as consistent hashing in Dynamo-style systems does), HyperDex hashes each object to a point in N-dimensional space, where N is the number of searchable attributes. Servers are responsible for regions (hypercubes) of this space. A search for objects where attribute A = x AND attribute B = y maps to a subspace intersection, allowing the system to identify exactly which servers hold matching objects without a full scan. This is elegant — secondary attribute searches become O(servers in subspace) rather than O(all servers).

HyperDex came out of Cornell University research and was notable enough that Ryan and others in the NoSQL community called it "fascinating" at the time. The practical limitations: hyperspace hashing requires knowing your query patterns at schema design time (which attributes will be searched), and the approach doesn't generalize well to arbitrary ad-hoc queries. It remained primarily a research project rather than achieving production adoption at scale.

## Key points

- "Hyperspace hashing" maps objects to points in N-dimensional space, one dimension per searchable attribute.
- Servers own hypercube regions; secondary attribute searches intersect subspaces rather than doing full scans.
- Solves the core key-value store weakness: efficient search on non-primary-key attributes.
- Came from Cornell University research; the lead researcher was Emin Gün Sirer.
- Design requires knowing query patterns upfront — doesn't support ad-hoc queries on arbitrary attributes.
- Remained a research project; didn't achieve the production adoption that Cassandra or MongoDB did.

[Original](http://hyperdex.org/papers/hyperdex.pdf)
