---
title: "\"Hey Machine, What's My Invoice Total?\" (Impira Blog)"
date: 2022-09-02
categories:
  - document-ai
  - nlp
  - ocr
  - machine-learning
  - enterprise
description: Impira's explainer on document understanding ML — how to extract structured data like invoice totals from unstructured documents using layout-aware models. Covers why document AI is harder than it looks and how layout-aware transformers like LayoutLM changed the problem.
params:
  source: pinboard
  sourceUrl: https://www.impira.com/blog/hey-machine-whats-my-invoice-total
---

## Summary

Impira's blog post covers the document understanding problem through the lens of invoice processing: how do you extract the total amount from an invoice that could be formatted in dozens of different ways? This seems trivial for humans — we find the "Total" label and read the number next to it — but is non-trivial for machines because invoices are unstructured, vendor-specific, and mix visual layout cues with text.

The naive approach — OCR followed by keyword matching — fails because "Total" might be Grand Total, Amount Due, Invoice Amount, or nothing at all (just a bottom-line number positioned spatially). Layout matters: the number to the right of "Total" is the total, not the one above or below it. This is where layout-aware models like LayoutLM (Microsoft, 2020) changed the problem: by encoding both the text content and the bounding box coordinates of each word, the model learns that a number adjacent to a total-label is the invoice total, independent of exact label wording.

Impira was building a no-code document AI platform allowing businesses to train extractors on their own document types. The core insight: document layouts are business-specific enough that pretrained models need fine-tuning on company-specific examples, but layout-aware architectures reduce the data needed to 50-200 examples per document type rather than thousands. This post is an accessible introduction to the problem that document AI vendors (Impira, Docugami, AWS Textract, Azure Form Recognizer) were solving in 2022.

## Key points

- Invoice total extraction requires both OCR (reading text) and layout understanding (spatial relationships).
- Keyword matching fails: "Total" has many variants; position/layout is the reliable signal.
- LayoutLM encodes text + bounding box coordinates — enables layout-aware information extraction.
- Fine-tuning on ~50-200 examples per document type is often sufficient with layout-aware models.
- Impira built a no-code platform for this; category includes AWS Textract, Azure Form Recognizer, Docugami.
- Document AI is a large enterprise market — AP/AR automation, contract review, forms processing.

[Original](https://www.impira.com/blog/hey-machine-whats-my-invoice-total)
