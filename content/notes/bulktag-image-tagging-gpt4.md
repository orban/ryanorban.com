---
title: "Bulktag: Batch Image Tagging with GPT-4 Vision"
date: 2023-12-05
categories:
  - llm
  - vision
  - gpt-4
  - image-processing
  - open-source
description: Bulktag uses GPT-4 Vision to batch-tag images automatically — send a folder of images, get back descriptive tags for each. An early practical application of GPT-4V for metadata generation and image library organization.
params:
  source: pinboard
  sourceUrl: https://github.com/vladignatyev/bulktag
---

![Bulktag: Batch Image Tagging with GPT-4 Vision](/images/notes/bulktag-image-tagging-gpt4.png)

## Summary

Bulktag is a command-line tool that sends batches of images to GPT-4 Vision and collects descriptive tags for each. The use case: you have a large image library without metadata — stock photos, screenshots, design assets, photos — and you want searchable tags without manually labeling each one. GPT-4V generates relevant, accurate tags from visual understanding rather than filename or EXIF data.

GPT-4 Vision (released November 2023) was the first frontier multimodal model that could reliably describe image content in detail. Early applications naturally gravitated toward metadata generation — describing, tagging, captioning — because these were clear-cut tasks where the model's visual understanding was directly useful and the output quality was easy to evaluate.

The practical output of a tool like Bulktag feeds into search indexes, DAMs (Digital Asset Management systems), or content management workflows. For a designer with thousands of assets, or a photographer with years of photos, automated tagging with a vision model is genuinely transformative — work that would take days of manual effort takes minutes. The cost is OpenAI API token consumption per image, which made batch processing more economical than single-image queries.

## Key points

- CLI tool: point at a directory → GPT-4 Vision tags each image → outputs structured tag data.
- Earliest practical use case for GPT-4V: metadata generation at scale.
- Output: tags, descriptions, or custom labels depending on configuration.
- Token cost per image makes batching important — Bulktag handles this in bulk rather than one-by-one.
- Feeds into: image search systems, DAM workflows, content management.
- Related tools: similar functionality appeared in LlamaIndex image node parsers and LangChain vision chains.

[Original](https://github.com/vladignatyev/bulktag) → GitHub
