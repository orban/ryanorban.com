---
title: Why REST Keeps Me Up At Night
date: 2012-05-16
categories:
  - rest
  - api-design
  - web-architecture
  - hypermedia
description: A ProgrammableWeb post on the practical frustrations of RESTful API design — that most APIs called 'REST' are really just HTTP+JSON with none of the hypermedia constraints Roy Fielding actually specified. A perennial tension between REST's academic ideal and real-world API conventions.
params:
  source: pinboard
  sourceUrl: http://blog.programmableweb.com/2012/05/15/why-rest-keeps-me-up-at-night/
---

## Summary

This ProgrammableWeb post engaged with one of the recurring frustrations in API design: that "REST" had become a marketing term applied to any API using HTTP verbs and JSON, with no connection to what Roy Fielding actually described in his 2000 dissertation. Fielding's REST (Representational State Transfer) is a specific architectural style with specific constraints — statelessness, uniform interface, HATEOAS (Hypermedia as the Engine of Application State), layered system, and code on demand. The vast majority of RESTful APIs in 2012 ignored most of these constraints, especially HATEOAS.

The practical consequence: without hypermedia controls, clients have to know the URL structure of the API in advance. The server can't evolve its URL structure without breaking clients. Documentation has to describe every URL explicitly. Compare this to the web, which is actually RESTful: you follow links, you don't need to know URL schemas in advance, and sites can restructure their URLs as long as they redirect properly. Most "REST" APIs don't work this way.

This was a live debate in 2012. Alternatives like GraphQL (not yet announced) and OData were being developed. HAL (Hypertext Application Language) and JSON-LD were attempts to add hypermedia to JSON APIs. Roy Fielding had a famously terse blog post in 2008 titled "REST APIs Must Be Hypertext-Driven" making the same point. The conclusion many developers eventually reached: pragmatic HTTP+JSON APIs are fine, but calling them REST creates confusion about what REST means and what properties to expect.

## Key points

- Roy Fielding's REST requires HATEOAS: clients discover URLs via hypermedia links, don't hardcode them.
- Most "REST" APIs are just HTTP+JSON with CRUD semantics — a different (pragmatic, valid) pattern.
- Consequence of no HATEOAS: tight coupling between client URL knowledge and server structure; hard to evolve.
- Fielding's 2008 post "REST APIs Must Be Hypertext-Driven" is the canonical primary source on this point.
- By 2015, GraphQL became the dominant alternative for complex data fetching, sidestepping the REST debate.

[Original](http://blog.programmableweb.com/2012/05/15/why-rest-keeps-me-up-at-night/) → REST API
