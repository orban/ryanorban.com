---
title: "Hypercycle: Blockchain Architecture for Scalable AI Microservices"
date: 2022-04-12
categories:
  - blockchain
  - ai
  - microservices
  - decentralized
  - cardano
  - singularitynet
description: SingularityNET's Hypercycle whitepaper proposes a lightweight agent-based blockchain architecture for cheap, high-speed execution of AI microservices, built on Cardano's EUTxO model, the TODA ledgerless blockchain, and a Proof of Reputation system. An ambitious attempt to make AI services composable on-chain.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/HyperCycle-WP-2.pdf
---

## Summary

Ben Goertzel, Toufi Saliba, and colleagues from SingularityNET Foundation and TODA Network present Hypercycle, a blockchain architecture designed for cheap, high-speed on-chain execution of AI microservices. The design addresses a real problem: existing blockchains are too slow and expensive to coordinate many fine-grained AI service calls at machine speed.

Hypercycle combines several components: Cardano's EUTxO model and Plutus smart contract language for security guarantees, the Hydra interoperability framework for Cardano, the TODA/IP ledgerless blockchain for local high-speed transaction processing, and SingularityNET's Proof of Reputation system. The network consists of autonomous agents organized into rings that collaborate to execute consensus for smart contract execution. Each Hypercycle agent owns its own transaction history and accumulates reputation.

The target applications include swarm AI (evolutionary learning, algorithmic chemistry, ensemble ML), rating/reward systems for media networks, decentralized compute payments, and public/private chain interoperability. The OpenCog Hyperon framework's MeTTa programming language is also planned for integration with Plutus, potentially enabling low-code smart contract DSLs. This whitepaper represents the decentralized AI coordination vision of Ben Goertzel's post-AGI infrastructure thinking.

## Key points

- Combines TODA ledgerless blockchain (local speed) with Cardano mainchain (security guarantees via Hydra) — a two-layer approach
- Proof of Reputation consensus: agents accumulate trust through history rather than staking capital
- Agents organized into rings for lightweight consensus — designed for AI microservice call patterns (many small transactions)
- Target use cases: swarm AI, decentralized compute markets, content rating/reward systems
- MeTTa language integration aims to make on-chain AI programming accessible via auto-generated DSLs
- Part of Ben Goertzel's broader vision for SingularityNET and decentralized AGI infrastructure

[Original whitepaper (SingularityNET Foundation, 2022)](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/HyperCycle-WP-2.pdf) → AI agent
