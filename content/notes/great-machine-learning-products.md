---
title: Great Machine Learning Products
date: 2012-04-16
categories:
  - machine-learning
  - product-design
  - ai
  - ux
  - data-products
description: O'Reilly Radar's 2012 analysis of what distinguishes great machine learning products from mediocre ones — written during the pre-deep-learning ML era when practitioners were figuring out how to ship ML-powered features users would actually trust and use.
params:
  source: pinboard
  sourceUrl: http://radar.oreilly.com/2012/04/great-machine-learning-products.html
---

## Summary

This O'Reilly Radar piece from 2012 examines what makes machine learning-powered products good — a question that was less crowded then than it would become after deep learning took over. In 2012, ML in products typically meant recommendation systems, spam filters, search ranking, and fraud detection — all areas where the model's output was visible to users and trust was critical.

The central design challenge for ML products is that the model is probabilistic and users are not. A system that is right 95% of the time looks great statistically and feels broken to users who experience the 5% failures. This asymmetry means that error handling and graceful degradation matter as much as model accuracy — what happens when the model is wrong matters as much as how often it's right.

The piece also touches on the feedback loop problem: ML models improve with data, but getting good labeled data often requires users to interact with the product in ways they won't if the product isn't good yet. This cold start problem for machine learning products is related to but distinct from the network effect cold start — you need enough data to have a good model, but you need a good model to get the data.

## Key points

- Great ML products invest in how they handle errors, not just how often they're right — the failure mode matters as much as the accuracy number.
- Users need feedback mechanisms to understand what the system knows and doesn't, and to correct mistakes — passive ML is less trusted than interactive ML.
- The cold start problem for ML is getting labeled data without a working product; most successful approaches involve hybrid human-machine systems initially.
- Model confidence should be surfaced to users in appropriate ways — we think you'll like this means something different than you'll definitely like this.
- 2012 was the inflection point: consumer ML was becoming common enough that product thinking about ML was necessary, not just algorithm thinking.

[Original](http://radar.oreilly.com/2012/04/great-machine-learning-products.html)
