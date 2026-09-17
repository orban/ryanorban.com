---
title: All the Hard Stuff Nobody Talks About When Building with LLMs
date: 2023-05-28
categories:
  - llm
  - production
  - engineering
  - lessons-learned
  - observability
description: Honeycomb's post-mortem on building their LLM-powered Query Assistant — the engineering challenges they didn't expect, including output validation, latency at the tail, prompt brittleness, and user trust. Unusually honest practitioner account from a team that shipped an LLM feature to production.
params:
  source: pinboard
  sourceUrl: https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm
---

![All the Hard Stuff Nobody Talks About When Building with LLMs](/images/notes/hard-stuff-building-llms-honeycomb.png)

## Summary

Honeycomb's post on building their Query Assistant — an LLM-powered feature that translates natural language questions into Honeycomb query syntax — is one of the more honest practitioner accounts of the challenges that don't show up in demos. Written by Phillip Carter, it covers the gap between it works in testing and "it works reliably for production users."

The specific challenges Honeycomb encountered: output format validation (the LLM would produce syntactically wrong queries that needed retry logic), tail latency (p99 response times from OpenAI were unpredictably high, affecting perceived quality), prompt brittleness (small changes to the prompt would break cases that previously worked), hallucination of valid-looking but wrong query fields, and user trust calibration (users would trust obviously wrong outputs if they looked plausible).

The trust calibration problem is the most interesting. When the Query Assistant returned a query, users would often run it without checking — and get wrong results without realizing it. The solution involved surfacing confidence signals and making the system's reasoning more transparent, not just making the output more accurate. This is a product design insight that doesn't come from technical benchmarks.

## Key points

- Output validation is mandatory: LLM outputs fail format requirements frequently — always have retry logic.
- Tail latency from LLM APIs is unpredictable — p99 is much worse than median; design for it.
- Prompt brittleness: small prompt edits break previously working cases — evals are required before any change.
- User trust miscalibration: users over-trust plausible-looking wrong outputs — transparency design matters.
- From Honeycomb (observability tool) — credible practitioner account, not a vendor pitch.

[Original](https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm)
