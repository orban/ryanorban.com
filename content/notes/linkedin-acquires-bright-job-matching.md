---
title: "LinkedIn Acquires Bright: Big Data Job Matching"
date: 2014-02-07
categories:
  - machine-learning
  - recruiting
  - nlp
  - acquisition
  - linkedin
description: LinkedIn's ~$120M acquisition of Bright, a job-matching startup that used machine learning to score candidate-job fit from resume and job description text. A signal of how ML-powered matching was becoming central to professional network platforms.
params:
  source: pinboard
  sourceUrl: http://techcrunch.com/2014/02/06/linkedin-acquires-bright-a-jobs-search-engine-that-used-big-data-to-match-candidates-and-employers/
---

## Summary

LinkedIn acquired Bright in early 2014 for approximately $120M — one of the larger talent-tech acquisitions of the era. Bright built a job search engine that went beyond keyword matching: it used machine learning to score the fit between a candidate's resume and a job description, ranking opportunities by predicted match quality rather than keyword occurrence or recency.

The technical core of Bright's system was natural language processing applied to resume and job description text — extracting skills, titles, industries, and career trajectory signals, then learning from click and application behavior which matches users found relevant. This is a recommendation system problem: given a user profile and a corpus of items (job listings), rank items by predicted relevance. LinkedIn's existing Jobs product was mostly keyword-search; Bright's ML-powered matching was the capability they were buying.

The acquisition happened at the moment when LinkedIn was becoming serious about machine learning as a core capability. They had already built people you may know and skills endorsements using graph-based and collaborative filtering techniques. Adding Bright's job-matching ML to the stack let them close the loop: LinkedIn knew where you'd worked (profile), who you knew (network), and now could predict what jobs you'd want to apply to.

## Key points

- Bright: ML-powered job matching — scored candidate-job fit from resume and listing text rather than keyword overlap.
- LinkedIn acquisition thesis: add ML matching to complement their graph-based network and profile data.
- NLP on resumes: extracting structured signals (skills, titles, seniority, career trajectory) from unstructured text — a classic information extraction problem.
- Recommendation system framing: jobs as items to rank for each user, with click/application behavior as implicit feedback.
- ~$120M price: reflects the value of a trained ML system plus the engineering team who built it — the acqui-hire + IP pattern.

[Original](http://techcrunch.com/2014/02/06/linkedin-acquires-bright-a-jobs-search-engine-that-used-big-data-to-match-candidates-and-employers/)
