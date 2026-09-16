---
title: "django-seal: Queryset Sealing for Django"
date: 2021-02-19
categories:
  - django
  - python
  - orm
  - performance
  - database
description: django-seal lets you mark a QuerySet as 'sealed' so that any lazy evaluation attempt (iterating after the context is closed, triggering N+1 queries) raises an exception. It enforces eager loading discipline at the queryset level, catching ORM performance mistakes in development.
params:
  source: pinboard
  sourceUrl: https://github.com/charettes/django-seal
---

## Summary

[django-seal](/notes/django-seal/) is a Django application that adds a `.seal()` method to QuerySets. A sealed queryset raises `SealedModelIterable` if anything attempts to lazily evaluate it after the point of sealing — specifically, accessing related objects that weren't prefetched with `select_related()` or `prefetch_related()`. It's a development-time guard against N+1 query problems, the most common Django ORM performance footgun.

The problem it solves: Django's ORM is lazy by default. Accessing `order.customer.name` on a queryset that didn't include `select_related('customer')` triggers an additional database query per row. In development these queries are hard to notice (they succeed silently), but in production with thousands of rows the latency is catastrophic. [django-seal](/notes/django-seal/) converts these silent additional queries into loud exceptions during development and testing.

The workflow: in tests or development, apply `.seal()` to querysets at the service/view layer, then write tests that exercise your views. Any lazy access that slips through will raise an exception immediately, telling you exactly where to add `select_related()` or `prefetch_related()`. This is more targeted than query logging (which shows you all queries but doesn't pinpoint where lazy evaluation happened) or django-debug-toolbar (which requires a browser).

## Key points

- `.seal()` marks a QuerySet so lazy evaluation of unanticipated related objects raises an error immediately.
- Catches N+1 query problems during development before they become production performance issues.
- Works with `select_related()` and `prefetch_related()` — sealed querysets that properly prefetch don't raise exceptions.
- More targeted than django-debug-toolbar for catching lazy loading issues in automated tests.
- Follows the pattern of using Python's type system and exceptions as development-time guardrails rather than runtime costs.

[Original](https://github.com/charettes/django-seal) → GitHub
