---
title: "PDFTriage: Question Answering over Long, Structured Documents"
date: 2023-09-20
categories:
  - rag
  - pdf
  - question-answering
  - llm
  - research
  - paper
description: PDFTriage is a method for question answering over long, structured PDF documents that uses the document's structure (pages, sections, tables of contents) as a triage layer before retrieval — letting the LLM navigate the document intelligently rather than relying on flat embedding search.
params:
  source: pinboard
  sourceUrl: https://huggingface.co/papers/2309.08872
---

![PDFTriage: Question Answering over Long, Structured Documents](/images/notes/pdftriage-question-answering.png)

## Summary

PDFTriage is a research approach for question answering over long PDF documents that exploits the document's inherent structure. Instead of treating a PDF as a flat sequence of text to chunk and embed, PDFTriage first builds a structural representation (a table of contents, page-level summaries, section headers) and uses this as a triage layer — the LLM first navigates to the relevant section of the document, then performs detailed retrieval within that section.

The motivation: long PDF documents (legal contracts, research papers, financial reports, technical manuals) have strong structural signals that standard RAG ignores. A question about a specific clause in a contract should be routed to that clause's section, not retrieved by semantic similarity across the entire document. PDFTriage uses a two-stage approach: coarse-grained navigation via structure, then fine-grained retrieval within the relevant portion.

This connects to the broader 2023 theme of RAG systems needing to be structure-aware rather than treating all documents as undifferentiated text. The same intuition appears in Neum AI's contextual splitting work — documents have structure, and good retrieval should exploit it.

## Key points

- Two-stage PDF QA: structural navigation first (section/page triage), then fine-grained retrieval.
- Exploits PDF structure (TOC, headers, page boundaries) that flat RAG ignores.
- LLM navigates the document structure before retrieving — reduces the haystack size for retrieval.
- Particularly effective for long structured documents: contracts, reports, technical manuals.
- From HuggingFace papers (arxiv 2309.08872) — September 2023 publication.
- Complements Neum AI contextual splitting and the broader retrieval quality improvement trend.

[Original](https://huggingface.co/papers/2309.08872) → HuggingFace
