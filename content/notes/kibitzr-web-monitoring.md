---
title: "Kibitzr: Self-Hosted Web Page Monitoring"
date: 2022-01-29
categories:
  - automation
  - monitoring
  - self-hosted
  - notifications
  - open-source
description: Kibitzr is a self-hosted web monitoring and notification tool — watch pages for changes, parse content with CSS/XPath, run bash/Python transforms, and route alerts to Slack or email. Configured in YAML and deployable on minimal hardware.
params:
  source: pinboard
  sourceUrl: https://kibitzr.github.io/
---

## Summary

Kibitzr is a self-hosted automation tool for monitoring web pages and triggering notifications when content changes. The use cases are mundane but genuinely useful: track whether a library has released a new version, watch for a specific status change on a service, alert when a job posting appears. The alternative is either manual checking or paying for a monitoring SaaS.

The architecture is minimal: configure monitoring jobs in YAML, specifying what to fetch, how to parse it (CSS selectors, XPath, or regular expressions), any transforms to apply (bash scripts, Python), and where to send notifications (Slack, Mailgun, email). Selenium handles cases where pages require JavaScript rendering. It runs continuously in the background, polling on user-defined schedules.

The self-hosted nature is a meaningful advantage for cases involving authentication — you can use your own session cookies or API keys without handing them to a third-party service. Works on minimal hardware, including a Raspberry Pi. The MIT license and active community on GitHub make it a solid choice for personal monitoring infrastructure.

## Key points

- YAML-configured monitoring jobs: fetch → parse (CSS/XPath/regex) → transform (bash/Python) → notify (Slack, email).
- Selenium support for JavaScript-heavy pages that require a full browser.
- Self-hosted advantage: you control credentials — no third-party SaaS sees your auth tokens.
- Runs on minimal hardware; good fit for Raspberry Pi or small VPS.
- Common uses: library release tracking, job alert monitoring, service status checks, account balance alerts.

[Original](https://kibitzr.github.io/)
