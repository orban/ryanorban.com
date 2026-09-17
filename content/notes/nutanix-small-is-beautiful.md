---
title: Small is Beautiful — Nutanix
date: 2012-10-19
categories:
  - nutanix
  - hyperconverged
  - infrastructure
  - enterprise-storage
  - software-defined
description: Nutanix's 2012 blog post arguing that converged, software-defined appliances will displace massive monolithic storage arrays — the 'small is beautiful' thesis against EMC and NetApp incumbents. Retweeted by Vinod Khosla, signaling venture backing for the architectural argument.
params:
  source: pinboard
  sourceUrl: http://www.nutanix.com/blog/2012/10/11/small-is-beautiful/
---

![Small is Beautiful — Nutanix](/images/notes/nutanix-small-is-beautiful.png)

## Summary

This Nutanix blog post from October 2012 lays out the company's core architectural argument: smaller, converged appliances built on commodity x86 hardware would displace the massive monolithic SAN and NAS arrays that dominated enterprise storage. The post was retweeted by Vinod Khosla of Khosla Ventures, one of Nutanix's key investors — a signal that this wasn't just marketing copy but a thesis the venture world was aligned behind.

The small is beautiful framing inverts the traditional enterprise storage premium. Incumbent vendors like EMC and NetApp competed on capacity and feature richness of individual systems — selling the biggest, most capable storage array. Nutanix's argument was that the right unit of scale wasn't a monolithic system but a node: start small, add nodes as you grow, distribute the storage intelligence across commodity hardware rather than concentrating it in expensive proprietary controllers. Scale-out instead of scale-up.

The post connects to a broader shift in infrastructure thinking that was happening in 2012. Amazon Web Services had demonstrated that massive scale could be achieved with commodity hardware by treating individual components as disposable and building reliability through software redundancy. Nutanix was applying that logic to on-premises enterprise infrastructure — a market that was more conservative but also much larger. The timing was notable: VMware's virtual SAN wouldn't ship for another two years, leaving the field open for a hardware startup to define the category.

## Key points

- Scale-out vs. scale-up: add commodity nodes to grow, rather than buying ever-larger monolithic arrays — Nutanix's core disruption thesis.
- Hyperconverged infrastructure philosophy: storage intelligence lives in software running on each node, not in proprietary array controllers.
- Vinod Khosla retweet: investor-level endorsement of the architectural argument, not just the business case.
- The AWS lesson applied on-premises: commodity hardware + software reliability > premium proprietary hardware.
- 2012 timing: VMware vSAN wasn't shipping yet, EMC and NetApp were still dominant — the window for a disruptor was open.

[Original](http://www.nutanix.com/blog/2012/10/11/small-is-beautiful/)
