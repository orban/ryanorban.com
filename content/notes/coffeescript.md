---
title: CoffeeScript
date: 2012-04-15
categories:
  - javascript
  - coffeescript
  - transpiler
  - web-development
  - language
description: CoffeeScript homepage bookmarked at its 2012 peak — a language that compiles to JavaScript, borrowing syntax from Ruby and Python. Preceded Babel and TypeScript in proving that transpilation was a viable path to better JS.
params:
  source: pinboard
  sourceUrl: http://coffeescript.org/
---

## Summary

[CoffeeScript](/notes/coffeescript/) (created by Jeremy Ashkenas in 2009) compiles to JavaScript, offering cleaner syntax borrowed from Python and Ruby: significant whitespace, implicit returns, arrow functions, list comprehensions, and string interpolation. In 2012 it was at peak adoption — GitHub had famously written parts of its frontend in [CoffeeScript](/notes/coffeescript/), and it was popular enough that Rails 3.1 added it to the asset pipeline by default.

The value proposition was simple: JavaScript in 2012 was verbose and had many rough edges (no classes, no modules, no `let`/`const`, no template literals). CoffeeScript fixed most of these through transpilation before ES6 (2015) addressed them in the language spec itself. In retrospect, CoffeeScript's main contribution was proving the market for better JavaScript — which is why both TypeScript and Babel succeeded.

CoffeeScript's decline was rapid after ES6 shipped. The language removed its reason to exist by solving the same problems natively. By 2016 it was effectively obsolete for new projects, though existing CoffeeScript codebases (including GitHub's) persisted for years as painful migrations.

## Key points

- [CoffeeScript](/notes/coffeescript/) pioneered the transpiler model for JavaScript — compile-to-JS became normal partly because of its success.
- GitHub's CoffeeScript usage was a powerful endorsement that accelerated adoption in 2011-2012.
- Rails 3.1 bundled CoffeeScript by default — the Rails community heavily influenced its peak.
- Obsoleted by ES6/ES2015 (2015), which incorporated many of the same improvements into JavaScript itself.
- TypeScript is the spiritual successor in spirit but a fundamentally different bet: static types rather than syntactic sugar.

[Original](http://coffeescript.org/)
