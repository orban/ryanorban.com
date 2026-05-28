---
title: Why I'm Not a Fan of R-Squared
date: 2016-07-24
categories:
  - statistics
  - data-science
  - regression
  - model-evaluation
  - mathematics
description: John Myles White's argument that R-squared is a misleading metric for regression model quality — it conflates the variance of x with model fit and can be gamed. A clean critique that every data scientist who uses linear regression should read.
params:
  source: pinboard
  sourceUrl: http://www.johnmyleswhite.com/notebook/2016/07/23/why-im-not-a-fan-of-r-squared/
---

![Why I'm Not a Fan of R-Squared](/images/notes/why-not-fan-r-squared.png)

## Summary

John Myles White — statistician and Julia contributor — makes a pointed case against over-relying on R-squared (the coefficient of determination) as a model quality metric. The argument is that R² is not a pure measure of fit: it depends heavily on the variance of the predictor variables. A model that explains the same fraction of variance in the data will report a higher R² when the predictors are spread over a wide range and a lower R² when they're clustered — even if the model's actual predictive accuracy is identical.

The core issue is that R² = 1 - (SS_residual / SS_total), and SS_total depends on the variance of the outcome variable in your sample. If you collect data over a narrow range of predictor values (restricted range), SS_total shrinks, SS_residual stays similar, and R² drops even though nothing about the model changed. Conversely, you can inflate R² by sampling widely in the predictor space. This makes R² a poor choice for comparing models across datasets or experimental designs.

White's preferred alternatives depend on the goal: for comparing across samples, root mean squared error (RMSE) or mean absolute error (MAE) are invariant to the predictor variance; for understanding explained variance relative to baseline, the comparison should be made explicitly rather than baked into a single number. This critique complements the more famous Anscombe's Quartet argument that summary statistics alone can hide dramatically different underlying relationships.

## Key points

- R-squared conflates model fit with predictor variance — the same model reports different R² depending on how widely you sampled the predictor.
- SS_total (the denominator) changes with sample composition, making R² non-comparable across studies or experimental designs.
- Restricted range inflates or deflates R² without any change to the model's actual predictive accuracy.
- Better alternatives: RMSE and MAE for prediction accuracy; explicit variance decomposition for explaining "how much does this variable matter."
- John Myles White is a statistician known for advocating rigorous quantitative thinking over statistical convention — also contributed to Julia language development.

[Original](http://www.johnmyleswhite.com/notebook/2016/07/23/why-im-not-a-fan-of-r-squared/)
