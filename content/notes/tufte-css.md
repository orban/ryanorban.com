---
title: Tufte CSS
date: 2020-07-14
categories:
  - web-design
  - typography
  - css
  - open-source
  - data-visualization
description: Tufte CSS brings Edward Tufte's book typography principles to the web — wide margins for sidenotes, clean serif typography, and minimal chrome. A CSS library for anyone who wants their web writing to read like a well-designed book.
params:
  source: pinboard
  sourceUrl: https://edwardtufte.github.io/tufte-css/
---

![Tufte CSS](/images/notes/tufte-css.png)

## Summary

[Tufte CSS](/notes/tufte-css/) is a CSS stylesheet implementing the typographic principles from Edward Tufte's books on data visualization and analytical design. Tufte is known for minimalist, information-dense design: wide margins used for sidenotes instead of footnotes (keeping references close without interrupting flow), clean typography with good line length control, and minimal decorative chrome that distracts from content.

The library brings these principles to web pages. Key features: **sidenotes** displayed in the margin alongside the text they annotate (not at the bottom of the page), **margin figures** (small charts or images in the margin), clean serif typography with controlled measure (line width), and responsive behavior that converts margin notes to numbered footnotes on narrow screens where margins aren't available.

The design philosophy is particularly suited to long-form analytical writing — essays, documentation, research summaries — where the typical blog aesthetic (wide columns, few images, footnotes at the bottom) loses information or forces awkward reading patterns. Tufte's sidenote approach is borrowed from classic book design and is demonstrably better for dense technical writing than browser-convention footnotes.

Used by several academic and technical blogs that prioritize readability over conventional web design patterns.

## Key points

- Implements Edward Tufte's typography principles in CSS: sidenotes, margin figures, clean serif type.
- **Sidenotes**: annotations displayed in the margin, not at page bottom — keeps context visible while reading.
- Wide-margin layout built into the grid; responsive fallback collapses sidenotes to numbered footnotes.
- Best suited for: long-form essays, research summaries, documentation — analytical writing that benefits from dense annotation.
- Part of a tradition of web typography that prioritizes reading over convention: see also Practical Typography (Butterick).

[Original](https://edwardtufte.github.io/tufte-css/) → GitHub
