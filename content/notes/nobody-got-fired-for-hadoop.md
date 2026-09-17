---
title: Nobody Ever Got Fired for Using Hadoop on a Cluster
date: 2013-05-14
categories:
  - hadoop
  - enterprise
  - opinion
  - big-data
  - procurement
description: "Steve Loughran's riff on the classic 'nobody got fired for buying IBM' adapted for the big data era: Hadoop became the safe enterprise choice for data infrastructure, which brought both legitimacy and the mediocrity that comes with default choices."
params:
  source: pinboard
  sourceUrl: http://steveloughran.blogspot.com/2012/07/nobody-ever-got-fired-for-using-hadoop.html
---

![Nobody Ever Got Fired for Using Hadoop on a Cluster](/images/notes/nobody-got-fired-for-hadoop.png)

## Summary

Steve Loughran (an Apache Hadoop committer at Cloudera) wrote this post riffing on the classic enterprise technology meme "nobody ever got fired for buying IBM" — adapted to the 2012 big data moment: nobody ever got fired for using Hadoop on a cluster. By 2012, Hadoop had become the safe, defensible choice for data infrastructure in large enterprises, regardless of whether it was technically the right choice for the workload.

The observation cuts both ways. Hadoop's ubiquity was legitimizing — it meant tooling, consultants, training materials, and Cloudera/Hortonworks support contracts were available, which reduced risk. But safe default choices also carry the costs of mediocrity: Hadoop was being deployed for workloads that PostgreSQL or MySQL could handle, justified primarily by the political safety of choosing the industry consensus tool.

Loughran knew the codebase from the inside, which gave the post a specific credibility: a core committer acknowledging that Hadoop had crossed from technically superior solution to politically safe choice. This is a critical transition for any technology — it signals maturity but also the beginning of the incumbent's vulnerability to genuinely better alternatives. Apache Spark would be that alternative.

## Key points

- "Nobody got fired for buying IBM" pattern: the safe, defensible enterprise choice regardless of technical fit
- Hadoop by 2012 had certified partners (Cloudera, Hortonworks), consultants, and enterprise support — reducing career risk for IT decision-makers
- The flip side: Hadoop was being deployed for workloads where simpler tools (PostgreSQL, columnar stores) were better
- Steve Loughran was a Hadoop committer — an inside view of the technology transitioning to enterprise default
- Written by someone who knew where Hadoop was genuinely strong and where it was being applied defensively
- Hadoop's successor: Apache Spark displaced it not just on technical merits but because Spark also became a safe default

[Original](http://steveloughran.blogspot.com/2012/07/nobody-ever-got-fired-for-using-hadoop.html)
