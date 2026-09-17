---
title: "In a Nutshell: How OpenStack Works"
date: 2013-02-11
categories:
  - openstack
  - cloud
  - infrastructure
  - iaas
description: Victoria Martínez de la Cruz's plain-English explainer of how OpenStack works — breaking down Horizon, Nova, Quantum, Cinder, Glance, Swift, and Keystone into digestible roles. The definitive 2013 quick-reference for the OpenStack component architecture.
params:
  source: pinboard
  sourceUrl: http://vmartinezdelacruz.com/in-a-nutshell-how-openstack-works/
---

![In a Nutshell: How OpenStack Works](/images/notes/how-openstack-works.png)

## Summary

Victoria Martínez de la Cruz wrote this clear breakdown of OpenStack's component architecture at a time when the platform was rapidly gaining enterprise interest as an AWS-independent open-source cloud. OpenStack is composed of discrete services that communicate via APIs — understanding what each component does is essential to understanding why the system is architecturally complex.

The saved content summarizes: "Distilling OpenStack — Horizon, Nova, Quantum, Cinder, Glance, Swift, & Keystone explained in plain, simple English." Each component handled a specific cloud primitive:

- **Horizon**: the web dashboard — the human-facing control plane
- **Nova**: compute service — provisions and manages virtual machines (the AWS EC2 equivalent)
- **Quantum** (later Neutron): networking — virtual networks, subnets, routers, floating IPs
- **Cinder**: block storage — persistent volumes attached to virtual machines (like AWS EBS)
- **Glance**: image service — stores and retrieves VM images (like AMIs)
- **Swift**: object storage — distributed object store (the AWS S3 equivalent)
- **Keystone**: identity and auth — token-based authentication for all other services

## Key points

- OpenStack's loosely-coupled, service-oriented architecture made it flexible but operationally complex — each component could be deployed and scaled independently
- Nova was the core compute engine; Neutron networking was historically the most operationally challenging component
- Swift (object storage) was one of OpenStack's earliest and most mature components — predated the unified project
- Keystone token-based auth was a source of operational complexity: token expiry, scope, and PKI management required careful configuration
- OpenStack vs VMware: the key differentiator was open-source licensing and no per-VM cost — but operational complexity drove many enterprises back to VMware or toward managed clouds

[Original](http://vmartinezdelacruz.com/in-a-nutshell-how-openstack-works/)
