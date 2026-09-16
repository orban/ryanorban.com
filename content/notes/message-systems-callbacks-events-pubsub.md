---
title: "Message Systems in Programming: Callbacks, Events, Pub/Sub, Promises, and Streams"
date: 2014-10-20
categories:
  - javascript
  - async
  - architecture
  - messaging
  - programming-patterns
description: Jesse Warden's survey of async communication patterns in programming — callbacks, events, pub/sub, promises, and streams. A clear taxonomy of a domain where the terminology is often muddled, especially relevant to JavaScript's async evolution in 2014.
params:
  source: pinboard
  sourceUrl: http://jessewarden.com/2014/10/message-systems-in-programming-callbacks-events-pub-sub-promises-and-streams.html
---

## Summary

Jesse Warden's 2014 post surveys the landscape of asynchronous communication patterns in programming, with a focus on JavaScript. This was a moment when JavaScript was in the middle of a fundamental transition: the callback-hell era was ending, Promises were gaining traction, and RxJS/streams were emerging. Having a clear taxonomy mattered.

The five patterns form a spectrum of coupling and composability. **Callbacks** are the most direct: you pass a function to be called when something finishes — tight coupling, error handling is manual, nesting creates the famous callback pyramid of doom. **Events** decouple sender from receiver via named channels — the emitter doesn't know who's listening, listeners don't know who emitted. **Pub/Sub** extends events with a message broker, allowing true decoupling across system boundaries. **Promises** represent a future value — chainable with `.then()`, composable with `Promise.all()`, they turn async code back into a linear reading order. **Streams** model continuous data: observables that emit values over time, with transformation operators that compose (map, filter, flatMap).

In 2014 JavaScript, this taxonomy mapped directly to the tool landscape: Node.js EventEmitter for events, jQuery's Deferred for a promise-like pattern, Backbone.js events for application-level decoupling, and RxJS for reactive streams.

## Key points

- Callbacks: direct but creates nesting and error-handling complexity — the "callback pyramid of doom."
- Event emitters: named channels decouple sender from receiver — standard in [Node.js](/notes/nodejs/) via `EventEmitter`.
- Pub/Sub: adds a broker layer — true decoupling across processes or services.
- Promises: represent future values, chainable — ES6 Promises standardized this in 2015, resolving the fragmentation.
- Streams / Observables: sequences of values over time — RxJS brought this pattern to JavaScript.
- These patterns remain the foundation: modern async/await is syntactic sugar over Promises; reactive libraries still use Observables.

[Original](http://jessewarden.com/2014/10/message-systems-in-programming-callbacks-events-pub-sub-promises-and-streams.html)
