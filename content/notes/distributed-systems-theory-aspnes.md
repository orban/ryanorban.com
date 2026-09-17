---
title: Notes on Theory of Distributed Systems
date: 2022-08-25
categories:
  - distributed-systems
  - theory
  - consensus
  - algorithms
  - textbook
description: James Aspnes's freely-distributed lecture notes on the theory of distributed systems, covering fault tolerance, consensus, synchrony models, and randomized algorithms. A rigorous but accessible graduate reference that grounds distributed computing in formal models.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/notes.pdf
---

## Summary

*Notes on Theory of Distributed Systems* is an ongoing set of lecture notes by James Aspnes of Yale University, last updated August 2022. Unlike most distributed systems textbooks that focus on practical implementation, Aspnes's notes take a rigorous theoretical approach: every claim is treated as a theorem requiring proof, and the emphasis is on formal models and complexity-theoretic limits rather than engineering patterns.

The notes cover the foundational problems in distributed computing. The synchrony model section distinguishes synchronous, partially synchronous, and asynchronous systems — a distinction that determines what's computationally possible. The consensus problem (getting all correct processes to agree on a value despite failures) is central, and the notes prove the classic impossibility results: FLP impossibility (consensus is impossible in asynchronous systems with even one crash failure) and bounds on the number of Byzantine faults that can be tolerated. The notes also cover leader election, distributed snapshots, logical clocks, and the CAP theorem with precise formulations.

A notable strength is the treatment of randomized algorithms for distributed problems — using randomness to circumvent impossibility results in asynchronous models. Las Vegas algorithms and Monte Carlo algorithms are developed for consensus and related problems. The notes are maintained as a living document under a Creative Commons license and reflect decades of Yale graduate courses.

## Key points

- Covers FLP impossibility, Byzantine fault tolerance, and CAP theorem with full proofs — not just intuitions
- Synchrony models (synchronous vs. asynchronous vs. partial synchrony) are the organizing framework; results in one model don't transfer directly to others
- Randomized algorithms are presented as the principled escape from impossibility results in asynchronous distributed computing
- Includes logical clocks (Lamport clocks, vector clocks), distributed snapshots (Chandy-Lamport algorithm), and leader election complexity bounds
- Freely available under CC license — regularly updated as lecture notes evolve; used in graduate theory-of-computation courses

[Original (PDF)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/notes.pdf)
