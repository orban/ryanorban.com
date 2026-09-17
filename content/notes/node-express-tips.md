---
title: Node and Express Tips
date: 2012-08-06
categories:
  - nodejs
  - express
  - javascript
  - web-development
  - backend
description: A collection of practical tips for building web applications with Node.js and Express in 2012, covering middleware patterns, error handling, and performance. Reflects the early period when Node's non-blocking I/O model was still novel to most web developers.
params:
  source: pinboard
  sourceUrl: http://calv.info/node-and-express-tips/
---

## Summary

A practical tips post for building web applications with Node.js and Express from 2012, a period when Node.js was still fairly new and the ecosystem was developing rapidly. Calvin French-Owen (a founder of Segment) shared tips covering Express middleware patterns, error handling, environment configuration, and performance considerations.

Node.js's core proposition in 2012 was its non-blocking, event-driven I/O model — the same single thread that handled HTTP requests could handle thousands of simultaneous connections without blocking, because I/O operations (database queries, file reads, network calls) were handled asynchronously via callbacks rather than blocking the thread. This made Node.js attractive for I/O-bound web servers, chat applications, and API proxies, where the bottleneck is waiting for network or disk, not CPU computation.

Express was (and remains) the dominant Node.js web framework, built around the concept of middleware functions chained together in a pipeline. Each middleware function receives `req`, `res`, and `next` — process the request, optionally modify the response, and call `next()` to pass to the next middleware in the chain. This composable middleware pattern was Express's key architectural insight and became the model for many subsequent web frameworks. By 2012, tips around this pattern — how to structure middleware, handle errors gracefully, use environment variables for configuration — represented the shared knowledge of the small community of Node.js practitioners.

## Key points

- Node.js non-blocking I/O handles thousands of concurrent connections on a single thread via event loop and callbacks.
- Express middleware pipeline: each function receives `req`, `res`, `next` — process and pass control forward.
- Error handling in Express: 4-argument middleware `(err, req, res, next)` for centralized error processing.
- Environment-based configuration (`NODE_ENV`) for separating dev/staging/production behavior.
- Node.js best suited for I/O-bound applications; CPU-heavy work blocks the event loop and degrades performance.
- Calvin French-Owen was a founder of Segment — context for why he was building on Node in 2012.

[Original](http://calv.info/node-and-express-tips/)
