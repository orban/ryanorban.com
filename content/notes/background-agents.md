---
title: "The Self-Driving Codebase: background agents for enterprise delivery"
date: 2026-02-28
categories:
  - ai-agents
  - infrastructure
  - enterprise
  - developer-tools
description: "The Self-Driving Codebase thesis: individual developer speed from laptop agents doesn't translate to org velocity. Background agents need cloud isolation, event routing, and governance to actually move DORA metrics."
params:
  source: pinboard
  sourceUrl: https://background-agents.com/
---

![The Self-Driving Codebase: background agents for enterprise delivery](/images/notes/background-agents.png)

## Summary

[Background Agents](/notes/background-agents/) (background-agents.com / Ona) makes a specific argument about where the AI coding agent paradigm breaks down: running agents on a laptop hits a ceiling. Machines sleep, agents conflict over state, secrets get exposed in prompts, and there's no governance layer. The thesis is that individual developer speed doesn't automatically become organizational velocity — you can have faster PRs but no improvement in cycle time or DORA metrics.

The self-driving codebase vision is infrastructure that handles development tasks autonomously: AI agents triggered by events (PRs, CVEs, Slack messages, schedules) operating in isolated cloud environments with proper audit trails and blast-radius controls. Developers shift from writing code to reviewing and calibrating agent output. High-value automation targets include dependency updates across repos, CVE remediation, CI migrations, and standards enforcement.

Ona provides the three missing pieces: isolated compute environments that spin up on demand, event routing systems that connect triggers to appropriate agents, and governance layers enforcing permissions and maintaining audit trails. The pull request remains the review gate — agents write code, humans review it.

## Key points

- Laptop agents don't scale: machine sleep, state conflicts, secret exposure, and no governance are structural limits.
- Faster individual PRs ≠ better DORA metrics — cycle time improvements require systemic change, not faster typing.
- Event routing connects real triggers (CVEs, PRs, Slack messages, schedules) to the right agent.
- Human review stays at the PR gate — agents write, humans review.
- Targets high-value automation: dependency updates, CVE remediation, CI migrations, standards enforcement.

[Original](https://background-agents.com/)
