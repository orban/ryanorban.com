---
title: DeFi Safety — Protocol Security Reviews
date: 2022-07-08
categories:
  - defi
  - security
  - ethereum
  - smart-contracts
  - risk
description: DeFi Safety is a security review and rating service for DeFi protocols, scoring them on code quality, documentation, admin key controls, and testing practices. One of the few systematic attempts to give DeFi users a reliable signal about protocol security posture.
params:
  source: pinboard
  sourceUrl: https://www.defisafety.com/
---

## Summary

[DeFi Safety](/notes/defi-safety/) is a platform that publishes structured security reviews and scores for DeFi protocols. Unlike smart contract audits (which are point-in-time technical code reviews), DeFi Safety reviews assess broader security posture: code quality, documentation completeness, admin key controls, test coverage, and whether the team follows security best practices over time.

The scoring model produces a percentage score across several dimensions: code documentation and comments, access control (who can upgrade or pause the contracts?), testing evidence (do test suites exist and are they run in CI?), oracle usage and risk, and team transparency. This gives users a quick signal about whether a protocol has thought seriously about security versus deployed code without adequate safeguards.

By mid-2022, the DeFi ecosystem had experienced multiple major exploits — Ronin Bridge ($625M), Wormhole Bridge ($320M), Harmony Horizon Bridge ($100M) — most exploiting admin key compromise or logic errors that audits had missed or that postdated the audit. DeFi Safety's ongoing review model addresses the audit-staleness problem: a protocol that scores well at launch may degrade if admin keys aren't rotated, documentation goes stale, or new features are added without security review.

## Key points

- Scores DeFi protocols across documentation, access control, testing, and team transparency — not just smart contract code
- Admin key controls are a critical dimension: many DeFi hacks exploited compromised multisig signers or overly powerful upgrade keys
- Reviews are ongoing, not point-in-time — captures protocol security as it evolves post-launch
- Pairs with code4rena and Immunefi for a complete picture of the DeFi security ecosystem (audits → continuous monitoring → bug bounties)
- Context: mid-2022 had ~$1B in bridge exploits, mostly from admin key compromise rather than complex code vulnerabilities

[Original](https://www.defisafety.com/)
