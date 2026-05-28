---
title: "EPNS: Decentralized Push Notification Service"
date: 2022-03-24
categories:
  - web3
  - blockchain
  - notifications
  - ethereum
  - infrastructure
description: EPNS (Ethereum Push Notification Service, now Push Protocol) is a decentralized notification layer for Web3 — enabling dApps to send opt-in push notifications to wallet addresses across chains. Fills the gap between on-chain events and user awareness.
params:
  source: pinboard
  sourceUrl: https://messari.io/article/push-it-real-good-decentralized-notification-service-in-a-multichain-world
---

![EPNS: Decentralized Push Notification Service](/images/notes/push-decentralized-notifications.png)

## Summary

EPNS (Ethereum Push Notification Service, later rebranded to Push Protocol) is a decentralized notification layer designed for the Web3 stack. The fundamental problem it solves: in Ethereum and other blockchains, important events (liquidations approaching, governance votes, large transfers, price thresholds) happen on-chain, but users have no native way to receive real-time alerts. They have to actively check dashboards or get notified by centralized services that spy on their activity. EPNS creates an opt-in, wallet-to-wallet notification channel.

The mechanism: protocols (channels) send notifications to subscribers; users subscribe by signing a message (no transaction required), and notifications are delivered via EPNS nodes to wallets, mobile apps, or browser extensions. Crucially, subscriptions are opt-in — you control which protocols can notify you. This is different from email notifications (which require sharing your email with a protocol) or centralized services (which require trusting a third party not to sell your activity data). The notification payload is stored on IPFS and the channel registration and subscriber lists are on-chain (Ethereum mainnet, with cheaper interactions on Polygon).

The Messari analysis positions EPNS within the infrastructure layer of Web3 — a communication primitive that enables more sophisticated user experiences. The comparison to email infrastructure is apt: you need it to exist before you can build on top of it. DeFi protocols can warn users when their collateral ratio approaches liquidation, DAOs can alert voters when governance proposals are live, NFT marketplaces can notify holders of bids — all without users sharing email addresses or surrendering privacy. The PUSH token governs the protocol and is used for staking by channel operators.

## Key points

- Opt-in wallet-to-wallet notifications: users subscribe to channels; no email required, no centralized spy.
- On-chain channel registration on Ethereum mainnet; subscriber lists on Polygon for lower gas costs.
- Notification payloads stored on IPFS — decentralized storage for the actual message content.
- Key use cases: DeFi liquidation warnings, DAO governance alerts, NFT bid notifications, threshold alerts.
- PUSH token for governance and channel operator staking — economic incentive for reliable delivery.
- Rebranded from EPNS to Push Protocol as the service expanded beyond Ethereum.

[Original](https://messari.io/article/push-it-real-good-decentralized-notification-service-in-a-multichain-world)
