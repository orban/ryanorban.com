---
title: Why You Should Be Spot-Checking Algorithms on Your Machine Learning Problems
date: 2014-02-07
categories:
  - machine-learning
  - model-selection
  - experimentation
  - workflow
  - best-practices
description: Jason Brownlee's Machine Learning Mastery argument for spot-checking — trying 10-15 algorithms quickly on a new dataset before committing to tuning any single one. Saves time by letting the data tell you which algorithm families are worth investing in.
params:
  source: pinboard
  sourceUrl: http://machinelearningmastery.com/why-you-should-be-spot-checking-algorithms-on-your-machine-learning-problems/
---

## Summary

Jason Brownlee's post on [Machine Learning Mastery](/notes/machine-learning-mastery/) makes the case for spot-checking as the starting point of any new ML project. The default mistake: pick an algorithm you like or know well, spend time tuning it, and declare it your model. The spot-checking approach: try 10-15 algorithms from different families (linear models, tree-based models, kernel methods, instance-based learners, ensemble methods) with default parameters and compare their untuned performance first.

The rationale is empirical rather than theoretical. You can't know in advance whether a linear model or a nonlinear model will work better on a given dataset without looking at the data. Tree-based methods might dominate because the features have threshold structure. Linear models might dominate because the decision boundary is roughly linear. K-nearest neighbors might dominate because the data has local cluster structure. Spot-checking gets you signal on algorithm families before investing in hyperparameter tuning.

The implementation is straightforward in scikit-learn: define a list of estimators, run the same k-fold cross-validation on each, collect mean accuracy and standard deviation, rank by performance. This gives you a horse race — not a final answer, but direction. Algorithms in the top 2-3 are candidates for tuning; the others are eliminated early. This workflow respects the principle that algorithm selection is part of the modeling problem, not something you should pre-decide.

## Key points

- Spot-checking: evaluate many algorithm families quickly with default settings before tuning any — let the data reveal which approach is promising.
- Algorithm families to spot-check: linear (logistic regression, linear SVM, ridge), tree-based (decision tree, random forest, gradient boosting), kernel (RBF SVM), instance-based (KNN), ensemble (bagging, boosting).
- Use cross-validation throughout spot-checking — not the test set. The test set is for final evaluation only.
- Spot-checking in scikit-learn: loop over estimators, call `cross_val_score`, collect results — 10 lines of code.
- Once you have a shortlist, hyperparameter tuning via `GridSearchCV` or `RandomizedSearchCV` makes sense; before that shortlist exists, it wastes time.

[Original](http://machinelearningmastery.com/why-you-should-be-spot-checking-algorithms-on-your-machine-learning-problems/)
