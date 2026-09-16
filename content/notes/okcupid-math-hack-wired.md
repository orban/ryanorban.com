---
title: How a Math Genius Hacked OkCupid to Find True Love
date: 2014-01-22
categories:
  - data-science
  - k-means
  - collaborative-filtering
  - okcupid
  - applied-ml
description: Chris McKinlay scraped OkCupid, clustered female users with k-means, and optimized his profile to score high compatibility across all clusters — then met his wife through the resulting message flood. A crowd-pleasing 2014 story about data science applied to dating.
params:
  source: pinboard
  sourceUrl: http://www.wired.com/wiredscience/2014/01/how-to-hack-okcupid/
---

## Summary

Chris McKinlay, a UCLA math PhD student, scraped OkCupid profiles and used k-means clustering to segment the female user population, then used that clustering to optimize his own profile answers. He answered questionnaire items strategically to score high compatibility with the centroid of each cluster, not with any specific target. After reprofiling himself this way, he went from a handful of responses per week to a flood.

The Wired story covers both the technical approach — k-means on questionnaire data, with collaborative filtering-like matching — and the human outcome: he met and married one of the women who messaged him. The story became a popular example of data science applied to everyday life, partly because the outcome was genuinely good rather than unsettling.

## Key points

- Used Python to scrape ~20,000 OkCupid profiles and extract feature vectors from questionnaire answers
- Applied k-means clustering to segment users into 7 types, each with distinct answer patterns
- Optimized his answers to maximize compatibility scores across all clusters simultaneously — gaming the proxy metric
- Exploits OkCupid's matching algorithm, which uses something like collaborative filtering on revealed preferences
- Part of the 2014 wave of "data science solves everyday problems" narratives that helped the field gain mainstream attention

[Original](http://www.wired.com/wiredscience/2014/01/how-to-hack-okcupid/)
