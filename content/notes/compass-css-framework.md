---
title: Compass — CSS Authoring Framework
date: 2012-04-15
categories:
  - css
  - sass
  - compass
  - frontend
  - web-development
description: Compass homepage bookmarked in 2012 alongside Sass — a Sass-based CSS authoring framework providing cross-browser mixins, a grid system, and sprite generation. Part of the 2012 frontend toolchain before PostCSS and modern CSS made preprocessor frameworks less necessary.
params:
  source: pinboard
  sourceUrl: http://compass-style.org/
---

## Summary

Compass was a CSS authoring framework built on top of [Sass](/notes/sass/), created by Chris Eppstein in 2008. Where [Sass](/notes/sass/) provided the language primitives (variables, nesting, mixins), Compass provided the pre-built mixins for practical CSS problems: cross-browser CSS3 (vendor prefixes for `border-radius`, `box-shadow`, `transitions` before they were standardized), a grid system (960gs or Susy), and CSS sprite generation.

In 2012 this was genuinely useful. CSS3 features like `border-radius` required `-webkit-border-radius`, `-moz-border-radius`, and `border-radius` — three declarations for one visual effect. Compass had `@include border-radius(5px)` which expanded to all three. The same pattern applied to dozens of CSS3 features. Without a tool like Compass, maintaining vendor prefix consistency across a codebase was tedious and error-prone.

Compass's decline was predictable: Autoprefixer (2013) handled vendor prefixes by processing CSS post-compilation, making the Compass mixin approach redundant. Flexbox and CSS Grid reduced the need for grid frameworks. [Sass](/notes/sass/) itself incorporated more features, making the Compass utilities less necessary. By 2016, Compass was effectively unmaintained.

## Key points

- Compass solved 2012's most painful CSS problem: vendor prefixes for CSS3 — write once, expand to all required vendor variants.
- The CSS sprite generation feature was genuinely innovative: concatenate multiple small images into one file, use background-position to display them.
- Autoprefixer (2013) made Compass's vendor prefix approach obsolete by handling prefixes at post-processing time, not authoring time.
- Built on [Sass](/notes/sass/), so bookmarked alongside it — they were typically used together in the 2012 Ruby on Rails frontend stack.
- The pattern: tools that solve browser inconsistency problems become unnecessary when browsers converge on standards.

[Original](http://compass-style.org/)
