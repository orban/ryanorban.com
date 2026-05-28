---
title: "sdump: SSH-native HTTP request bin for webhook debugging"
date: 2024-01-31
categories:
  - developer-tools
  - webhooks
  - debugging
  - ssh
  - terminal
description: sdump is an SSH-native HTTP request bin for debugging webhooks — spin up a URL, connect via SSH to inspect incoming requests in your terminal, no browser required. Self-hostable with a public instance available.
params:
  source: pinboard
  sourceUrl: https://github.com/adelowo/sdump
---

![sdump: SSH-native HTTP request bin for webhook debugging](/images/notes/sdump.png)

## Summary

[sdump](/notes/sdump/) is an open-source HTTP request inspection tool that is accessed via SSH rather than a browser. The use case is the same as RequestBin or webhook.site — you get a temporary URL, point a webhook at it, and inspect the incoming HTTP requests. What distinguishes [sdump](/notes/sdump/) is the interface: you connect with `ssh` and interact with a TUI in your terminal rather than opening a browser tab.

The architecture has two components: an HTTP server that receives and stores incoming requests in a PostgreSQL database, and an SSH server that provides the terminal inspection interface. When you connect via SSH, you see a keyboard-driven TUI with syntax highlighting, request headers, body, and timing. URLs are stable across sessions — using the same SSH key gives you the same URL each time, which is useful for testing webhooks with persistent identifiers.

[sdump](/notes/sdump/) is self-deployable (Docker or binary) with a public hosted instance also available. It addresses the dependency on third-party request bin services or the complexity of tools like Ngrok for local webhook testing. The SSH interface means no browser, no web UI to load — just a terminal connection that works everywhere SSH works, including from servers that don't have a browser.

## Key points

- HTTP request bin for webhook debugging accessed via SSH, not a browser.
- TUI with syntax highlighting, headers, body inspection — keyboard-driven.
- Stable URLs per SSH key — consistent endpoint for persistent webhook testing.
- Architecture: HTTP server + SSH server backed by PostgreSQL.
- Self-hostable or use the public instance.
- Alternative to RequestBin, webhook.site, Ngrok for server-side or terminal-first workflows.

[Original](https://github.com/adelowo/sdump) → GitHub
