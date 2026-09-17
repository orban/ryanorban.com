---
title: "Target Practice: The Power of Predictive Analytics"
date: 2013-07-29
categories:
  - predictive-analytics
  - retail
  - data-science
  - privacy
  - machine-learning
description: Forbes coverage of Target's predictive analytics program — the famous pregnancy prediction story that showed retail chains could infer major life events from purchase patterns. A case study in both the power and the social friction of behavioral prediction at scale.
params:
  source: pinboard
  sourceUrl: http://www.forbes.com/sites/rahimkanani/2013/07/29/target-practice-the-power-of-predictive-analytics/
---

![Target Practice: The Power of Predictive Analytics](/images/notes/target-predictive-analytics-forbes.png)

## Summary

This Forbes piece covers Target's predictive analytics program, which became one of the most-cited examples of retail machine learning in the early 2010s. The original story — broken by Charles Duhigg at the New York Times in 2012 — revealed that Target's data science team had built a pregnancy prediction model that assigned every customer a pregnancy score based on purchases like unscented lotion, calcium supplements, and large bags of cotton balls. The model was accurate enough to predict due dates within a short window, enabling Target to market baby products at exactly the moment new parents are forming long-term brand loyalties.

The reason this story traveled so widely: it arrived before most people had internalized what behavioral prediction at retail scale looked like. The Target statistician Andrew Pole had built a model demonstrating that subtle purchase pattern shifts in the second trimester were more predictive of an impending birth than an explicit baby registry. The friction this created — a father receiving coupons for infant gear before his daughter had told him she was pregnant — revealed the gap between what companies could infer and what customers expected.

The business logic behind this was sound: new-parent households represent one of the most valuable acquisition moments in retail, since shopping patterns are in flux and brand loyalty is up for grabs. Predictive analytics here wasn't academic — it drove revenue. The privacy implications foreshadowed a decade of debates about what's appropriate to infer, store, and act on from behavioral data.

## Key points

- Target's pregnancy prediction model used ~25 signals including purchase of unscented products, vitamin supplements, and nesting behavior to assign a pregnancy score without ever asking.
- Andrew Pole, Target's statistician, built this to capture the lucrative new-parent demographic at a moment of maximum brand-loyalty malleability.
- The ethical tension: inference from behavioral data can surface information people haven't disclosed — and act on it before they're ready to acknowledge it publicly.
- Predictive modeling in retail was proven as a revenue driver by 2013; the debate shifted to what models *should* do rather than what they *can* do.
- This story was a canonical example cited in every data science course as a real-world case where model accuracy and human values weren't aligned.

[Original](http://www.forbes.com/sites/rahimkanani/2013/07/29/target-practice-the-power-of-predictive-analytics/)
