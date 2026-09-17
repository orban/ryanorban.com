---
title: "Descope: identity platform for humans and AI agents"
date: 2026-01-23
categories:
  - identity
  - ai-agents
  - mcp
  - security
  - authentication
description: Descope is an External IAM platform that handles identity for both human users and AI agents — the same system covers user auth, business customer identity, MCP server auth, and agentic workflows. Identity as the control plane for human+agent systems.
params:
  source: pinboard
  sourceUrl: https://www.descope.com/
---

![Descope: identity platform for humans and AI agents](/images/notes/descope.png)

## Summary

[Descope](/notes/descope/) is an External Identity and Access Management (IAM) platform that explicitly covers AI agent identity alongside human user authentication. The framing has evolved: the tagline mentions users, business customers, partners, AI agents, and MCP servers as distinct identity principals. This reflects the operational reality that agentic systems need their own identity management separate from, but integrated with, human authentication.

The MCP server authentication angle is practically significant. As MCP-based tool use becomes standard in AI agent workflows, each MCP server connection creates an identity question: what is this agent authorized to do? [Descope](/notes/descope/) offers a controlled answer to that rather than leaving each team to implement ad-hoc API key management.

This puts [Descope](/notes/descope/) in the emerging category of infrastructure for AI agent production deployment — the layer that handles "who is this agent, what can it access, and how do we audit what it did?" The same problems human identity solved for web apps, now applied to multi-agent systems.

## Key points

- Manages identity for users, business customers, AI agents, and MCP servers in a single platform.
- MCP server authentication: define what each agent is authorized to access.
- Positions identity as the control plane for systems where humans and agents both operate.
- External IAM approach: not embedded per-app, but a standalone platform multiple systems connect to.
- Security and audit layer for agentic workflows, not just user-facing applications.

[Original](https://www.descope.com/)
