---
title: "Open-Inspect: open-source background coding agent system"
date: 2026-01-28
categories:
  - ai-agents
  - background-agents
  - open-source
  - github
  - multi-agent
description: Open-Inspect is an open-source background coding agent system inspired by Ramp's internal Inspect tool — agents work in full dev environments while you're elsewhere, then create PRs. Supports multiplayer sessions and Anthropic or OpenAI models.
params:
  source: pinboard
  sourceUrl: https://github.com/ColeMurray/background-agents
---

![Open-Inspect: open-source background coding agent system](/images/notes/background-agents-open-inspect.png)

## Summary

Open-Inspect is an open-source implementation of a background coding agent system, directly inspired by Ramp's internal "Inspect" tool. The premise: agents work on tasks in background development environments with all the tools engineers have, while the developer does other things. When done, agents create PRs with proper commit attribution.

The system supports web, Slack, and Chrome extension clients. Multiplayer sessions let multiple people collaborate on the same agent run. Model choice is flexible — Anthropic Claude or OpenAI Codex via ChatGPT subscription. This positions Open-Inspect as the open-source version of what proprietary tools like Devin, SWE-agent, and now Ramp's Inspect do internally.

The security model is intentionally single-tenant: all users share the same GitHub App installation and can access any repo the App has access to. The README is explicit about this — it's not designed for multi-organization SaaS, but for trusted teams where everyone should have equal access. PR creation still uses per-user OAuth tokens, so attribution is correct even though the underlying credentials are shared.

## Key points

- Background agents work in full development environments while you focus elsewhere, then submit PRs.
- Inspired by Ramp's internal Inspect tool — open-source recreation of enterprise-internal agent infrastructure.
- Clients: web, Slack, Chrome extension; supports multiplayer sessions.
- Anthropic Claude or OpenAI Codex model choice.
- Single-tenant security model by design — shared GitHub App credentials, per-user OAuth for PR attribution.
- Part of the pattern of enterprise background-agent infrastructure becoming available in open-source.

[Original](https://github.com/ColeMurray/background-agents)
