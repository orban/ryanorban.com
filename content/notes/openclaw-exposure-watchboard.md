---
title: "OpenClaw Exposure Watchboard: tracking exposed AI agent deployments"
date: 2026-03-03
categories:
  - security
  - ai-agents
  - infrastructure
  - defensive-security
description: The OpenClaw Exposure Watchboard tracks 569K+ publicly reachable AI agent instances — many with leaked credentials, CVEs, and active threat actor interest. Useful for checking if your own deployment is inadvertently public.
params:
  source: pinboard
  sourceUrl: https://openclaw.allegro.earth/
---

![OpenClaw Exposure Watchboard: tracking exposed AI agent deployments](/images/notes/openclaw-exposure-watchboard.png)

## Summary

The [OpenClaw Exposure Watchboard](/notes/openclaw-exposure-watchboard/) is a public database listing publicly reachable active OpenClaw instances for defensive security awareness. The scale is striking: it documents 569,512 exposed instances, heavily concentrated in China (334,567) and the United States (135,597). The site's purpose is to help organizations check whether their own AI agent deployments are inadvertently exposed and take corrective action.

The concern isn't just that these instances are publicly accessible — many show Leaked credential status, active threat actor interest, and associations with known CVEs and APT groups. An exposed AI agent with tool-calling capabilities and active credentials is a meaningful attack surface: it can read files, execute code, make API calls, and potentially pivot to other systems.

The defensive framing is genuine: verify your deployment, enable authentication, and remove unsafe public exposure. For organizations running AI agent infrastructure, this is a useful reconnaissance tool to check your own stack before threat actors do it for you.

## Key points

- 569,512 exposed OpenClaw instances documented publicly — China (334K) and US (135K) are the biggest concentrations.
- Many instances show leaked credentials, CVE associations, and active APT interest — not just misconfigured, actively exploited.
- Useful for organizations to self-check whether their own agent infrastructure is accidentally public-facing.
- Highlights the AI agent security surface area: exposed agents with tool access are more dangerous than exposed static services.
- Defensive tool: the explicit advice is to enable auth, remove direct public exposure, and patch immediately.

[Original](https://openclaw.allegro.earth/)
