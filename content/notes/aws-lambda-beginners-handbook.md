---
title: The Complete AWS Lambda Handbook for Beginners
date: 2020-10-07
categories:
  - aws
  - serverless
  - cloud
  - functions
  - architecture
description: Dashbird's intro to AWS Lambda — the event-driven serverless compute model, execution contexts, triggers, IAM roles, and key gotchas like cold starts and timeout constraints. A solid foundation for serverless architecture thinking.
params:
  source: pinboard
  sourceUrl: https://dashbird.io/blog/complete-aws-lambda-handbook-beginners-part-1/
---

## Summary

Dashbird (an AWS monitoring platform) published this handbook as an introduction to AWS Lambda, the serverless compute service that runs code in response to events without requiring server provisioning or management. Lambda supports Python, [Node.js](/notes/nodejs/), C#, Go, and Java — the choice of handler and runtime configuration are the main implementation decisions.

The core model: an event triggers a Lambda function, AWS provisions an execution context (a containerized environment), your code runs, and results return. Auto-scaling is handled entirely by AWS — Lambda handles concurrency by spinning up additional execution contexts in parallel. You pay only for actual compute time (measured in GB-seconds), making it cost-efficient for sporadic workloads.

The main components to configure: **triggers** (the event sources — API Gateway calls, S3 uploads, DynamoDB streams, SQS messages), **execution role** (IAM permissions for what the function can access), **memory allocation** (which also controls CPU proportionally), and **timeout** (max duration per invocation, up to 15 minutes).

## Key points

- **Cold starts** are the main latency concern: the first invocation after a period of inactivity takes longer as AWS provisions the execution context. Keep-warm strategies (scheduled pings) exist but add cost.
- **Memory and CPU are coupled**: increasing memory allocation also increases proportional CPU — the only way to get more compute per invocation.
- **Execution context reuse**: Lambda reuses containers between invocations when possible — database connections and global variables persist between calls. Design accordingly.
- Lambda suits: event-driven processing, API backends, scheduled jobs, data transformation pipelines, and fan-out architectures. Not suited for long-running processes or sub-10ms latency requirements.
- Alternative serverless compute options: AWS Fargate (containerized, longer-running), Google Cloud Functions, Cloudflare Workers (edge, extremely low latency), Vercel Functions.

[Original](https://dashbird.io/blog/complete-aws-lambda-handbook-beginners-part-1/)
