---
title: Moldable Development
date: 2023-10-06
categories:
  - software-development
  - tooling
  - ide
  - pharo
  - smalltalk
description: Moldable Development is a philosophy and tooling approach from the GT (Glamorous Toolkit) project — the idea that development tools should be easily moldable to fit the specific domain you're working in, rather than forcing all domains into the same generic interface.
params:
  source: pinboard
  sourceUrl: https://moldabledevelopment.com/
---

![Moldable Development](/images/notes/moldable-development.png)

## Summary

[Moldable Development](/notes/moldable-development/) is a software development philosophy and methodology centered on the idea that development tools should be adaptable to the specific domain and problem you're working with. Rather than using generic debuggers, inspectors, and editors for every kind of software, [moldable development](/notes/moldable-development/) argues you should quickly build custom tools that expose the right views and interactions for your specific system.

The concept comes primarily from Tudor Gîrba and the Glamorous Toolkit (GT) project — an open-source development environment built in Pharo Smalltalk that implements the philosophy. In GT, you can write a custom object inspector in a few lines — a domain-specific visualization that replaces the generic object tree with something meaningful for your data model. A calendar object shows a calendar view; a graph object shows a graph view. The environment rewards building these contextual tools because the overhead is low.

The argument: most software is explored, understood, and debugged through generic tools that weren't designed for the specific abstractions you're working with. This forces developers to mentally translate between their domain concepts and the tool's representation. [Moldable Development](/notes/moldable-development/) inverts this: spend a little effort making the tool understand your domain, and every subsequent interaction gets easier. It's related to Literate Programming and the idea that programs should be readable, but extends it to the development environment itself.

## Key points

- Development tools should be adaptable per domain — not one-size-fits-all generic views.
- From Tudor Gîrba and Glamorous Toolkit (GT) built on Pharo Smalltalk.
- Low cost of building custom inspectors/tools in GT — a few lines of code per domain-specific view.
- Mental model: reduce the translation overhead between domain concepts and tool representation.
- Related to Literate Programming and self-documenting system ideals.
- An alternative philosophy to the current mainstream of generic, language-server-protocol-based IDEs.

[Original](https://moldabledevelopment.com/) → Glamorous Toolkit
