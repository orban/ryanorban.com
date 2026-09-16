---
title: How Multi-Disk Failures Happen
date: 2012-12-31
categories:
  - storage
  - raid
  - reliability
  - operations
  - sysadmin
description: "SysAdmin1138's analysis of how multi-disk failures actually happen in RAID arrays — debunking the assumption that independent failure is the norm. The real failure modes are correlated: same-batch drives, vibration propagation, and recovery-induced failures."
params:
  source: pinboard
  sourceUrl: http://sysadmin1138.net/mt/blog/2012/12/how-multi-disk-failures-happen.shtml
---

![How Multi-Disk Failures Happen](/images/notes/multi-disk-failure-patterns.png)

## Summary

This post explains why RAID arrays suffer multiple simultaneous disk failures far more often than naive probability calculations predict. The conventional model assumes disk failures are independent events — if each disk has a 1% annual failure rate, the probability of two simultaneously failing is 0.01%. In practice, multi-disk failures are correlated for several reasons.

First, manufacturing batches: drives purchased together were manufactured at the same time, often with the same firmware and the same latent defects. A firmware bug that causes failure under specific conditions will affect all drives from that batch simultaneously when those conditions occur. Second, vibration: in a dense enclosure, a failing drive vibrates the enclosure; that vibration mechanically stresses adjacent drives and increases their failure probability. Third, RAID rebuild stress: when one drive fails, the RAID controller reads every sector of every remaining drive during the rebuild. This intensive read operation is precisely when latent bad sectors on aging drives manifest — the rebuild stress causes a second failure during recovery.

The practical guidance: don't treat RAID as equivalent to backup — it protects against hardware failure, not against correlated failure, logical corruption, or operator error. RAID-6 (two-parity) is substantially more robust than RAID-5 (one-parity) against the rebuild-induced second failure scenario. And diversifying drive sources (different batches, manufacturers, purchase dates) reduces batch-correlation risk.

## Key points

- Drive failures in arrays are correlated, not independent — manufacturing batches, vibration, and rebuild stress create simultaneous failure scenarios
- RAID rebuild is the highest-risk period: reads every sector of surviving drives under time pressure — latent bad sectors cause second failures
- RAID-5 vs RAID-6: RAID-5 cannot survive a single additional failure during rebuild; RAID-6 can — the difference matters enormously given correlated failure rates
- Drive batch correlation: same-model drives purchased together share manufacturing defects and firmware bugs
- RAID is not backup: protects against hardware failure, not deletion, corruption, or ransomware — requires separate backup strategy

[Original](http://sysadmin1138.net/mt/blog/2012/12/how-multi-disk-failures-happen.shtml)
