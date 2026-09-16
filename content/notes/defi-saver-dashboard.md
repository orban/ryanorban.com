---
title: "DeFi Saver: Next-Generation DeFi Management Dashboard"
date: 2022-09-13
categories:
  - defi
  - ethereum
  - finance
  - tools
  - portfolio-management
description: DeFi Saver is a management dashboard for creating and tracking DeFi positions across Maker, Aave, Compound, and other protocols from a single interface. It adds automation features like automated liquidation protection that native protocol interfaces don't offer.
params:
  source: pinboard
  sourceUrl: https://defisaver.com/
---

## Summary

DeFi Saver is an aggregated management interface for decentralized finance positions. Rather than managing a MakerDAO vault, Aave loan, and Compound supply in separate UIs, DeFi Saver consolidates them into a single dashboard. The core value proposition beyond aggregation is automation: DeFi Saver can automatically repay debt when a collateralization ratio drops toward the liquidation threshold — protecting positions without requiring constant manual monitoring.

The liquidation protection feature is significant in DeFi: volatile asset prices can push CDPs (collateralized debt positions) below their minimum collateralization ratio faster than users can react, especially during overnight moves. DeFi Saver's automated repayment system uses flash loans to repay debt and unlock collateral atomically, avoiding Ethereum liquidation penalties that can reach 10-15% of the position. This turns what was a high-maintenance position into something closer to a managed product.

DeFi Saver also supports leverage and deleverage operations in a single transaction using flash loans — a user can open a 2x leveraged ETH position on Aave in one click by flash-borrowing USDC, buying ETH, depositing the ETH as collateral, and repaying the flash loan from the collateral in one atomic transaction. This kind of operation, while possible manually, requires multiple steps and careful ordering that most users can't execute reliably.

## Key points

- Aggregated DeFi dashboard for MakerDAO, Aave, Compound, and others in a single interface.
- Automated liquidation protection: repays debt automatically when collateral ratio approaches the minimum threshold.
- Uses flash loans for atomic leverage/deleverage in a single transaction.
- Avoids Ethereum on-chain liquidation penalties (10-15%) through automated debt repayment.
- Target user: active DeFi users with leveraged positions who need automation, not passive yield farmers.
- Illustrates how middleware tooling adds significant value on top of DeFi primitives.

[Original](https://defisaver.com/)
