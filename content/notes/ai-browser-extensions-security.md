---
title: AI Browser Extensions Are a Security Nightmare
date: 2023-06-08
categories:
  - security
  - browser-extensions
  - ai
  - privacy
  - enterprise
description: Kolide's analysis of why AI browser extensions are a security and privacy risk — they require broad DOM access permissions that give them access to every page you visit, including sensitive internal tools. A practical warning for enterprise security teams evaluating AI productivity tools.
params:
  source: pinboard
  sourceUrl: https://www.kolide.com/blog/ai-browser-extensions-are-a-security-nightmare
---

![AI Browser Extensions Are a Security Nightmare](/images/notes/ai-browser-extensions-security.png)

## Summary

This post from Kolide (an endpoint security company) explains why AI browser extensions present outsized security risks compared to typical extensions. The core problem: AI writing assistants like early versions of Grammarly, various ChatGPT extensions, and similar tools require broad DOM access permissions — they need to read page content to function. This means they have access to every page you visit, including internal tools with sensitive data.

The permission model for browser extensions is binary at the host level: either the extension can read a page's content or it can't. There's no "read only Gmail, not Salesforce" option in the standard permissions model. When a user installs a write better emails AI extension, they're granting it access to their banking interface, their internal HR system, and their company's admin dashboards — all of which the extension can read silently.

The risk compounds because AI extensions typically send content to external servers for processing. Unlike a traditional extension that might just be reading DOM content locally, AI extensions need to transmit that content to LLM APIs. Every page's content potentially traverses the extension developer's infrastructure, with privacy and data residency implications that most users don't consider. From Kolide's perspective (they monitor endpoint security for enterprises), this is a shadow IT problem — employees installing these tools without security review.

## Key points

- AI browser extensions need broad DOM access to function — they read every page you visit.
- No granular host permissions: read email only isn't available; it's all-or-nothing per extension.
- Page content sent to external servers for LLM processing — data leaves your organization's infrastructure.
- Shadow IT risk: employees install individually, security teams often don't know, and policies aren't enforced.
- Enterprise implication: block or carefully vet AI extensions with access to internal tools and sensitive data.

[Original](https://www.kolide.com/blog/ai-browser-extensions-are-a-security-nightmare)
