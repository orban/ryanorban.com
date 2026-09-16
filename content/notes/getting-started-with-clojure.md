---
title: Getting Started with Clojure
date: 2013-01-09
categories:
  - clojure
  - lisp
  - functional-programming
  - jvm
  - learning
description: jrheard's beginner guide to getting started with Clojure — covering setup, REPL workflow, and the first concepts that trip people up. A 2013 onramp into Clojure during its peak growth period.
params:
  source: pinboard
  sourceUrl: http://jrheard.tumblr.com/post/40024238467/getting-started-with-clojure
---

## Summary

Clojure was in its peak growth period in 2012-2013. Rich Hickey had released it in 2007 as a practical Lisp for the JVM, emphasizing immutability, persistent data structures, and software transactional memory (STM). By 2013, it had an active community, a growing ecosystem (Leiningen for builds, Ring and Compojure for web, Datomic as Hickey's commercial database venture), and was attracting serious attention from developers who wanted the power of Lisp with Java ecosystem interop.

Getting started with Clojure had specific friction points that this guide addressed. The REPL-driven workflow was unfamiliar to developers coming from file-based languages. The prefix notation (s-expressions) required mental adjustment. The persistent data structures (vectors, maps, sets) had different performance characteristics than mutable equivalents. And configuring the build tooling (Leiningen) before you could write your first meaningful program was a barrier.

The 2013 context: Clojure was the language that many functional programming-curious developers chose before Haskell felt too academic and after Scala felt too complex. The community was producing excellent learning resources — Joy of Clojure, Clojure Programming (O'Reilly), and 4Clojure for exercises — and the language had established itself as a credible production choice, not just an experiment.

## Key points

- Rich Hickey's design philosophy: Clojure as simple made easy — immutability and pure functions by default, state management explicit
- REPL-driven development: the primary Clojure workflow; evaluate expressions interactively, build programs incrementally
- Leiningen: the standard Clojure build tool and dependency manager; analogous to npm or Maven
- Persistent data structures: structurally-shared immutable collections — the foundation of Clojure's approach to state
- ClojureScript: Clojure compiling to JavaScript; released 2011, gaining traction in 2013; eventually became the more compelling use case for many developers

[Original](http://jrheard.tumblr.com/post/40024238467/getting-started-with-clojure)
