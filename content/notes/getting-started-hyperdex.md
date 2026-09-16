---
title: Getting Started with HyperDex
date: 2012-08-12
categories:
  - nosql
  - hyperdex
  - databases
  - tutorial
description: A practitioner's getting-started guide to HyperDex — the NoSQL database based on hyperspace hashing — showing how to install, configure, and run basic operations. Pairs with the academic paper as the hands-on entry point.
params:
  source: pinboard
  sourceUrl: http://micrypt.com/2012/08/10/Getting-started-with-HyperDex.html
---

![Getting Started with HyperDex](/images/notes/getting-started-hyperdex.png)

## Summary

A practitioner's getting-started guide to HyperDex, the NoSQL database based on hyperspace hashing, walking through installation, cluster setup, and basic CRUD operations. The guide was written shortly after HyperDex was published as a research paper, serving as the hands-on complement to the academic description.

HyperDex's setup involved a coordinator node (which managed cluster membership and hyperspace assignments) and data nodes (which stored the actual data and handled client requests). The client API was available in Python and C at the time, with the Python bindings being the more accessible starting point. Basic operations looked similar to other key-value stores: `put(space, key, attributes)` and `get(space, key)`, with the unique feature being `search(space, predicate)` which efficiently searched across attribute combinations using the hyperspace partitioning.

The guide was part of a small but enthusiastic community around HyperDex in 2012 — the idea was genuinely clever and the implementation appeared solid. The limitation that became apparent to practitioners: the hyperspace must be defined upfront with all searchable attributes specified, and adding new searchable attributes later required data migration. This schema-on-write requirement for query patterns was an unusual constraint for a system marketed as NoSQL (which generally promised schema flexibility).

## Key points

- HyperDex setup: coordinator node for cluster management + data nodes for storage.
- Client APIs available in Python and C; Python bindings most accessible for experimentation.
- `search(space, predicate)` is the killer feature — efficient multi-attribute search via hyperspace partitioning.
- Searchable attributes must be declared upfront — a schema-on-write constraint unusual for NoSQL.
- Adding new searchable attributes after initial deployment requires data migration.
- Active but small community in 2012; never achieved widespread production adoption.

[Original](http://micrypt.com/2012/08/10/Getting-started-with-HyperDex.html)
