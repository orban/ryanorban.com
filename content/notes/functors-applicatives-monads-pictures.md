---
title: Functors, Applicatives, and Monads in Pictures
date: 2013-05-19
categories:
  - haskell
  - functional-programming
  - category-theory
  - education
description: Aditya Bhargava's illustrated guide to functors, applicatives, and monads using colorful box-and-function diagrams. The best visual introduction to these Haskell/category theory concepts for programmers coming from imperative languages.
params:
  source: pinboard
  sourceUrl: http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html
---

![Functors, Applicatives, and Monads in Pictures](/images/notes/functors-applicatives-monads-pictures.png)

## Summary

Aditya Bhargava (adit.io) wrote an illustrated explanation of three foundational Haskell abstractions — functor, applicative functor, and monad — using a consistent visual metaphor: values in contexts (boxes), and functions that operate on or transform those contexts. The post became one of the most widely linked explanations of these concepts, because the box metaphor makes the type signatures intuitive before you need to understand the category theory they formalize.

The progression is clean: a **functor** is anything you can `fmap` over (apply a function to the value inside a context). A `Maybe Int` is a functor — `fmap (+3) (Just 5)` gives `Just 8`. An **applicative** is a functor where the function itself can also be in a context — `Just (+3) <*> Just 5`. A **monad** extends this further: you can chain operations where each step produces a new context — this is what `>>=` (bind) does, allowing sequencing of operations that might fail, produce multiple values, or have side effects.

The real value of monads is not mathematical elegance but practical composition: `Maybe` for nullable computations, `IO` for effects, `Either` for error handling, `[]` for nondeterminism — all share the same interface. This connects to the Giry monad used in probabilistic programming and category-theoretic Bayesian inference.

## Key points

- **Functor**: `fmap f (Box x)` → `Box (f x)` — apply a pure function to a value inside a context
- **Applicative functor**: `(Box f) <*> (Box x)` → `Box (f x)` — apply a wrapped function to a wrapped value
- **Monad**: `(Box x) >>= f` where `f :: a -> Box b` — chain context-producing operations, flattening the extra layer
- `Maybe` monad: automatic short-circuit on `Nothing` — eliminate nested null checks
- `IO` monad: sequences effects in a pure language by threading the "world" as a value
- The box metaphor is informal but pedagogically sound; the formal version is category theory (objects, arrows, natural transformations)
- Post was part of a wave of accessible Haskell pedagogy that made functional concepts accessible to non-academics

[Original](http://adit.io/posts/2013-04-17-functors,_applicatives,_and_monads_in_pictures.html)
