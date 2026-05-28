---
title: Bayesian Statistical Analysis with PyMC
date: 2013-11-13
categories:
  - bayesian
  - statistics
  - pymc
  - python
  - mcmc
description: PyTennessee 2013 presentation on Bayesian statistical analysis with PyMC — introducing probabilistic programming in Python as a practical alternative to frequentist methods. PyMC let practitioners write down generative models and get MCMC inference without implementing samplers from scratch.
params:
  source: pinboard
  sourceUrl: http://preview.getprismatic.com/story/1384292949221?share=true
---

![Bayesian Statistical Analysis with PyMC](/images/notes/bayesian-statistical-analysis-pymc.png)

## Summary

This PyTennessee 2013 conference presentation introduced Bayesian statistical analysis using PyMC — a Python library for probabilistic programming that lets you define generative models and run MCMC (Markov Chain Monte Carlo) inference without implementing sampling algorithms yourself. PyMC2 was the primary version in 2013; PyMC3 (with Theano backend and NUTS sampler) came in 2015, and PyMC (v4+) migrated to Aesara/PyTensor.

The central appeal of PyMC for applied data scientists: write down the model you believe generated your data (priors, likelihood), call `pm.sample()`, and get posterior samples back. You don't need to derive analytical posteriors (often intractable) or implement a sampler (complex and error-prone). The abstraction brings Bayesian inference to practitioners who understand the statistical concepts but don't want to implement Metropolis-Hastings or Hamiltonian Monte Carlo by hand.

The 2013 timing is notable: this is the era when probabilistic programming was becoming practical for applied users. Allen Downey's *Think Bayes* (2012) and Cam Davidson-Pilon's *Bayesian Methods for Hackers* (written in 2013 using PyMC) were the accessible entry points for the same audience.

## Key points

- PyMC: probabilistic programming in Python — define model → sample from posterior with MCMC.
- Frees practitioners from deriving intractable analytical posteriors or implementing samplers manually.
- Key workflow: specify priors and likelihood → `pm.sample()` → analyze posterior trace.
- MCMC in PyMC: Metropolis-Hastings sampler in PyMC2; NUTS (No-U-Turn Sampler) in PyMC3 dramatically improved efficiency.
- Context: 2013 was the moment Bayesian methods were becoming accessible to Python data scientists, not just statisticians.
- Related resources: *Bayesian Methods for Hackers* by Cam Davidson-Pilon (free online, uses PyMC2/3 throughout).

[Original](http://preview.getprismatic.com/story/1384292949221?share=true)
