---
title: "ChunkViz: Visualize Text Splitting for RAG Pipelines"
date: 2023-12-09
categories:
  - rag
  - llm
  - text-chunking
  - developer-tools
  - visualization
description: ChunkViz is a visual tool for comparing different text splitting strategies — see exactly how your documents get chunked with different chunk sizes, overlap settings, and splitting methods. Essential for debugging RAG pipelines where chunking quality directly affects retrieval quality.
params:
  source: pinboard
  sourceUrl: https://github.com/gkamradt/ChunkViz
---

![ChunkViz: Visualize Text Splitting for RAG Pipelines](/images/notes/chunkviz-text-splitting.png)

## Summary

ChunkViz is a small visualization tool by Greg Kamradt that shows how text gets divided under different chunking strategies — chunk size, chunk overlap, and splitting method (character, recursive character, sentence, etc.). The motivation: text splitting is a critical but often-invisible step in RAG pipelines, and getting it wrong silently degrades retrieval quality.

In a RAG system, documents are split into chunks before embedding. Too large: chunks contain multiple unrelated concepts and retrieval becomes noisy. Too small: chunks lose context and retrieved fragments don't have enough information to answer questions. Too much overlap: redundant retrieval results inflate context. The right parameters depend on document structure — legal contracts chunk differently than technical documentation or conversational transcripts.

ChunkViz makes this concrete by rendering exactly where boundaries fall in a real document under each strategy. You paste in text, adjust parameters, and see the split points highlighted. This turns a guessing game into an observable process. LangChain's text splitters are the standard backend — `RecursiveCharacterTextSplitter`, `TokenTextSplitter`, `SpacyTextSplitter` — and ChunkViz provides a UI to compare them side-by-side.

## Key points

- Visual inspection of chunk boundaries for different splitters and parameters.
- Compare LangChain splitters: `RecursiveCharacterTextSplitter`, `TokenTextSplitter`, sentence-based.
- Chunk size and overlap interact — increasing overlap helps context but increases total chunks and cost.
- Document structure matters: headers, code blocks, and lists need different splitting than prose.
- Debugging tool: if retrieval quality is poor, chunk visualization often reveals the problem.
- By Greg Kamradt — same author as the chunking survey 5 Levels of Text Splitting.

[Original](https://github.com/gkamradt/ChunkViz/tree/main) → GitHub
