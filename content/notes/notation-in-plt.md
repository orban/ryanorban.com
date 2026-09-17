---
title: Crash Course on Notation in Programming Language Theory
date: 2014-01-10
categories:
  - programming-languages
  - type-theory
  - notation
  - academic
  - formal-methods
description: Jeremy Siek's crash course on the mathematical notation used in programming language theory — inference rules, judgments, big-step and small-step semantics. Essential reading before tackling any PL paper.
params:
  source: pinboard
  sourceUrl: http://siek.blogspot.com/2012/07/crash-course-on-notation-in-programming.html
---

## Summary

Jeremy Siek's blog post decodes the mathematical notation that programming language theory (PLT) papers use without explanation. Inference rules, typing judgments, operational semantics (big-step and small-step), and the sequent notation (⊢) that appears everywhere in type theory — these are the vocabulary every PL paper assumes you know, and they're almost never explained in the papers themselves.

The post bridges the gap between I understand programming and I can read a PL paper. The notation isn't intrinsically hard — it's pattern-matching on mathematical symbols with specific conventional meanings — but the learning curve is steep if you're self-studying without a course.

## Key points

- Inference rules (horizontal line, premises above, conclusion below) are the primary notation for defining type systems and operational semantics
- Typing judgment notation `Γ ⊢ e : τ` means "in context Γ, expression e has type τ" — this appears in virtually every type system definition
- Big-step semantics maps expressions directly to values; small-step semantics shows individual reduction steps — the choice affects what properties are easy to prove
- The `[x := v]` substitution notation for variable capture and substitution is explained with concrete examples
- Reading fluency in this notation is a prerequisite for papers in dependent types, effect systems, gradual typing, and most PL research

[Original](http://siek.blogspot.com/2012/07/crash-course-on-notation-in-programming.html)
