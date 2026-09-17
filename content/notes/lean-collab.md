---
title: "lean-collab: multi-agent theorem proving in Lean 4"
date: 2026-02-13
categories:
  - ai-agents
  - theorem-proving
  - lean4
  - multi-agent
  - formal-verification
description: lean-collab applies multi-agent collaboration to Lean 4 theorem proving, using the Ensue Memory Network to coordinate agents across complex mathematical proofs. An unusual intersection of formal verification and multi-agent AI.
params:
  source: pinboard
  sourceUrl: https://github.com/mutable-state-inc/lean-collab
---

![lean-collab: multi-agent theorem proving in Lean 4](/images/notes/lean-collab.png)

## Summary

[lean-collab](/notes/lean-collab/) applies multi-agent collaboration to formal theorem proving in Lean 4, using the Ensue Memory Network from ensue.dev to coordinate agents across complex proofs. The core observation driving this project is that complex mathematical problems benefit from the same parallel, specialized-agent approach used in software development — rather than a single agent attempting an entire proof, multiple agents can work on subgoals in parallel.

Lean 4 is a functional programming language and theorem prover. With Mathlib (the community mathematics library), it can formalize mathematics from basic algebra through advanced topology. The bottleneck for automated theorem proving is the difficulty of exploring large proof search spaces; multi-agent coordination is one approach to managing that exploration more efficiently.

The Ensue Memory Network handles the coordination layer — shared memory and communication between agents so they can share partial progress and avoid redundant work. This is conceptually similar to how [Agent Swarm](/notes/agent-swarm/) and Cord handle multi-agent coordination in software contexts, applied to a much more structured domain (formal proofs have clear correctness criteria that software often lacks).

## Key points

- Multi-agent collaboration for Lean 4 formal theorem proving.
- Uses Ensue Memory Network for agent coordination and shared memory.
- Mathlib integration gives access to the full community mathematics library.
- Requires Lean 4 with elan, Rust, and an Ensue API key.
- Addresses proof search complexity by distributing work across specialized agents.
- MIT license from mutable-state-inc.

[Original](https://github.com/mutable-state-inc/lean-collab)
