---
title: Internet Major Outages — January 2013
date: 2013-01-31
categories:
  - internet
  - outages
  - infrastructure
  - twitter
  - personal
description: Personal tweet from January 2013 noting simultaneous major internet service outages affecting Twitter, Amazon, and Facebook — a memorable moment when multiple major platforms went down in close succession.
params:
  source: pinboard
  sourceUrl: https://twitter.com/ryanorban/status/297123494192349184/photo/1
---

![Internet Major Outages — January 2013](/images/notes/internet-major-outages.png)

## Summary

This pinboard entry is a personal tweet from @ryanorban (January 31, 2013): "First Twitter, then Amazon, and now Facebook? Who broke the Internet?!" — capturing a moment when multiple major internet platforms experienced outages in close succession.

The coincidence of multiple high-profile outages was enough to prompt speculation about a coordinated cause, though large-scale internet outages at major platforms typically result from independent failures: DNS misconfigurations, BGP routing issues, database failures, or CDN problems. The fact that Twitter, Amazon AWS, and Facebook all had issues around the same time likely reflected the interconnected nature of internet infrastructure — many services depend on shared DNS providers or routing infrastructure.

This moment is a small historical marker of the era when cloud platform reliability was still unpredictable enough that simultaneous outages across major services were notable events. AWS outages in particular carried outsized impact because so many other services ran on it — an AWS East region failure could take down dozens of seemingly unrelated websites simultaneously.

## Key points

- Large platform outages in 2013 were more frequent than today — AWS, Facebook, and Twitter each experienced notable reliability incidents in 2012-2013
- The interdependency problem: Amazon S3 and EC2 outages had cascading effects on other services that used AWS as infrastructure — single platform failures were amplified
- DNS and BGP routing issues were common causes: misconfiguration or route leaks could cause widespread inaccessibility
- The cultural reflex of tweeting during a Twitter outage — or checking Facebook's status on Facebook — captured the circular dependency of platform-era communication
- This preceded more sophisticated incident management and multi-region redundancy practices that have made major platform outages less frequent and shorter

[Original](https://twitter.com/ryanorban/status/297123494192349184/photo/1)
