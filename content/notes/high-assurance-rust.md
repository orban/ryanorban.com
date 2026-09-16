---
title: High Assurance Rust
date: 2022-04-01
categories:
  - rust
  - security
  - systems-programming
  - education
  - book
description: High Assurance Rust is a free online book teaching systems security through Rust — covering memory safety, type systems, cryptography, and formal verification. Aimed at developers who want to write software that's provably hard to exploit.
params:
  source: pinboard
  sourceUrl: https://highassurance.rs/landing.html
---

## Summary

[High Assurance Rust](/notes/high-assurance-rust/) is a free, open-source book that teaches systems programming and software security through Rust. The framing is deliberate: high assurance is a term from safety-critical and defense engineering meaning software whose correctness can be demonstrated through formal methods, rigorous testing, and principled design — not just through hoping bugs don't exist. The book applies this standard to Rust, which has the unusual property of being both a practical systems language and one with a type system expressive enough to encode security invariants.

The book covers Rust's ownership and borrowing model from a security angle — not "here's how to appease the borrow checker but here's why these constraints eliminate whole classes of memory safety vulnerabilities." Stack vs. heap allocation, lifetimes, and the absence of null pointers are reframed as security properties. Then it moves into cryptographic primitives, secure coding patterns, and using type-level programming to enforce security policies at compile time (e.g., encoding whether a handle is authenticated or not into the type system itself, so you can't accidentally use an unauthenticated handle where authentication is required).

The target audience is developers who want to go beyond write safe code as a slogan and understand the mechanics of why Rust programs are harder to exploit than equivalent C or C++ programs. Formal verification with tools like Prusti and Kani gets coverage — methods that let you prove properties about your code rather than just test them. This is increasingly relevant as Rust adoption grows in security-critical domains: Linux kernel, Android, Windows, cryptographic libraries.

## Key points

- Rust's type system encodes memory safety at compile time — ownership prevents use-after-free, borrowing prevents data races, no null references.
- Type-level security invariants: encode authentication state, capability possession, or encryption status into types so the compiler enforces them.
- Covers cryptographic primitives in Rust: hashing, symmetric encryption, asymmetric encryption, signatures.
- Formal verification tools (Prusti, Kani) can prove properties about Rust code — not just test them.
- Free, open-source, available at highassurance.rs — maintained by security researchers.
- Complements The Rust Programming Language book (the official Rust book) but focuses on security rather than general language features.

[Original](https://highassurance.rs/landing.html)
