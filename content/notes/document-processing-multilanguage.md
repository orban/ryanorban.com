---
title: Document Processing in Multiple Languages
date: 2022-02-05
categories:
  - ocr
  - document-processing
  - nlp
  - machine-learning
  - internationalization
description: Nanonets' overview of multilingual document processing — extracting structured data from invoices, forms, and documents in non-English languages. Covers the ML challenges of multilingual OCR and key-value extraction at scale.
params:
  source: pinboard
  sourceUrl: https://nanonets.com/blog/document-processing-multilanguage/
---

![Document Processing in Multiple Languages](/images/notes/document-processing-multilanguage.png)

## Summary

Nanonets' guide covers multilingual document processing — the challenge of extracting structured data (names, dates, amounts, addresses) from documents written in non-English languages. The ML pipeline: OCR to convert images to text, NLP to extract and classify fields, and post-processing to normalize values into structured output.

The multilingual challenge compounds at every step. OCR models trained on Latin characters don't generalize to Arabic (right-to-left), Chinese (character-based), or Devanagari scripts. Named entity recognition models require language-specific training data. Date, currency, and number formats vary by locale — parsing "2/3/22" requires knowing whether the document is French or American. Most commercial document processing APIs in 2022 were English-first.

Nanonets built their product around this gap: a low-code platform for training custom document extraction models that could handle arbitrary document layouts and languages. The practical use case they target is accounts payable automation — processing invoices from international suppliers where the layout and language vary. Related products in this space include AWS Textract, Google Document AI, Microsoft Form Recognizer, and Docsumo.

## Key points

- Multilingual OCR: script recognition must precede text extraction for non-Latin documents.
- Layout understanding: key-value extraction depends on spatial relationships, not just text — invoice fields vary by template.
- Language-specific NLP: entity extraction models require per-language training data or multilingual foundation models.
- Locale normalization: dates, numbers, and currencies need locale-aware parsing rules.
- Nanonets platform: train custom extraction models without writing code — relevant for AP automation.

[Original](https://nanonets.com/blog/document-processing-multilanguage/)
