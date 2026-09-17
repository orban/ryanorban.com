---
title: "libaws: AWS Should Be Easy"
date: 2022-05-24
categories:
  - aws
  - cli
  - infrastructure
  - developer-tools
  - serverless
description: libaws is Nathan Tippy's opinionated Go CLI that wraps AWS APIs to make them 'easy' — single-command Lambda deployments, simplified IAM, and declarative infrastructure for common patterns. A lightweight alternative to CDK/Terraform for developers who want less abstraction.
params:
  source: pinboard
  sourceUrl: https://github.com/nathants/libaws
---

## Summary

[libaws](/notes/libaws/) by Nathan Tippy (nathants) is a Go-based CLI tool that wraps AWS APIs with the explicit goal of making common AWS operations straightforward. The tagline aws should be easy captures the frustration: AWS's surface area is enormous, the official CLI is verbose, and setting up even simple deployments with Lambda, API Gateway, S3, and IAM roles requires assembling many moving parts.

[libaws](/notes/libaws/) takes an opinionated approach — it makes choices for you about how things should be structured (file layout, naming conventions, IAM policy scoping) so you don't have to configure them from scratch. The focus is Lambda deployments, where it provides a simplified workflow: write a Go or Python function, run `libaws deploy`, and the tool handles packaging, role creation, and API Gateway wiring. This is closer to the experience of Vercel or Fly.io than to vanilla AWS.

The alternative framing is: if you're not working at a scale that justifies Terraform or CDK, and you just want to run serverless functions on AWS without the cognitive overhead, [libaws](/notes/libaws/) is a lightweight option. It doesn't try to cover all of AWS — it covers the subset of patterns that come up repeatedly for developers (functions, queues, queues triggering functions, HTTP endpoints, S3 buckets). Related tools in this space: AWS SAM (official), Serverless Framework, SST, and at the extreme end Pulumi or CDK.

## Key points

- [libaws](/notes/libaws/): opinionated Go CLI for common AWS patterns — Lambda deploys, IAM, API Gateway, S3 without Terraform/CDK complexity
- Target user: developer who wants serverless AWS without infrastructure engineering overhead
- One-command Lambda deploy: handles packaging, role creation, and API Gateway wiring automatically
- Opinionated choices: reduces configuration surface by making sensible defaults non-negotiable
- Not a full Infrastructure as Code system — intentionally narrow in scope
- Sits between raw AWS CLI and heavy IaC: useful for personal projects and small teams

[Original](https://github.com/nathants/libaws)
 → GitHub
