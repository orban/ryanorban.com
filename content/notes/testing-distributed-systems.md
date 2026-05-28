---
title: Testing Distributed Systems
date: 2022-02-11
categories:
  - distributed-systems
  - testing
  - reliability
  - chaos-engineering
  - reference
description: A curated list of resources on testing distributed systems — covering Jepsen, TLA+, chaos engineering, simulation testing, and formal verification. The most comprehensive reference starting point for this notoriously hard problem.
params:
  source: pinboard
  sourceUrl: https://asatarin.github.io/testing-distributed-systems/
---

![Testing Distributed Systems](/images/notes/testing-distributed-systems.png)

## Summary

This curated list by Andrey Satarin collects the most important papers, talks, and tools for testing distributed systems — arguably one of the hardest problems in software engineering. The fundamental challenge: distributed systems fail in ways that are non-deterministic and time-dependent, which makes traditional testing approaches largely useless. You can't easily reproduce bugs, and the failure modes (network partitions, clock skew, Byzantine faults) are difficult to simulate.

The resources span the main approaches: Jepsen (Kyle Kingsbury's framework for testing distributed databases under network faults), TLA+ / formal verification for specifying and model-checking system invariants before writing code, chaos engineering à la Netflix's Chaos Monkey for fault injection in production, and simulation testing where the entire distributed system runs inside a deterministic simulator. FoundationDB's simulation testing approach is one of the landmark examples — they test their entire database by simulating it with deterministic time and injecting faults at will.

The collection is valuable because the field is scattered across academic papers (many from OSDI, SOSP, EuroSys), engineering blog posts, and conference talks. Having them curated in one place makes it possible to get oriented without spending weeks searching.

## Key points

- Jepsen: nemesis-based fault injection for databases — has exposed bugs in etcd, Redis, Cassandra, MongoDB.
- TLA+: formal specification language for modeling distributed protocols before implementation.
- Chaos engineering: intentional fault injection in staging or production to find gaps in resilience.
- Simulation testing: run the whole system in a deterministic, time-controllable simulator — the gold standard.
- Property-based testing and fuzzing are increasingly used for distributed protocol implementations.

[Original](https://asatarin.github.io/testing-distributed-systems/) → GitHub
