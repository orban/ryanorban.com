---
title: Customize Twitter Bootstrap to Not Look Bootstrap-y
date: 2012-08-25
categories:
  - css
  - bootstrap
  - web-design
  - frontend
  - ui
description: A guide to customizing Twitter Bootstrap so your site doesn't look like every other Bootstrap site in 2012. The default Bootstrap aesthetic had become so recognizable that it was a liability for any product that wanted to appear design-forward.
params:
  source: pinboard
  sourceUrl: http://antjanus.com/blog/web-design-tips/user-interface-usability/customize-twitter-bootstrap-into-themes/
---

![Customize Twitter Bootstrap to Not Look Bootstrap-y](/images/notes/customize-twitter-bootstrap.png)

## Summary

A practical guide to customizing Twitter Bootstrap so that the resulting site didn't immediately read as a default Bootstrap template. In 2012, Bootstrap had become enormously popular — it was easy to adopt and provided a solid grid system and component library. But the default Bootstrap aesthetic (rounded gray buttons, blue navbar, specific typography) had become instantly recognizable, and any site using it without customization looked generic and rushed.

The author walked through the main levers for Bootstrap differentiation: changing the color palette (Bootstrap's LESS variables controlled almost everything), customizing typography (font choice was the highest-leverage change), overriding the navbar to use a different height, color, and navigation pattern, and selectively replacing or hiding components that were too Bootstrap-specific. The key insight: Bootstrap was a foundation, not a design, and treating it as a design was where teams went wrong.

The broader context was the rise of CSS frameworks as a common starting point for web development. Before Bootstrap, each frontend engineer would build custom grids and components from scratch. Bootstrap dramatically reduced this work but created a new problem: homogenization. The Bootstrapped look became a signal that a product hadn't invested in design. The solution the guide outlined — use Bootstrap's grid and layout system, but override everything visual — became the standard approach for teams that wanted the productivity benefit without the aesthetic cost. Bootstrap's LESS-based theming (and later [Sass](/notes/sass/)) was specifically designed to support this workflow.

## Key points

- Bootstrap's default aesthetic became instantly recognizable by 2012 — a liability for design-conscious products.
- Highest-leverage customizations: color palette (LESS variables), typography (font choice), navbar design.
- Strategy: use Bootstrap's grid and layout, override all visual styling — get the structural benefit without the aesthetic.
- Bootstrap used LESS preprocessor with variables controlling almost every visual property.
- The "Bootstrapped look" signaled insufficient design investment — customization was reputational necessity.
- Pattern continued: Bootstrap 4 (moved to [Sass](/notes/sass/)) and 5 made theming even more systematic.

[Original](http://antjanus.com/blog/web-design-tips/user-interface-usability/customize-twitter-bootstrap-into-themes/)
