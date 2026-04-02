---
title: Architectural Decision Records (ADRs)
date: 2026-01-23
categories:
  - architecture
  - documentation
  - decision-records
description: The ADR (Architectural Decision Records) site is the canonical resource for documenting significant design choices alongside their context and rationale. It matters because decision records address the institutional memory problem in software teams—why something was built a certain way is often lost over time, leaving future developers unable to distinguish intentional choices from accidents.
params:
  source: pinboard
  sourceUrl: https://adr.github.io/
---

![Architectural Decision Records (ADRs)](/images/notes/adrs.png)

## Summary

An Architectural Decision Record (ADR) captures a single architectural decision and its rationale. The collection of ADRs in a project forms its decision log—a record of what was chosen, why, and what the tradeoffs were. The practice sits within Architectural Knowledge Management (AKM), though ADRs can cover any design decision, not just high-level architecture.

An Architecturally Significant Requirement (ASR) is the kind of requirement that has a measurable effect on the system's structure or quality. ADRs exist to document how teams responded to these requirements. Without records, the reasoning behind design choices disappears as people leave or memory fades.

The format is intentionally lightweight: a short text file, typically in Markdown, stored in version control alongside the code it describes. That proximity matters—decisions live with the system they shaped, making them easier to find and update when things change.

## Key points

- An ADR captures a single architectural decision with context and consequences, not a full design doc
- The collection of ADRs forms a project's **decision log**, useful for onboarding and audits
- ASRs are the trigger—requirements with measurable structural impact warrant an ADR
- ADRs extend beyond pure architecture to any meaningful design decision (any decision record)
- The practice connects to broader Architectural Knowledge Management tooling and standards

[Original](https://adr.github.io/)
