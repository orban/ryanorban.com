---
title: First Hundred Days of Clojure
date: 2012-04-17
categories:
  - clojure
  - lisp
  - functional-programming
  - jvm
  - learning
description: Niclas Meier's reflection after 100 days of learning Clojure — a practitioner's account of what the language demands and what it delivers, written when Clojure was still a relatively young and unusual choice. A snapshot of the functional programming learning curve.
params:
  source: pinboard
  sourceUrl: http://www.niclas-meier.de/2012/04/first-hundred-days-of-clojure/
---

![First Hundred Days of Clojure](/images/notes/clojure-first-hundred-days.png)

## Summary

Niclas Meier's reflection after 100 days of learning Clojure captures the experience of a working developer crossing into Lisp-land for the first time via a modern, pragmatic vehicle. Clojure (created by Rich Hickey in 2007) was by 2012 gaining traction in the JVM ecosystem as a functional, dynamically-typed alternative to Java — one that ran on the same JVM and could call Java libraries directly, making it practical in a way that earlier Lisps hadn't been.

The first hundred days format is useful because it spans the arc from initial strangeness to early fluency. The features most distinctive about Clojure — persistent data structures, immutability by default, software transactional memory (STM), and the REPL-driven development cycle — are initially disorienting for developers from imperative backgrounds, but practitioners consistently report that the constraints make reasoning about concurrent programs much easier once internalized.

The 2012 context matters: this was before the explosion of functional programming concepts into mainstream languages (before Scala became mainstream, before Rust appeared, before JavaScript frameworks embraced immutability patterns). Learning Clojure in 2012 meant genuinely challenging the way you thought about state and time in programs.

## Key points

- Clojure's persistent data structures make immutability practical: "modified" collections share structure with their predecessors rather than copying.
- The REPL-driven workflow is qualitatively different from compile-run-test cycles — it changes how you explore and develop code.
- Clojure runs on the JVM and interoperates with Java, which made it adoptable in enterprise contexts where other Lisps couldn't reach.
- Rich Hickey's emphasis on simplicity over ease (his Simple Made Easy talk is the canonical reference) permeates the language's design decisions.
- 2012 Clojure was early-stage-mainstream — significant enough to have a real community and libraries, unusual enough that learning it was still a countercultural choice.

[Original](http://www.niclas-meier.de/2012/04/first-hundred-days-of-clojure/)
