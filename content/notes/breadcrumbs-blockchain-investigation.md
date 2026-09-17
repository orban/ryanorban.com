---
title: "Breadcrumbs: Blockchain Investigation Tool"
date: 2022-04-17
categories:
  - blockchain
  - analytics
  - crypto
  - investigation
  - on-chain
description: Breadcrumbs is a visual blockchain investigation tool — traces transaction flows as a graph, identifies counterparty clusters, and flags sanctioned addresses. Used for AML compliance, due diligence, and on-chain forensics.
params:
  source: pinboard
  sourceUrl: https://www.breadcrumbs.app/home
---

## Summary

Breadcrumbs is a visual blockchain analytics and investigation tool for tracing cryptocurrency transaction flows. It renders on-chain transaction history as an interactive graph — addresses are nodes, transactions are edges — making it possible to follow funds across hops, identify clusters of addresses likely controlled by the same entity, and flag connections to sanctioned wallets or known exchange wallets. It's positioned at the intersection of on-chain analytics and anti-money laundering (AML) compliance.

The investigative workflow: start from a wallet address, expand its transaction history, identify where funds came from and went to, and progressively map the graph until you reach a labeled entity (an exchange, a sanctioned address, a known mixer like Tornado Cash). The visual graph approach is more intuitive for investigation than querying raw transaction tables — you can see the flow visually rather than mentally constructing it from data.

The tool competes with Chainalysis, TRM Labs, Elliptic, and Nansen in the on-chain analytics space, but is positioned for individuals and smaller teams rather than enterprise compliance departments. This makes it more accessible for researchers, journalists, and independent investigators doing blockchain forensics. In 2022, the on-chain investigation space was growing rapidly alongside crypto adoption — the Ronin Bridge hack ($600M), Wormhole exploit, and the beginning of Tornado Cash sanctions investigations created significant demand for these tools.

## Key points

- Visual transaction graph for blockchain forensics: addresses as nodes, transactions as edges, interactive expansion.
- Tracks fund flows across hops — identify the origin or destination of funds through multiple intermediary wallets.
- AML use: flags sanctioned addresses, known mixers, exchange deposit addresses.
- Accessible alternative to enterprise tools like Chainalysis, TRM Labs — oriented toward individual researchers.
- 2022 context: Tornado Cash sanctions, major bridge hacks, and growing crypto adoption drove demand for on-chain forensics.
- Connects to MEV analysis and on-chain due diligence for investors entering DeFi protocols.

[Original](https://www.breadcrumbs.app/home)
