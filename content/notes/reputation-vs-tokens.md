---
title: Reputation vs. Tokens — DAOtalk Discussion
date: 2022-01-06
categories:
  - dao
  - governance
  - reputation
  - tokens
  - mechanism-design
description: DAOtalk discussion on the fundamental tension between reputation-based and token-based governance in DAOs. Reputation is earned and non-transferable; tokens are liquid and purchasable — each encodes very different values about how power should be distributed.
params:
  source: pinboard
  sourceUrl: https://daotalk.org/t/reputation-vs-tokens/452/3
---

## Summary

This DAOtalk thread explores one of the most fundamental design questions in DAO governance: should decision-making power derive from reputation (earned, non-transferable, contribution-linked) or governance tokens (purchased, liquid, transferable)? The two mechanisms encode fundamentally different theories of legitimate authority.

Token voting is simple to implement and liquid: buy tokens, get votes. It maps onto shareholder democracy in corporate governance. The problem is that it's straightforwardly plutocratic — anyone with enough capital can acquire governance control without ever contributing to the organization. Uniswap's governance, for example, has historically been dominated by large token holders including VCs with lockup-expiry timing incentives that diverge from long-term protocol health.

Reputation systems (as in Colony, SourceCred, or DAOstack's original design) tie governance to demonstrated contribution — you earn influence by doing work. Reputation is typically non-transferable and decays over time, so it tracks ongoing engagement. The problems: bootstrapping (how do you assign initial reputation?), subjectivity (who judges contribution quality?), and exit (what happens to reputation when contributors leave?).

The thread likely covers: hybrid designs, the meritocracy vs plutocracy tension, attack vectors on each system, and whether reputation can be made sybil-resistant. By 2022 most practical DAO implementations defaulted to token voting because it was technically simpler, despite the theoretical arguments for reputation.

## Key points

- Token voting: liquid, purchasable, maps to shareholder democracy — but creates plutocracy at scale
- Reputation: contribution-linked, non-transferable — captures meritocracy but harder to implement and bootstrap
- SourceCred attempted contribution-based reputation quantification; Colony built it into their protocol
- Most deployed DAOs use token voting despite its flaws — simplicity wins over theoretical elegance
- Hybrid designs: tokens for proposals, reputation for voting weight; or minimum reputation threshold to vote

[Original](https://daotalk.org/t/reputation-vs-tokens/452/3)
