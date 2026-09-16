---
title: Django for Startup Founders
date: 2021-06-24
categories:
  - django
  - python
  - saas
  - architecture
  - startups
description: Alex Krupp's guide to Django architecture for SaaS founders — arguing against the default 'fat models' pattern in favor of service layers, clear separation of concerns, and patterns that scale with a small team. Opinionated and practical.
params:
  source: pinboard
  sourceUrl: https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html
---

## Summary

Alex Krupp's essay argues that the default Django architecture — fat models, thin views — doesn't scale well for SaaS startups. The conventional guidance to put business logic in models leads to God objects, hard-to-test code, and circular imports as apps grow. He proposes an alternative: a service layer architecture where models stay thin (just database schema and simple accessors) and business logic lives in separate service objects.

The proposed architecture borrows from patterns common in other ecosystems: explicit service functions (or classes) that handle business operations, clean separation between HTTP handling (views) and business logic (services), and predictable conventions that make onboarding new engineers easier. The framing is specifically aimed at small teams — where architectural clarity matters more because there's less institutional knowledge to fall back on.

The essay also addresses Django REST Framework patterns, Celery task architecture, and how to structure a codebase that will be worked on by 2-5 engineers over multiple years. It's not a radical departure from Django's idioms but a disciplined set of additional conventions on top of them.

## Key points

- Argues against fat models in favor of a service layer pattern for Django SaaS apps.
- Service objects contain business logic; models stay as thin database wrappers.
- Better testability: service functions are easier to unit test than model methods with database dependencies.
- Aimed at 1-5 engineer startups where conventions reduce coordination overhead.
- Compatible with Django REST Framework and Celery async task patterns.

[Original](https://alexkrupp.typepad.com/sensemaking/2021/06/django-for-startup-founders-a-better-software-architecture-for-saas-startups-and-consumer-apps.html)
