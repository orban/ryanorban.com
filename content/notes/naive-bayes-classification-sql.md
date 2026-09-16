---
title: Naive Bayes Classification in SQL at Zipfian Academy
date: 2013-10-09
categories:
  - naive-bayes
  - sql
  - zipfian-academy
  - nlp
  - text-classification
description: A Zipfian Academy student's tweet about implementing Naive Bayes classification in SQL, categorizing the New York Times corpus one word at a time. A striking demonstration that ML concepts can be expressed in unexpected substrate.
params:
  source: pinboard
  sourceUrl: https://twitter.com/clearspandex/status/388011471286063104/photo/1
---

![Naive Bayes Classification in SQL at Zipfian Academy](/images/notes/naive-bayes-classification-sql.png)

## Summary

A tweet from a Zipfian Academy student (clearspandex) showing Naive Bayes classification implemented in SQL, categorizing New York Times articles one word at a time. This is a remarkable exercise: Naive Bayes text classification is fundamentally a counting and probability problem, and SQL is a perfectly capable tool for counting and aggregating.

The implementation likely uses SQL aggregations to compute word counts per category, then calculates conditional probability tables, and finally applies Bayes' theorem via a query that multiplies per-word probabilities for each document. The math works out to a join + aggregation, which is bread-and-butter SQL.

This illustrates something important about machine learning: many algorithms are not inherently mysterious or complex. Naive Bayes is counts and products. k-means is distances and averages. Implementing familiar ML algorithms in an unfamiliar substrate (SQL instead of Python) forces you to understand the mechanics rather than just calling `fit()`. The Zipfian Academy pedagogy valued this kind of exercise.

## Key points

- Naive Bayes in SQL: word counts per class → conditional probability table → Bayes' theorem applied via aggregation query.
- Implementing ML algorithms in unexpected substrates (SQL, spreadsheets) builds understanding of mechanics, not just API usage.
- Zipfian Academy curriculum included unconventional exercises like this to ensure students understood algorithms, not just libraries.
- Using the New York Times corpus as the test dataset — a large, richly labeled text collection available for academic use.
- Ryan saved this from a classmate's tweet — peer learning within the cohort was a key part of the bootcamp model.

[Original](https://twitter.com/clearspandex/status/388011471286063104/photo/1)
