---
title: Git (and Github) for Data
date: 2013-07-02
categories:
  - git
  - data
  - version-control
  - open-data
  - collaboration
description: Open Knowledge Foundation's 2013 post on using Git and GitHub for data versioning — exploring whether the version control model that worked for code could work for datasets. An early articulation of what became the data-as-code movement.
params:
  source: pinboard
  sourceUrl: http://blog.okfn.org/2013/07/02/git-and-github-for-data/
---

## Summary

The Open Knowledge Foundation published this post in July 2013 exploring whether Git and GitHub could serve as version control infrastructure for data — not just code. The core question: if version control provides collaboration, history, branching, and auditability for software, why not apply the same model to datasets?

The idea was appealing in 2013 for several reasons. Open data projects were proliferating, and the tools for collaborating on datasets were primitive — typically file shares or databases with no change history. The CSV and JSON formats that most small datasets used were text-based, making them technically compatible with Git's diff model. And GitHub's collaborative workflow — fork, edit, pull request, merge — was already understood by the engineering community that worked most closely with data.

The post identifies the real limitations too: Git was designed for text files where line-by-line diffs are meaningful. Large binary datasets, database dumps, and versioning of schema changes don't map cleanly to the Git model. GitHub rendering previews for GeoJSON and CSV files was a step forward, but data lineage and provenance tracking needed something more structured. Tools like dat (later DVC — Data Version Control) would emerge in subsequent years to address this gap.

## Key points

- Git's branch-and-merge workflow transfers naturally to collaborative data editing for small, text-format datasets.
- GitHub CSV rendering and GeoJSON maps showed there was appetite for hosting and visualizing data alongside code.
- The binary file problem: large datasets, database dumps, and scientific data files don't diff meaningfully in Git — file size and format break the model.
- dat project (from Max Ogden at OKFN) was an early attempt to build a Git-like distributed version control system specifically for datasets.
- This 2013 discussion anticipated the data version control ecosystem (DVC, Delta Lake, LakeFS) that matured 5-7 years later.

[Original](http://blog.okfn.org/2013/07/02/git-and-github-for-data/)
