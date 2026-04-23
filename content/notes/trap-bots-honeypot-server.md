---
title: Trap bots on your server
date: 2025-10-27
categories:
  - security
  - self-hosting
  - bots
  - honeypot
  - web
description: Maurycy's writeup on setting up a bot honeypot on your server — serving intentionally garbled content and endless links to trap and slow down scrapers. A practical defensive technique for server operators dealing with aggressive crawlers.
params:
  source: pinboard
  sourceUrl: https://maurycyz.com/projects/trap_bots/
---

![Trap bots on your server](/images/notes/trap-bots-honeypot-server.png)

## Summary

Maurycy's blog documents a technique for trapping and slowing down web scrapers and bots on your server using a honeypot approach. The idea: create a section of your site that serves intentionally garbage/garbled content and infinite links, causing bots to waste CPU time and bandwidth crawling an endless maze that yields nothing useful.

The implementation is a classic tarpit pattern from server defense: lure bots with plausible-looking links, then serve them content designed to occupy them indefinitely — circular links, randomly generated text, pages that point to more pages. This wastes the bot's resources rather than yours, and can help identify scrapers (they'll hit the honeypot while legitimate users won't).

This is a low-cost defensive technique particularly useful for self-hosting setups where a small number of aggressive scrapers can noticeably affect server load. More sophisticated versions rate-limit or block detected bots; this approach complements rate-limiting by consuming attacker resources rather than just refusing them. Related to fail2ban, robots.txt, and other bot management techniques.

## Key points

- Honeypot technique: serve garbage content and infinite circular links to trap web scrapers.
- Wastes bot resources (CPU, bandwidth) rather than consuming your own with blocking logic.
- Effective tarpit: bots get stuck crawling a procedurally generated endless maze.
- Complements rate-limiting and fail2ban for complete bot defense.
- Low-effort to implement; particularly useful for personal self-hosting setups.

[Original](https://maurycyz.com/projects/trap_bots/)
