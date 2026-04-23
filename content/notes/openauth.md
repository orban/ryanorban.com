---
title: OpenAuth
date: 2024-12-17
categories:
  - authentication
  - oauth
  - open-source
  - developer-tools
  - javascript
description: OpenAuth is a universal, standards-based auth provider from the SST team — framework-agnostic, runs on any JS runtime, and follows OAuth 2.0 spec rather than inventing custom auth patterns. An alternative to Auth.js, Clerk, and hosted auth services for teams who want standards compliance without vendor lock-in.
params:
  source: pinboard
  sourceUrl: https://openauth.js.org/
---

![OpenAuth](/images/notes/openauth.png)

## Summary

[OpenAuth](/notes/openauth/) is a universal, standards-based OAuth 2.0 authentication library from the SST (Serverless Stack) team. It runs on any JavaScript runtime — Node.js, Bun, Deno, edge runtimes — and is framework-agnostic. The design philosophy is strict OAuth 2.0 and OIDC (OpenID Connect) compliance rather than building custom auth flows that happen to use JWTs. This means the library is interoperable with any OAuth-compatible client without custom integration work.

The alternative to [OpenAuth](/notes/openauth/) for most teams is either a hosted service (Clerk, Auth0, WorkOS) or a framework-specific library (NextAuth / Auth.js, Lucia). Hosted services have vendor lock-in and recurring costs at scale. Framework-specific libraries are often opinionated about infrastructure in ways that constrain deployment. [OpenAuth](/notes/openauth/) targets teams who want to own their auth stack, run it anywhere, and stay close to the standards rather than a library's abstraction.

The SST team's track record (building the most-used open-source deployment framework for AWS serverless) gives [OpenAuth](/notes/openauth/) credibility as production-grade software. The standards focus is the right call for new auth infrastructure: OAuth 2.0 and OIDC are stable, well-audited protocols, and building on top of them means your auth system is legible to any developer familiar with the standards.

## Key points

- Universal OAuth 2.0 / OIDC auth provider — runs on Node, Bun, Deno, edge.
- Framework-agnostic: no opinion about your routing or framework.
- From the SST team (Serverless Stack), well-established in the JS ecosystem.
- Standards-first design: OAuth 2.0 compliance rather than custom token flows.
- Alternative to Clerk, Auth0, Auth.js for teams who want full ownership.

[Original](https://openauth.js.org/)
