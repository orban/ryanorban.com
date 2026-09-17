---
title: Express — Node Web Framework
date: 2012-04-15
categories:
  - javascript
  - nodejs
  - express
  - web-framework
  - backend
description: Express.js homepage bookmarked in 2012, when it was the de facto web framework for Node.js. Express's minimal, middleware-composable design made it the starting point for almost every Node web project and set patterns that persist in modern frameworks.
params:
  source: pinboard
  sourceUrl: http://expressjs.com/
---

## Summary

Express (created by TJ Holowaychuk in 2010) became the dominant web framework for [Node.js](/notes/nodejs/) by applying a deliberately minimal philosophy: provide routing and middleware composition, nothing else. No ORM, no template engine, no session management baked in — just the ability to mount middleware functions that handle requests in a pipeline. This made Express extremely flexible and kept it small enough that adding what you needed didn't feel like fighting the framework.

The middleware model is Express's core idea: each request flows through a series of functions, each of which can modify the request/response or call the next middleware. This composability meant you could assemble an application from small, focused, independently testable pieces. Passport.js for auth, Mongoose for MongoDB, Morgan for logging, Multer for file uploads — all designed as Express middleware.

By 2012 Express had effectively won the Node.js web framework competition against Sinatra-inspired alternatives like Geddy and Flatiron. The MEAN stack (MongoDB, Express, Angular, Node) later became a standard web development shorthand. Express 4.x (2014) removed the bundled middleware in favor of explicit requires — a further commitment to minimalism.

## Key points

- Middleware composition is Express's fundamental abstraction: functions take `(req, res, next)` and chain together to build up app behavior.
- Minimal core + rich ecosystem of middleware: this pattern influenced Koa, Fastify, and the entire Node.js framework generation.
- TJ Holowaychuk wrote Express, Mocha, Jade/Pug, Stylus, and many other Node.js staples in an extraordinary burst of productivity 2010-2013.
- Still the most-used Node.js web framework by install count, despite being unmaintained for periods — a testament to its stability and simplicity.
- The 2012 version was pre-async/await, so middleware used callbacks — which made error handling particularly painful.

[Original](http://expressjs.com/)
