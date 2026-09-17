---
title: Introducing Tabula
date: 2013-04-27
categories:
  - data-extraction
  - pdf
  - open-source
  - journalism
  - tools
description: Tabula is an open-source tool for extracting tabular data from PDFs — a specific but critical pain point for data journalists and researchers working with government and scientific publications that publish data as PDFs instead of structured files.
params:
  source: pinboard
  sourceUrl: http://source.mozillaopennews.org/en-US/articles/introducing-tabula/
---

## Summary

Tabula was introduced via Source (the Mozilla OpenNews project supporting data journalism) as an open-source tool for extracting tabular data from PDF files. The pain point it solved was a specific and widespread frustration: government agencies, scientific journals, and corporations frequently publish structured data in PDF format — budget tables, statistical reports, regulatory filings — making it inaccessible for computational analysis without manual re-entry.

The tool allowed users to draw a box around a table in a PDF and export the contents as CSV or Excel. Under the hood it used PDFBox (a Java PDF library) to parse the text layer and infer table structure from character positioning. This worked well for PDFs containing actual text (created by printing to PDF from a document) but not for scanned images — those required OCR first.

Tabula was built by Manuel Aristarán, Mike Tigas, and Jeremy Merrill — journalists and technologists in the investigative data journalism community. Its release in 2013 was part of a broader movement around civic tech and open data tools that made previously inaccessible government data available for analysis. The ProPublica and New York Times data teams were early users. It became a standard tool in the data journalism workflow and is still actively maintained.

## Key points

- Extracts tabular data from text-layer PDFs by inferring table structure from character x/y positions — not OCR, so requires text-based PDFs
- CSV and Excel export — the bridge between PDFs and spreadsheet/database workflows
- Critical for investigative data journalism: government budgets, campaign finance records, regulatory filings, congressional reports all come in PDF
- Built by journalists for journalists — ProPublica, NYT, IRE community were primary early users
- Open source (MIT license), runs as a local web server — no data leaves your machine, important for sensitive documents
- Limitations: scanned PDFs require preprocessing with Tesseract OCR; complex layouts (merged cells, multi-column tables) need manual cleanup

[Original](http://source.mozillaopennews.org/en-US/articles/introducing-tabula/)
