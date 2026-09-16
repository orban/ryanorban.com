---
title: Audience Modeling and Customer Lifetime Value 101
date: 2014-05-13
categories:
  - marketing
  - data-science
  - customer-lifetime-value
  - audience-modeling
  - predictive-analytics
description: A primer on audience modeling and customer lifetime value for digital marketers — explaining how CLV models work and how they connect to targeting and bidding decisions. Bridges the gap between ML modeling and marketing strategy.
params:
  source: pinboard
  sourceUrl: http://marketingland.com/audiences-modeling-customer-lifetime-value-101-83105
---

## Summary

This Marketing Land piece introduces customer lifetime value (CLV) modeling in the context of audience modeling for digital advertising — connecting the statistical problem to the business decision it supports. The core argument: rather than optimizing for immediate conversion, advertisers should bid based on the predicted long-run value of acquiring a given user. A user with a high predicted CLV is worth paying more to acquire.

Customer lifetime value is typically modeled as the net present value of future purchases, discounted by time. The simplest formula is CLV = average order value × purchase frequency × customer lifespan. More sophisticated approaches use survival analysis to model churn, RFM analysis (recency, frequency, monetary value) as features, or hazard models that predict the probability distribution of future purchase timing.

Audience modeling in this context means building lookalike models — finding users who resemble your high-CLV customers in their behavioral and demographic features. This turns CLV modeling into a classification problem: score new users by similarity to known high-value customers and bid proportionally. The connective tissue between statistical modeling and ad spend allocation is the key insight.

## Key points

- Customer lifetime value = NPV of future purchases — a model output, not a measurement, which requires churn prediction and purchase frequency modeling.
- RFM analysis (recency, frequency, monetary value) is the simple feature set for CLV models — computable from transaction history, widely predictive.
- Lookalike modeling extends CLV from existing customers to prospects: find users who look like your best customers in feature space, bid up their acquisition cost.
- Survival analysis / hazard models give probabilistic churn predictions — more principled than threshold-based churn classifiers.
- The feedback loop matters: CLV models trained on acquired customers are biased by past targeting decisions — a form of selection bias to account for.

[Original](http://marketingland.com/audiences-modeling-customer-lifetime-value-101-83105)
