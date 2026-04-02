---
title: "LangExtract: Gemini-powered structured information extraction"
date: 2026-02-13
categories:
  - llm
  - information-extraction
  - nlp
  - gemini
  - open-source
description: LangExtract is Google's open-source Python library for structured information extraction from unstructured text using Gemini's controlled generation. Maps every extracted element back to exact character positions in source text.
params:
  source: pinboard
  sourceUrl: https://developers.googleblog.com/introducing-langextract-a-gemini-powered-information-extraction-library/
---

![LangExtract: Gemini-powered structured information extraction](/images/notes/langextract.png)

## Summary

[LangExtract](/notes/langextract/) is an open-source Python library from Google that transforms unstructured text into structured data using Gemini models. The core mechanism is \Controlled Generation\ — Gemini produces output that conforms to a user-defined schema, guided by few-shot examples. You define what you want to extract and provide examples; [LangExtract](/notes/langextract/) handles the extraction at scale with source traceability.

The traceability feature is the distinguishing design choice: every extracted element maps back to exact character positions in the original text. This matters for downstream validation — you can verify that what was extracted actually appeared in the source, not hallucinated. For high-stakes domains like medical or legal text, this makes the extraction auditable.

The domain coverage in the examples is broad: medications and dosages from clinical notes, entities from legal/financial documents, characters and relationships from narrative text, structured fields from radiology reports. It handles long documents through chunking and parallel processing. Beyond Gemini, it supports on-device LLMs as well, which is a useful option for sensitive documents. Interactive HTML visualization for extracted data is built in.

## Key points

- Structured extraction from unstructured text with user-defined schemas and few-shot examples.
- Every extracted element traced back to exact character position in source text — auditable, not just outputs.
- Uses Gemini Controlled Generation; also supports on-device LLMs.
- Domain examples: medical/clinical, legal/financial, literary, radiology.
- Chunking and parallel processing for long documents.
- Open-source Python library from Google.

[Original](https://developers.googleblog.com/introducing-langextract-a-gemini-powered-information-extraction-library/)
