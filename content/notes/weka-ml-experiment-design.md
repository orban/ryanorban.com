---
title: Design and Run Your First Experiment in Weka
date: 2014-02-25
categories:
  - machine-learning
  - weka
  - model-evaluation
  - cross-validation
  - tools
description: Jason Brownlee's Machine Learning Mastery guide to designing and running experiments in Weka — the GUI-based ML tool from Waikato. Shows how to set up proper comparative experiments with statistical testing, not just running one algorithm.
params:
  source: pinboard
  sourceUrl: http://machinelearningmastery.com/design-and-run-your-first-experiment-in-weka/
---

## Summary

Jason Brownlee at [Machine Learning Mastery](/notes/machine-learning-mastery/) used Weka as the vehicle for teaching systematic machine learning experiment design. Weka (Waikato Environment for Knowledge Analysis) is a Java-based GUI tool from the University of Waikato in New Zealand that makes it possible to run ML experiments without writing code — load a dataset, select algorithms, configure evaluation settings, and compare results through a graphical interface.

The experiment design framing is deliberate: most beginner ML tutorials show how to run one algorithm on a dataset. The harder lesson is setting up a *fair comparison* across algorithms. This means using the same cross-validation folds for all algorithms (so differences in performance come from the algorithm, not from lucky/unlucky data splits), running multiple replication folds to estimate variance, and applying statistical significance tests (typically a paired t-test) to distinguish real performance differences from noise.

Weka's Experimenter interface supports this workflow: you define a list of classifiers and datasets, configure evaluation (e.g., 10-fold cross-validation repeated 10 times), run all combinations, and then load results into the Analyser which runs pairwise statistical tests and marks statistically significant differences with up/down arrows. This is the kind of rigorous comparison that machine learning researchers expected in papers — a useful standard to bring to applied work.

## Key points

- Weka: Java GUI ML tool — no coding required for standard classification, regression, and clustering experiments on tabular data.
- Proper experimental design: same CV folds across all algorithms, multiple replications, paired statistical tests — not just "algorithm A got 87%, algorithm B got 85%."
- Weka Experimenter: the evaluation harness built into Weka — configure, run, and compare many algorithm/dataset combinations systematically.
- Corrected paired t-test: statistical test designed for repeated cross-validation (accounts for the correlation between folds from the same dataset).
- Weka was a dominant ML education tool before scikit-learn democratized the Python API — still used in ML courses that want to separate algorithm concepts from programming.

[Original](http://machinelearningmastery.com/design-and-run-your-first-experiment-in-weka/)
