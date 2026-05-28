---
title: "Introduction to Backbone.js: Models"
date: 2012-04-12
categories:
  - javascript
  - backbone-js
  - mvc
  - frontend
  - web-development
description: Introduction to Backbone.js tutorial bookmarked in 2012, when Backbone was the leading client-side MVC framework. A historical reference point for how JavaScript frontend architecture was organized before React and virtual DOM changed everything.
params:
  source: pinboard
  sourceUrl: http://www.joezimjs.com/javascript/introduction-to-backbone-js-part-1-models-video-tutorial/
---

![Introduction to Backbone.js: Models](/images/notes/backbone-js.png)

## Summary

Backbone.js (created by Jeremy Ashkenas in 2010) was the dominant client-side MVC framework in 2012, providing structure to JavaScript applications when the alternative was jQuery spaghetti. It gave you Models (with validation and change events), Collections (observable arrays of models), Views (rendering logic tied to DOM elements), and a Router (hash-based URL routing). Minimal but opinionated enough to enforce consistency across a team.

The tutorial video series on joezimjs.com was typical of how people learned Backbone in 2012 — before Egghead.io and modern screencasting platforms matured. The community had recognized that Backbone was powerful but required significant boilerplate, and tutorials explaining the patterns were essential.

Backbone's philosophy was provide just enough structure. It didn't prescribe how you fetched data or how templates worked — you could use Handlebars, Mustache, or inline strings. This flexibility was its strength and its weakness: teams could build coherent apps, but each team's Backbone app looked different. The heavy lifting was left to the developer.

React (2013) made Backbone's approach obsolete by solving the view layer problem differently — rather than manually syncing model state to DOM updates, virtual DOM diffing automated it. By 2015, Backbone was in decline for new projects, though Backbone-built applications (LinkedIn, Airbnb, SoundCloud from the 2012 era) persisted.

## Key points

- Backbone.js was the MVC framework of 2011-2013 JavaScript — the first widely-adopted solution to organizing complex client-side code.
- Model + Collection + View + Router: minimal but sufficient structure for apps that were too complex for jQuery alone.
- Jeremy Ashkenas wrote Backbone, Underscore.js, and [CoffeeScript](/notes/coffeescript/) — an extraordinary concentration of influence on the era.
- React's virtual DOM (2013) solved Backbone's most painful problem (keeping DOM and model in sync) more elegantly, ending Backbone's growth.
- The era it represents: before npm made JavaScript modular, before Webpack bundled complex apps, before the component model.

[Original](http://www.joezimjs.com/javascript/introduction-to-backbone-js-part-1-models-video-tutorial/)
