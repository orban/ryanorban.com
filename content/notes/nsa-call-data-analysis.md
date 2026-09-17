---
title: How the NSA Analyzes Call Metadata
date: 2013-06-07
categories:
  - nsa
  - surveillance
  - graph-analysis
  - social-networks
  - privacy
description: GigaOm's technical explanation of how the NSA processes bulk call metadata — published in June 2013 immediately after the Snowden revelations. The article explains the graph analysis techniques that make even metadata (not call content) a powerful surveillance tool.
params:
  source: pinboard
  sourceUrl: http://gigaom.com/2013/06/06/heres-how-the-nsa-analyzes-all-that-call-data/
---

## Summary

This GigaOm piece was published in the immediate aftermath of the Edward Snowden revelations in June 2013 and explained the technical side of what the NSA's bulk call metadata collection actually enabled. The common defense — "we only collect metadata, not content" — was technically true but missed the point: graph analysis of who calls whom, when, and for how long is extraordinarily powerful even without listening to conversations.

The technique is social network analysis applied at national scale. Phone call records form a graph where nodes are phone numbers and edges are calls. The NSA could perform multi-hop analysis: find a suspect, identify all contacts, then all contacts of contacts — standard breadth-first search on a communication graph. This reveals organizational structure (who is central, who is peripheral), communication patterns, and network clustering. With enough hops, you can map entire organizations.

The article made explicit what data scientists already understood: metadata is not anonymous or harmless. Temporal patterns, call frequency, and network position are often more revealing than content. This was a pivotal moment for public understanding of what mass data collection enables.

## Key points

- Call metadata (who, when, duration — not content) is sufficient for powerful social network analysis
- Multi-hop graph traversal from a seed number can map entire communication networks in real time
- Centrality measures (degree, betweenness) identify key nodes in a communication graph
- Scale advantage: bulk collection means any phone number can be queried retroactively, not just prospectively
- The 2013 disclosure, via Edward Snowden, revealed the PRISM program and Section 215 metadata collection
- Directly relevant to debates around data minimization and privacy by design — metadata is not harmless

[Original](http://gigaom.com/2013/06/06/heres-how-the-nsa-analyzes-all-that-call-data/)
