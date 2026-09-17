---
title: "ScanMyCode: Code Security Scanner"
date: 2022-05-29
categories:
  - smart-contracts
  - security
  - code-scanning
  - sast
  - auditing
description: ScanMyCode is a code security scanner with smart contract support — static analysis for Solidity and general code security issues. Likely saved alongside the other smart contract security tools (Slither, Sec3, Quantstamp) as part of an audit tooling survey.
params:
  source: pinboard
  sourceUrl: https://app.scanmycode.io/
---

## Summary

[ScanMyCode](/notes/scanmycode/) is a web-based code security scanning platform offering SAST (Static Application Security Testing) for multiple languages, with smart contract scanning included. It was saved alongside Slither-simil, Sec3 Pro, and Quantstamp — suggesting it was part of a survey of automated security tools for the blockchain security space.

The platform provides code scanning through a web interface, aiming to lower the barrier to entry for security checks compared to setting up local tools like Slither, Mythril, or MythX. For Solidity contracts, the goal is to catch common vulnerability patterns (reentrancy, integer overflow, unchecked return values) before a paid audit. The web interface model also makes it accessible to teams without dedicated security engineers.

In the broader landscape, [ScanMyCode](/notes/scanmycode/) represents the automated pre-audit tier — below the thoroughness of Trail of Bits or Quantstamp manual audits, but faster and cheaper. The best practice for high-value DeFi protocol launches by 2022 was: automated scanner first (catches obvious issues), followed by formal verification for critical invariants (Certora, Halmos), then manual audit from a reputable firm.

## Key points

- Web-based SAST scanner with Solidity / smart contract support
- Lower friction than local tools — web interface, no setup required
- Catches standard vulnerability patterns: reentrancy, overflow, unchecked calls
- Fits in the "automated pre-audit" tier: faster/cheaper than manual audits, less thorough
- Best practice stack: automated scanner → formal verification → manual audit for high-value contracts
- Peers: MythX (ConsenSys automated scanner), Slither (CLI static analysis), Oyente (early Ethereum analyzer)

[Original](https://app.scanmycode.io/)
