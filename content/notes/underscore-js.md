---
title: Underscore.js
date: 2012-04-15
categories:
  - javascript
  - functional-programming
  - utility-library
  - web-development
description: Underscore.js homepage bookmarked in 2012, when JavaScript lacked built-in functional programming utilities. Underscore provided map, filter, reduce, and dozens of other collection helpers that are now standard in ES6+ but were missing from pre-2015 JavaScript.
params:
  source: pinboard
  sourceUrl: http://documentcloud.github.com/underscore/
---

## Summary

Underscore.js (created by Jeremy Ashkenas, also the creator of [CoffeeScript](/notes/coffeescript/) and Backbone.js) provided a consistent toolkit of functional programming utilities for JavaScript before the language had them natively. The core: `_.map()`, `_.filter()`, `_.reduce()`, `_.each()`, `_.find()`, `_.pluck()`, `_.sortBy()`, and ~80 other utility functions for collections, arrays, objects, and functions.

The gap it filled was real. Pre-ES5, `Array.prototype.forEach` didn't exist everywhere; pre-ES6, there was no `Array.prototype.find()`, no destructuring, no spread operator. JavaScript in 2012 needed a library layer to be ergonomic for functional-style code. jQuery had some of this for DOM operations; Underscore provided it for data transformation.

Lo-Dash forked from Underscore in 2012 to address performance issues, and the two competed until Lodash effectively superseded Underscore by 2014. Meanwhile, ES6 (2015) shipped native equivalents for most of Underscore's most-used functions (`Array.from`, `Map`, `Set`, arrow functions, spread). The library is now largely obsolete for new code but remains one of the most influential JavaScript libraries ever written.

## Key points

- Underscore.js was the standard utility library for JavaScript before ES6 added equivalent features to the language.
- Lo-Dash (2012) forked from Underscore for better performance and more consistent behavior — by 2014, Lodash had largely replaced it.
- Jeremy Ashkenas wrote Underscore, [CoffeeScript](/notes/coffeescript/), and Backbone.js — an unusual concentration of influence on 2012 JavaScript culture.
- The pattern: useful library fills a language gap → language spec eventually incorporates the feature → library loses its reason to exist.
- Still used in millions of projects via transitive dependencies, even as direct adoption has fallen sharply.

[Original](http://documentcloud.github.com/underscore/) → GitHub
