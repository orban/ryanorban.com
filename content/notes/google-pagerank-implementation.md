---
title: "Google PageRank: Implementation"
date: 2013-01-17
categories:
  - algorithms
  - graph-theory
  - search-engines
  - pagerank
  - link-analysis
description: A practical explainer on implementing the original Google PageRank algorithm — walking through the iterative link-analysis computation from the Brin/Page paper. Saved when learning graph algorithms and search engine internals.
params:
  source: pinboard
  sourceUrl: http://pr.efactory.de/e-pagerank-implementation.shtml
---

![Google PageRank: Implementation](/images/notes/google-pagerank-implementation.png)

## Summary

PageRank is the link-analysis algorithm that was central to Google's original breakthrough in web search. Developed by Larry Page and Sergey Brin at Stanford in the late 1990s, it assigns each web page a score based on the quantity and quality of other pages linking to it — treating links as votes, weighted by the authority of the voter. A page linked to by many high-PageRank pages gets a high PageRank itself, regardless of its content.

The implementation described on this site follows the iterative algorithm from the original Anatomy of a Large-Scale Hypertextual Web Search Engine paper. The computation: start each page with equal rank, then repeatedly redistribute each page's rank equally among the pages it links to. After many iterations, the scores converge to the stationary distribution of a random walk on the web graph — the probability that a random surfer clicking links at random lands on any given page. The damping factor (typically 0.85) models the probability of continuing to click vs. jumping to a random page.

The mathematical foundation is linear algebra: PageRank is an eigenvector of the web's adjacency matrix. The iterative computation is the power iteration method for finding this eigenvector. Computing this efficiently at web scale required significant engineering — the original Google implementation was distributed across commodity hardware with careful partitioning of the link graph.

## Key points

- PageRank: iterative rank propagation through the web link graph; a page's rank is the weighted sum of the ranks of its linkers
- Damping factor (d=0.85): probability of continuing to follow links vs. teleporting to a random page — prevents rank sinks in pages with no outlinks
- Mathematical equivalence: PageRank is the principal eigenvector of the Google matrix (modified adjacency matrix)
- Power iteration: the computation method — multiply the rank vector by the Google matrix repeatedly until convergence
- Context: PageRank's advantage over pure keyword matching was that it incorporated human editorial judgment (links) into ranking

[Original](http://pr.efactory.de/e-pagerank-implementation.shtml)
