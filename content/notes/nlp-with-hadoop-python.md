---
title: Natural Language Processing with Apache Hadoop and Python
date: 2013-04-05
categories:
  - nlp
  - hadoop
  - python
  - big-data
  - text-processing
description: Cloudera's 2010 post (bookmarked in 2013) on running natural language processing pipelines with Apache Hadoop and Python using Hadoop Streaming — an early recipe for scaling NLP beyond single-machine limits using commodity clusters.
params:
  source: pinboard
  sourceUrl: http://blog.cloudera.com/blog/2010/03/natural-language-processing-with-hadoop-and-python/
---

## Summary

This Cloudera blog post from 2010 (bookmarked three years later, suggesting it remained a useful reference) showed how to run natural language processing pipelines on Apache Hadoop using Hadoop Streaming — a feature that allowed any language to write MapReduce jobs by communicating over stdin/stdout. Python was the language of choice for NLP practitioners (via NLTK, the dominant NLP library at the time), and Hadoop Streaming made it possible to scale Python NLP code across a cluster without rewriting it in Java.

The typical pipeline: use Hadoop to distribute a large text corpus across a cluster, run tokenization, part-of-speech tagging, or named entity recognition in parallel across all documents, then aggregate results in the reduce phase. For tasks like building large inverted indexes, computing TF-IDF over millions of documents, or training language models on massive corpora, the single-machine constraint was the bottleneck — Hadoop Streaming removed it without requiring Python developers to learn Java.

This approach prefigured the pattern that Apache Spark would later make much easier via PySpark — but in 2010, Hadoop Streaming was the practical path for Python-heavy NLP work. The limitation: Streaming jobs were slower than native Java MapReduce due to serialization overhead and forking Python processes per record, but for NLP tasks dominated by text processing latency, the overhead was often acceptable.

## Key points

- Hadoop Streaming: any language (Python, Ruby, Perl) can write MapReduce jobs by reading from stdin and writing to stdout — the framework handles distribution.
- NLTK at scale: Python NLP pipelines (tokenize, POS tag, NER) that worked on single machines could be scaled to cluster-sized corpora via Streaming.
- TF-IDF at Hadoop scale: distributed computation of term frequency-inverse document frequency over millions of documents — a canonical Streaming use case.
- Python-Java bridge: Streaming was slower than native Java MapReduce but practical for NLP tasks where text processing dominated runtime.
- Later superseded by PySpark (Apache Spark's Python API), which avoided the serialization overhead of Streaming and added in-memory caching.

[Original](http://blog.cloudera.com/blog/2010/03/natural-language-processing-with-hadoop-and-python/)
