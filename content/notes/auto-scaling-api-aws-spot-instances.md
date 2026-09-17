---
title: Auto Scaling API with AWS Spot Instances
date: 2020-07-23
categories:
  - aws
  - infrastructure
  - api
  - auto-scaling
  - cost-optimization
description: Adapty's guide to designing a scalable API on AWS using spot instances — how to structure your infrastructure to tolerate spot interruptions while dramatically reducing compute costs. A practical architecture pattern for cost-conscious API deployments.
params:
  source: pinboard
  sourceUrl: https://blog.adapty.io/designing-scalable-api-on-aws-stop-instance/
---

## Summary

Adapty published this architecture guide for building a scalable REST API on AWS using Spot instances — EC2 instances available at 70-90% discount in exchange for the possibility of interruption with 2-minute warning. The key design challenge: Spot instance interruptions are unpredictable, so applications must be designed to tolerate sudden instance loss without dropping requests.

The pattern: put a Load Balancer (ALB or NLB) in front of an Auto Scaling Group (ASG) that mixes Spot and On-Demand instances. Use a diversified Spot request spanning multiple instance types and Availability Zones — this dramatically reduces the probability of simultaneous interruptions. The ASG health checks detect interrupted instances and launch replacements, while the load balancer drains connections from terminating instances before removing them from rotation.

For stateless APIs (the ideal case), Spot interruption handling is straightforward: the load balancer stops routing to the instance on termination notice, existing connections drain, and a new instance starts from a fresh AMI. For stateful applications (session state, in-flight jobs), you need either external state storage (Redis, DynamoDB) or graceful job migration.

The cost savings are significant: a large EC2 workload running on 70% Spot can cut compute costs by 50%+. For high-traffic APIs where compute is the dominant cost, this architectural pattern is well worth the added complexity.

## Key points

- Spot instances: 70-90% discount vs On-Demand, with 2-minute interruption notice — ideal for fault-tolerant stateless workloads.
- Architecture: ALB → Auto Scaling Group with diversified Spot pool across instance types and AZs.
- Interruption handling: connection draining at the load balancer allows graceful request completion before instance loss.
- Stateless design is the key enabler — external state in Redis or DynamoDB decouples compute from state.
- Cost impact: 50%+ compute cost reduction is achievable for high-traffic API deployments.
- Related: Airflow on Fargate (similar serverless/ephemeral execution principle) in vault.

[Original](https://blog.adapty.io/designing-scalable-api-on-aws-stop-instance/)
