---
title: The Mathematical Hacker
date: 2012-12-13
categories:
  - mathematics
  - programming
  - statistics
  - learning
  - career
description: Evan Miller's essay arguing that programmers who invest in mathematical fluency gain compounding advantages — because math enables them to evaluate methods rather than just apply them, and to work with uncertainty and probability naturally. The case for quantitative education in software.
params:
  source: pinboard
  sourceUrl: http://www.evanmiller.org/mathematical-hacker.html
---

![The Mathematical Hacker](/images/notes/the-mathematical-hacker.png)

## Summary

Evan Miller (author of How Not To Run an A/B Test and other widely-read statistics articles) wrote this essay arguing that programmers who develop genuine mathematical fluency — beyond the CS curriculum's discrete math and algorithms — gain qualitatively different problem-solving capabilities. The specific claim: mathematics trains you to reason about the structure of problems before writing code, to evaluate whether a method is appropriate before applying it, and to work with probabilistic and uncertain information rather than treating everything as deterministic.

The essay distinguishes between programmers who know how to code and programmers who know when a problem calls for a particular mathematical approach. A programmer implementing gradient descent without understanding calculus can copy the algorithm but can't debug it, tune it, or recognize when it's the wrong tool. A programmer who understands the convexity properties of the objective function can make principled decisions about initialization, step size, and convergence.

Miller's practical advice focuses on specific areas: linear algebra (matrix operations underlie nearly all machine learning and much data processing), statistics and probability theory (essential for any data-driven work), and calculus (for optimization). These aren't about applying formulas but about building the intuitions that let you reason about whether an approach will work before spending time implementing it.

## Key points

- Mathematical fluency enables evaluation of methods, not just application — you can ask is this the right approach? rather than just how do I implement this?
- Linear algebra: the substrate for machine learning, graphics, and signal processing — matrix thinking is increasingly general-purpose
- Statistics / probability: unavoidable in any data-driven domain; wrong intuitions here produce confidently wrong conclusions
- The compounding argument: mathematical fluency is a meta-capability that applies across domains; domain-specific skills are narrower
- Miller's related work: How Not To Run an A/B Test applies the same rigor to a common programming practice (A/B testing) that's often done with wrong statistical assumptions

[Original](http://www.evanmiller.org/mathematical-hacker.html)
