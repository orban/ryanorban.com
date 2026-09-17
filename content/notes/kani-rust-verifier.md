---
title: Using the Kani Rust Verifier on a Firecracker Example
date: 2022-07-14
categories:
  - rust
  - formal-verification
  - security
  - aws
  - model-checking
description: Kani is AWS's Rust model checker — a formal verification tool that proves correctness properties of Rust code by exhaustively exploring execution paths. This post shows it applied to Firecracker, AWS's microVM hypervisor, demonstrating industrial-scale use of formal methods.
params:
  source: pinboard
  sourceUrl: https://model-checking.github.io//kani-verifier-blog/2022/07/13/using-the-kani-rust-verifier-on-a-firecracker-example.html
---

## Summary

Kani is an open-source model checker for Rust developed by AWS, and this post demonstrates applying it to Firecracker — AWS's microVM hypervisor used in Lambda and Fargate. The combination is significant: formal verification applied to production security-critical systems code, not just toy examples.

Kani works by translating Rust code into a form that can be fed to the CBMC (C Bounded Model Checker) backend, which then exhaustively explores execution paths up to a bounded depth. Unlike unit testing which checks specific cases, model checking verifies that a property holds for *all possible* inputs within the bound. For something like Firecracker's VirtIO device handling — where guest VMs send potentially adversarial requests — this matters enormously.

The key workflow: you write a harness in Rust annotated with `#[kani::proof]`, specify assumptions about inputs using `kani::assume()`, and assert properties with `kani::assert()`. Kani then proves or disproves whether the property holds. When it finds a violation, it produces a concrete counterexample. This is much more powerful than fuzzing (which finds bugs probabilistically) but more scalable than full theorem proving (which requires manual proof writing).

## Key points

- Kani is a bounded model checker for Rust — exhaustively checks code properties up to a bound depth, catches bugs fuzzing misses
- Built by AWS on top of CBMC; integrates with `cargo kani` as a standard build tool
- Harnesses look like Rust test functions but make assertions about all possible inputs, not specific cases
- Firecracker use case shows production viability: verifying VirtIO device ring buffer handling in a security boundary
- Complements property-based testing (QuickCheck/proptest) — those sample inputs, Kani proves exhaustively

[Original](https://model-checking.github.io//kani-verifier-blog/2022/07/13/using-the-kani-rust-verifier-on-a-firecracker-example.html) → GitHub
