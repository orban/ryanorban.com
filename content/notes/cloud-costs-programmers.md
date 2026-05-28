---
title: Cloud Costs Every Programmer Should Know
date: 2023-10-07
categories:
  - cloud
  - aws
  - infrastructure
  - cost
  - reference
description: Vantage's reference on cloud costs every programmer should internalize — covering compute, storage, networking egress, and database tiers across AWS, GCP, and Azure with rough mental models for estimating costs. Essential calibration for engineers making architectural decisions.
params:
  source: pinboard
  sourceUrl: https://www.vantage.sh/blog/cloud-costs-every-programmer-should-know
---

![Cloud Costs Every Programmer Should Know](/images/notes/cloud-costs-programmers.png)

## Summary

Vantage (a cloud cost management platform) published this reference of rough cost figures every programmer should have internalized when making infrastructure decisions. The goal is calibration: engineers often have poor intuitions about which resources are cheap vs. expensive, leading to architectural decisions that optimize the wrong things or miss obvious cost savings.

The key numbers the post covers: AWS EC2 instance pricing by type and size, S3 storage and request costs, AWS RDS vs. self-managed database costs, data transfer and egress pricing (notoriously expensive — often the hidden cost in cloud architectures), Lambda and serverless compute costs vs. always-on instances, and CDN pricing. The comparison across AWS, GCP, and Azure reveals that egress is expensive everywhere but pricing otherwise varies.

A few mental models from the post that stick: network egress is the stealth cost that surprises teams at scale — data leaving a cloud region to the internet or to another provider costs roughly $0.09/GB and adds up fast; storage is cheap but request volume can exceed storage cost; reserved instances and savings plans provide 30–70% discounts over on-demand but require commitment. These calibrations inform architectural choices: prefer batched API calls over per-request calls, avoid unnecessary cross-region data movement, and prefer storage to recomputation when storage is cheap and compute is expensive.

## Key points

- Cloud egress is expensive and often the dominant unexpected cost at scale — ~$0.09/GB out-of-region.
- S3 storage is cheap; request volume can exceed storage cost at high throughput.
- Reserved instances / savings plans: 30–70% discount over on-demand — significant for stable workloads.
- Lambda vs. always-on: serverless cheaper for irregular loads, instances cheaper for sustained traffic.
- Network topology matters: cross-region and cross-provider transfers compound egress costs.
- From Vantage, a cloud cost management tool — they have strong incentive to make costs legible.

[Original](https://www.vantage.sh/blog/cloud-costs-every-programmer-should-know) → Vantage
