---
title: Spine.js vs Backbone.js
date: 2012-05-01
categories:
  - javascript
  - mvc
  - frontend
  - frameworks
  - web-development
description: A 2012 comparison of Spine.js and Backbone.js — the two leading JavaScript MVC frameworks before Angular, Ember, and React. Both aimed to bring structure to increasingly complex client-side web apps.
params:
  source: pinboard
  sourceUrl: http://hjortureh.tumblr.com/post/22117245794/spine-js-vs-backbone-js
---

![Spine.js vs Backbone.js](/images/notes/spine-js-vs-backbone-js.png)

## Summary

In 2012, Backbone.js and Spine.js were the two most talked-about solutions to the same problem: JavaScript applications were getting complex enough that the jQuery soup approach — event handlers wired up to DOM elements, application state scattered across global variables — wasn't cutting it. Both frameworks brought MVC architecture to the client side, giving developers models, views, and controllers (or their equivalents) to organize growing codebases.

Backbone.js, written by Jeremy Ashkenas of DocumentCloud, was the more established of the two. It was deliberately minimal — it provided models with key-value binding and custom events, collections, views with declarative event handling, and a router. It didn't enforce how you organized things beyond that. Underscore.js (also by Ashkenas) was a dependency and encouraged a functional style. Backbone.js was used by Rdio, LinkedIn Mobile, and others.

Spine.js, written by Alex MacCaw, was more opinionated. It was influenced by [CoffeeScript](/notes/coffeescript/) and had a cleaner class-based model. It handled asynchronous operations differently — its spine was built around the idea that UI updates should happen optimistically, with server sync happening in the background. The comparison explored which approach better fit real-world single-page application development.

## Key points

- Backbone.js was minimal and flexible; Spine.js was more opinionated with a stronger class model.
- Both predated AngularJS, Ember.js, and React — which would eventually win the JavaScript framework wars.
- Spine.js's optimistic UI updates were ahead of their time, anticipating patterns that React and Redux would later popularize.
- Backbone.js had more community traction and real-world adoption by 2012.
- The deeper tension: convention over configuration (Spine) vs. unopinionated primitives (Backbone) — a debate that recurs with every framework generation.
- Both are now largely historical artifacts, superseded by React, Vue, and Angular.

[Original](http://hjortureh.tumblr.com/post/22117245794/spine-js-vs-backbone-js)
