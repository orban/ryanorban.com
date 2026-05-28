---
title: A Multi-Level Bayesian Analysis of Racial Bias in Police Shootings
date: 2016-07-08
categories:
  - statistics
  - bayesian
  - racial-bias
  - policing
  - research
description: A PLOS ONE paper applying multi-level Bayesian hierarchical models to police shooting data across US counties from 2011–2014, finding significant racial disparities in lethal force use. Notable for applying rigorous statistical methods to a politically charged dataset.
params:
  source: pinboard
  sourceUrl: http://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0141854
---

![A Multi-Level Bayesian Analysis of Racial Bias in Police Shootings](/images/notes/bayesian-racial-bias-police-shootings.png)

## Summary

This PLOS ONE paper by Johnson, Tress, Burkel, Taylor, and Larson analyzes police shooting records from 2011-2014 across US counties using Bayesian hierarchical models. The research question: after controlling for county-level crime rates, demographics, and socioeconomic factors, is there evidence of racial bias in police use of lethal force?

The analytical approach is methodologically careful — a multi-level Bayesian model that accounts for the fact that counties are nested within states, that crime rates vary enormously across jurisdictions, and that small counties have high variance in shooting rates (a low absolute number of incidents means any given year could look extreme). Using Bayesian inference rather than frequentist methods allowed the authors to propagate uncertainty properly through the hierarchical structure and produce posterior distributions for the bias estimates rather than single point estimates.

The findings showed disparities in officer-involved shootings at the county level after controlling for these factors, with Black civilians at elevated risk of being shot relative to White civilians. The paper contributed to the empirical literature on policing and race during a period (2014-2016) when high-profile police shootings and the Black Lives Matter movement had made the topic intensely public. One important caveat: the paper uses officer-involved shooting records from a specific database, and underreporting is a significant known issue — deaths not recorded as police-involved would bias results.

## Key points

- Bayesian hierarchical model with county-level nesting — propagates uncertainty across jurisdictions rather than treating each county independently.
- Controls for local crime rates, demographics, and socioeconomic factors before estimating racial disparity.
- Found elevated risk of police shooting for Black civilians at county level after controls — a pattern consistent across multiple model specifications.
- Data limitations: officer-involved shooting databases had significant underreporting in 2011-2014; later work used more complete data sources.
- Published in PLOS ONE (open access) during the peak of Black Lives Matter public discourse — 2016 was also the year FiveThirtyEight was publishing its own analyses.

[Original](http://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0141854)
