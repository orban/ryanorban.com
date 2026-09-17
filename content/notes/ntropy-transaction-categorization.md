---
title: "Ntropy: Transaction Enrichment API"
date: 2022-04-01
categories:
  - fintech
  - machine-learning
  - nlp
  - banking
  - api
description: Ntropy is a transaction enrichment API that cleans, labels, and categorizes raw banking transaction data using ML — turning the noisy strings in bank feeds into structured, queryable merchant and category data.
params:
  source: pinboard
  sourceUrl: https://ntropy.com/
---

## Summary

Ntropy is a fintech API for cleaning and enriching raw banking transaction data. The core problem: raw bank transaction strings are a mess — "SQ *COFFEE SHOP 12345 PORTLAND OR" means something to a human but is opaque to any system trying to categorize spending or identify merchants. Ntropy's ML pipeline normalizes these strings into structured data: canonical merchant name, category, subcategory, merchant logo, website, and enriched metadata. This is the missing data layer between raw bank feeds (via Plaid or direct connections) and financial applications that need to understand what users are spending.

The NLP challenge is genuinely hard. Transaction descriptions vary wildly by bank, country, merchant, and payment method. AMZN MKTP US and AMAZON.COM AMZN.COM/BILL WA are both Amazon; a model needs to learn these variations, their canonical identity, and the right category. The multi-geo, multi-lingual claim in the tagline reflects that transaction strings look different across countries — European banks, in particular, produce very different formats than US ones. Training data for this requires licensed transaction datasets from financial institutions.

Ntropy positioned itself as enabling a banking data stack — similar to how dbt and Fivetran handle data transformation and ingestion for analytics, Ntropy handles the specific transformation problem of financial transaction data. The downstream use cases are personal finance apps (categorize spending), SMB accounting (reconcile expenses), lending (assess spending patterns for credit decisions), and financial analytics. The API model means fintech companies don't need to build or maintain their own transaction normalization infrastructure.

## Key points

- Transaction enrichment: raw bank strings → canonical merchant name + category + metadata — the data cleaning layer for fintech.
- Multi-geo and multi-lingual: different banks/countries produce very different transaction string formats.
- Downstream uses: personal finance categorization, SMB expense reconciliation, credit decisioning, fraud detection.
- Positioned as infrastructure — fintech equivalent of dbt for analytics (handles the normalization layer).
- Input sources: Plaid, direct bank connections, CSV exports — any raw transaction data.
- Competes with: Mastercard transaction enrichment, Fiserv, and in-house ML teams at larger fintechs.

[Original](https://ntropy.com/)
