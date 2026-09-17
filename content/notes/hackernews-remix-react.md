---
title: Hacker News Clone with Remix and React
date: 2022-02-17
categories:
  - react
  - remix
  - typescript
  - open-source
  - reference-architecture
description: A Hacker News clone built with Remix and React in universal TypeScript — same codebase runs on server and client. A clean reference architecture for modern full-stack React apps using the Remix framework at a time when it was newly open-sourced.
params:
  source: pinboard
  sourceUrl: https://github.com/clintonwoo/hackernews-remix-react
---

## Summary

This Hacker News clone by Clinton Woo is a reference implementation of a full-stack app using Remix and React with universal TypeScript — the same code runs on both server and client. It's primarily a teaching/reference project that demonstrates how Remix handles data loading, server-side rendering, and form mutations in a real application with non-trivial data requirements.

Remix was open-sourced by the React Router team in late 2021, positioning itself as a framework that takes web fundamentals (HTTP, forms, URLs) seriously rather than abstracting them away. The HN clone is a useful demonstration vehicle because everyone knows what HN looks like and it involves nested data, pagination, and user interactions that stress-test framework assumptions.

The universal TypeScript aspect is notable: Next.js had established the SSR React pattern, but Remix's approach to data loading (loaders/actions co-located with routes) was architecturally distinct. This repo was one of the early real-world Remix examples that helped developers understand how to think in the Remix model versus Next.js patterns.

## Key points

- Remix framework: route-based data loading (loaders), mutations (actions), and nested layouts.
- Universal TypeScript: shared types across server and client code in a single codebase.
- Server-side rendering: all data loaded server-side by default, then hydrated client-side.
- Reference architecture for nested routes — HN's comment trees are a natural fit for nested route layouts.
- Contrasts with Next.js approach: Remix uses web platform primitives (forms, HTTP) more directly.

[Original](https://github.com/clintonwoo/hackernews-remix-react) → GitHub
