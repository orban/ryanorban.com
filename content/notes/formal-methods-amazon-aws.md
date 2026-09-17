---
title: How Amazon Web Services Uses Formal Methods
date: 2022-07-14
categories:
  - formal-methods
  - distributed-systems
  - tla-plus
  - aws
  - engineering
description: Newcombe et al. (CACM 2015) describe how Amazon Web Services engineers use TLA+ to specify and verify distributed systems protocols, finding real bugs in S3, DynamoDB, and EBS before deployment. One of the few industrial accounts of formal methods working in production at scale.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/formal-methods-amazon.pdf
---

## Summary

Chris Newcombe, Tim Roscoe, Fan Zhang, Markus Kuppe, Marc Brooker, Nir Yaron, and Saar Hadar from Amazon Web Services describe how AWS engineering teams adopted TLA+ — a formal specification language developed by Leslie Lamport — to specify, verify, and find subtle bugs in distributed systems protocols. Published in *Communications of the ACM* (2015), this paper is one of the most influential industrial accounts of formal methods working at scale outside of safety-critical systems.

The impetus was a series of latent concurrency bugs in systems like Amazon S3, DynamoDB, and Amazon EBS that were not caught by traditional testing, code review, or simulation. Distributed systems at cloud scale have enormous state spaces: race conditions that occur in one in a million executions become near-certainties under heavy traffic. TLA+ allows engineers to specify the *intended behavior* of a protocol mathematically and then use the TLC model checker to exhaustively verify that all reachable system states satisfy that specification. This caught real, critical bugs before deployment.

The paper documents the organizational journey as much as the technical one. Engineers initially resisted formal methods as an academic exercise. What changed was evidence: TLA+ found a bug in DynamoDB replication that had survived months of testing, one that could have caused data loss in production. Once leadership saw this, adoption spread. AWS now uses TLA+ routinely for consensus protocols, storage replication, and distributed transaction systems. The paper includes worked examples of state machine specifications and explicit failures detected. The lesson is not that formal methods replace testing but that they find a specific class of subtle, timing-dependent bugs that no amount of testing can reliably surface.

## Key points

- TLA+ (Leslie Lamport) is a formal specification language based on temporal logic and set theory used to specify distributed protocol behavior.
- TLC model checker exhaustively explores all reachable states of a specification — effective for concurrency bugs that probabilistic testing misses.
- Found real critical bugs in Amazon S3, DynamoDB, and Amazon EBS replication before deployment.
- Adoption at AWS was driven by demonstrated evidence, not top-down mandate — one DynamoDB replication bug convinced leadership.
- Specs are typically 300-500 lines of TLA+; the model checker runs on clusters to handle large state spaces.
- Key takeaway: formal methods are complementary to testing, not a replacement — they target the class of subtle timing-dependent, concurrent bugs.

[Original PDF](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/formal-methods-amazon.pdf)
