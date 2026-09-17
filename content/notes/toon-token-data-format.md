---
title: "TOON: Token-Oriented Object Notation"
date: 2025-10-27
categories:
  - llm
  - data-format
  - typescript
  - tooling
  - efficiency
description: TOON (Token-Oriented Object Notation) is a compact data format for LLMs — ~40% fewer tokens than JSON while remaining human-readable. Combines YAML indentation with CSV-style tabular layouts, with TypeScript SDKs and CLI tools.
params:
  source: pinboard
  sourceUrl: https://github.com/johannschopplich/toon
---

![TOON: Token-Oriented Object Notation](/images/notes/toon-token-data-format.png)

## Summary

TOON (Token-Oriented Object Notation) is a compact, human-readable data format designed as a lossless alternative to JSON optimized specifically for use with large language models. It achieves approximately 40% fewer tokens than equivalent JSON while maintaining data integrity — by combining YAML-style indentation with CSV-like tabular layouts for arrays.

The efficiency gain comes from recognizing how LLM tokenizers process structured data. JSON's explicit property names on every array object are repeated redundantly from the tokenizer's perspective. TOON uses explicit structural metadata (array lengths, field headers) to express the schema once, then tabular CSV-like rows for the data — analogous to how columnar storage differs from row-based storage.

TOON is useful in contexts where you're passing large amounts of structured data through LLM context windows, particularly uniform arrays of objects (database query results, API responses, spreadsheet data). The 40% reduction matters at scale: it directly translates to lower API costs and more data fitting into a given context window. From johannschopplich, who also builds Nuxt-related tooling. Includes TypeScript SDKs and CLI tools.

## Key points

- 40% fewer tokens than JSON for structured data — useful for LLM context efficiency.
- Combines YAML indentation + CSV-style tabular layouts for arrays.
- Lossless: maintains data integrity, just more token-efficient representation.
- Works best with uniform arrays of objects (DB results, API responses).
- TypeScript SDKs, CLI tools, multiple language implementations available.

[Original](https://github.com/johannschopplich/toon) → GitHub
