---
title: Data Hacking and Coffee
date: 2013-05-01
categories:
  - data-collection
  - tfidf
  - meteor
  - mongodb
  - javascript
  - experiment-design
description: "A coffee tasting experiment turned into a data project: 80 samples, 4 bean varieties, 3 brewing methods, TF-IDF scoring of flavor descriptors, and a Meteor/MongoDB web app for collection. A clever example of applying text analysis methods to sensory rating data."
params:
  source: pinboard
  sourceUrl: http://heypodo.com/blog/2013/04/29/data_hacking_and_coffee.html
---

![Data Hacking and Coffee](/images/notes/data-hacking-coffee-meteor-tfidf.png)

## Summary

This blog post documents a systematic office coffee experiment built as a data collection and analysis project. The author built a tasting app using Meteor (the real-time JavaScript framework) and MongoDB, had 25 tasters evaluate 4 bean varieties brewed 3 different ways (espresso, pour over, AeroPress) — producing 80 samples rated on taste, aroma, acidity, and body. The analysis used TF-IDF on flavor descriptor words to identify which terms were characteristic of each bean type rather than universally applied.

The TF-IDF application is the interesting methodological choice: usually TF-IDF applies to text documents, but here each "document" is the set of descriptors applied to a bean variety. A descriptor that appears for all four beans (like "smooth") has a low IDF and low discriminative value; a descriptor that appears mostly for one bean has high IDF and is characteristic of that variety. This is a case of adapting a text analysis technique to a non-text domain — sensory description data with the same statistical structure as documents.

Meteor was a good fit for this use case: the framework's real-time sync meant that as tasters submitted ratings, the analysis view updated live. In 2013 Meteor was a promising full-stack JavaScript framework before React/Node.js patterns became dominant — it used a distributed data protocol that synced MongoDB collections to the browser in real time.

## Key points

- TF-IDF applied to sensory descriptors: treats bean varieties as documents and flavor words as terms — words that distinguish one bean from others score highest
- Meteor + MongoDB for rapid prototyping of data collection apps — a 2013 full-stack JavaScript stack that enabled real-time collaborative data entry
- 2^2 factorial design element: 4 beans × 3 brew methods × multiple tasters = structured experiment rather than informal preference polling
- Guatemala Finca El Injerto won because its flavor profile was consistent across brewing methods — an insight only visible in multi-method structured data
- Broader pattern: applying quantitative methods from text/ML to domain-specific structured data — the statistics transfer even when the data type changes
- Example of the data for fun culture in the SF tech community in 2013 — hackathon-style personal projects applying big-data techniques to small personal questions

[Original](http://heypodo.com/blog/2013/04/29/data_hacking_and_coffee.html)
