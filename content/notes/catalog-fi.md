---
title: "Catalog: Trustless P2P Crypto Trading"
date: 2022-07-14
categories:
  - defi
  - p2p-trading
  - bitcoin
  - ethereum
  - trustless
description: Catalog is a peer-to-peer trustless trading platform for Bitcoin, Ethereum, and other crypto assets — using on-chain escrow and atomic swaps rather than custodial order books. Designed for OTC-style large trades without trusting a centralized exchange.
params:
  source: pinboard
  sourceUrl: https://catalog.fi/
---

## Summary

Catalog is a peer-to-peer trading platform for Bitcoin, Ethereum, and other crypto assets that uses trustless on-chain mechanisms rather than a centralized custodian. The core idea: two parties can agree on a trade and execute it via smart contract escrow or atomic swaps, with neither party ever handing custody of assets to a third party.

The problem it solves is the trust gap in large OTC trades. On centralized exchanges (CEXes), you send assets to the exchange and trust them to hold and match. For large trades, this counterparty risk is significant — as demonstrated by FTX's collapse in November 2022 (five months after this bookmark). Atomic swaps between chains allow trustless settlement: the swap either completes atomically or reverts, with no window where one party holds both assets.

By 2022, the trustless trading space had several competing approaches: 0x Protocol for EVM-native token swaps, THORChain for cross-chain swaps via liquidity pools, and various peer-to-peer platforms trying to enable Bitcoin-to-Ethereum trading without intermediaries. Catalog's approach was more OTC-desk oriented — aimed at traders doing large blocks who needed the trust guarantees of on-chain settlement with the flexibility of bilateral negotiation.

## Key points

- Atomic swap or escrow smart contract execution — neither party has custody during the trade
- Targets OTC-style large trades where counterparty risk on a centralized exchange is unacceptable
- Supports cross-asset trading including Bitcoin (harder than EVM-to-EVM due to Bitcoin's limited scripting)
- Historical context: bookmarked before the FTX collapse, which dramatically validated the trustless trade thesis
- Competes with 0x, THORChain, and AirSwap in the trustless trading space

[Original](https://catalog.fi/)
