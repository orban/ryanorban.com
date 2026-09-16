---
title: Coded Mails — Responsive HTML Email Templates
date: 2020-10-09
categories:
  - email
  - html
  - templates
  - web-development
  - tools
description: Coded Mails provides 60+ responsive HTML email templates built with MJML across six categories — receipt, welcome, reset, notification, newsletter, and general. Tested across 80+ email clients including Outlook, eliminating the table-nesting pain of hand-coded emails.
params:
  source: pinboard
  sourceUrl: https://codedmails.com/
---

## Summary

Coded Mails is a library of pre-built, responsive HTML email templates designed to eliminate the painful process of hand-coding emails that render correctly across clients. The underlying technology is MJML — a markup language that compiles to production-ready HTML, handling the VML, MSO hacks, and Outlook compatibility quirks that make raw HTML email authoring so tedious.

The library offers 60+ templates across six categories: general, receipt, welcome, reset, notification, and newsletter. Templates are organized into 12 professional themes, so you get a matching set across email types for brand consistency. Templates are tested across 80+ email clients including all Outlook versions (historically the most painful to support), Gmail, and Apple Mail.

The value proposition is concrete: MJML's semantic components allow writing ~80% less code compared to raw HTML emails, and the output is cross-client compatible by design. You get both the MJML source and pre-compiled HTML, so you can either modify the source and recompile or use the HTML directly. No ESP (email service provider) lock-in — the output is plain HTML you can drop into Mailchimp, SendGrid, SES, or wherever.

## Key points

- MJML solves the email rendering problem at the source: it abstracts away table-based layout, VML for Outlook, and media queries for responsive design into semantic components.
- Outlook's proprietary rendering engine (Word-based in older versions) is the main compatibility challenge in HTML email — tested templates remove that uncertainty.
- The 12-theme system makes picking a consistent set for a product (welcome, reset, notification, receipt) straightforward without custom design work.
- Free for commercial use — 400+ GitHub stars suggests active community usage.
- Alternatives: Litmus (testing platform, not templates), Email on Acid, Postmark's template library. Coded Mails occupies the free + well-designed niche.

[Original](https://codedmails.com/)
