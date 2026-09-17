---
title: "Cloud Prizefight: VMware vs. OpenStack"
date: 2013-02-09
categories:
  - openstack
  - vmware
  - cloud
  - infrastructure
  - enterprise
description: Mirantis's analysis comparing VMware and OpenStack for enterprise private cloud — clearly biased toward OpenStack (Mirantis was an OpenStack services company), but provides a useful breakdown of the real trade-offs between proprietary and open-source virtualization stacks.
params:
  source: pinboard
  sourceUrl: http://www.mirantis.com/blog/cloud-prizefight-vmware-vs-openstack/
---

![Cloud Prizefight: VMware vs. OpenStack](/images/notes/vmware-vs-openstack.png)

## Summary

Mirantis — an OpenStack professional services company — published this comparison between VMware and OpenStack for private cloud deployments. The bias is transparent (Mirantis sold OpenStack consulting), but the comparison raised real issues that enterprise architects were working through in early 2013.

The framing as a prizefight captured the genuine competition: VMware had dominated enterprise virtualization since the early 2000s, but its licensing costs were substantial and OpenStack offered a credible open-source alternative for organizations willing to invest in the operational complexity. Rackspace and NASA had co-founded OpenStack in 2010; by 2013, Red Hat, HP, IBM, and Canonical had all made major commitments to it.

The real trade-offs: VMware offered mature tooling, proven stability, strong vendor support, and operational simplicity at the cost of significant per-VM licensing fees and vendor lock-in. OpenStack offered no licensing cost and multi-vendor flexibility at the cost of operational complexity — it required specialized expertise that was scarce and expensive. Many enterprises that chose OpenStack for cost reasons found that the operational complexity cost exceeded the licensing savings.

## Key points

- VMware's cost advantage: no licensing fees, but OpenStack's operational complexity required specialized engineers — the TCO comparison was less clear than it appeared
- OpenStack governance: controlled by the OpenStack Foundation (now Open Infrastructure Foundation) with vendor-neutral stewardship — no single vendor lock-in
- Mirantis was the leading independent OpenStack systems integrator; Red Hat OpenStack Platform was the largest enterprise-supported distribution
- The debate resolved differently than either side expected: managed clouds (AWS, Azure, GCP) captured most enterprise workloads, and both VMware and OpenStack lost ground to public cloud
- Broadcom's 2023 acquisition of VMware and subsequent pricing changes may finally accelerate the OpenStack adoption that 2013 predicted

[Original](http://www.mirantis.com/blog/cloud-prizefight-vmware-vs-openstack/)
