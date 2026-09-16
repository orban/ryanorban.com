---
title: Secure Multiparty Computation (MPC)
date: 2022-04-19
categories:
  - cryptography
  - privacy
  - secure-computation
  - mpc
  - distributed-computing
description: Yehuda Lindell's accessible overview of secure multiparty computation (MPC) — how parties can jointly compute on private inputs without revealing them. Traces the field from Yao's two-party garbled circuits through modern practical protocols used in industry.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2020-300.pdf
---

## Summary

Yehuda Lindell (Bar-Ilan University / Unbound Tech) wrote this survey as an accessible introduction to secure multiparty computation (MPC) — the branch of cryptography that asks: how can a group of parties jointly compute a function over their private inputs, without any party learning anything beyond the output? The canonical example is a private auction: bidders can determine the winner and winning price without anyone learning others' bids.

MPC was introduced theoretically in the 1980s: Andrew Yao solved the two-party case with garbled circuits at FOCS 1986, and Goldreich, Micali, and Wigderson extended it to the multiparty case at STOC 1987. For decades it was a purely academic curiosity — provably correct but hopelessly slow. The survey's main narrative thread is MPC's transition from theoretical object to practical technology: modern protocols like SPDZ, ABY, and ABY3 are fast enough for real applications. Lindell's own company, Unbound Tech, deploys MPC for threshold cryptography and key management.

Security is formalized via the simulation paradigm: a protocol is secure if the adversary's view in the real protocol is computationally indistinguishable from what could be simulated given only the output. This definition handles both honest-but-curious adversaries (who follow the protocol but try to infer private data) and malicious adversaries (who deviate). The survey covers both security models and the gap in efficiency between them. Applications include private machine learning (training models on data no party directly sees), privacy-preserving genomic analysis, and electronic voting.

## Key points

- MPC lets parties compute joint functions on private inputs with zero-knowledge guarantees — only the output is revealed
- Andrew Yao's garbled circuits (1986) and Goldreich-Micali-Wigderson protocol (1987) are the foundational constructions; the survey traces how they became practical
- Simulation paradigm is the formal definition of security: a protocol is secure iff the adversary's view can be simulated from public information alone
- Modern protocols (SPDZ, ABY3) are fast enough for private machine learning and real-time applications — MPC is now an industry technology
- Key application areas: threshold cryptography, privacy-preserving auctions, private genomics, and federated learning-adjacent private analytics

[Original (PDF)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2020-300.pdf)
