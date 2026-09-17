---
title: Gmail No Response — Follow Up on Unanswered Emails
date: 2013-12-23
categories:
  - gmail
  - productivity
  - email
  - tool
  - python
description: Jonathan Kim's Gmail script to identify emails you sent that never received a reply — queries the Gmail API for sent messages with no subsequent reply thread. A small automation that solves a real followup problem before commercial tools like Boomerang addressed it.
params:
  source: pinboard
  sourceUrl: http://jonathan-kim.com/2013/Gmail-No-Response/
---

## Summary

Jonathan Kim wrote a Python script that queries the Gmail API to identify emails you sent that never received a reply. The problem is common: you fire off an important email, get distracted, and it disappears from your working memory. A week later you realize no one responded and you needed that information.

The approach is simple but effective: query your Sent Mail folder, find threads where you sent the last message, and flag those as candidates for follow-up. The Gmail API (via OAuth) gives programmatic access to thread data, so you can find threads where your message is the most recent item.

This kind of lightweight email hygiene automation was a niche of personal productivity scripting in 2013 — before commercial tools like Boomerang for Gmail, Mixmax, or Gmail's own built-in nudges addressed the problem. The script represents the era when developers built their own tools for problems that are now solved by SaaS products.

## Key points

- Queries Gmail API (OAuth) for sent-mail threads where your message is the last — no reply received.
- Solves the "I sent an important email and forgot to follow up" problem programmatically.
- Built in Python with Gmail API client libraries — a few dozen lines.
- Predates commercial solutions: Boomerang for Gmail, Mixmax, and Gmail's built-in nudge features now handle this use case.
- Part of a genre of personal productivity scripts that appeared before SaaS tools addressed the underlying need.
- The underlying Gmail API approach is still valid for anyone wanting custom email workflow automation.

[Original](http://jonathan-kim.com/2013/Gmail-No-Response/)
