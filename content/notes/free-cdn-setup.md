---
title: How to Set Up a Practically Free CDN
date: 2022-01-15
categories:
  - cdn
  - infrastructure
  - web
  - self-hosting
  - devops
description: A GitHub gist guide to setting up a practically free CDN for personal projects using Cloudflare and free-tier object storage. Covers the stack for serving static assets globally without paying enterprise CDN prices.
params:
  source: pinboard
  sourceUrl: https://gist.github.com/charlesroper/f2da6152d6789fa6f25e9d194a42b889
---

## Summary

This GitHub gist by charlesroper documents a configuration for running a personal CDN (Content Delivery Network) at near-zero cost by stacking free-tier services. The typical approach combines Cloudflare (free tier CDN/proxy with global PoPs) with cheap or free object storage backends like Backblaze B2, Cloudflare R2, or similar S3-compatible storage to serve static assets.

The appeal: professional CDN services (AWS CloudFront, Fastly, Akamai) are priced for enterprise usage, but personal sites and small projects mostly need bandwidth-efficient static asset delivery — images, fonts, JavaScript, CSS. The Cloudflare free tier handles the edge caching and global distribution; the origin storage provides persistence at minimal cost. Backblaze B2 has a Cloudflare partnership that makes B2 → Cloudflare egress free (no bandwidth charges), making the total cost essentially just storage ($0.006/GB/month).

The configuration involves setting up a Cloudflare Worker or page rule to proxy requests from a custom subdomain to the object storage bucket, configuring cache TTLs, and handling CORS headers for cross-origin requests. Cloudflare R2 (launched October 2021) simplified this further by being directly integrated with Cloudflare's network with zero egress fees.

## Key points

- Stack: Cloudflare CDN (free tier) + Backblaze B2 or Cloudflare R2 origin storage (cheap/free egress)
- Cloudflare-Backblaze B2 Bandwidth Alliance: B2 egress through Cloudflare is free — only pay storage
- Cloudflare R2: native zero-egress S3-compatible storage, the simplest solution as of late 2021
- Use case: personal sites, static assets, image hosting, software distribution without enterprise CDN costs
- Cloudflare Workers for URL rewriting, custom headers, and cache control logic

[Original](https://gist.github.com/charlesroper/f2da6152d6789fa6f25e9d194a42b889)
