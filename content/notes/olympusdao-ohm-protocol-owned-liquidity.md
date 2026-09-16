---
title: "OlympusDAO: OHM Liquidity Management and Protocol-Owned Liquidity"
date: 2022-02-22
categories:
  - defi
  - olympusdao
  - protocol-owned-liquidity
  - tokenomics
description: ""
params:
  source: papers
  sourceUrl: https://docs.olympusdao.finance/
---

## Summary

OlympusDAO is a DeFi protocol built on Ethereum that introduced a novel approach to liquidity: rather than renting it from external liquidity providers via yield incentives, the protocol owns its own liquidity through a mechanism called bonding. Users sell LP tokens or reserve assets (like DAI or ETH) to the Olympus treasury at a discount in exchange for OHM tokens that vest over a short period. This lets the protocol accumulate protocol-owned liquidity (POL) rather than depending on mercenary capital that leaves when incentives dry up.

The core mechanism distinguishes OlympusDAO from typical yield farming protocols. In a standard AMM liquidity program, the protocol pays yield to attract external LPs, but those LPs have no loyalty — they exit when rewards fall, taking liquidity with them and causing price instability. OlympusDAO's bonding turns the treasury into a permanent LP, so the protocol captures trading fees and maintains deep markets regardless of external incentive conditions. OHM is backed (not pegged) by the treasury at a floor price of 1 DAI per OHM, giving it a risk floor while allowing it to trade at a market premium.

Staking is the complementary mechanism: OHM holders stake to receive rebases — dilutive emissions that maintain staker purchasing power relative to the growing supply. The (3,3) game theory framing that made the protocol famous argues that mutual staking is the dominant strategy in a two-player game. In practice, the protocol attracted enormous attention in 2021–2022 as a model for reserve currency design in DeFi, spawning many forks (OHM forks / Olympus pro bonding-as-a-service). Critics noted the model depends on perpetual growth to sustain staking APYs, which led to significant drawdowns when sentiment turned.

## Key points

- Protocol-owned liquidity (POL): OlympusDAO buys its own LP positions via bonding, eliminating dependence on mercenary liquidity providers
- Bonding mechanism: users trade LP tokens or reserve assets to the Olympus treasury for discounted OHM with a vesting period, accruing POL for the protocol
- OHM is treasury-backed (not pegged) — the treasury holds reserve assets giving OHM a backing floor, while market price can trade above that floor
- Staking + rebase: stakers receive inflationary rebases to maintain proportional ownership; the "(3,3)" framing treats mutual staking as a coordination equilibrium
- The protocol became a template for DeFi reserve currency design and bonding-as-a-service, though high APY mechanics proved unsustainable as growth slowed

[Original paper](https://docs.olympusdao.finance/)
