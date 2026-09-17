---
title: Stop More Bugs with Our Code Review Checklist
date: 2015-01-09
categories:
  - code-review
  - engineering-practices
  - software-quality
  - fog-creek
  - checklist
description: Fog Creek's code review checklist for systematically increasing defect detection — from Joel Spolsky's company, so carrying the weight of serious engineering practice thinking. A checklist-based approach to making code review consistent rather than reviewer-dependent.
params:
  source: pinboard
  sourceUrl: http://blog.fogcreek.com/increase-defect-detection-with-our-code-review-checklist-example/
---

## Summary

This Fog Creek post (from Joel Spolsky's company, known for *Joel on Software* and building FogBugz) presents a structured code review checklist designed to increase defect detection rates systematically. The idea: unstructured code review catches different bugs depending on who's reviewing and what they happen to focus on — a checklist makes coverage more consistent and complete.

Code review checklists are a form of cognitive offloading: rather than relying on a reviewer to remember all the failure modes they should be looking for, you provide a structured list that covers categories they might otherwise miss. This is the same reason surgical checklists reduce errors in the OR — expert knowledge doesn't protect against attention failures.

The Fog Creek checklist covers the main categories of review concern: logic errors, security vulnerabilities (injection, authentication, authorization), performance (N+1 queries, missing indices), testing adequacy, API/interface design, error handling, and documentation. The emphasis on security and performance categories reflects the lessons of shipping production software at scale.

## Key points

- Checklists make code review coverage consistent — reduces reviewer-dependent variation in what gets caught.
- Applies the checklist manifesto principle to code review: expert knowledge + structured reminder > expert knowledge alone.
- Key categories: logic, security (injection/auth), performance (N+1/indexes), tests, API design, error handling.
- From Fog Creek / Joel Spolsky — carries weight as serious engineering practice thinking.
- Relevant to team onboarding: new reviewers with a checklist can catch more categories than experienced reviewers without one.
- Connects to automated static analysis and linting as the scalable version of checklist items.

[Original](http://blog.fogcreek.com/increase-defect-detection-with-our-code-review-checklist-example/)
