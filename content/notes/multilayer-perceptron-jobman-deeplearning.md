---
title: Multilayer Perceptron with Jobman
date: 2014-02-11
categories:
  - deep-learning
  - neural-networks
  - theano
  - mlp
  - research-tools
description: Deeplearning.net tutorial on training a multilayer perceptron using Jobman — a job scheduling system from the Montreal LISA Lab for running batches of hyperparameter experiments. Shows the infrastructure behind systematic deep learning research in 2014.
params:
  source: pinboard
  sourceUrl: http://deeplearning.net/software/jobman/mlp_jobman.html#mlp-jobman
---

## Summary

This tutorial from deeplearning.net (the website of the LISA Lab at Université de Montréal, home of Yoshua Bengio's group) shows how to train a multilayer perceptron (MLP) using Jobman, a job management system designed for running systematic hyperparameter search experiments. The combination reflects the research workflow at LISA Lab in 2013-2014: Theano for GPU-accelerated neural network computation, Jobman for orchestrating parallel experiments, and deeplearning.net as the public documentation and tutorial site.

Jobman (also called Jobdispatch) solves the experiment management problem: you have a grid of hyperparameter combinations to try (learning rate, hidden layer sizes, regularization strengths, activation functions), and you want to run them in parallel across multiple GPUs or cluster nodes, track which have completed, and retrieve results. Without such tooling, researchers kept manual spreadsheets — Jobman was an early answer to what MLflow and Weights & Biases later solved more comprehensively.

The multilayer perceptron tutorial itself covers: stacking fully-connected layers with sigmoid or tanh activations, training with stochastic gradient descent (SGD), and applying L1/L2 regularization and dropout to reduce overfitting. These are foundational concepts that remain unchanged — the 2014-era MLP in Theano code differs only in ergonomics from a 2024-era MLP in PyTorch.

## Key points

- Jobman: LISA Lab's experiment scheduler — submits hyperparameter configurations as jobs, tracks completion, retrieves results. The research-grade predecessor to MLflow.
- Theano as the substrate: symbolic computation library that compiled mathematical expressions to CUDA GPU code — the framework used at LISA Lab before TensorFlow and PyTorch.
- Multilayer perceptron: the foundational deep learning architecture — stacked linear transformations with nonlinear activation functions.
- Hyperparameter search in 2014: typically grid search over a manual configuration space — random search and Bayesian optimization were known but less common.
- The LISA Lab produced foundational deep learning work: Yoshua Bengio, Aaron Courville, Ian Goodfellow all trained or worked there.

[Original](http://deeplearning.net/software/jobman/mlp_jobman.html#mlp-jobman)
