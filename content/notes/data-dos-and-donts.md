---
title: "Data Do's and Don'ts: Lessons from the Front Line"
date: 2016-04-25
categories:
  - data-science
  - best-practices
  - talk
  - lessons-learned
  - career
description: Domino Data Lab's 'Data Do's and Dont's' slides from Data Popup Austin — practical lessons from working data scientists about what actually goes wrong in production ML and analytics projects. A practitioner's guide to avoiding common pitfalls.
params:
  source: pinboard
  sourceUrl: http://www.slideshare.net/dominodatalab/data-science-popup-austin-data-dos-and-donts-lessons-from-the-front-line
---

## Summary

This Domino Data Lab talk from Data Popup Austin is the kind of practitioner knowledge that doesn't make it into textbooks: what actually goes wrong when data science hits production. The front line framing emphasizes hard-won lessons over theory — the mistakes that practicing data scientists make repeatedly until they learn not to.

Common patterns in talks like this from the 2015-2016 era: the gap between notebook code and production code (models that work in Jupyter notebooks but break when deployed); the perils of data leakage (accidentally using future information during model training, leading to unrealistically optimistic validation metrics); communication failures with stakeholders (presenting uncertainty incorrectly, overselling model confidence); and reproducibility failures (running experiments without recording seeds, library versions, or data snapshots).

Domino Data Lab was a platform specifically for reproducible data science — the company had strong opinions about these practices because their product addressed them. Their talks at conferences like Data Popup were essentially articulating the problem space their product solved. Both slides (SlideShare) and video (Vimeo) versions were bookmarked simultaneously, suggesting the original share was of the video with the slides linked.

## Key points

- Notebook-to-production gap: code that works interactively often breaks when deployed or shared.
- Data leakage: most insidious pitfall — future information in training data inflates validation metrics.
- Reproducibility: models are worthless if you can't reproduce them — version data, code, environment.
- Stakeholder communication: presenting predictions without appropriate uncertainty leads to trust failures.
- Domino Data Lab context: the talk directly articulates the problems their reproducibility platform solves.

[Slides](http://www.slideshare.net/dominodatalab/data-science-popup-austin-data-dos-and-donts-lessons-from-the-front-line) | [Video](https://vimeo.com/163292131)
