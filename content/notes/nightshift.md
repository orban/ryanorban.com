---
title: "Nightshift: overnight codebase maintenance with leftover token budget"
date: 2026-02-17
categories:
  - ai-agents
  - developer-tools
  - code-quality
  - background-agents
description: Nightshift uses your leftover Claude/Codex token budget to run overnight code maintenance — dead code, doc drift, test gaps, security issues — landing everything as PRs. Like a Roomba for your codebase.
params:
  source: pinboard
  sourceUrl: https://github.com/marcus/nightshift
---

![Nightshift: overnight codebase maintenance with leftover token budget](/images/notes/nightshift.png)

## Summary

[Nightshift](/notes/nightshift/) is a tool that uses your remaining daily LLM token budget to run code maintenance tasks overnight, delivering results as pull requests on your branches. The framing is apt: \"like a Roomba for your codebase — runs overnight, worst case you close the PR.\" You never write directly to your primary branch; everything is a PR. Don't like something? Close it.

The types of work [Nightshift](/notes/nightshift/) looks for: dead code, documentation drift (docs that no longer match implementation), test gaps, security issues, and 20+ other categories. It's budget-aware — you configure a max spend (default 75% of remaining daily allotment) and it stays within that. You can point it at multiple repos and it already knows what to look for in each.

The setup is a `nightshift setup` CLI wizard that walks you through provider configuration (supports Claude and Codex), project selection, budget calibration, and daemon setup. Then `nightshift preview` shows you what it will do before it runs. This is the same design territory as [background agents](/notes/background-agents/) — long-running autonomous maintenance work — but specifically scoped to the useful residual budget problem that occurs when you have unused tokens at end of day.

## Key points

- Runs overnight using leftover LLM token budget — budget-aware with configurable max spend.
- Detects dead code, doc drift, test gaps, security issues, and 20+ other code maintenance categories.
- Everything lands as a pull request — never touches the primary branch directly.
- Budget-aware daemon with preview mode before running.
- Multi-project support; supports Claude and Codex providers.
- Written in Go, installed via Homebrew or binary.

[Original](https://github.com/marcus/nightshift)
