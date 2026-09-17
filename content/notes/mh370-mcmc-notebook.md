---
title: MH370 MCMC Notebook — Conor Myhrvold
date: 2014-03-28
categories:
  - bayesian
  - mcmc
  - data-science
  - jupyter
  - python
description: Conor Myhrvold's IPython notebook using Monte Carlo simulation to analyze the probable flight path of MH370 from satellite pings. An early high-profile example of using Bayesian inference and simulation for real-world analysis.
params:
  source: pinboard
  sourceUrl: http://nbviewer.ipython.org/github/myhrvold/MH370_MCMC/blob/master/MH370_MC_ConorMyhrvold.ipynb?create=1
---

![MH370 MCMC Notebook — Conor Myhrvold](/images/notes/mh370-mcmc-notebook.png)

## Summary

Shortly after Malaysian Airlines flight MH370 disappeared in March 2014, Conor Myhrvold published an IPython notebook using Monte Carlo simulation to analyze the probable flight path. Working from the Inmarsat satellite data that had been publicly reported — specifically the ping rings showing distances from a satellite at roughly hourly intervals — the notebook used MCMC to sample over possible flight paths consistent with the observations.

The analysis is a real-world Bayesian inference problem: given a prior over flight paths (the aircraft had to be moving at a physically plausible speed and heading) and a likelihood function over the ping data, sample from the posterior over flight paths. The notebook was notable both for the novelty of the application and for the quality of the exposition — Myhrvold walked through the probabilistic reasoning clearly in Markdown cells alongside the code.

This became one of the most-shared IPython notebooks of 2014, and represented the genre of data science as journalism — using quantitative tools to analyze breaking news rather than waiting for official reports. It also demonstrated that Jupyter notebooks (then still called IPython notebooks) were a compelling medium for communicating technical analysis to a broad audience.

## Key points

- Monte Carlo simulation over MH370 flight paths conditioned on Inmarsat satellite ping distances.
- Bayesian inference framework: prior over flight physics, likelihood from satellite data, posterior sampling.
- One of the most-shared IPython notebooks of 2014 — viral example of data-driven news analysis.
- Demonstrated that Jupyter notebooks work as a medium for communicating probabilistic reasoning.
- Satellite "ping rings" are constraint circles; MCMC samples paths consistent with all constraints.

[Original](http://nbviewer.ipython.org/github/myhrvold/MH370_MCMC/blob/master/MH370_MC_ConorMyhrvold.ipynb?create=1) → GitHub
