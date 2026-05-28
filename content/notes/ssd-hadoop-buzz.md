---
title: The Buzz and Fuzz on SSD in Hadoop
date: 2013-05-14
categories:
  - ssd
  - hadoop
  - storage
  - performance
  - big-data
description: Hadoopsphere's analysis of SSD adoption in Hadoop clusters — the trade-off between SSD's dramatically faster random I/O and its higher cost per GB compared to spinning disk. An early look at how flash storage would eventually reshape big data infrastructure.
params:
  source: pinboard
  sourceUrl: http://www.hadoopsphere.com/2012/09/the-buzz-and-fuzz-on-ssd.html
---

![The Buzz and Fuzz on SSD in Hadoop](/images/notes/ssd-hadoop-buzz.png)

## Summary

Hadoopsphere examined the case for solid-state drives (SSD) in Hadoop clusters in 2012, at a time when SSD prices were falling fast but still 10-20x more expensive per gigabyte than spinning disk. The core question: does SSD's dramatically better random I/O and lower latency translate to Hadoop performance gains that justify the cost premium?

The answer in 2012 was nuanced. Hadoop's MapReduce model was designed around sequential I/O — the shuffle/sort phase writes and reads large sequential blocks to disk. For this pattern, fast sequential reads on SATA spinning disk were competitive. But HDFS random reads (metadata operations, small file access, intermediate shuffle data) and the NameNode's metadata operations could benefit substantially from SSD.

The trajectory was clear: as SSD prices continued falling, the calculus would shift. By 2015-2016, NVMe SSDs at sub-$1/GB made all-flash Hadoop clusters economically viable. Nutanix and similar hyper-converged infrastructure platforms used tiered storage (SSD for hot data, HDD for cold) from the start, which is part of what made their I/O performance competitive with traditional SANs.

## Key points

- MapReduce is primarily sequential I/O — less benefit from SSD than random-read workloads
- SSD wins for: NameNode metadata, shuffle/sort intermediate data, and short-circuit local reads
- 2012 price: SSD ~10-20x cost/GB premium over HDD — required careful cost justification
- HDFS datanode with SSD + HDD tiering: hot data on SSD, bulk storage on HDD
- Trend: SSD prices fell ~30%/year; by 2015 all-flash Hadoop clusters became cost-viable
- Nutanix hyper-converged design used SSD+HDD tiering from launch — ahead of the mainstream Hadoop debate

[Original](http://www.hadoopsphere.com/2012/09/the-buzz-and-fuzz-on-ssd.html)
