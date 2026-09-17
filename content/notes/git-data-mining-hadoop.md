---
title: Git Data Mining with Hadoop
date: 2013-09-18
categories:
  - hadoop
  - git
  - data-mining
  - big-data
  - version-control
description: WANdisco's post on mining git repository data at scale using Hadoop — applying distributed batch processing to version control history to extract patterns across large codebases. An early example of treating code evolution as a data science problem.
params:
  source: pinboard
  sourceUrl: http://blogs.wandisco.com/2013/09/17/git-data-mining-with-hadoop/
---

## Summary

WANdisco — a company focused on distributed version control and Hadoop replication — explored using Hadoop's MapReduce model to mine git repository data at scale. The core idea: treat a version control history as a large dataset, and apply distributed processing to extract patterns that would be impractical to compute on a single machine. Commit logs, authorship graphs, file change frequencies, and collaboration networks across thousands of repositories could all be inputs.

Git stores history as a directed acyclic graph (DAG) — commits, trees, and blobs — and this structure maps naturally onto graph analysis. Mining it with Hadoop means running map tasks over individual commits or file histories, then reducing to aggregate statistics: most-changed files, contributor pair frequencies, bug-fix commit patterns. This kind of analysis was beginning to attract research interest as tools like GitHub made massive code repositories publicly accessible.

The post appeared in the context of WANdisco's interest in both Hadoop replication (making HDFS fault-tolerant across data centers) and distributed git workflows. Treating code metadata as big data was a natural intersection of their product surface.

## Key points

- Git history as a big data problem: version control logs from large repositories (Linux kernel, GitHub public repos) can easily exceed what single-machine tools handle comfortably.
- MapReduce maps well to commit-level analysis: map over each commit to extract features, reduce to aggregate across authorship, time windows, or file paths.
- WANdisco had strong incentive to promote this use case — they built replication infrastructure for both Hadoop (via Apache Zookeeper-based consensus) and git.
- Predecessor to tools like git-of-theseus and modern software analytics platforms — the 2013 version of what would later be called repository mining.
- Conceptually related to MSR (Mining Software Repositories) — an academic field that grew significantly as GitHub made data available at scale.

[Original](http://blogs.wandisco.com/2013/09/17/git-data-mining-with-hadoop/)
