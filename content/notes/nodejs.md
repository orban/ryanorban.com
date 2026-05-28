---
title: Node.js
date: 2012-04-15
categories:
  - javascript
  - nodejs
  - server-side
  - runtime
  - web-development
description: Node.js homepage bookmarked in 2012, when server-side JavaScript was still a novel and contested idea. Node's event-loop architecture and npm ecosystem would go on to reshape backend development across the industry.
params:
  source: pinboard
  sourceUrl: http://nodejs.org/
---

## Summary

[Node.js](/notes/nodejs/) (created by Ryan Dahl in 2009) brought JavaScript to the server, enabling the same language on both frontend and backend. Its distinguishing architectural choice was the event loop — a single-threaded, non-blocking I/O model designed for high-concurrency workloads like web servers. Rather than spawning a new thread per request (the Apache model), Node handles thousands of concurrent connections in a single thread by deferring I/O operations asynchronously.

In April 2012, Node was still being established. Version 0.6.x was current; the npm registry was growing but not yet the enormous ecosystem it would become. The main debates were about whether JavaScript was a serious language for server work and whether the single-threaded model would hold up under CPU-intensive workloads (spoiler: it doesn't — those require worker threads or external processes). But for I/O-heavy applications like REST APIs and real-time services, the model proved genuinely efficient.

The bookmark is likely part of the same exploration session as Express, Socket.IO, and Underscore.js — the core Node.js web stack of the era.

## Key points

- Event loop architecture: single thread, non-blocking I/O — excellent for concurrent I/O, poor for CPU-intensive computation.
- JavaScript on both client and server was the pitch: one language, shared code, no context-switching for full-stack developers.
- npm (Node Package Manager) would become as significant as Node itself — the largest software registry in the world by 2015.
- 2012 Node was pre-Express dominance, pre-Promises standardization, pre-async/await — callback-heavy, often criticized as callback hell.
- Ryan Dahl left the project in 2012; later created Deno as a Node.js redesign addressing its early architectural mistakes.

[Original](http://nodejs.org/)
