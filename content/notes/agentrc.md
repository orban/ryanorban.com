---
title: "AgentRC: context engineering and AI-readiness for repos"
date: 2026-01-29
categories:
  - ai-agents
  - context-engineering
  - developer-tools
  - microsoft
  - coding-agent
description: AgentRC (formerly Primer) measures and generates AI-readiness for repos — scoring across 9 pillars, generating instruction files, and running CI drift detection so agent context stays current as code evolves.
params:
  source: pinboard
  sourceUrl: https://github.com/pierceboggan/primer
---

![AgentRC: context engineering and AI-readiness for repos](/images/notes/agentrc.png)

## Summary

[AgentRC](/notes/agentrc/) (from Microsoft, formerly in a repo called primer) is a CLI tool and VS Code extension that measures how AI-ready a repository is and generates the missing context files. The premise: AI coding agents work best when they know how to build, test, and lint the code, plus the architecture, conventions, and external services the team uses. Most repos ship none of that. [AgentRC](/notes/agentrc/) generates it.

The tool operates on a three-step cycle: **Measure** (score across 9 pillars and a 5-level maturity model), **Generate** (produce tailored instruction files, evals, and dev configs via the Copilot SDK), and **Maintain** (CI drift detection so context doesn't go stale as the codebase changes). The 9-pillar readiness model is specific to agent-oriented documentation: from basic build/lint instructions up to MCP server configs.

The CI/CD integration for drift monitoring is the most practically valuable feature. The common failure mode for CLAUDE.md and similar context files is that they're written once and never updated. [AgentRC](/notes/agentrc/) turns that into an automated check: any CI run that detects context drift surfaces it as a failing test. No config needed — runs on any repo with Node.js 20+.

## Key points

- Measures AI-readiness across 9 pillars and a 5-level maturity model — surfaces what context is missing.
- Generates CLAUDE.md, instruction files, evals, and dev configs tailored to the actual codebase.
- CI/CD drift monitoring keeps agent context current as code evolves.
- No config required — runs on any repo with Node.js 20+ via `npx github:microsoft/agentrc`.
- Doubles as a VS Code extension for interactive use.
- From Microsoft, positioned as a complement to GitHub Copilot workflows.

[Original](https://github.com/pierceboggan/primer)
