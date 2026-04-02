---
title: "Miasma: AI scraper honeypot that serves poisoned training data"
date: 2026-04-01
categories:
  - anti-scraping
  - ai-defense
  - web-security
  - open-source
description: Lightweight server that traps AI scrapers in an endless loop of poisoned data. A honeypot for the bot era.
params:
  source: pinboard
  sourceUrl: https://github.com/austin-weeks/miasma
---

![Miasma: AI scraper honeypot that serves poisoned training data](/images/notes/miasma.png)

## Summary

[Miasma](/notes/miasma/) is a lightweight HTTP server that defends websites against AI web scrapers by trapping them in an endless pit of poisoned data. When a scraper hits it, Miasma serves corrupted training data alongside self-referential links, creating a recursive loop where the bot keeps consuming worthless content forever.

The deployment model is simple: you run [Miasma](/notes/miasma/) as a separate service and embed hidden links on your real site that point to it. Legitimate users never see the links (they're invisible in the UI), but automated scrapers follow them and get routed into the trap. The server is fast and low-memory since it generates garbage on the fly rather than serving real content.

This is an interesting approach to the AI training data problem — instead of trying to block scrapers (which is an arms race), you let them in and contaminate what they collect. It's the digital equivalent of a honeypot, but the goal is pollution rather than detection.

## Key points

- Serves poisoned training data and self-referential links that trap AI scrapers in an infinite loop of useless content.
- Hidden links on your real site route only automated scrapers to Miasma — legitimate users are unaffected.
- Lightweight HTTP server with minimal resource usage, generates garbage data on the fly.
- Flips the anti-scraping strategy from blocking (arms race) to poisoning (asymmetric defense).
- Open source, easy to deploy alongside any existing website.

[Original](https://github.com/austin-weeks/miasma)
