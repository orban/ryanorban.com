---
title: "microfeed: Self-Hosted CMS on Cloudflare"
date: 2022-12-27
categories:
  - cms
  - cloudflare
  - self-hosting
  - podcasting
  - open-source
description: microfeed is a lightweight self-hosted CMS that runs entirely on Cloudflare's free tier — Workers, R2, D1 — for publishing podcasts, blogs, photos, videos, and curated links. An elegant example of serverless CMS architecture with near-zero hosting costs.
params:
  source: pinboard
  sourceUrl: https://github.com/microfeed/microfeed
---

## Summary

microfeed is a lightweight, self-hosted CMS that runs on Cloudflare's infrastructure — Cloudflare Workers for logic, Cloudflare R2 for object storage, and Cloudflare D1 (SQLite at the edge) for data. The architecture lets you publish podcasts, blogs, photos, videos, documents, and curated URLs from a single admin interface at essentially zero cost using Cloudflare's generous free tiers.

The design philosophy is minimal and focused: no database server to manage, no compute instances to scale, no storage costs to worry about. Everything runs at Cloudflare's edge, meaning your content is served from locations close to your readers globally without any CDN configuration. This is the serverless CMS pattern taken to its logical conclusion — the entire application is a set of edge functions and managed storage.

microfeed is particularly interesting for podcasters who want to own their RSS feed and episode storage without paying for podcast hosting platforms. By hosting on Cloudflare R2 (no egress fees), podcast episode files can be served for free regardless of download volume — a meaningful saving for popular shows. The project demonstrates how Cloudflare's edge platform, originally positioned for performance and security, became a compelling self-hosting substrate for full applications.

## Key points

- Runs entirely on Cloudflare free tier: Workers + R2 + D1 — near-zero hosting cost.
- Supports podcasts, blogs, photos, videos, documents, and curated links from one admin.
- No egress fees on Cloudflare R2 — podcast episode serving is effectively free at any scale.
- Cloudflare D1 (SQLite at edge) for structured data; R2 for media storage.
- Example of Cloudflare Workers as a complete application substrate, not just middleware.

[Original](https://github.com/microfeed/microfeed) → GitHub
