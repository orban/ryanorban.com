---
title: "GitAgent: git-native open standard for AI agents"
date: 2026-03-14
categories:
  - ai-agents
  - git
  - open-standard
  - developer-tools
  - portability
description: GitAgent defines AI agents as version-controlled files in a git repo — SOUL.md, SKILL.md, agent.yaml — exportable to any framework. The bet is that agent definitions should live in your repo, not a vendor's cloud.
params:
  source: pinboard
  sourceUrl: https://gitagent.sh/
---

![GitAgent: git-native open standard for AI agents](/images/notes/gitagent.png)

## Summary

[GitAgent](/notes/gitagent/) is an open standard for defining AI agents as version-controlled files stored natively in a git repository. Instead of configuring agents through a vendor dashboard or proprietary SDK, you define them as plain files: `SOUL.md` for identity, `SKILL.md` for capabilities, and `agent.yaml` for configuration. These files are committed to your repo, giving you branching, history, code review, and CI/CD integration for free.

The framework-agnostic design is the key differentiator. A [GitAgent](/notes/gitagent/) definition can be exported to Claude, OpenAI, CrewAI, Lyzr, and other platforms — you're not locked to any single vendor runtime. The MIT license and public development on GitHub reinforce the open standard positioning, contrasting with the many proprietary agent platforms that require you to stay within their ecosystem.

The CLI scaffolds a new agent repository, then you configure the three core components. The practical benefit is institutional: your agent definitions are auditable by the same code review processes as any other code, can be reviewed in PRs, are protected by your existing backup and access controls, and evolve alongside the codebase they're meant to serve.

## Key points

- Agent definitions as plain files in git: `SOUL.md` (identity), `SKILL.md` (skills), `agent.yaml` (config) — fully version-controlled and reviewable.
- Framework-agnostic: export to Claude, OpenAI, CrewAI, Lyzr without rewriting agent definitions.
- MIT-licensed open standard — explicitly contrasting with proprietary agent platforms.
- Agents inherit all git tooling: branching, history, CI/CD, code review.
- Addresses institutional control: your agents live in your repo, not a SaaS vendor's database.

[Original](https://gitagent.sh/)
