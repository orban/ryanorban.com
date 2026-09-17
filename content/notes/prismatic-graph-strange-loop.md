---
title: Prismatic's Graph at Strange Loop
date: 2012-10-12
categories:
  - clojure
  - functional-programming
  - data-flow
  - graph-computation
  - architecture
description: Prismatic's Strange Loop 2012 talk introducing their Graph library — a Clojure framework for declarative, composable data flow computation where functions are wired together as a directed dependency graph. An early influence on the functional reactive programming ideas that would shape ClojureScript and later frontend architectures.
params:
  source: pinboard
  sourceUrl: http://blog.getprismatic.com/blog/2012/10/1/prismatics-graph-at-strange-loop.html
---

![Prismatic's Graph at Strange Loop](/images/notes/prismatic-graph-strange-loop.png)

## Summary

Prismatic presented their Graph library at Strange Loop 2012, a functional computation framework written in Clojure that powered their news recommendation and personalization system. The core idea: instead of writing imperative code that chains function calls, you declare a directed acyclic graph where each node is a pure function and edges represent data dependencies. The runtime resolves the execution order and handles data flow automatically.

The problem Graph solved was coordination of complex, interdependent computations in a way that remained testable and composable. In Prismatic's recommendation system, the feed generation involved many derived computations — user interest models, article features, scoring functions, filter layers — each depending on outputs from earlier stages. With imperative code, these dependencies are implicit and tangled. With Graph, they're explicit in the structure of the graph itself. Adding a new computation means declaring its inputs; removing one doesn't break anything that didn't depend on it.

The Clojure implementation leveraged the language's strength in data-oriented programming: maps as the primary data structure, pure functions transforming them, and macros to make graph declarations readable. The library influenced Plumbing, the open-source version Prismatic later released, and connected to broader ideas about dataflow programming that would surface again in Re-frame (the ClojureScript Redux-like framework), Reagent's ratom system, and eventually in the signals model now popular in JavaScript frameworks. Strange Loop was the natural venue — the conference consistently surfaced ideas that influenced mainstream programming 3–5 years later.

## Key points

- Directed acyclic graph of pure functions: data dependencies are explicit in the graph structure, not implicit in call order.
- Clojure maps as the universal data carrier between nodes — idiomatic functional style applied to computation graphs.
- Prismatic's practical motivation: news recommendation pipelines with complex interdependencies that needed to be testable and composable.
- Influenced Plumbing (open-sourced Clojure graph library) and prefigured Re-frame's subscription graph in ClojureScript.
- Strange Loop as the venue: a 2012 preview of dataflow programming ideas that mainstream JavaScript frameworks adopted a decade later via signals/reactivity.

[Original](http://blog.getprismatic.com/blog/2012/10/1/prismatics-graph-at-strange-loop.html)
