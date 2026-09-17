---
title: What Is It Like to Join a DAO?
date: 2022-03-22
categories:
  - dao
  - web3
  - blockchain
  - community
  - governance
description: Aragon's first-person account of joining a DAO — the onboarding friction, the role of Discord, token-gating, contribution paths, and how governance proposals actually work in practice. Ground-level view of how decentralized organizations operate day-to-day.
params:
  source: pinboard
  sourceUrl: https://blog.aragon.org/what-is-it-like-to-join-a-dao/
---

![What Is It Like to Join a DAO?](/images/notes/joining-a-dao.png)

## Summary

Aragon's blog post answers the question practically rather than theoretically: not what a DAO is, but what you actually do when you want to join one. The experience is surprisingly human — it starts with Discord, not a blockchain. Most DAOs use Discord as their primary coordination layer; the smart contracts handle treasury management and formal governance votes, but day-to-day communication and soft consensus happen in Discord channels. Joining means reading pinned messages, introducing yourself in an #introductions channel, and figuring out which working groups are active.

Token-gating determines what you can access. Many DAOs require holding a minimum amount of the governance token to participate in certain channels or vote on proposals. This creates a tiered membership structure: observers, contributors, and token holders with voting rights. The barrier varies widely — some DAOs have cheap tokens, others require expensive membership NFTs. Snapshot is the standard tool for off-chain governance votes (gas-free signaling), while on-chain votes using tools like Aragon, Compound Governor, or Gnosis Safe actually execute decisions.

Contribution paths matter more than formal membership. The DAOs with healthy contributor bases have clear tasks: writing documentation, building integrations, reviewing grants, organizing events. The compensation model is typically bounties or streaming payments in the DAO's native token — you complete a task and receive tokens. This creates a loop where contributors earn governance power through contribution. The post is honest about the coordination overhead: DAO communication is asynchronous, decisions are slow, and without dedicated stewards keeping things moving, important work falls through the cracks.

## Key points

- Discord is the actual coordination layer; Snapshot and on-chain contracts handle formal governance — the social layer is as important as the technical one.
- Token-gating: governance token or NFT ownership determines voting rights and channel access.
- Contribution-to-governance loop: bounties and streaming payments in governance tokens earn participants voice in the DAO.
- Snapshot = off-chain gasless signaling; Aragon / Compound Governor / Gnosis Safe = on-chain execution.
- DAOs face real coordination overhead — asynchronous communication, slow decisions, contributor dropout without active stewards.
- The model works best for protocols (where smart contracts handle most coordination) and worse for operational organizations that need fast execution.

[Original](https://blog.aragon.org/what-is-it-like-to-join-a-dao/)
