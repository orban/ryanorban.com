---
title: Getting Started with Amazon EC2
date: 2012-07-16
categories:
  - aws
  - ec2
  - cloud-computing
  - devops
  - tutorial
description: Paul Stamatiou's 2012 getting-started guide to Amazon EC2 — launching instances, SSH access, security groups, and basic server setup. Representative of the era when 'cloud' meant learning EC2 from scratch with no managed services.
params:
  source: pinboard
  sourceUrl: http://paulstamatiou.com/how-to-getting-started-with-amazon-ec2
---

![Getting Started with Amazon EC2](/images/notes/getting-started-amazon-ec2.png)

## Summary

Paul Stamatiou published practical, photography-heavy tutorials in the 2010-2014 era that served as de facto documentation for developers approaching AWS for the first time. The EC2 getting-started guide covered the workflow that was non-obvious to developers coming from dedicated hosting or shared hosting: launching an AMI (Amazon Machine Image), configuring security groups as the firewall primitive, attaching Elastic IPs for stable addressing, and SSH-ing into the new instance.

The AWS console in 2012 was significantly less friendly than today. Concepts like security groups, key pairs, availability zones, and AMIs had no analogues in the hosting world most developers knew. The barrier wasn't technical — an EC2 instance is just a Linux server — it was conceptual. Tutorials like this one served as translation layers between prior mental models (cPanel hosting, Linode VPS) and the AWS model (compute as API calls, networking as explicit configuration, nothing managed by default).

The historical context: in 2012, running your application meant almost certainly running it on EC2 if you wanted elastic scaling. There was no Heroku for serious workloads, no DigitalOcean, no Elastic Beanstalk (it launched in 2012 as a very early product). If you needed a server, you probably launched an EC2 instance and configured it manually. Chef and Puppet were the advanced path; most small teams SSHed in and ran apt-get.

## Key points

- EC2 key concepts (2012): AMIs (machine images), security groups (stateful firewall rules), key pairs (SSH auth), Elastic IPs (static addresses), regions and availability zones.
- The mental model shift: from hosting account to API-controlled compute — EC2 doesn't manage anything; every configuration is explicit.
- 2012 ecosystem context: EC2 was essentially the only option for self-managed scalable compute. Heroku and DigitalOcean existed but at limited scale/feature sets.
- User data scripts for instance initialization were advanced usage; most developers SSHed in and configured manually in 2012.
- Tutorial artifacts: guides like this had enormous impact because AWS's own documentation was dense and assumed existing infrastructure knowledge.

[Original](http://paulstamatiou.com/how-to-getting-started-with-amazon-ec2)
