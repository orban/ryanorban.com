---
title: "Bayes' Theorem: Conditional Probabilities"
date: 2012-06-08
categories:
  - statistics
  - probability
  - bayesian
  - mathematics
  - reference
description: "A Vassarstats reference page on Bayes' Theorem and conditional probabilities. The theorem is the backbone of Bayesian reasoning: updating prior beliefs with new evidence to get a posterior probability."
params:
  source: pinboard
  sourceUrl: http://vassarstats.net/bayes.html
---

![Bayes' Theorem: Conditional Probabilities](/images/notes/bayes-theorem-conditional-probability.png)

## Summary

Bayes' theorem describes how to update a probability estimate given new evidence. The formula — P(A|B) = P(B|A) × P(A) / P(B) — expresses the posterior probability of A given B as a function of the likelihood (how probable B is if A is true), the prior probability of A, and the marginal probability of B. In plain terms: start with what you already believe (prior), observe evidence, and compute what you should believe now (posterior).

The Vassarstats page (by Richard Lowry at Vassar College) provided an accessible introduction to conditional probability, aimed at students of statistics and psychology. It worked through concrete examples — the classic medical testing scenario, where a test with 99% accuracy on a rare disease still produces mostly false positives because the disease is so rare (the base rate fallacy). This is counterintuitive enough that even doctors get it wrong in studies.

Bayesian reasoning underlies a huge range of applications: spam filtering (naive Bayes classifiers), Bayesian inference in machine learning, A/B testing with Bayesian alternatives to frequentist p-values, medical diagnosis, and the philosophy of scientific reasoning. The theorem was known to Thomas Bayes in the 18th century but formalized and named by Pierre-Simon Laplace. The Bayesian vs. frequentist debate in statistics ran hot through the 20th century and remains partially unresolved.

## Key points

- Formula: P(A|B) = P(B|A) × P(A) / P(B) — prior belief updated by likelihood of evidence.
- Base rate fallacy: even very accurate tests produce mostly false positives when the condition is rare — ignoring the prior.
- Bayes' theorem is the foundation of naive Bayes spam filters, Bayesian networks, and Bayesian A/B testing.
- Named for Thomas Bayes (1701–1761), formalized by Pierre-Simon Laplace.
- The frequentist vs. Bayesian debate: whether probability represents long-run frequency or degree of belief.

[Original](http://vassarstats.net/bayes.html)
