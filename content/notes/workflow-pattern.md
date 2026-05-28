---
title: The Workflow Pattern
date: 2023-10-06
categories:
  - software-architecture
  - patterns
  - workflow
  - state-machines
  - design
description: A blog post describing the Workflow Pattern — an architectural pattern for modeling multi-step business processes as explicit state machines rather than tangled procedural code. Argues that making workflow state explicit and persistent improves reliability, observability, and testability.
params:
  source: pinboard
  sourceUrl: https://blog.bittacklr.be/the-workflow-pattern.html
---

![The Workflow Pattern](/images/notes/workflow-pattern.png)

## Summary

The Workflow Pattern is an architectural approach for modeling multi-step business processes as explicit, persistent state machines rather than implicit procedural logic. The central argument: complex multi-step operations (order processing, document approval, data pipelines) are better represented as a series of named states with defined transitions than as nested if-statements and procedural steps.

The pattern makes workflow state explicit and persistent in storage — rather than state existing only in call stack variables or in-memory objects, each step's completion and the current state of a process are written to a database. This enables resilience (processes can resume after crashes), observability (you can query "how many orders are in state X?"), and auditability (full state transition history). It's the same concept underlying temporal.io, Apache Airflow, and AWS Step Functions — they're all implementations of workflow state persistence with different tradeoffs.

The blog post on bittacklr.be likely frames this around a specific language or framework, but the pattern itself transcends implementation. The key insight is that most applications have workflows hiding inside them — the order-management loop, the user onboarding sequence, the data import process — and these are better modeled as first-class state machines than as ad-hoc procedural code with implicit state scattered across service calls and database rows.

## Key points

- Workflow state should be explicit and persistent — not implicit in call stacks or in-memory objects.
- Makes processes resumable (crash resilience), queryable (observability), and auditable (history).
- Same concept as Temporal, Apache Airflow, Step Functions — different implementations of the same pattern.
- Most applications have hidden workflows; making them explicit improves reliability.
- State machine modeling: named states, defined transitions, explicit trigger conditions.
- Pairs with saga pattern for distributed transactions and event sourcing for full audit trails.

[Original](https://blog.bittacklr.be/the-workflow-pattern.html)
