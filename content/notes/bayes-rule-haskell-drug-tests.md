---
title: Bayes' Rule in Haskell, or Why Drug Tests Don't Work
date: 2013-05-02
categories:
  - probability
  - bayesian-inference
  - haskell
  - statistics
  - drug-testing
description: "Classic probabilistic reasoning example using drug tests to illustrate Bayes' rule: even a highly accurate test produces mostly false positives when the base rate of drug use is low. Implemented in Haskell to make conditional probability feel like simple if-statements."
params:
  source: pinboard
  sourceUrl: http://www.randomhacks.net/articles/2007/02/22/bayes-rule-and-drug-tests
---

![Bayes' Rule in Haskell, or Why Drug Tests Don't Work](/images/notes/bayes-rule-haskell-drug-tests.png)

## Summary

This article from randomhacks.net uses workplace drug testing as the running example to make Bayes' theorem concrete and intuitive. The counterintuitive result: even a drug test that is 99% accurate (1% false positive rate, 1% false negative rate) will produce mostly false positives when the population being tested has a low base rate of drug use (say, 0.5%). If 1000 employees are tested, ~5 actually use drugs and ~10 non-users will test positive due to the 1% false positive rate — meaning about two-thirds of positive results are wrong.

The base rate fallacy (ignoring prior probability) is one of the most reliably misleading cognitive errors in probabilistic reasoning. Most people's intuition treats 99% accurate test as meaning "99% of positives are true positives" — but that conflates sensitivity (true positive rate) with positive predictive value, which depends critically on prevalence. Bayes' theorem is exactly the formula that converts between these two quantities using the prior.

The Haskell framing is clever: the author shows that Bayes' rule can be implemented as a simple conditional probability calculation that reads almost like English. This was an early example of using functional programming to make probabilistic reasoning feel natural — an idea later developed more fully in probabilistic programming languages like Church, Pyro, and Stan. The simplicity of the Haskell code makes the probability arithmetic feel less intimidating than the formula presentation.

## Key points

- Base rate neglect: the probability of a true positive depends on how common the condition is in the tested population, not just on test accuracy
- Low prevalence + moderate false positive rate = most positives are false positives — counterintuitive and practically important
- Bayes' theorem: P(drug user | positive test) = P(positive test | drug user) × P(drug user) / P(positive test)
- The positive predictive value of any test is heavily sensitive to prevalence — this applies to COVID-19 testing, cancer screening, spam filters, and fraud detection
- Haskell used to show that conditional probability update is essentially a filter on joint probabilities — the functional framing makes the mechanics transparent
- Connected to the broader case for Bayesian reasoning as a more calibrated alternative to binary hypothesis testing

[Original](http://www.randomhacks.net/articles/2007/02/22/bayes-rule-and-drug-tests)
