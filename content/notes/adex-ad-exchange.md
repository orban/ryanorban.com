---
title: "AdEx: Decentralized Ad Exchange"
date: 2022-09-27
categories:
  - advertising
  - blockchain
  - web3
  - decentralized
  - adtech
description: ""
params:
  source: papers
  sourceUrl: file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/Adex Ad Exchange.pdf
---

## Summary

AdEx is a decentralized advertising exchange built on Ethereum that aims to remove intermediaries from digital advertising — the ad networks, SSPs, DSPs, and data brokers that currently sit between publishers and advertisers while taking a significant cut. The AdEx whitepaper/technical documentation describes a system where ad inventory is traded peer-to-peer on a blockchain, with payments settled in ADX tokens and campaign performance verified on-chain.

The core problems AdEx targets are well-documented in traditional adtech: opaque auction mechanics, hidden fees at each intermediary layer, pervasive ad fraud (bots claiming impressions), and advertiser uncertainty about where their ads actually appeared. Blockchain-based settlement theoretically addresses the fraud and opacity problems by making impression events cryptographically verifiable and payment settlement trustless. Publishers receive payment directly rather than waiting 60+ days for network reconciliation.

The design is a OUTPACE (Off-chain Unidirectional Trustless Payment Channel) layer for payments combined with a DISC (Decentralized Identity for Supply Chain) for inventory verification. The system is part of a broader pattern of DeFi-adjacent infrastructure projects trying to apply crypto primitives to traditional industries — alongside Orchid for VPNs and Akash Network for cloud compute. Whether advertising actually benefits from blockchain's trustlessness properties (versus just needing better industry standards and APIs) remained a live question in 2022.

## Key points

- Decentralized ad exchange using Ethereum and ADX tokens — removes intermediary ad networks from publisher-advertiser relationships
- OUTPACE payment channels enable off-chain micropayments for impressions with on-chain settlement, avoiding per-impression gas costs
- On-chain impression verification addresses ad fraud by making bot traffic economically unprofitable to fake
- Transparent auction mechanics: advertisers can verify where their ads ran and what they paid, end-to-end
- Part of the broader DePIN / blockchain-for-infrastructure thesis alongside Akash Network (compute) and Orchid (VPN)
- Faces the standard tension: publishers and advertisers already have contractual relationships with existing networks, making decentralized alternatives hard to bootstrap

[Source PDF](file:///Users/ryo/Library/Mobile Documents/com~apple~CloudDocs/Papers/[Adex Ad Exchange](/notes/adex-ad-exchange/).pdf)
