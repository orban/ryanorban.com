---
title: Disk Prices on eBay
date: 2024-12-14
categories:
  - hardware
  - storage
  - price-tracking
  - homelab
  - self-hosting
description: A price tracker for hard disk drives on eBay, sorted by cost-per-TB. Useful when building out storage-heavy homelab or NAS setups where getting the best $/TB matters.
params:
  source: pinboard
  sourceUrl: https://unli.xyz/diskprices/
---

![Disk Prices on eBay](/images/notes/disk-prices-ebay.png)

## Summary

Disk Prices on eBay (unli.xyz/diskprices) tracks used and refurbished hard disk drive listings on eBay, sorted by cost-per-terabyte. The site aggregates active listings and calculates $/TB so you can compare storage options directly without manually calculating density and price for each listing.

This is a practical tool for homelab builders, NAS (Network Attached Storage) enthusiasts, and anyone building out large-capacity storage on a budget. Used enterprise drives sold off-lease or decommissioned are often the best value for bulk storage — you can get 8-14TB drives at $10-20/TB vs $30-50/TB for new retail. The catch is that used drives have unknown wear history; checking hours (via SMART data) is essential.

The resource is part of the broader homelab tooling ecosystem alongside Grafana dashboards, TrueNAS forums, and r/datahoarder community resources. It sits in the same category as diskprices.com (new drives, by model) but specifically targets the used eBay market where the best deals often appear.

## Key points

- Tracks eBay hard drive listings sorted by $/TB — finds the best value per terabyte.
- Targets the used/refurbished market where best bulk storage prices are found.
- Essential caveat: check SMART data and drive hours before buying used drives.
- Part of the homelab / data hoarding community toolkit.
- Companion to diskprices.com (new drives) for the used market.

[Original](https://unli.xyz/diskprices/)
