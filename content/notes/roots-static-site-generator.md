---
title: Roots — Static Site Generator
date: 2012-12-13
categories:
  - static-site-generator
  - node-js
  - web-development
  - build-tools
  - frontend
description: Roots was a Node.js static site generator from Carrot Creative, combining Jade/Stylus/CoffeeScript with a clean CLI workflow. Representative of the 2012 wave of Node-based build tools that challenged Ruby-world tools like Jekyll and Middleman.
params:
  source: pinboard
  sourceUrl: http://roots.cx/
---

![Roots — Static Site Generator](/images/notes/roots-static-site-generator.png)

## Summary

Roots was a [Node.js](/notes/nodejs/)-based static site generator built by Carrot Creative (a Brooklyn digital agency). Released around 2012, it combined Jade (HTML templating), Stylus (CSS preprocessing), and [CoffeeScript](/notes/coffeescript/) (JavaScript compilation) into a single CLI workflow aimed at fast frontend development.

The 2012 static site generator landscape was crowded: Jekyll (Ruby, GitHub Pages integration) was dominant, Middleman (also Ruby) was gaining ground in the agency world, and Node-based tools like Roots were emerging as the ecosystem matured. Roots' differentiator was its opinionated default stack — pick it up and you had a working build pipeline immediately rather than assembling one from parts.

Jade (now Pug) in particular was a significant aesthetic choice — its whitespace-sensitive, bracket-free HTML templating felt clean to developers coming from Haml and Rails. The choice of Stylus over [Sass](/notes/sass/) or LESS aligned with the preference for minimal syntax. Roots targeted the agency/contractor use case: building marketing sites and landing pages quickly without a backend.

## Key points

- Roots used Jade + Stylus + [CoffeeScript](/notes/coffeescript/) as its default stack — maximally minimal syntax choices
- [Node.js](/notes/nodejs/)-based vs. Ruby-based generators (Jekyll, Middleman) — represented the Node ecosystem maturing in 2012
- Built by Carrot Creative, a Brooklyn agency — the tool reflected real agency workflow needs
- Later evolved and was eventually superseded by Webpack-era tools and Next.js-style frameworks
- Part of the 2012-2013 Node for frontend tooling wave that led to Grunt, Gulp, and then Webpack

[Original](http://roots.cx/)
