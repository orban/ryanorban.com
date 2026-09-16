---
title: Interpretable Machine Learning
date: 2022-01-31
categories:
  - machine-learning
  - interpretability
  - explainability
  - book
  - open-access
description: Christoph Molnar's free online book covering the theory and practice of interpretable machine learning — from inherently interpretable models (decision trees, linear regression) to post-hoc methods (SHAP, LIME, counterfactuals). The standard reference for understanding and explaining ML model behavior.
params:
  source: pinboard
  sourceUrl: https://christophm.github.io/interpretable-ml-book/
---

## Summary

[Interpretable Machine Learning](/notes/interpretable-machine-learning/) is a free online book by Christoph Molnar that covers the full landscape of techniques for understanding and explaining machine learning model predictions. As models have become more capable and more consequential, understanding why they produce specific outputs has become as important as the outputs themselves — this book is the standard reference for that problem.

The book distinguishes between inherently interpretable models — decision trees, linear regression, rule-based models — and post-hoc explanation methods applied to black-box models. The post-hoc methods include both local approaches like LIME (approximating a complex model locally with a simpler one) and SHAP values (Shapley values from game theory, distributing prediction credit among features), and global methods like partial dependence plots and feature importance.

For neural networks specifically, the book covers saliency maps, concept-based explanations, and adversarial examples. The 3rd edition added chapters on LOFO (Leave-One-Feature-Out) importance and Ceteris Paribus profiles. The critical stance throughout — evaluating each method's weaknesses as well as strengths — makes it more useful than a pure tutorial.

## Key points

- Distinguishes inherently interpretable models (decision trees, linear models) from post-hoc explainability applied to black-boxes.
- SHAP values (Shapley-based) provide theoretically sound feature attribution; LIME provides local approximations for individual predictions.
- Partial dependence plots and feature importance reveal global model behavior; counterfactual explanations show what would need to change to get a different prediction.
- For deep learning, saliency maps and concept detection methods offer gradient-based interpretations.
- Critical evaluation of each method — not just how they work, but when they mislead — makes this the most trustworthy reference in the space.
- Freely available online at the URL above; also available as a print book.

[Original](https://christophm.github.io/interpretable-ml-book/) → GitHub
