---
title: Netflix to Open Source Army of Cloud Monkeys
date: 2012-04-16
categories:
  - netflix
  - distributed-systems
  - chaos-engineering
  - resilience
  - open-source
description: Wired's report on Netflix open-sourcing the Simian Army — a suite of tools including Chaos Monkey that deliberately broke production systems to test resilience. The foundational document of chaos engineering as a discipline.
params:
  source: pinboard
  sourceUrl: http://www.wired.com/wiredenterprise/2012/04/netflix_monkeys/
---

## Summary

Netflix announced in April 2012 that it was open-sourcing the Simian Army — a suite of tools including the now-famous Chaos Monkey that it used to deliberately inject failures into its own production systems. The premise was counterintuitive: the best way to build a resilient system is to break it constantly in controlled ways so you find weaknesses before real failures do.

Chaos Monkey is the most well-known of the tools. It randomly terminates virtual machine instances in the AWS production environment during business hours — forcing engineers to design every service to survive instance failures. The logic: if failures happen at predictable times when engineers are awake and watching, they can be fixed; if they happen at 3am during peak traffic, they're disasters. The monkey is named because of the chaos it deliberately introduces.

The Simian Army included other tools: Latency Monkey (introduces artificial network delays), Conformity Monkey (identifies instances not following best practices), Janitor Monkey (cleans up unused resources), and Chaos Gorilla (terminates entire AWS Availability Zones). Together they constituted an early instantiation of what would later be called chaos engineering — a practice that has since become standard at large-scale distributed systems companies.

Open-sourcing these tools was significant because it spread the practice beyond Netflix and codified it as a legitimate engineering methodology rather than an eccentricity of one company's culture.

## Key points

- Chaos Monkey terminates random EC2 instances in production during business hours — by design, to surface weaknesses.
- The full Simian Army addresses latency, resource conformance, cleanup, and zone-level failures, not just instance termination.
- The release formalized chaos engineering as a discipline with transferable tooling and a documented philosophy.
- Netflix's fail fast in production approach was only viable because of their deep investment in microservices and stateless design patterns.
- The open-source release turned an internal Netflix practice into an industry standard — Chaos Monkey is now a reference point in every distributed systems conversation.

[Original](http://www.wired.com/wiredenterprise/2012/04/netflix_monkeys/)
