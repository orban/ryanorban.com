---
title: Getting Started With Ember.js
date: 2012-06-12
categories:
  - javascript
  - emberjs
  - frontend
  - mvc
  - framework
description: Andy Matthews' getting started guide for Ember.js, written in early 2012 when Ember was still called SproutCore 2.0 and the framework was in flux. Ember was the ambitious option in the Backbone vs Ember vs Angular debate that defined frontend JS frameworks in 2012.
params:
  source: pinboard
  sourceUrl: http://www.andymatthews.net/read/2012/03/07/Getting-Started-With-EmberJS
---

![Getting Started With Ember.js](/images/notes/getting-started-emberjs.png)

## Summary

Ember.js (previously SproutCore 2.0) launched in late 2011 and was positioning itself as the opinionated, full-featured alternative to Backbone.js for building single-page applications. Where Backbone gave you minimal structure and left architecture decisions to the developer, Ember provided conventions over configuration: a router, two-way data binding, computed properties, and an object model with KVO (Key-Value Observing). The tradeoff was a steeper learning curve and more framework buy-in.

Andy Matthews' post walked through initial setup in early 2012, a period when Ember was changing rapidly. The core team (Yehuda Katz and Tom Dale) were still finalizing the router API and template system. Early Ember used Handlebars for templating — a logic-less template language that kept rendering concerns separate from application logic. The framework's data layer (Ember Data) was also in early development, with the model/persistence story still evolving.

The 2012 JavaScript framework landscape was genuinely contested. Backbone.js (Backbone.js, Jeremy Ashkenas) had first-mover advantage and was lightweight. Angular.js (Google, 1.0 released in 2012) was gaining momentum with its two-way binding approach. Ember was the ambitious option with the highest convention density. The debate was often framed as "how much framework do you want?" — and different answer led to different choices.

## Key points

- Ember.js (formerly SproutCore 2.0): opinionated full-stack JavaScript MVC framework released 2011.
- Core differentiators: two-way data binding, computed properties, strong conventions, built-in router.
- Core team: Yehuda Katz (Ruby on Rails core, jQuery team) and Tom Dale — brought Rails-style conventions to JS.
- 2012 was a period of rapid API change — early Ember docs frequently became outdated.
- Framework landscape: Backbone (minimal) vs. Ember (opinionated) vs. Angular (two-way binding) — each representing a different philosophy.

[Original](http://www.andymatthews.net/read/2012/03/07/Getting-Started-With-EmberJS)
