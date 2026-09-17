---
title: Sass
date: 2012-04-15
categories:
  - css
  - sass
  - preprocessor
  - web-development
  - frontend
description: Sass homepage bookmarked in 2012, when CSS preprocessors were the primary tool for managing stylesheet complexity. Sass introduced variables, nesting, mixins, and partials to CSS before native custom properties existed.
params:
  source: pinboard
  sourceUrl: http://sass-lang.com/
---

## Summary

[Sass](/notes/sass/) (Syntactically Awesome Style Sheets) is a CSS preprocessor — it extends CSS with variables, nesting, mixins, functions, and partials, then compiles to plain CSS. Created by Hampton Catlin and developed by Natalie Weizenbaum, it was the dominant CSS preprocessor by 2012, competing primarily with LESS (which had slightly simpler syntax but fewer features).

The problem [Sass](/notes/sass/) solved was real: CSS in 2012 had no variables (so hex colors were repeated everywhere), no nesting (so you'd write `.nav ul li a { }` instead of nested rules), no reusable chunks (no mixins or functions), and no way to split large stylesheets into manageable files without multiple HTTP requests. Sass addressed all of these.

Two syntaxes existed: the original indented syntax (`.sass` files, significant whitespace) and SCSS (Sassy CSS), which was a superset of CSS. SCSS won in practice because existing CSS was valid SCSS, making adoption incremental. Compass was built on top of Sass as a framework providing cross-browser mixins and a grid system.

CSS custom properties (variables) shipped in browsers starting around 2014-2016, and CSS nesting is now in modern browsers — gradually eroding Sass's value proposition. But in 2012, Sass was essential for any serious CSS codebase.

## Key points

- [Sass](/notes/sass/) solved CSS's biggest pain points before the CSS spec addressed them: variables, nesting, mixins, partials.
- SCSS syntax (superset of CSS) won over the original indented syntax because existing CSS was valid SCSS.
- Compass extended Sass with cross-browser mixins and a grid system — the full stack for structured CSS in 2012.
- LESS was the main competitor; [Sass](/notes/sass/)/SCSS won primarily because of stronger tooling and the Ruby on Rails integration.
- Modern CSS (custom properties, nesting) has reduced the necessity of preprocessors, but Sass's compile-time features (loops, functions) still have no native equivalent.

[Original](http://sass-lang.com/)
