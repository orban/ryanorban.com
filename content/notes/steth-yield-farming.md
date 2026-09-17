---
title: Farming stETH Yield with Curve, Convex, and Concentrator
date: 2022-03-25
categories:
  - defi
  - ethereum
  - yield-farming
  - curve
  - staking
description: YouTube walkthrough of farming 10% APY on stETH via Curve, Convex, and Concentrator — a 2022 DeFi yield stacking strategy combining liquid staking, AMM liquidity provision, and yield auto-compounding.
params:
  source: pinboard
  sourceUrl: https://m.youtube.com/watch?v=02jC7X3wLfs
---

## Summary

This video documents a DeFi yield strategy popular in early 2022: stacking Lido's stETH (liquid staked Ethereum) through Curve Finance, Convex Finance, and Concentrator to target ~10% APY. The strategy is a chain of protocols where each layer adds yield on top of the previous: stETH provides base staking rewards (~4-5%), Curve's stETH/ETH pool adds trading fees, Convex boosts CRV rewards, and Concentrator auto-compounds everything. This yield stacking pattern was one of the defining strategies of the 2021-2022 DeFi bull market.

stETH is Lido's liquid staking token — you deposit ETH, receive stETH that accrues staking rewards, and can use stETH in DeFi while still earning validator rewards. The Curve stETH/ETH pool is one of the largest and most efficient AMM pools for this pair — it has historically tight peg because both assets accrue ETH staking rewards. Convex Finance sits on top of Curve: it aggregates veCRV voting power to boost Curve LP rewards, then distributes those boosted rewards to depositors who stake their Curve LP tokens in Convex.

Concentrator (from AladdinDAO) added the auto-compounding layer: it takes the multi-token reward stream from Convex (CRV, CVX, sometimes others) and automatically sells them and reinvests into the same position. This removes the gas overhead of manual compounding and simplifies the yield into a single number. The strategy represents the DeFi composability thesis at its most extreme — four protocols stacked to optimize a yield position — but also the complexity and smart contract risk that comes with that composability.

## Key points

- stETH: Lido liquid staking token — ETH staking rewards without locking ETH; usable in DeFi.
- Curve Finance stETH/ETH pool: efficient AMM for correlated assets; LP earns trading fees + CRV emissions.
- Convex Finance: aggregates Curve's veCRV boost — depositing Curve LP in Convex unlocks higher CRV rewards.
- Concentrator: auto-compounds multi-token reward streams — removes manual harvesting gas overhead.
- DeFi composability: four protocols stacked to optimize one position — higher yield but compounded smart contract risk.
- Strategy context: peak 2022 DeFi; stETH de-pegged during June 2022 Celsius / 3AC crisis — this strategy had real drawdown risk.

[Original](https://m.youtube.com/watch?v=02jC7X3wLfs)
