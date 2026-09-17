---
title: "Hacker Laws: Laws, Theories, Principles, and Patterns for Developers"
date: 2022-01-04
categories:
  - software-engineering
  - principles
  - programming
  - organizational-dynamics
description: Dave Kerr's curated reference of laws, principles, and patterns that recur in software development and technology organizations, covering everything from Brooks' Law to Conway's Law to the Pareto Principle. A useful mental model library for recognizing why projects, teams, and systems behave the way they do.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/hacker-laws.pdf
---

## Summary

Hacker Laws is a reference collection compiled by Dave Kerr cataloging the recurring laws, principles, and patterns that practitioners in software engineering and technology organizations repeatedly encounter. Rather than a textbook, it's a living reference — each entry names the concept, explains it, and often gives historical origin and practical implications. The collection spans organizational dynamics (Brooks' Law, Conway's Law, Goodhart's Law), software design (DRY principle, SOLID principles, the Robustness Principle), cognitive limits (Hofstadter's Law, Parkinson's Law), and technology trends (Moore's Law, Metcalfe's Law).

The value of this kind of collection is pattern recognition: experienced engineers implicitly know that "adding engineers to a late project makes it later," but having Brooks' Law as a named concept makes it easier to communicate and reason about. Named principles compress institutional knowledge and make it transferable. Conway's Law — that system architecture mirrors the communication structure of the organization that built it — is a particularly powerful example: it explains patterns in distributed systems and microservices that seem like technical decisions but are actually organizational artifacts.

The collection is explicitly non-prescriptive. Many entries note that the law describes a tendency, not an absolute, and that context determines applicability. Goodhart's Law ("when a measure becomes a target, it ceases to be a good measure") is framed as a caution for engineering metrics rather than a prohibition on measurement. The collection is especially useful for new engineers trying to develop the vocabulary to name patterns they've observed but couldn't articulate, and for senior engineers building shared mental models with their teams.

## Key points

- Brooks' Law: adding human resources to a late software project makes it later — due to ramp-up time and increased communication overhead, not a failure of individual effort
- Conway's Law: organizations design systems that mirror their communication structure, meaning architectural changes often require organizational changes first
- Goodhart's Law: optimizing for a proxy metric corrupts it as a measure — engineering teams that hit 100% test coverage by writing trivial tests are a canonical example
- Hofstadter's Law: it always takes longer than you expect, even when you account for Hofstadter's Law — a recursive observation about systematic underestimation in complex projects
- Parkinson's Law: work expands to fill the time available — relevant to sprint planning, feature scoping, and why deadlines (even artificial ones) are necessary forcing functions

[Original](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/hacker-laws.pdf)
