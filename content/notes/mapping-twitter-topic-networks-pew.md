---
title: "Mapping Twitter Topic Networks: From Polarized Crowds to Community Clusters"
date: 2014-03-01
categories:
  - social-networks
  - twitter
  - network-analysis
  - data-visualization
  - polarization
description: Pew Research Center's 2014 network analysis of Twitter conversations — classifying discussion patterns into six archetypes (polarized crowds, tight crowds, brand clusters, community clusters, broadcast networks, support networks). A rigorous look at how online discourse actually structures itself.
params:
  source: pinboard
  sourceUrl: http://www.pewinternet.org/2014/02/20/mapping-twitter-topic-networks-from-polarized-crowds-to-community-clusters/
---

## Summary

Pew Research Center's Marc Smith and colleagues analyzed thousands of Twitter conversations and found that network structure — not content alone — reveals how discussions are organized. Rather than treating Twitter as a single homogeneous medium, the analysis identified six distinct archetypes that recur across different topics, each with characteristic shapes in the conversation graph.

The six archetypes are: **polarized crowds** (two dense clusters of users who don't talk to each other — common on contentious political topics), **tight crowds** (a dense, well-connected community sharing common interest), **brand clusters** (hub-and-spoke pattern where a brand account connects to many unconnected users), **community clusters** (multiple sub-communities with bridges between them), **broadcast networks** (few influential accounts pushing content to many disconnected followers), and **support networks** (companies responding to customer queries — star topology around a support account).

The methodology used network analysis tools (NodeXL, developed at the Social Media Research Foundation) to collect Twitter data via the API and compute network metrics: degree centrality, betweenness centrality, clustering coefficient, and community detection via modularity optimization. This made the patterns visible as force-directed graph visualizations where cluster structure is apparent from the layout. The finding that polarization is a structural feature (two disconnected communities) rather than a content feature has significant implications for how you'd measure or moderate it.

## Key points

- Polarized crowds: the signature of political controversy — two dense clusters with almost no cross-cluster connections, even when discussing the same topic.
- Network structure is diagnostic: graph topology predicts the type of conversation without reading content.
- NodeXL: the Excel-based network analysis tool that made Twitter network collection accessible to social scientists without programming.
- Betweenness centrality: measures which nodes are bridges between communities — high betweenness nodes are information brokers.
- Implications for filter bubbles: the polarized crowd pattern shows empirically that people on opposite sides often occupy separate conversation spaces, not just separate opinions.

[Original](http://www.pewinternet.org/2014/02/20/mapping-twitter-topic-networks-from-polarized-crowds-to-community-clusters/)
