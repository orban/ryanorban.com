---
title: Probability Theory — A Primer
date: 2013-01-09
categories:
  - mathematics
  - probability
  - statistics
  - education
  - programming
description: Jeremy Kun's Math ∩ Programming blog post introducing probability theory from first principles — sample spaces, events, probability measures, conditional probability, and random variables. Part of his series making advanced mathematics accessible to programmers.
params:
  source: pinboard
  sourceUrl: http://jeremykun.com/2013/01/04/probability-theory-a-primer/
---

![Probability Theory — A Primer](/images/notes/probability-theory-primer-jeremykun.png)

## Summary

Jeremy Kun's Math ∩ Programming blog was known for introducing advanced mathematics to programmers through concrete examples and code. This primer on probability theory builds the formal framework from scratch: starting with sample spaces (the set of all possible outcomes), defining events (subsets of the sample space), introducing probability measures as functions that assign numbers satisfying the Kolmogorov axioms, then building to conditional probability, independence, and random variables.

The motivation for the formal treatment is that informal intuitions about probability fail in non-obvious ways. The Monty Hall problem, Simpson's paradox, and base rate neglect all stem from probability reasoning that feels right but violates the formal structure. Learning the formal framework doesn't just teach you theorems — it gives you a structure to check intuitions against and a language to describe probabilistic systems precisely.

The primer is written for programmers by showing how the abstract definitions connect to things they already work with: a sample space is like a sample from a statistical distribution, a random variable is like a function from outcomes to numbers, and conditional probability is like filtering a dataset. The goal is building the intuition that lets you apply and evaluate probabilistic methods, not just memorize formulas.

## Key points

- Sample space: the set of all possible outcomes — the foundation of the probability formalism
- Kolmogorov axioms: the three rules that define a valid probability measure (non-negativity, normalization, countable additivity)
- Conditional probability: P(A|B) = P(A∩B)/P(B) — probability of A given that B has occurred; the most-misapplied concept in probability
- Bayes' theorem: derived from conditional probability; the formal tool for updating beliefs given evidence
- Math ∩ Programming's value: translating formal mathematics into programming intuitions, not just teaching math in isolation

[Original](http://jeremykun.com/2013/01/04/probability-theory-a-primer/)
