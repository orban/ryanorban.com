---
title: Probability and Statistics Cookbook
date: 2012-09-16
categories:
  - statistics
  - probability
  - reference
  - mathematics
  - cheatsheet
description: Matthias Vallentin's probability and statistics cookbook — a dense reference PDF covering distributions, estimation, hypothesis testing, and Bayesian methods in concise formula sheets. The kind of reference you keep open in a second tab when doing statistical work.
params:
  source: pinboard
  sourceUrl: http://matthias.vallentin.net/probability-and-statistics-cookbook/cookbook-en.pdf
---

![Probability and Statistics Cookbook](/images/notes/probability-statistics-cookbook.png)

## Summary

Matthias Vallentin's probability and statistics cookbook is a concise reference document organized like a cheat sheet — dense with formulas, definitions, and key results without derivations or extended explanation. It covers probability theory (distributions, moments, generating functions, inequalities), statistical inference (frequentist estimation, hypothesis testing, confidence intervals), Bayesian inference (prior/posterior, conjugate distributions), and linear models.

The document sits in a useful niche: between a textbook (comprehensive but slow to consult) and a Wikipedia article (often incomplete or inconsistently formatted). For a practitioner who needs to remember the moment generating function of the gamma distribution or the form of the Neyman-Pearson lemma without re-reading a chapter, a well-formatted single-document reference is genuinely valuable. The probability and statistics cookbook format was a category — Jay Sklar's SQL cheat sheets, LaTeX reference cards — that predated Stack Overflow for technical reference.

The scope of the document signals where applied statistics was in 2012: heavy on classical frequentist methods (ANOVA, t-tests, chi-squared tests), with Bayesian inference covered but not dominant. MCMC methods were covered briefly. The machine learning overlap was minimal — this was stats as a discipline with its own epistemological commitments, not the "statistics is just features-in-model-out" framing that would dominate a few years later.

## Key points

- Dense formula reference for probability distributions, moments, estimators, hypothesis tests, and Bayesian inference — organized for consultation, not reading
- Covers conjugate prior families — key for Bayesian inference without numerical methods: Beta-Binomial, Dirichlet-Categorical, Normal-Normal, Gamma-Poisson
- Chebyshev's inequality, Markov inequality, Jensen's inequality — the fundamental probabilistic bounds used throughout applied math
- Frequentist framing: confidence intervals as procedures (not probability statements about the parameter), p-values correctly defined
- Useful complement to Larry Wasserman's *All of Statistics* — the cookbook gives lookup access to the formulas Wasserman derives

[Original](http://matthias.vallentin.net/probability-and-statistics-cookbook/cookbook-en.pdf)
