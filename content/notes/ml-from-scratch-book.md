---
title: Machine Learning from Scratch
date: 2020-09-01
categories:
  - machine-learning
  - mathematics
  - education
  - algorithms
  - textbook
description: Machine Learning from Scratch is a free online book deriving seven core ML algorithms from first principles — linear regression, logistic regression, naive Bayes, decision trees, ensembles, and neural networks. Mathematically rigorous, aimed at practitioners who want to understand how algorithms work mechanistically.
params:
  source: pinboard
  sourceUrl: https://dafriedman97.github.io/mlbook/content/introduction.html
---

![Machine Learning from Scratch](/images/notes/ml-from-scratch-book.png)

## Summary

Machine Learning from Scratch by Daniel Friedman is a free open-source textbook that derives seven core machine learning algorithms from mathematical first principles, then implements each in Python. The goal is mechanistic understanding — not just knowing that gradient descent minimizes a loss, but being able to derive why it works from calculus. Each chapter follows a consistent structure: concept (mathematical derivation), construction (implementation design), and code (working Python).

The algorithms covered are: ordinary linear regression, linear regression extensions (regularization), logistic regression, Naive Bayes, decision trees, tree ensemble methods (Random Forest, Gradient Boosting), and neural networks. These span the core of classical supervised learning — the selection is deliberately focused rather than encyclopedic.

Prerequisites are modest by textbook standards: calculus (derivatives, chain rule), basic probability theory, and linear algebra fundamentals. The book includes an appendix reviewing the necessary mathematical background. The target reader has some modeling experience (knows what a model is, has run sklearn) but wants to understand what's happening inside the black box.

## Key points

- Deriving algorithms from scratch builds intuition that survives encountering new variations — if you understand why MSE leads to the normal equations, you can adapt when the loss function changes.
- The normal equations solution to linear regression (closed form) vs. gradient descent — the book explains both and when each is practical.
- The treatment of decision trees from impurity metrics through recursive splitting gives a foundation for understanding why Random Forest and Gradient Boosting work.
- Free and open-source — hosted on GitHub Pages, so it's always accessible without paywall.
- Complementary resource: The Elements of Statistical Learning (ESL) for more theoretical depth; Hands-On ML with Scikit-Learn for practical application depth.

[Original](https://dafriedman97.github.io/mlbook/content/introduction.html)
