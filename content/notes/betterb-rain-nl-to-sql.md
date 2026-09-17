---
title: "BetterBrain: Natural Language to SQL with Schema Awareness"
date: 2022-10-05
categories:
  - llm
  - sql
  - natural-language
  - tools
  - developer-tools
description: BetterBrain converts natural language to SQL while correctly handling schema constraints — an early 2022 demo of LLM-powered text-to-SQL that understood the database schema rather than generating syntactically-valid but semantically-wrong queries.
params:
  source: pinboard
  sourceUrl: https://twitter.com/abhargava20/status/1577713811150311444
---

## Summary

BetterBrain is an early text-to-SQL tool that converts natural language questions into SQL queries while respecting the actual database schema. The key differentiation from naive LLM SQL generation: it doesn't just produce syntactically valid SQL, it produces queries that correctly reference actual table names, column names, and relationships in your schema.

The schema-awareness problem is the hard part of text-to-SQL. A model that doesn't know your schema generates SQL that might be grammatically correct but references nonexistent tables or columns. BetterBrain takes your schema as input and conditions generation on it — an approach that later became standard in tools like Vanna, SQLAI, and the RAG-augmented SQL generation patterns in LangChain.

Demonstrated by Abhay Bhargava on Twitter in October 2022, this sits in the early wave of LLM applications that showed specific domain tasks — rather than general chat — could be done reliably by conditioning models on structured context. The demo anticipated what became a significant enterprise use case: giving non-technical users SQL access to their own databases through natural language.

## Key points

- Text-to-SQL with schema awareness — generates queries that reference actual table/column names.
- Addresses the core challenge: naive LLM SQL generation fails on real schemas.
- Conditions generation on the database schema to produce semantically correct queries.
- Early demo (Oct 2022) of an approach that became mainstream in enterprise data tools.
- Precursor to tools like Vanna, SQLAI, and RAG-based SQL generation.
- Demoed by Abhay Bhargava on Twitter.

[Original](https://twitter.com/abhargava20/status/1577713811150311444)
