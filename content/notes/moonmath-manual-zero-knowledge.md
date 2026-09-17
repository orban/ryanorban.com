---
title: "The MoonMath Manual: A Practitioner's Guide to Zero-Knowledge Proof Systems"
date: 2022-10-25
categories:
  - zero-knowledge-proofs
  - cryptography
  - zk-snarks
  - mathematics
  - blockchain
description: The MoonMath Manual is a comprehensive, example-driven introduction to zero-knowledge proof systems, covering the mathematics from finite fields through elliptic curves to Groth16 and PLONK. Written to be accessible to practitioners without a cryptography PhD, it became a widely-used self-study resource for the ZK ecosystem.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/moonmath.pdf
---

## Summary

The **MoonMath Manual** is a self-contained introduction to zero-knowledge proofs (ZKPs) authored by Least Authority and developed with community contributions. It targets engineers, protocol designers, and mathematically curious readers who want to understand the internals of zkSNARKs and related proof systems without needing a formal cryptography background. The name references the perceived difficulty of ZK mathematics — it builds toward the moon step by step.

The book starts from the mathematical primitives: finite fields, group theory, and elliptic curve cryptography. These are the structures underlying the hard computational problems that give ZK proofs their security (discrete log, elliptic curve discrete log problem). From there it builds to polynomial commitment schemes, which are the key ingredient that lets a prover convince a verifier of a statement without revealing the witness. The core proof systems covered in depth include Groth16 (the canonical R1CS-based pairing-based SNARK), PLONK (the universally trusted-setup permutation-based system), and STARKs (scalable, transparent, post-quantum arguments from hash functions rather than pairings).

A distinguishing feature is the emphasis on concrete circuits: the book walks through writing arithmetic circuits (R1CS constraints) for specific computations, showing how abstract mathematical statements are "compiled" into the algebraic structures that SNARK provers operate on. This is where most practitioners get stuck — the gap between "I want to prove I know a value x such that f(x) = y" and the actual R1CS/PLONK constraint system that encodes this. The MoonMath Manual bridges this with worked examples including SHA-256 circuit construction and Merkle tree membership proofs, both common building blocks in blockchain applications.

## Key points

- Covers ZK mathematics from scratch: finite fields → elliptic curves → polynomial commitment schemes → zkSNARKs.
- Three major proof systems: Groth16 (pairing-based, R1CS), PLONK (universal setup, permutation-based), STARKs (hash-based, no trusted setup).
- Practitioner-focused: shows how to write arithmetic circuits (R1CS constraints) for real computations like SHA-256 and Merkle proofs.
- Trusted setup ceremonies (multi-party computation) explained — why Groth16 requires per-circuit setup while PLONK requires only a universal one.
- Security model: soundness, completeness, zero-knowledge properties defined rigorously with intuitive explanations.
- Open-source community resource; widely used in the Ethereum, Starknet, and broader ZK ecosystem for onboarding.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/moonmath.pdf)
