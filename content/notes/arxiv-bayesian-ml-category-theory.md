---
title: Bayesian Machine Learning via Category Theory
date: 2013-12-10
categories:
  - bayesian
  - category-theory
  - machine-learning
  - mathematics
  - arxiv
description: Culbertson and Sturtz's 2013 paper applying category theory to Bayesian machine learning — using the Kleisli category of the Giry monad to formalize supervised learning, stochastic processes as priors, and the Kalman filter. Heavy theory, but part of the broader push to give probabilistic ML rigorous foundations.
params:
  source: pinboard
  sourceUrl: http://arxiv.org/pdf/1312.1445v1.pdf
---

## Summary

This 2013 arxiv paper by Jared Culbertson and Kirk Sturtz applies category theory to provide a mathematical framework for Bayesian machine learning. The vehicle is the Kleisli category of the Giry monad — a categorical construction that models conditional probability distributions as morphisms. This allows supervised learning to be formulated abstractly: data, parameters, and predictions become objects, and inference maps become arrows between them.

The key contribution is showing how stochastic processes can serve as prior probability distributions (as arrows to function spaces), and that the resulting inference maps can often be constructed analytically within a symmetric monoidal weakly closed category. The Kalman filter emerges as a concrete example within this framework — it's the canonical example of a Hidden Markov Model in the categorical setting.

The paper is 74 pages and requires comfort with both category theory and Bayesian inference. It represents the ongoing project of grounding probabilistic ML in rigorous abstract algebra — relevant to those interested in probabilistic programming foundations and the theoretical underpinnings of Bayesian methods.

## Key points

- Uses the Kleisli category of the Giry monad to model conditional probability: morphisms are probability kernels, not just functions.
- Formalizes both parametric and nonparametric Bayesian inference on function spaces using categorical constructions.
- Stochastic processes as arrows to function spaces → prior distributions in supervised learning.
- Kalman filter as a worked example: a concrete Hidden Markov Model in the categorical framework.
- Connects to probabilistic programming research — this mathematical foundation underlies systems like Church and Gen.
- 74-page paper: accessible if you know both category theory and probability theory.

[Original](http://arxiv.org/pdf/1312.1445v1.pdf)
