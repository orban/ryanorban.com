---
title: An Introduction to Programming in Go
date: 2014-05-14
categories:
  - go
  - programming
  - book
  - tutorial
description: Caleb Doxsey's free online book introducing the Go programming language — a clean, concise introduction covering types, functions, concurrency primitives, and the standard library. Go had just turned four years old in 2014 and was attracting serious attention for systems and network programming.
params:
  source: pinboard
  sourceUrl: http://www.golang-book.com/
---

## Summary

Caleb Doxsey's free online book is one of the earlier accessible introductions to the Go programming language, written around Go 1.2. By 2014, Go had carved out a niche: it offered near-C performance with garbage collection, a clean type system without classes, and built-in concurrency primitives (goroutines and channels) that made concurrent programming dramatically less error-prone than threads.

The book covers the language's distinctive design choices: static typing with type inference via `:=`, value vs. pointer semantics, interfaces as implicit (structural typing rather than explicit `implements`), and the Go concurrency model based on Communicating Sequential Processes (CSP). The goroutine + channel model encourages share memory by communicating rather than communicate by sharing memory — the insight that prevents most race conditions.

By 2014, Go was gaining adoption in infrastructure and backend systems: Docker had just been open-sourced (written in Go), etcd and Kubernetes were early, and companies like SoundCloud had written blog posts about migrating services from Ruby to Go for performance and operational simplicity. The book is a good entry point for understanding why Go attracted that early infrastructure crowd.

## Key points

- Goroutines are lightweight (a few KB stack), enabling thousands of concurrent operations — the concurrency model scales where threads don't.
- Channels are typed communication pipes between goroutines — first-class synchronization primitives that replace mutexes for most use cases.
- Interfaces in Go are implicit: any type that implements the required methods satisfies the interface, no declaration needed — enables flexible composition.
- The standard library is unusually complete: net/http, crypto, encoding/json, testing — production-ready without third-party dependencies for many tasks.
- Go's compilation speed (seconds for large programs) was a deliberate design goal, making it practical for large codebases unlike C++.

[Original](http://www.golang-book.com/)
