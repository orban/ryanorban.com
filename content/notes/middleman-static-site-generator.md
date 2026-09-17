---
title: "Middleman: Hand-Crafted Frontend Development"
date: 2012-12-13
categories:
  - static-sites
  - ruby
  - web-development
  - tools
  - jamstack
description: Middleman — a Ruby-based static site generator for building hand-crafted websites. Saved in the same cluster as other frontend/static site tools when static site generators were becoming the standard for developer personal sites and documentation.
params:
  source: pinboard
  sourceUrl: http://middlemanapp.com/
---

![Middleman: Hand-Crafted Frontend Development](/images/notes/middleman-static-site-generator.png)

## Summary

Middleman is a Ruby-based static site generator that uses familiar Ruby templating (ERB, Haml, Markdown) to produce static HTML/CSS/JS output. It was designed for developers who were comfortable with Ruby and wanted the workflow of a full web framework (partials, layouts, asset pipeline, helpers) without running a server. The "hand-crafted frontend development" tagline positioned it against both WordPress (too heavy) and plain HTML (too manual).

In December 2012, the static site generator ecosystem was in a competitive phase. Jekyll (Ruby, GitHub Pages-native) was gaining share, Octopress was the blogging layer on top of Jekyll, Nanoc and Middleman were for more complex sites, and alternatives in other languages (Pelican in Python, Hyde) existed. The Jamstack term didn't exist yet but the pattern was becoming clear: pre-generate HTML, serve from CDN, add interactivity via JavaScript APIs.

Middleman had a strong position in 2012-2013 for design-heavy marketing sites and developer documentation: it had more templating power than Jekyll, better [Sass](/notes/sass/) and [CoffeeScript](/notes/coffeescript/) integration, and a clean project structure. Many design agencies used it as their standard site framework. It later faced competition from Hugo (Go-based, much faster), Gatsby (React-based, integrates with CMSs), and Eleventy (JavaScript).

## Key points

- Middleman vs Jekyll: both Ruby-based static generators; Jekyll is simpler and GitHub Pages-native; Middleman has more framework features for complex sites
- Asset pipeline: Sprockets-based (same as Rails); compiles [Sass](/notes/sass/), [CoffeeScript](/notes/coffeescript/), concatenates and fingerprints assets
- Middleman Deploy: built-in deploy commands for S3, GitHub Pages, rsync — deployment without a server
- 2012-2013 use cases: design agency marketing sites, developer documentation, personal sites that needed more than Jekyll offered
- Pre-build era: before Gatsby, Vite, and modern JS bundlers, Ruby-based generators handled the asset compilation that JavaScript tools now own

[Original](http://middlemanapp.com/)
