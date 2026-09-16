---
title: "Empirical Analysis of EIP-1559: Transaction Fees, Waiting Time, and Consensus Security"
date: 2022-01-17
categories:
  - ethereum
  - eip-1559
  - blockchain
  - transaction-fees
  - mechanism-design
  - crypto
description: This empirical study of Ethereum's EIP-1559 upgrade analyzes real on-chain data from the August 2021 London Hardfork to measure effects on transaction fees, waiting times, and miner incentives. It confirms improved fee predictability but also identifies new volatility patterns and security implications from the base fee burn mechanism.
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/2201.05574 (1).pdf
---

## Summary

EIP-1559 was the first major overhaul of Ethereum's transaction fee mechanism (TFM), activated in the London Hardfork on August 5, 2021. It replaced the first-price auction model with a base fee that adjusts dynamically based on block fullness, plus a user-specified priority fee (tip) to incentivize miners. This paper from Duke University, Peking University, and SciEcon CIC is among the first empirical analyses using real on-chain data to evaluate whether EIP-1559 delivered on its promises.

The core finding is that fee predictability improved substantially: users can now reliably estimate transaction costs using the base fee, and the chaotic fee variance of the first-price auction era is reduced. However, the base fee mechanism introduces new dynamics — gas usage becomes volatile around block fullness thresholds, and during demand spikes the base fee can still climb rapidly. The paper uses game theory analysis alongside empirical data, examining incentive compatibility for both myopic and strategic miners.

On consensus security, the paper analyzes whether the burn mechanism (base fees are destroyed rather than paid to miners) changes miner incentives in ways that could threaten 51% attack economics or encourage selfish mining strategies. The shift from a revenue model where miners capture all fees to one where they only capture tips has implications for long-run miner behavior as block subsidies decrease.

## Key points

- EIP-1559's base fee mechanism substantially improved fee predictability compared to the pre-London first-price auction model — the headline promise was largely delivered.
- Gas usage exhibits new volatility patterns around block capacity targets; blocks alternate between near-empty and near-full, a pattern prior models didn't anticipate.
- The priority fee (tip) market still resembles a first-price auction for time-sensitive transactions, preserving some pre-EIP-1559 dynamics in high-demand periods.
- Base fee burn changes miner revenue composition: as block rewards decrease over time, miners become more dependent on tips, which may affect long-run network security economics.
- The paper provides empirical grounding for prior theoretical work by Tim Roughgarden and others, confirming incentive compatibility for myopic miners in practice.

[Original paper](file:///Users/ryo/Library/Mobile%20Documents/com~apple~CloudDocs/Papers/2201.05574%20(1).pdf)
