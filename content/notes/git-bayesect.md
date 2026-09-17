---
title: "git_bayesect: Bayesian git bisect for flaky tests"
date: 2026-04-01
categories:
  - developer-tools
  - git
  - bayesian-inference
  - debugging
  - python
description: Bayesian git bisect for flaky tests. Finally a way to handle probabilistic failures that standard bisect can't.
params:
  source: pinboard
  sourceUrl: https://github.com/hauntsaninja/git_bayesect
---

![git_bayesect: Bayesian git bisect for flaky tests](/images/notes/git-bayesect.png)

## Summary

[git_bayesect](/notes/git-bayesect/) is a Python tool by hauntsaninja (Shantanu) that applies Bayesian inference to the problem of git bisect. Standard bisect requires deterministic pass/fail outcomes, which breaks down when you're hunting for a commit that made a flaky test worse rather than introducing a clean failure. git_bayesect handles this probabilistic case by treating test outcomes as observations drawn from an unknown distribution and inferring where the underlying failure rate shifted.

The core algorithm uses greedy minimization of expected entropy to pick which commit to test next, squeezing maximum information from each run. It relies on a Beta-Bernoulli conjugacy trick to keep the posterior probability calculations tractable even though the actual failure rates on either side of the change point are unknown. You don't need to specify parameters upfront -- just run tests and let the model update its beliefs.

The project is MIT-licensed, installable via pip or uv, and ships with a demo synthetic repo containing a deliberately flaky script so you can see the bisection process in action.

## Key points

- Solves the specific problem of finding commits that change the *probability* of failure, not just commits that introduce deterministic bugs -- a gap that standard git bisect can't address.
- Uses information theory (expected entropy minimization) to select the most informative commit to test at each step, making the search efficient even with noisy observations.
- The Beta-Bernoulli conjugacy trick makes the Bayesian inference math tractable without requiring the user to guess failure rates in advance.
- Written in Python, integrates with existing Git workflows, and installs with a single `pip install` or `uv` command.
- Detailed mathematical explanation available on the author's blog for those who want to understand the theory behind the approach.

[Original](https://github.com/hauntsaninja/git_bayesect)
