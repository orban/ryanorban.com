---
title: Yelp Hipster Finder (SF Word Map)
date: 2013-07-02
categories:
  - yelp
  - san-francisco
  - data-visualization
  - geospatial
  - urban
description: Yelp's word map feature visualizing geographic density of the word 'hipster' in SF business reviews. A small data visualization curiosity that mapped subcultural geography through review language.
params:
  source: pinboard
  sourceUrl: http://www.yelp.com/wordmap/sf/hipster
---

## Summary

Yelp's word map feature let users visualize the geographic density of any word appearing in San Francisco business reviews. The hipster map showed concentrations in the Mission District, Haight-Ashbury, and parts of SoMa — consistent with the cultural geography of 2013 SF. Ryan's bookmark note (Looks about right!) is an endorsement of the map's accuracy from someone living in the city at the time.

The feature was a clever use of natural language processing on Yelp's review corpus: aggregate all reviews by geographic location, count word frequencies per region, and render a heat map. It revealed subcultural geography encoded in review language — a bottom-up map of how neighborhoods were perceived by the people frequenting them, rather than top-down demographic data.

This kind of feature — turning user-generated text data into a geographic visualization — prefigured the Twitter sentiment maps and Instagram density maps that became common data journalism tools later in the decade.

## Key points

- Word maps: NLP technique of aggregating word frequency by geographic bounding box across a review corpus.
- Geographic subcultural signal: review language reveals perceived neighborhood character better than census data.
- Yelp data scale: millions of reviews allowed fine-grained geographic resolution — individual city blocks showed distinct word profiles.
- Data journalism application: the same technique was later used to map socioeconomic divides, cultural preferences, and demographic patterns from social media data.

[Original](http://www.yelp.com/wordmap/sf/hipster)
