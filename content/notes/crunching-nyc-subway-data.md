---
title: "Crunching NYC Subway Data: A New Yorker's Busiest Stations"
date: 2013-06-05
categories:
  - data-analysis
  - open-data
  - sql
  - nodejs
  - visualization
  - transit
description: "A data analysis post combining Node.js and SQL to parse MTA turnstile data and identify New York City's busiest subway stations. An early example of civic data journalism: public transit data as a lens on urban density and movement."
params:
  source: pinboard
  sourceUrl: http://blogging.alastair.is/crunching-subway-data-a-new-yorkers-busiest-stations/
---

## Summary

This post by Alastair Coote used [Node.js](/notes/nodejs/) and SQL to analyze MTA turnstile data — a public dataset the Metropolitan Transit Authority releases weekly — to identify New York City's busiest subway stations. The MTA turnstile data is an excellent entry-level civic dataset: it's messy (cumulative counters that reset, anomalous readings) but well-structured enough for someone learning data analysis to get real results.

The technical pipeline: download raw turnstile CSVs from the MTA open data portal, parse and clean the data (handling counter resets and errors), load into SQLite or PostgreSQL, then run aggregation queries to compute entries per station. The choice of [Node.js](/notes/nodejs/) for data processing in 2013 was unusual — Python with pandas was already more common for this kind of work — but demonstrated that any language with decent CSV handling and a database driver could do exploratory data analysis.

The broader significance: urban transit data as open data was a new idea in 2013. NYC's open data initiative (launched around 2012) made datasets like MTA turnstiles publicly available, and hackers and journalists were just beginning to explore what insights they contained. Posts like this seeded a cottage industry of transit data analysis.

## Key points

- MTA turnstile data is released weekly as CSV — entry and exit counts per turnstile per station every 4 hours
- Data quality challenges: cumulative counters that overflow, anomalous spikes, inconsistent station names across datasets
- SQL aggregation (group by station, sum entries) is sufficient for basic analysis after data cleaning
- [Node.js](/notes/nodejs/) as a data analysis tool in 2013 — less ergonomic than Python/pandas but functional
- Times Square, Grand Central, and Herald Square reliably top entry counts — aligns with intuition and validates the analysis
- NYC open data portal made this kind of civic analysis possible without any special access

[Original](http://blogging.alastair.is/crunching-subway-data-a-new-yorkers-busiest-stations/)
