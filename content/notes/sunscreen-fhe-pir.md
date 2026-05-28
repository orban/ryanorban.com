---
title: "Sunscreen FHE: Private Information Retrieval via Matrix Operations"
date: 2023-08-26
categories:
  - fhe
  - cryptography
  - privacy
  - rust
  - research
description: Sunscreen's documentation on Private Information Retrieval via Fully Homomorphic Encryption — demonstrating how FHE enables querying a database without the server learning what you searched for. A practical introduction to FHE programming via a concrete PIR example.
params:
  source: pinboard
  sourceUrl: https://docs.sunscreen.tech/fhe/fhe_programs/pir_matrix.html
---

![Sunscreen FHE: Private Information Retrieval via Matrix Operations](/images/notes/sunscreen-fhe-pir.png)

## Summary

Sunscreen is a Rust-based Fully Homomorphic Encryption (FHE) framework, and this documentation page demonstrates Private Information Retrieval (PIR) as a worked example. PIR is the problem of querying a database without the server learning which record you retrieved — a privacy primitive that FHE solves elegantly but that has historically been impractical to implement.

FHE allows computation on encrypted data: the server performs the database lookup on your encrypted query, and returns an encrypted result that only you can decrypt. From the server's perspective, it sees an encrypted blob and returns an encrypted result — it learns nothing about what you were looking for. This is fundamentally different from HTTPS, which hides your query from third parties but not from the server.

The Sunscreen framework makes FHE programming accessible through a Rust compiler that handles the low-level cryptographic operations (noise management, parameter selection, bootstrapping). The PIR example using matrix operations shows the programming model: you express the computation as if working with plaintext, and the framework handles the FHE mechanics. The practical limitation remains performance — FHE computation is orders of magnitude slower than plaintext computation — but the gap has been narrowing rapidly, and use cases with small databases or low query frequency become viable.

## Key points

- FHE enables Private Information Retrieval: query a database without the server learning what you looked for.
- Sunscreen makes FHE programming accessible via Rust — handles noise/parameter management automatically.
- The matrix PIR example demonstrates the programming model: write normal-looking code, FHE handles encryption.
- Key limitation: FHE computation is significantly slower than plaintext — but gap is narrowing.
- Different from standard encryption: HTTPS hides from third parties; FHE hides from the server itself.

[Original](https://docs.sunscreen.tech/fhe/fhe_programs/pir_matrix.html)
