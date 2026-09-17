---
title: Python and Real-time Web
date: 2013-06-24
categories:
  - python
  - real-time
  - websockets
  - tornado
  - web-development
description: Technical overview of real-time web patterns in Python circa 2013 — comparing Tornado, Twisted, gevent, and the emerging WebSocket ecosystem. A snapshot of Python's async web story before asyncio standardized the concurrency model.
params:
  source: pinboard
  sourceUrl: http://mrjoes.github.io/2013/06/21/python-realtime.html
---

## Summary

This 2013 post by Serge Koval (mrjoes) surveyed the Python ecosystem for building real-time web applications — those requiring push notifications, live feeds, or persistent connections rather than the traditional request-response model. In 2013, this meant choosing between a small set of async frameworks: Tornado, Twisted, gevent, and the newly emerging asyncio that would eventually become Python 3.4's standard library answer.

The fundamental problem: Python's Global Interpreter Lock (GIL) prevents true CPU parallelism in threads, and traditional synchronous web frameworks (Django, Flask) blocked on I/O while waiting for database queries or network responses. For real-time applications needing thousands of concurrent connections, you needed either an event loop (Tornado, Twisted) or cooperative multitasking via greenlets (gevent).

Socket.IO was the popular JavaScript-side solution at the time — it abstracted over WebSocket with fallbacks to long-polling for browsers that didn't support it. The Python side had gevent-socketio and tornadio2 as competing adapters. The post compared their approaches, performance characteristics, and compatibility. The conclusion in 2013: Tornado was the most production-proven; gevent was ergonomically simpler but less mature at scale.

## Key points

- WebSocket vs long-polling: WebSockets require a persistent TCP connection with bidirectional framing; long-polling is HTTP-based fallback — Socket.IO handled both transparently.
- Tornado: non-blocking I/O server written explicitly for high-concurrency use cases; used at FriendFeed and Facebook.
- gevent: monkey-patches the standard library to be non-blocking using greenlets — you write synchronous-looking code that runs asynchronously.
- asyncio (then called Tulip): Guido van Rossum was developing this as the standardized async solution for Python 3; landed in 3.4 (2014).
- The fragmentation: Tornado, Twisted, and gevent each had their own async primitives and were incompatible — the problem asyncio was designed to solve.

[Original](http://mrjoes.github.io/2013/06/21/python-realtime.html)
 → GitHub
