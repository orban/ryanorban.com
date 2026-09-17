---
title: "Amazon Glacier: Ultra-Low-Cost Archival Storage"
date: 2012-08-22
categories:
  - aws
  - cloud-storage
  - archival
  - backup
  - infrastructure
description: Amazon Glacier launched in 2012 as an ultra-low-cost archival storage service at $0.01/GB/month — an order of magnitude cheaper than S3. The tradeoff was retrieval latency of hours, not milliseconds, making it purely for cold data.
params:
  source: pinboard
  sourceUrl: https://aws.amazon.com/glacier/
---

![Amazon Glacier: Ultra-Low-Cost Archival Storage](/images/notes/amazon-glacier-archival-storage.png)

## Summary

Amazon Glacier launched in 2012 as AWS's answer to the archival storage problem: what do you do with data you need to keep but almost never access? At $0.01/GB per month, it was roughly 10x cheaper than Amazon S3 (which was around $0.125/GB/month at the time). The price point made tape-replacement economics work in the cloud for the first time.

The design tradeoff was explicit: Amazon Glacier was optimized for write throughput and storage cost, not retrieval speed. Getting data back took 3–5 hours by default, or up to 12 hours for bulk retrievals. This was intentional — the retrieval delay was the mechanism that allowed AWS to use cheaper, slower hardware tiers underneath. You pay pennies to store, you wait hours to retrieve. For compliance archives, database backups, and raw media assets, that tradeoff is completely acceptable.

Amazon Glacier fit into a broader pattern of AWS tiering their storage: Amazon S3 for active data, Amazon S3 Infrequent Access (later) for data accessed occasionally, and Amazon Glacier for cold archives. AWS eventually integrated Amazon Glacier more tightly into Amazon S3 as S3 Glacier storage classes, so the same bucket lifecycle policies could automatically tier data down as it aged. This automated tiering is now a standard pattern in data lake architectures.

## Key points

- $0.01/GB/month — about 10x cheaper than Amazon S3 at launch.
- 3–5 hour retrieval time — explicitly designed for cold data, not active workloads.
- Targeted use cases: compliance archives, long-term database backups, raw media storage.
- Later integrated into Amazon S3 as the "S3 Glacier" storage class family.
- Automated lifecycle tiering (S3 → Glacier) became a standard data lake architecture pattern.
- Retrieved data charged separately — cost model designed to discourage frequent access.

[Original](https://aws.amazon.com/glacier/)
