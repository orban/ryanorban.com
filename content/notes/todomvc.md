---
title: TodoMVC
date: 2012-10-13
categories:
  - javascript
  - frameworks
  - benchmarking
  - open-source
  - frontend
description: TodoMVC is a project that implements the same Todo application across every major JavaScript framework, letting developers compare syntax and architecture side by side. It became the de facto benchmark for evaluating JS frontend frameworks.
params:
  source: pinboard
  sourceUrl: http://todomvc.com/
---

![TodoMVC](/images/notes/todomvc.png)

## Summary

[TodoMVC](/notes/todomvc/) is an open-source project that implements a canonical Todo application across dozens of JavaScript frameworks and libraries — React, Vue, Angular, Ember, Svelte, Backbone.js, vanilla JavaScript, jQuery, and compiled-to-JS languages like TypeScript, Elm, and Scala.js. The premise is simple: same spec, same features, different implementation. That constraint makes the comparison meaningful — you're seeing architectural differences, not feature differences.

The project's value is epistemological. In 2012, the JavaScript framework ecosystem was fragmenting rapidly. Backbone.js had just become popular, Angular.js was emerging from Google, Ember.js was being built by Yehuda Katz — each with different opinions about data binding, routing, and state management. [TodoMVC](/notes/todomvc/) let developers see the actual code rather than read sales pitches. It surfaced real tradeoffs: verbosity vs. magic, explicit vs. implicit data flow, component-based vs. template-based rendering.

The project has outlasted many of the frameworks it originally showcased, which is its own kind of statement. It later became a standard in browser performance benchmarks like Speedometer, moving from a developer education tool to an industry measurement baseline. The living maintenance model — community contributions update examples as frameworks evolve — has kept it current across a decade of churn.

## Key points

- Same spec implemented across all frameworks: eliminates feature differences so architectural tradeoffs are directly visible.
- Featured in Speedometer browser benchmarks — transitioned from educational resource to industry performance measurement.
- Covers not just frameworks but compiled-to-JS languages: TypeScript, Elm, Scala.js — showing the spectrum from library to language-level abstractions.
- Created in 2012 at peak JavaScript framework fragmentation, when the ecosystem needed a way to compare options empirically.
- Community-maintained, living resource — frameworks are added and updated as the ecosystem evolves.

[Original](http://todomvc.com/)
