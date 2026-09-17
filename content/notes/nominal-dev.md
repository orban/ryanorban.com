---
title: "Nominal: AI agents for autonomous production incident response"
date: 2026-03-01
categories:
  - ai-agents
  - devops
  - monitoring
  - incident-response
  - infrastructure
description: Nominal is AI agents that read your code, watch your infra, and fix production before you wake up — eliminating on-call by 2026. Early access, integrates with AWS/Cloudflare/Vercel/Fly.io and more.
params:
  source: pinboard
  sourceUrl: https://nominal.dev/
---

![Nominal: AI agents for autonomous production incident response](/images/notes/nominal-dev.png)

## Summary

Nominal is building AI agents that monitor infrastructure, read application code, diagnose issues, and fix production problems autonomously — before a human gets paged. The founder is Boris Tane, formerly of Cloudflare's observability team, and the claim is direct: "nobody should be on-call in 2026."

The platform integrates with major cloud providers and hosting platforms including AWS, Cloudflare, Vercel, Fly.io, Render, Railway, Supabase, PlanetScale, and Modal. The model is agents that can see both the infrastructure state and the application code — not just monitoring dashboards, but the actual code that produced the behavior. This combination (infra visibility + code context) is what separates detect and alert from diagnose and fix.

This is part of a broader pattern of AI agents entering the incident response space. The traditional on-call model — human gets paged at 3am, spends an hour diagnosing, applies a fix — is expensive, slow, and degrades engineer morale. Autonomous remediation closes the gap, at least for known failure patterns. Early access with rolling launch planned for April 2026.

## Key points

- AI agents that read code *and* watch infrastructure — diagnosis requires both, not just monitoring dashboards.
- Integrates with AWS, Cloudflare, Vercel, Fly.io, Render, Railway, Supabase, PlanetScale, and Modal.
- Built by Boris Tane, formerly of Cloudflare's observability team.
- Targets autonomous remediation before human on-call engineers are paged.
- Early access rolling launch April 2026.

[Original](https://nominal.dev/)
