---
title: Announcing Portia — Open Source Visual Web Scraper
date: 2014-04-01
categories:
  - web-scraping
  - open-source
  - tools
  - data-collection
description: Scrapinghub's Portia is an open-source visual web scraper — a point-and-click interface on top of Scrapy that lets you build scrapers without writing code. It made web scraping accessible to non-programmers while keeping Scrapy's power underneath.
params:
  source: pinboard
  sourceUrl: http://blog.scrapinghub.com/2014/04/01/announcing-portia/
---

![Announcing Portia — Open Source Visual Web Scraper](/images/notes/portia-open-source-visual-web-scraper.png)

## Summary

Portia is an open-source visual web scraping tool built by Scrapinghub on top of their Scrapy framework. Instead of writing Python code to define selectors and extraction rules, you interact with a browser-like interface and click on the data you want to extract — Portia generates the Scrapy spider from your annotations. The launch announcement positioned this as making web scraping as easy as it should be.

Scrapy is the dominant Python framework for serious web scraping — it handles crawling, request throttling, pipelines, and item storage well. But writing Scrapy spiders requires understanding XPath or CSS selectors and the spider class structure. Portia abstracts this away, which made it valuable for data science workflows where you want to quickly collect structured data from a website without writing a full scraper.

The visual scraping approach has limits: complex sites with JavaScript rendering, login walls, or anti-scraping measures still require code. But for the common case of scraping product listings, news articles, or structured directories, visual annotation can cover 80% of use cases. Portia was an early example of the no-code data collection tools that later became a category.

## Key points

- Point-and-click interface that generates Scrapy spiders from visual annotations.
- Built by Scrapinghub, the company behind Scrapy — tight integration with the underlying framework.
- Covers the common case: structured data from consistent page templates without JavaScript.
- Complex sites (JS-heavy, auth, anti-scraping) still require manual Scrapy code.
- Early example of the "visual" / no-code approach to data collection tooling.

[Original](http://blog.scrapinghub.com/2014/04/01/announcing-portia/)
