---
title: Adding Elixir to a Next.js Chat App
date: 2023-06-27
categories:
  - elixir
  - nextjs
  - real-time
  - architecture
  - websockets
description: Linen's engineering post on adding Elixir to their Next.js chat app for real-time features — why they chose Elixir/Phoenix over Node.js for WebSockets, the architecture trade-offs, and how they run both stacks in production. A candid account of a polyglot architecture decision.
params:
  source: pinboard
  sourceUrl: https://www.linen.dev/s/linen/t/8008310/building-a-chat-app-with-nextjs-and-elixir-table-of-content-
---

![Adding Elixir to a Next.js Chat App](/images/notes/linen-elixir-nextjs.png)

## Summary

Linen (a Slack-alternative chat tool) wrote this post about adding Elixir and Phoenix to their Next.js application for real-time features. The core problem: Next.js is well-suited for rendering and API routes, but real-time WebSocket-heavy workloads (chat, presence, live updates) hit Node.js's concurrency limits at scale. Elixir's BEAM VM handles thousands of concurrent WebSocket connections natively with lightweight processes.

The architecture decision: keep Next.js for the web frontend and REST API, add Elixir / Phoenix for the real-time layer (WebSockets, pub/sub, presence tracking). Phoenix Channels handle WebSocket connections; Phoenix Presence tracks who's online. This is a polyglot architecture — two languages, each used where it's strongest. The engineering post is honest about the trade-offs: operational complexity increased (now running two services, two languages, two deployment pipelines), but the real-time performance ceiling is dramatically higher.

Phoenix Channels + BEAM VM is a well-established pattern for high-concurrency real-time features: Discord famously runs millions of WebSocket connections on Elixir, and WhatsApp used Erlang (the language Elixir compiles to) for years. Linen's case study is interesting because they're a small team making this decision — showing the trade-off calculus isn't just for large companies.

## Key points

- Next.js for web/API, Elixir/Phoenix for real-time — each language where it's strongest.
- Phoenix Channels: abstracts WebSocket connections into channels — pub/sub with automatic reconnection.
- Phoenix Presence: distributed presence tracking built on CRDTs — who's online, across multiple nodes.
- BEAM VM: lightweight processes, millions of concurrent WebSocket connections — reason for choosing Elixir.
- Trade-off: higher operational complexity (two stacks, two languages) for real-time performance ceiling.
- Discord case study often cited as validation: millions of concurrent Elixir/BEAM WebSocket connections at scale.

[Original](https://www.linen.dev/s/linen/t/8008310/building-a-chat-app-with-nextjs-and-elixir-table-of-content-)
