---
title: "McFly: neural network-powered shell history search"
date: 2025-02-10
categories:
  - cli
  - shell
  - developer-tools
  - machine-learning
  - productivity
description: McFly replaces Ctrl+R shell history search with a small neural network that ranks suggestions by context — recent directory, exit codes, and command frequency all influence ranking. Works with bash, zsh, fish.
params:
  source: pinboard
  sourceUrl: https://github.com/cantino/mcfly
---

![McFly: neural network-powered shell history search](/images/notes/mcfly-neural-shell-history-search.png)

## Summary

McFly replaces the default Ctrl+R shell history search with a contextual ranking system backed by a small neural network. Where standard reverse history search finds the most recent matching command, McFly considers context: what directory you're in, the exit code of previous commands (failed commands rank lower), and overall command frequency. The result is that the command you actually want surfaces first, not just the most recent matching string.

The neural network is trained on your own history over time — it learns your personal command patterns. The architecture is lightweight (no GPU required) and runs in milliseconds. The database format is SQLite, same as Atuin, but McFly doesn't sync across machines — it's purely local history ranking.

The interface replaces Ctrl+R with a full-screen TUI showing ranked matches with timestamps. Context signals are visible in the UI. McFly supports bash, zsh, and fish. It's in the same category as Atuin but with different tradeoffs: Atuin adds cross-machine sync and richer metadata, McFly adds neural ranking of local history.

## Key points

- Replaces Ctrl+R with neural network-ranked history search based on current context.
- Context signals: current directory, command exit codes, frequency weighting.
- Trains on personal history over time — learns individual command patterns.
- SQLite backend; local-only (no sync, cf. Atuin).
- Supports bash, zsh, fish.
- Full-screen TUI replaces inline reverse-search.

[Original](https://github.com/cantino/mcfly) → GitHub
