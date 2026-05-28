---
title: iScroll — Mobile Scrolling Library
date: 2012-04-15
categories:
  - javascript
  - mobile
  - ux
  - ios
  - web-development
description: iScroll homepage bookmarked in 2012 — a JavaScript library that fixed momentum scrolling for mobile web apps, particularly on iOS where fixed-position elements and overflow scrolling were badly broken. A workaround for a platform limitation that browsers eventually solved natively.
params:
  source: pinboard
  sourceUrl: http://cubiq.org/iscroll
---

## Summary

iScroll (created by Matteo Spinelli) solved a painful mobile web problem: in 2012, iOS Safari did not support native momentum scrolling for `overflow: scroll` elements, and fixed position elements had severe rendering bugs. Web apps that needed scrollable regions inside a page — like a fixed header with a scrollable list — had to use JavaScript to simulate the scrolling behavior. iScroll was the standard solution.

The context is important. In 2012, mobile web development was dealing with the fact that mobile browsers were 3-4 years behind desktop browsers in feature support, and Apple was notoriously slow to fix Safari bugs that affected web apps (while being very fast to fix bugs that affected native app webviews). The `-webkit-overflow-scrolling: touch` CSS property that eventually solved the problem wasn't widely supported until iOS 5/iOS 6.

iScroll worked by intercepting touch events and calculating a simulated physics scroll (momentum, deceleration, bounce at edges) in JavaScript, then using CSS transforms to move the content. This was expensive in CPU terms and had many edge cases, but it was the only option for many use cases.

## Key points

- iOS Safari had a long-standing bug/limitation: `overflow: scroll` elements didn't have momentum scrolling until iOS 5+.
- iScroll used JavaScript touch event interception + CSS transforms to simulate native scrolling physics.
- Fixed-position elements were broken on mobile in 2012 — iScroll worked around this too, enabling fixed headers with scrollable content.
- Native CSS eventually resolved this with `-webkit-overflow-scrolling: touch` and then the `overscroll-behavior` property.
- A pattern of the mobile web era: JavaScript polyfills for platform features that browsers eventually implemented natively, making the library obsolete.

[Original](http://cubiq.org/iscroll)
