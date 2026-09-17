---
title: "Keycard: Identity and Access Control for AI Agents"
date: 2025-04-24
categories:
  - ai-agents
  - security
  - identity
  - access-control
  - zero-trust
description: Keycard is a security control plane for AI agents — every action an agent attempts is evaluated against policy before credentials are issued. Short-lived scoped tokens replace long-lived permissions, and every agent interaction is auditable back to a human identity.
params:
  source: pinboard
  sourceUrl: https://keycard.sh/
---

![Keycard: Identity and Access Control for AI Agents](/images/notes/keycard.png)

## Summary

[Keycard](/notes/keycard/) is a security platform that acts as an intermediary between AI agents and the tools, APIs, and data they access. The core problem it addresses: agents currently inherit full user permissions, pass sensitive data through context windows, and leave no audit trail. [Keycard](/notes/keycard/) inserts a policy enforcement layer that evaluates every agent action request before issuing credentials.

The architecture has three layers. Identity resolution: each request is evaluated against a composite identity combining user, device, agent, and task context — so actions map to a specific human+agent combination, not just a generic API key. Policy enforcement at the gate: requests are approved, denied, or escalated based on real-time rules (e.g., block PII access, require elevated approval for destructive operations). Scoped credentials: rather than sharing long-lived tokens, [Keycard](/notes/keycard/) issues short-lived, least-privilege credentials bound to the specific task, expiring on completion.

This addresses the zero trust principle applied to AI agent access: no standing permissions, every access justified, everything auditable. It's the agent-native version of Teleport's approach to human infrastructure access — ephemeral credentials tied to verified identity rather than persistent secrets. The timing matters: as agent autonomy increases, the blast radius of a compromised agent credential grows with it.

## Key points

- Policy enforcement layer between AI agents and the services they access.
- Composite identity: user + device + agent + task combined per request.
- Short-lived, least-privilege credentials issued per task — no standing permissions.
- Every action auditable back to a human identity.
- Prevents agents from accessing PII, taking destructive actions, or operating outside policy.
- Zero trust principles applied specifically to the AI agent threat model.

[Original](https://keycard.sh/)
