---
title: Proprietary Hadoop Is a Losing Strategy
date: 2013-03-12
categories:
  - hadoop
  - open-source
  - business-strategy
  - cloudera
  - hortonworks
description: ReadWrite's 2013 argument that commercial Hadoop vendors who added proprietary lock-in would lose to those who contributed everything upstream — a prescient thesis that proved partly right, partly wrong over the following decade.
params:
  source: pinboard
  sourceUrl: http://readwrite.com/2013/03/12/proprietary-hadoop-is-a-losing-strategy
---

![Proprietary Hadoop Is a Losing Strategy](/images/notes/proprietary-hadoop-losing-strategy.png)

## Summary

The core argument in this 2013 ReadWrite piece: the Hadoop ecosystem was too large and too community-driven for any single vendor to win by locking customers into proprietary extensions. Any feature Cloudera or another vendor added that wasn't upstreamed to Apache would eventually be replicated in the open-source project or competed away by rivals. Therefore, vendors should win on service quality, support, integration, and ease of use — not on proprietary code that created lock-in.

This was partly right and partly wrong. Hortonworks took the fully-open-source position and pushed everything back to Apache — they never made it as a standalone company, eventually merging with Cloudera in 2018. Cloudera, which had significant proprietary tooling (Cloudera Manager, enterprise security features, Impala optimizations), built a real business and went public. The market validated that enterprises would pay for proprietary value-add on top of open-source infrastructure when the quality gap was real.

The deeper truth the article missed: the moat for Hadoop vendors wasn't proprietary code, it was expertise and data gravity. Organizations that put their data in a vendor's managed Hadoop cluster became sticky because migrating petabytes is expensive, not because the software was locked in. Amazon EMR, Google Dataproc, and Azure HDInsight ultimately proved the article's point by providing excellent Hadoop as a service — but the winner was cloud providers, not open-source purity.

## Key points

- The proprietary Hadoop loses thesis proved partially right: Hortonworks (fully open) and Cloudera (mixed) both failed as independent companies, acquired or merged.
- Lock-in in big data infrastructure comes from **data gravity** and **operational expertise**, not from proprietary software APIs — the article missed this.
- Amazon EMR, Google Dataproc, Azure HDInsight: managed cloud Hadoop services proved more disruptive to the distributions than open-source purity debates.
- Apache Spark rendered much of the Hadoop MapReduce ecosystem moot by 2016, changing the competitive landscape entirely.
- The vendor consolidation the article predicted happened — just not for the reasons it argued.

[Original](http://readwrite.com/2013/03/12/proprietary-hadoop-is-a-losing-strategy)
