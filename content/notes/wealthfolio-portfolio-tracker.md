---
title: "Wealthfolio: offline open-source portfolio tracker"
date: 2025-11-21
categories:
  - finance
  - privacy
  - local-first
  - open-source
  - portfolio
description: Wealthfolio is an open-source, offline-first desktop portfolio tracker that stores all financial data locally. No subscriptions, no cloud sync, no account required — just a standalone app for tracking investments privately.
params:
  source: pinboard
  sourceUrl: https://wealthfolio.app/?v=2.0
---

![Wealthfolio: offline open-source portfolio tracker](/images/notes/wealthfolio-portfolio-tracker.png)

## Summary

Wealthfolio is a desktop portfolio tracker built on local-first software principles: all financial data stays on your computer, no cloud storage, no subscription required, no account needed. It's open-source and free, built with Tauri (Rust + web frontend) for a native desktop app feel across macOS, Windows, and Linux.

The appeal is straightforward: existing portfolio trackers (Personal Capital, Copilot, Monarch Money) all require you to hand over your financial data to a third-party cloud. For investors who hold significant assets, syncing brokerage credentials to a SaaS company's servers is a meaningful privacy and security exposure. Wealthfolio eliminates that entirely — you import data manually (CSV, OFX, or manual entry) and it never leaves your machine.

The tradeoff is manual data management. You don't get automatic transaction sync from brokerage APIs. But for investors who are already reviewing their positions regularly and don't want to rely on automated data pipelines that can break or expose credentials, this is a reasonable exchange. The open-source codebase means you can verify what it's actually doing with your data.

## Key points

- 100% local-first software: all financial data stored locally, no cloud sync.
- Open-source — auditable, no hidden telemetry.
- No subscription, no account, no brokerage credential exposure.
- Import via CSV, OFX, or manual entry — no automatic sync.
- Built with Tauri: Rust backend, cross-platform (macOS, Windows, Linux).
- Tradeoff vs. cloud alternatives: more privacy, more manual data maintenance.

[Original](https://wealthfolio.app/?v=2.0)
