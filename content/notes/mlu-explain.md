---
title: "MLU-Explain: Visual ML Education"
date: 2022-05-24
categories:
  - machine-learning
  - education
  - visualization
  - interactive
description: MLU-Explain is Amazon's collection of interactive visual explainers for core machine learning concepts — decision trees, random forests, bias-variance tradeoff, cross-validation, and more. Built as interactive articles in the style of Distill.pub, targeting practitioners who want intuition over math.
params:
  source: pinboard
  sourceUrl: https://mlu-explain.github.io/
---

## Summary

[MLU-Explain](/notes/mlu-explain/) is Amazon's open-source project publishing interactive visual explainers for core machine learning concepts. The presentation style follows Distill.pub's model of interactive, scroll-driven articles that build intuition through animation and direct manipulation — you can adjust parameters and watch how the concept changes rather than just reading about it.

Topics covered include bias-variance tradeoff, decision trees, random forests, cross-validation, train-test splits, linear regression, logistic regression, and more. Each explainer aims to be self-contained and accessible — the target reader knows some Python and statistics but might not have deep ML theory. The visual explanations make concepts like overfitting (watching a polynomial curve memorize training points) or the confusion matrix (seeing TP/FP/TN/FN cells populate as you adjust the decision threshold) click in ways that prose alone can't.

The project sits in the same space as 3Blue1Brown's neural network videos and Andrej Karpathy's micrograd tutorial — education through visualization rather than textbook exposition. What distinguishes [MLU-Explain](/notes/mlu-explain/) is the interactive component: readers control the demonstrations, which forces engagement rather than passive reading. Amazon released it as a public resource under their Machine Learning University program.

## Key points

- Interactive articles on bias-variance tradeoff, decision trees, random forests, cross-validation, confusion matrix, and more
- Built with D3.js for interactive visualizations — each article is a standalone scrollytelling piece
- Distill.pub style applied to practical ML education rather than research communication
- Amazon's Machine Learning University (MLU) resource — open-sourced and available without enrollment
- Related resources: Distill.pub, 3Blue1Brown neural network videos, Seeing Theory (probability), [Jay Alammar](/notes/jay-alammar/) transformer visualizations
- Pairs well with HuggingFace courses for moving from conceptual to hands-on

[Original](https://mlu-explain.github.io/)
 → GitHub
