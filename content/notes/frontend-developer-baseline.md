---
title: A Baseline for Front-End Developers
date: 2012-04-12
categories:
  - frontend
  - javascript
  - web-development
  - developer-skills
  - tooling
description: Rebecca Murphey's 2012 benchmark post defining what a serious front-end developer should know beyond jQuery — version control, testing, build tools, and real JavaScript fundamentals. The article that forced a conversation about professional standards in frontend development.
params:
  source: pinboard
  sourceUrl: http://rmurphey.com/blog/2012/04/12/a-baseline-for-front-end-developers/
---

![A Baseline for Front-End Developers](/images/notes/frontend-developer-baseline.png)

## Summary

In 2012, Rebecca Murphey published a widely-shared article arguing that the bar for frontend development had risen dramatically — and that too many people calling themselves front-end developers still relied entirely on jQuery without understanding JavaScript fundamentals, used no version control, and wrote no unit tests.

The post laid out a minimum baseline: know Git, use a CSS preprocessor like [Sass](/notes/sass/) or LESS, understand JavaScript well enough to work without jQuery as a crutch, write tests with something like QUnit or Jasmine, and use build tools to automate repetitive tasks. It also advocated for [Node.js](/notes/nodejs/) not as a backend platform but as a tooling environment — the beginning of what became the npm-driven frontend build pipeline.

What made the article significant was its willingness to be prescriptive. Frontend development in 2012 was still treated as a second-class SKILL. Murphey's argument — that frontend engineers should hold themselves to the same professional standards as backend engineers — helped shift that perception.

## Key points

- Know JavaScript properly before reaching for jQuery — abstractions should be chosen, not leaned on as defaults.
- Git (or version control generally) is non-negotiable for professional work.
- Unit testing belongs in frontend work, not just backend; tools like QUnit and Jasmine make it tractable.
- Build tools (Grunt, make) should automate concatenation, minification, and preprocessing.
- CSS preprocessors ([Sass](/notes/sass/), LESS) are part of a professional workflow, not optional.
- [Node.js](/notes/nodejs/) enables a powerful local toolchain independent of backend platform choice.
- Command line literacy is a basic professional expectation.

[Original](http://rmurphey.com/blog/2012/04/12/a-baseline-for-front-end-developers/)
