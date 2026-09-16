---
title: How to Compare VMware and OpenStack
date: 2013-01-23
categories:
  - openstack
  - vmware
  - cloud
  - infrastructure
  - comparison
description: Mirantis SlideShare deck on how to compare VMware and OpenStack for enterprise private cloud decisions — a companion to their widely-read blog post. Useful for the specific evaluation criteria and TCO framing they used to make the OpenStack case.
params:
  source: pinboard
  sourceUrl: http://www.slideshare.net/mirantis/how-to-compare-vmware-and-openstack
---

![How to Compare VMware and OpenStack](/images/notes/vmware-vs-openstack-mirantis-slideshare.png)

## Summary

Mirantis published this SlideShare deck as a companion to their written comparison of VMware and OpenStack. Mirantis was the leading independent OpenStack systems integrator in 2013 — they sold OpenStack consulting, training, and managed services, so their comparison had an obvious bias, but it also represented genuine expertise in both platforms and the specific trade-offs enterprises were navigating.

The evaluation framework covered several dimensions: total cost of ownership (TCO), which required separating VMware's per-VM licensing from OpenStack's operational labor costs; feature parity, where VMware had mature management tooling (vCenter) versus OpenStack's fragmented component landscape; vendor lock-in, where OpenStack's open-source nature and multi-vendor ecosystem was positioned against VMware's proprietary stack; and scalability, where OpenStack's horizontal scaling model was compared to VMware's more hierarchical architecture.

The comparison should be read alongside the vault note on the related blog post (2013-02-09-vmware-vs-openstack). The Mirantis argument was correct that TCO comparisons were less favorable to VMware than they appeared — but they understated how much of VMware's value came from operational simplicity and ecosystem maturity. Many enterprises that switched to OpenStack for cost reasons found that the operational complexity more than offset the licensing savings.

## Key points

- TCO framing: VMware licensing is visible and substantial; OpenStack operational labor costs are real but harder to quantify upfront
- vCenter vs OpenStack Horizon: VMware's management tooling was significantly more mature in 2013
- Vendor lock-in argument: OpenStack's multi-vendor ecosystem means no single-vendor dependency, but increases integration complexity
- Mirantis was the most technically credible OpenStack voice because they deployed it operationally at scale, not just theoretically
- Historical resolution: public cloud (AWS, Azure, GCP) won; both VMware and OpenStack lost ground to managed infrastructure

[Original](http://www.slideshare.net/mirantis/how-to-compare-vmware-and-openstack)
