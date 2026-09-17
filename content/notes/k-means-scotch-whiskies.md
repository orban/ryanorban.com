---
title: K-Means Clustering 86 Single Malt Scotch Whiskies
date: 2014-01-02
categories:
  - r
  - k-means
  - clustering
  - visualization
  - data-science
description: Clustering 86 single malt Scotch whiskies by flavor profile using k-means in R — a fun worked example that makes clustering tangible. Shows how to choose k and interpret results when the data has real-world meaning.
params:
  source: pinboard
  sourceUrl: http://blog.revolutionanalytics.com/2013/12/k-means-clustering-86-single-malt-scotch-whiskies.html
---

## Summary

This Revolution Analytics blog post applies k-means clustering to a dataset of 86 single malt Scotch whiskies, using flavor profile ratings (smoky, sweet, malty, etc.) as features. The result is a set of clusters that correspond loosely to regional styles — Islay peated malts in one group, light Highlands in another — demonstrating that the algorithm recovers structure that experts already know from sensory experience.

The worked example is valuable for teaching because the domain is intuitive: most people have some sense of what smoky vs fruity means, so the cluster assignments are immediately interpretable rather than abstract. It's also a good vehicle for showing how to choose k (elbow method on within-cluster sum of squares) and how to label clusters after the fact.

## Key points

- Uses a public dataset of 86 whiskies scored on 12 flavor dimensions (smoky, peaty, spicy, sweet, malty, fruity, etc.)
- k-means clustering in R groups whiskies by flavor similarity — Islay malts cluster together without any geographic labels
- Demonstrates the elbow method for choosing k: plot WCSS vs k, look for the inflection point
- Cluster interpretation step is where domain knowledge comes back in — the algorithm finds groups, humans name them
- Good counterpoint to abstract ML examples: clustering a sensory dataset shows that recovered structure has real meaning

[Original](http://blog.revolutionanalytics.com/2013/12/k-means-clustering-86-single-malt-scotch-whiskies.html)
