---
title: An Introduction to Gradient Descent and Linear Regression
date: 2014-06-26
categories:
  - machine-learning
  - optimization
  - gradient-descent
  - linear-regression
  - tutorial
description: A clear walkthrough of gradient descent applied to linear regression, with code — a good foundational tutorial connecting the mathematical update rule to a concrete implementation. One of the most-linked introductions to the algorithm for newcomers to ML.
params:
  source: pinboard
  sourceUrl: http://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/
---

## Summary

This Atomic Object blog post walks through gradient descent as the optimization algorithm underlying linear regression and, by extension, most of machine learning. The approach is pedagogical: start with a cost function (mean squared error), derive the gradient analytically, then implement the iterative update rule in code. The result is a working linear regression trained from scratch in under 50 lines.

Gradient descent works by computing the partial derivative of the loss function with respect to each parameter, then nudging each parameter in the direction that reduces the loss. The step size is controlled by the learning rate (α), which is the most sensitive hyperparameter: too large and the updates overshoot and diverge; too small and training is prohibitively slow. The post visualizes the cost surface as a bowl, with each gradient step rolling downhill toward the minimum.

For linear regression specifically, the cost surface is convex — there's a single global minimum and gradient descent will always find it given a suitable learning rate. This makes it a clean teaching example. Most real neural network cost surfaces are non-convex, but the same update rule applies, and the intuition from the linear case transfers directly.

## Key points

- Gradient descent is the engine behind training almost every parametric machine learning model — understanding it here transfers to neural networks, logistic regression, and beyond.
- The gradient of MSE w.r.t. weights has a closed-form — which is why linear regression can also be solved exactly via the normal equations, without iterative descent.
- Batch gradient descent uses all training examples per update; stochastic gradient descent uses one; mini-batch gradient descent uses a small subset — the practical default.
- Learning rate tuning is manual art or automated via schedules (cosine annealing, warm restarts) or adaptive optimizers like Adam optimizer and RMSProp.
- Feature scaling (standardization or normalization) dramatically speeds convergence by making the cost surface more symmetric.

[Original](http://spin.atomicobject.com/2014/06/24/gradient-descent-linear-regression/)
