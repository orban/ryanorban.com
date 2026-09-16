---
title: "Frequentism and Bayesianism: A Practical Introduction"
date: 2014-03-12
categories:
  - bayesian
  - statistics
  - python
  - frequentist
  - probability
description: Jake VanderPlas's Python-driven comparison of frequentist and Bayesian statistics — showing the two philosophies side-by-side with code. The most-cited accessible treatment of a distinction that confuses most practitioners.
params:
  source: pinboard
  sourceUrl: http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/
---

## Summary

Jake VanderPlas wrote this post as part of a series cutting through one of statistics' most persistent debates: frequentist statistics vs Bayesian statistics. The core disagreement is philosophical before it's technical. Frequentists define probability as the long-run frequency of outcomes across repeated experiments — a coin has a 50% chance of heads because half of infinite flips would be heads. Bayesians define probability as a degree of belief, updated as evidence arrives. Both are internally consistent; they answer different questions.

The practical divergence shows up in how each school handles estimation. Frequentist methods produce confidence intervals — ranges that would contain the true parameter in 95% of hypothetical replications of the experiment. This is not the same as saying there's a 95% chance the parameter is in the interval. Bayesian methods produce credible intervals — ranges where the parameter actually falls with 95% probability given the observed data and a prior. The distinction matters when you want to make claims about the specific dataset you have, not a theoretical population of experiments.

The post uses Python throughout — likely NumPy and SciPy — to show both approaches on the same estimation problem. This ground-up computation style was characteristic of the 2014 Python data science community, where Jake VanderPlas was a prominent voice pushing for accessible statistical education through code rather than textbooks.

## Key points

- Frequentist statistics: probability = long-run frequency; parameters are fixed but unknown; p-value and confidence intervals are the primary outputs.
- Bayesian inference: probability = degree of belief; parameters have distributions; posterior distribution = prior × likelihood (Bayes' theorem).
- Confidence intervals are commonly misinterpreted as credible intervals — frequentist intervals make claims about the procedure, not the specific interval computed.
- Maximum likelihood estimation (MLE) is the frequentist workhorse; maximum a posteriori estimation (MAP) is its Bayesian analogue with a prior.
- With flat (uninformative) priors, Bayesian and frequentist results often converge — the philosophical difference matters most when priors are informative or data is scarce.

[Original](http://jakevdp.github.io/blog/2014/03/11/frequentism-and-bayesianism-a-practical-intro/) → GitHub
