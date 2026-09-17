---
title: Deploying ElasticSearch with Chef Solo
date: 2012-04-15
categories:
  - elasticsearch
  - devops
  - chef
  - search
  - infrastructure
description: An early 2012 tutorial for deploying Elasticsearch using Chef Solo — a document from when both Elasticsearch and infrastructure-as-code were early in their mainstream adoption curves. Shows the 2012 devops toolchain before Ansible and Terraform emerged.
params:
  source: pinboard
  sourceUrl: http://www.elasticsearch.org/tutorials/2012/03/21/deploying-elasticsearch-with-chef-solo.html
---

## Summary

This 2012 Elasticsearch tutorial covers deployment using Chef Solo — a notable artifact of the 2012 DevOps toolchain, when infrastructure as code was still taking its current shape. Chef (and its cousin Puppet) were the dominant configuration management tools before Ansible (2012) and Terraform (2014) gained traction. Chef Solo was the non-server version: you'd run chef-solo on each machine rather than coordinating through a central Chef Server.

Elasticsearch in 2012 was early in its trajectory toward becoming the standard search and log-aggregation backend. Launched in 2010 by Shay Banon as a distributed, RESTful search engine built on Apache Lucene, it competed with Solr (which had been around since 2004). Elasticsearch's advantages were operational: easier clustering, a REST API from the start, and a document-oriented model that felt natural alongside MongoDB and CouchDB in the JSON-everything era.

Deploying Elasticsearch in 2012 required significant manual infrastructure work: configuring JVM heap sizes, managing cluster discovery, tuning shard counts. The Chef Solo tutorial addresses this by codifying the steps into reproducible recipes — the whole point of configuration management.

## Key points

- Elasticsearch in 2012 was pre-ELK stack (Elasticsearch, Logstash, Kibana) — the logging use case that drove mainstream adoption came later.
- Chef Solo deployment was typical for stateful services before containerization (Docker launched in 2013) changed the model.
- REST API and JSON-native design gave Elasticsearch significant UX advantages over Solr for developers in the 2012 ecosystem.
- The infrastructure-as-code movement that Chef and Puppet represented became mainstream in 2012 — this tutorial is from the early wave.
- Elasticsearch went from startup search tool to core infrastructure for log analysis, full-text search, and analytics — eventually becoming part of Elastic N.V. (IPO 2018).

[Original](http://www.elasticsearch.org/tutorials/2012/03/21/deploying-elasticsearch-with-chef-solo.html)
