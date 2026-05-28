---
title: "Hadoop Creator: Google Is Living a Few Years in the Future"
date: 2013-11-14
categories:
  - hadoop
  - google
  - distributed-systems
  - big-data
  - technology
description: Doug Cutting (Hadoop creator) on Google living years ahead in infrastructure — the observation that Google's internal systems consistently anticipate what the rest of the industry will need, and then the open-source community builds it later.
params:
  source: pinboard
  sourceUrl: http://preview.getprismatic.com/story/1384426539258?share=true
---

![Hadoop Creator: Google Is Living a Few Years in the Future](/images/notes/hadoop-creator-google-future.png)

## Summary

Doug Cutting, creator of Hadoop, gave an interview or quote to ZDNet with the observation that has since become something of a cliché: "Google is living a few years in the future and sending the rest of us messages." The messages being the landmark Google papers — GFS (2003), MapReduce (2004), Bigtable (2006) — which described infrastructure Google had already built and ran in production. The open-source community then spent years implementing equivalents: Hadoop, HBase, and eventually Spark and the rest of the big data ecosystem.

The framing captures something real about Google's research publication strategy at the time: they published systems papers about infrastructure they'd already moved on from, giving the industry a map of where the frontier had been rather than where it was. By the time MapReduce was published in OSDI 2004, Google was already evolving past it internally — but it took the open-source world years to catch up even to that earlier baseline.

Doug Cutting named Hadoop after his son's toy elephant — he created it at Yahoo while trying to build Nutch (an open-source search engine), after the Google papers gave him the blueprint.

## Key points

- Doug Cutting on Google: publishes infrastructure papers years after building and then moving past the systems — the industry gets a map of the past, not the present.
- Google's landmark systems papers: GFS (2003), MapReduce (2004), Bigtable (2006) → open-source responses: HDFS, Hadoop MapReduce, HBase.
- Hadoop named after Cutting's son's toy elephant; created at Yahoo based on the Google MapReduce and GFS papers.
- By 2013, Google had moved past MapReduce internally (toward Dremel, Spanner, FlumeJava) while the industry was still learning MapReduce.
- The pattern repeated: Google publishes Dremel, industry builds Impala/Presto; Google publishes Spanner, industry builds CockroachDB.
- A fundamental dynamic in the big data ecosystem: Google as unacknowledged curriculum-setter.

[Original](http://preview.getprismatic.com/story/1384426539258?share=true)
