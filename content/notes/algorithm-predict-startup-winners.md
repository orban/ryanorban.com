---
title: An Algorithm to Pick Startup Winners
date: 2012-07-10
categories:
  - startups
  - machine-learning
  - venture-capital
  - prediction
  - data-science
description: MIT Technology Review's 2012 piece on early attempts to predict startup success algorithmically — using team composition, funding history, and network signals. The prediction accuracy was modest; the methodological interest was in what features correlated with outcomes.
params:
  source: pinboard
  sourceUrl: http://www.technologyreview.com/news/428427/an-algorithm-to-pick-startup-winners/
---

![An Algorithm to Pick Startup Winners](/images/notes/algorithm-predict-startup-winners.png)

## Summary

MIT Technology Review's 2012 piece covered early research into predicting startup success using machine learning — primarily analyzing angel investment and seed funding records from CrunchBase and similar sources. The researchers applied standard classification algorithms to historical funding data, trying to identify what features predicted whether a startup would achieve a successful exit (IPO or acquisition above a threshold) vs. fail or stay private indefinitely.

The feature set reflected what was observable in structured data: team size, founder backgrounds, geography, industry sector, amount raised, number of investors, time between funding rounds. The accuracy was modest — better than random, but not dramatically so. The interesting finding wasn't the prediction accuracy itself but which features correlated most strongly: team composition and previous founder experience mattered more than sector or geography in most models. This aligned with conventional VC wisdom but gave it quantitative weight.

The deeper issue, which the piece touched on, is survivorship and selection bias. CrunchBase data in 2012 skewed toward funded companies that had chosen to publicize themselves — the sample wasn't representative of all startups. Failure modes were undercounted. The companies that failed quietly, returned investors nothing, and never made news are systematically underrepresented. Any model trained on this data would overestimate success rates and miss the features that predict failure.

## Key points

- Early ML on startup outcome prediction (2012): logistic regression + decision trees on CrunchBase funding data — team composition proved the strongest predictor.
- Survivorship bias problem: publicly-tracked funded startups are a selected, non-representative sample — failure is systematically undercounted in the training data.
- Results: better than random prediction on held-out data, but not dramatically so — consistent with how hard startup prediction remains even for experienced VCs.
- The feature importance finding (team experience > sector, geography) gave data support to "bet on the jockey not the horse" conventional wisdom.
- Methodologically adjacent to later quantitative VC approaches: SignalFire, Correlation Ventures, and others built fund strategies partly on similar pattern-matching.

[Original](http://www.technologyreview.com/news/428427/an-algorithm-to-pick-startup-winners/)
