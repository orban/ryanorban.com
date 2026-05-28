---
title: Beginning Node.js and Express
date: 2012-04-25
categories:
  - nodejs
  - javascript
  - express
  - web-development
  - tutorial
description: An introductory Node.js and Express tutorial from 2012 — part of the wave of content that helped JavaScript developers cross from browser scripting to server-side web development. Node.js was two years old and just starting to find its production audience.
params:
  source: pinboard
  sourceUrl: http://javascriptplayground.com/blog/2012/04/beginning-node-js-express-tutorial
---

![Beginning Node.js and Express](/images/notes/beginning-nodejs-express.png)

## Summary

By April 2012, [Node.js](/notes/nodejs/) was roughly two years past its debut at JSConf 2009 and was transitioning from an experimental curiosity to a production-viable server platform. Ryan Dahl had demonstrated the idea that JavaScript's event-driven, non-blocking model — which worked in browsers — could make a genuinely fast server if you built the runtime correctly. [Node.js](/notes/nodejs/)'s event loop architecture meant it could handle large numbers of concurrent connections without the memory overhead of traditional thread-per-request servers.

Express.js, built on top of Node, had emerged as the de facto minimal web framework — providing routing, middleware, and request/response handling without imposing application structure. The combination of Node and Express was the 2012 equivalent of Flask in Python: enough to build real things, thin enough not to get in the way. JavaScript Playground (Jack Franklin's blog) was one of several sites producing practical tutorials for developers making the shift to server-side JavaScript.

The appeal for JavaScript developers was straightforward: one language for browser and server meant smaller mental context switches and the ability to share code (validation logic, data models) between client and server. The npm ecosystem was growing rapidly. Companies like LinkedIn (who rebuilt their mobile backend in Node) and Walmart were beginning to demonstrate that Node was production-grade at scale. The tutorial represented a pedagogical moment: helping a generation of front-end developers discover that they could write their backend too.

## Key points

- [Node.js](/notes/nodejs/) launched at JSConf 2009; by 2012 it was production-viable and gaining real enterprise adoption.
- Event loop architecture: single-threaded, non-blocking I/O — efficient for concurrent connections, poor for CPU-intensive tasks.
- Express.js was the minimal web framework for Node — routing + middleware, no more.
- npm (Node Package Manager) was growing rapidly — by 2012 had thousands of packages and was reshaping how JavaScript was distributed.
- LinkedIn rebuilt their mobile backend in Node in 2011, reducing server count and improving performance — a major early validation.
- The unification of JavaScript client/server ("isomorphic JavaScript") was becoming a real pattern, not just a theoretical benefit.

[Original](http://javascriptplayground.com/blog/2012/04/beginning-node-js-express-tutorial)
