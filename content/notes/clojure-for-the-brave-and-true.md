---
title: Clojure for the Brave and True
date: 2014-03-01
categories:
  - clojure
  - functional-programming
  - lisp
  - learning
  - open-source
description: Daniel Higginbotham's free online book for learning Clojure — covers functional programming, the JVM, macros, and concurrency with a humor-forward style. One of the most recommended Clojure introductions for programmers coming from imperative languages.
params:
  source: pinboard
  sourceUrl: http://www.braveclojure.com
---

## Summary

Daniel Higginbotham wrote Clojure for the Brave and True as a free online book targeting programmers with an imperative background (Python, Ruby, Java) who want to understand functional programming through Clojure. The book's voice is deliberately approachable — using humor and narrative framing to lower the intimidation barrier of a Lisp-derived language with unfamiliar syntax.

Clojure runs on the JVM and compiles to Java bytecode, giving it access to the Java ecosystem (libraries, tooling, deployment) while being a fundamentally different language: immutable data by default, persistent data structures, first-class functions, and homoiconic syntax (code is data, data is code). The homoiconicity enables Clojure macros — code that writes code at compile time — which is one of the most powerful and confusing features of the Lisp family.

The book covers: REPL-driven development (the interactive development style that makes Lisp languages uniquely productive for exploration), higher-order functions (`map`, `filter`, `reduce`), lazy sequences, Clojure atoms and refs for managing state in concurrent programs, and basic macros. The context in the 2014 data science community: Rich Hickey's talks on simplicity and Datomic were influential, and Clojure was getting attention as a language for data pipelines and Storm (the distributed stream processing system written in Clojure).

## Key points

- Clojure: functional, JVM-based Lisp — immutable data structures, REPL-driven development, powerful macro system.
- Free online at braveclojure.com — also published by No Starch Press.
- Nathan Marz (creator of Storm) was a prominent Clojure advocate in 2014 — contributed to the language's reputation in distributed systems.
- Persistent data structures in Clojure: structural sharing makes copy-on-write efficient — old and new versions coexist without copying everything.
- REPL workflow: evaluate code interactively as you write it — faster feedback loop than compile/run cycles.

[Original](http://www.braveclojure.com)
