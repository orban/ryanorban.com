---
title: "Configurancy: keeping systems intelligible when agents write all the code"
date: 2026-02-10
categories:
  - ai-agents
  - software-architecture
  - specifications
  - electric-sql
  - ai-generated-code
description: "Kyle Mathews argues that AI makes code cheap, so the scarce asset is now system self-knowledge: explicit contracts, conformance suites, specs. Configurancy is the term for what lets bounded agents coherently co-evolve a shared system."
params:
  source: pinboard
  sourceUrl: https://electric-sql.com/blog/2026/02/02/configurancy
---

![Configurancy: keeping systems intelligible when agents write all the code](/images/notes/configurancy.png)

## Summary

Kyle Mathews at Electric SQL introduces the concept of \[configurancy\](/notes/configurancy/) — the explicit shared contracts that let bounded agents (human or AI agent) coherently work on the same system without creating contradictions. The core argument: AI agents make code cheap to produce, so the scarce asset shifts to the system's own self-knowledge. Specs, invariants, conformance suites — these become load-bearing infrastructure, not optional documentation.

The coordination problem is real. Both humans and AI have limited context windows and can't see the entire system. When multiple bounded agents make changes based on partial views, small divergences compound. Tests pass but the system loses intelligibility. Code gets written that technically works but that no one — human or agent — can confidently reason about. This is what Mathews calls the configurancy problem.

The solutions he proposes are structural: explicit contracts encoded in executable form, conformance suites that verify implementations match the contract across platforms, external oracles that anchor specs to verifiable ground truth (like Postgres for SQL behavior), and a spec hierarchy from ground truth down to prose rationale. The frame is that agentic AI changes what software engineering bottlenecks exist — implementation cost drops, system comprehension cost rises.

## Key points

- Configurancy: the shared contracts that let bounded agents coherently co-evolve a system.
- The bottleneck shifts when AI agents write code: from implementation to system self-knowledge.
- Context window limits mean agents always operate on partial views — without explicit contracts, divergences compound.
- Proposed solutions: executable specs, conformance suites, external oracles, spec hierarchies.
- Source: Kyle Mathews at Electric SQL, February 2026.

[Original](https://electric-sql.com/blog/2026/02/02/configurancy)
